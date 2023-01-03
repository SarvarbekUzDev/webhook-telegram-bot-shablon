from dp.handlers.handlers import Sends
from dp.handlers.request import Request



class Dispatcher(Sends, Request):
	""" Bot Dispatcher """
	def __init__(self, token, framework="flask"):
		self.token = token
		self.framework = framework

