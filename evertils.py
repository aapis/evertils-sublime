import os
import sublime
import sublime_plugin
import os.path
import Queue
import shutil
from commander import Commander

PACKAGE_DIR = sublime.packages_path()
USER_SETTINGS = PACKAGE_DIR + '/User/Evertils.sublime-settings'
PACKAGE_SETTINGS = PACKAGE_DIR + '/evertils-sublime/Evertils.sublime-settings'

class EvertilsGenerateDaily(sublime_plugin.TextCommand):
	def run(self, edit):
		sublime.status_message("Generating daily log")

		command = "evertils generate daily"
		queue = Queue.Queue()
		general = Commander(command, queue)
		general.start()
		settings = sublime.load_settings('Evertils.sublime-settings')

		if settings.get('always_wait_for_threads'):
			# The following code gets the response from the executed command, it's more
			# accurate but also requires you to wait for the thread to finish
			command_executed, message = queue.get()

			if(command_executed):
				sublime.message_dialog("Daily log generated")
			else:
				sublime.error_message("Problem generating log")
		else:
			sublime.message_dialog("Generating daily log")

class EvertilsGenerateWeekly(sublime_plugin.TextCommand):
	def run(self, edit):
		sublime.status_message("Generating weekly log")

		command = "evertils generate weekly"
		queue = Queue.Queue()
		general = Commander(command, queue)
		general.start()
		settings = sublime.load_settings('Evertils.sublime-settings')

		if settings.get('always_wait_for_threads'):
			# The following code gets the response from the executed command, it's more
			# accurate but also requires you to wait for the thread to finish
			command_executed, message = queue.get()

			if(command_executed):
				sublime.message_dialog("Weekly log generated")
			else:
				sublime.error_message("Problem generating log")
		else:
			sublime.message_dialog("Generating weekly log")

class EvertilsGenerateMonthly(sublime_plugin.TextCommand):
	def run(self, edit):
		sublime.status_message("Generating monthly log")

		command = "evertils generate monthly"
		queue = Queue.Queue()
		general = Commander(command, queue)
		settings = sublime.load_settings('Evertils.sublime-settings')

		if settings.get('always_wait_for_threads'):
			# The following code gets the response from the executed command, it's more
			# accurate but also requires you to wait for the thread to finish
			command_executed, message = queue.get()

			if(command_executed):
				sublime.message_dialog("Monthly log generated")
			else:
				sublime.error_message("Problem generating log")
		else:
			sublime.message_dialog("Generating monthly log")

class GranifyOpenSettingsCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		window = self.view.window()
		
		if(not os.path.isfile(USER_SETTINGS)):
			shutil.copyfile(PACKAGE_SETTINGS, USER_SETTINGS)

		window.open_file(USER_SETTINGS)
