import requests

# set webhook
class Webhook:
	def __init__(self, token):
		self.token = token

	def set_webhook(self, ngrok_url):
		api_url = f"https://api.telegram.org/bot{self.token}/"
		ngrok = f"setWebhook?url={ngrok_url}"

		response = requests.get(api_url+ngrok)

		return response


