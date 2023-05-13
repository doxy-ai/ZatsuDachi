# Import necessary modules
from flask import Flask
from flask_socketio import SocketIO
from app import App
from message import Message
from colour import Color
from datetime import datetime

# Initialize Flask and SocketIO instances
flask = Flask(__name__)
socketIO = SocketIO(flask)

# Create an instance of the App class
_singletonApp = App()

class PluginBase:
	"""
	Base class for creating plugins for the chat application.

	Attributes:
		name (str): The name of the plugin.
	"""

	name = "base"

	async def go(self):
		"""
		A method that will be called whenever the plugin is loaded.
		This method gets called in a seperate thread so it is perfectly fine to start infinate loops here if nessicary!
		"""
		pass

	def on_message_recieved(self, messages):
		"""
		A method that will be called whenever the application receives a new message.

		Args:
			messages (list of Message): A ring buffer of Message objects.
		"""
		pass

	def recieve_message(self, message):
		"""
		A method that can be called to signal to the application that a new message has been received.

		Args:
			message (Message): A Message object to be received by the application.
		"""
		_singletonApp.recieve_message(message)

	def register_emote(self, emote, url):
		"""
		A method that can be called to register an emote with the application.

		Args:
			emote (str): The name of the emote.
			url (str): The URL where the emote can be found.
		"""
		_singletonApp.register_emote(emote, url)
