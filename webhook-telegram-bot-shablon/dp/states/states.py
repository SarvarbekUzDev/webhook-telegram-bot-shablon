class State:
	data_ = {}
	def __init__(self, variable_name):
		self.bool_ = None
		self.data_ = State.data_
		self.variable_name = variable_name

	# is
	def is_(self):
		# self.state = {}
		if self.bool_:
			return True

		return False
			
	# set
	def set(self):
		self.bool_ = True
		return self.bool_

	# update
	def update(self, text):
		if self.bool_:
			self.data_[f"{self.variable_name}"] = text

	# get data
	def get(self):
		return self.data_

	# state finish
	def finish(self):
		self.bool_ = False
		return self.bool_