import re

class OutputFormatter:
	def from_ansi(self, string):
		ansi_escape = re.compile(r'\x1b[^m]*m')
		string = string.decode('utf-8').strip()

		return ansi_escape.sub('', string)
