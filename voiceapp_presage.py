import presage

class VoiceAppCallback(presage.PresageCallback):
	def __init__(self):
		presage.PresageCallback.__init__(self)
		self.buffer = ''

	def get_past_stream(self):
		return self.buffer

	def get_future_stream(self):
		return ''

class Predictions:
	def __init__(self):
		self.callback = VoiceAppCallback().__disown__()
		self.prsg = presage.Presage(self.callback)
	def GetPredictions(self,str):
		self.callback.buffer += str
		return self.prsg.predict()
	def __exit__(self, type, value, traceback):
		del self.prsg