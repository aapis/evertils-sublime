import os
import sublime
import sublime_plugin
import subprocess
import json
import threading
import Queue
from outputformatter import OutputFormatter

class Commander(threading.Thread):
	def __init__(self, command, queue):
		self.command = "source %s/.bash_profile && %s" % (os.path.expanduser('~'), command)
		self.result = None
		self.queue = queue
		threading.Thread.__init__(self)

	def run(self):
		# TODO: setup custom bash environment here so the source stuff above is not required
		pipe = subprocess.Popen(self.command, shell=True, stdout=subprocess.PIPE)
		output, error = pipe.communicate()
		return_code = pipe.poll()
		
		if return_code == 0 and error == None:
			convert = OutputFormatter()
			converted = str(convert.from_ansi(output).encode('utf-8'))

			if(self.is_json(converted)):
				_list = json.loads(converted)
				output = "".join(_list)
			else:
				output = converted

			self.result = (True, output.decode('utf-8'))
		else:
			self.result = (False, "Error occurred running\n%s" % error)

		self.queue.put(self.result)

	def is_json(self, input):
		try:
			json_object = json.loads(input)
		except ValueError, e:
			return False
		return True