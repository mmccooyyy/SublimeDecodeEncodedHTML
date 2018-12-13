import sublime
import sublime_plugin
import re


class DecodeEncodedHtmlCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		self._edit = edit
		self._replace_all(r"\\n", "\n")
		self._replace_all(r"\\/", "/")
		self._replace_all(r"\\\"", "\"")

	def _get_file_content(self):
		return self.view.substr(sublime.Region(0, self.view.size()))

	def _update_file(self, doc):
		self.view.replace(self._edit, sublime.Region(0, self.view.size()), doc)

	def _replace_all(self, regex, replacement):
		doc = self._get_file_content()
		p = re.compile(regex, re.UNICODE)
		doc = re.sub(p, replacement, doc)
		self._update_file(doc)
