import json

class Request:
	"""
	Request.
	"""
	message = None

	def __init__(self, framework="flask"):
		self.framework = framework
		self.state = None
		# Register
		self.register()
		# Message
		self.message = Request.message


	# Message handler
	def message_handler(self, request, command=None, text=None, content_types=None,
							state=None):
		request = self.get_json(request=request)
		# command and text 
		try:
			rq = request["message"]["text"]

			if command or text or state:
				# Command
				if command and command[0] in ["/","?"] and command == rq:
					response = request
				# Text
				elif text == rq:
					response = request
				# State
				elif state and request or state == "*":
					return True
				else:
					return False

				return response
		except KeyError as KEY:
			pass

		# Content types
		try:
			if content_types:
				rq = request["message"]
				response = rq[str(content_types)]
				return response				
		except KeyError as KEY:
			pass

		# State
		if state and request or state == "*":
			return True
		else:
			return False




	# callback data
	def callback_data(self, request, text):
		if text:
			try:
				rq = self.get_json(request=request)
				response = rq["callback_query"]["data"]
				if str(response) == str(text):
					return response
				else:
					return False

			except KeyError as KEY:
				return False  			


	# get_json
	def get_json(self, request):
		if self.framework.lower() == "flask":
			request = request.get_json()

		elif self.framework.lower() == "django":
			request = json.loads(request.body)

		self.message = request.get("message")
		return request

	# register.
	def register(self):
		if self.framework.lower() in ["django","flask"]:
			return self.framework
		else:
			raise NameError (f"{self.framework} is not framework. All frameworks: ['flask','django']")

