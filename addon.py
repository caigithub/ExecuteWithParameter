import os
import sublime, sublime_plugin

class ExecuteWithParameterCommand(sublime_plugin.TextCommand):
    def run(self, edit, cmd_path):
        self.cmd_path = cmd_path

        for region in self.view.sel():
            if region.begin() == region.end():
               word = self.view.word(region)
            else:
                word = region

        if not word.empty():
            keyword = self.view.substr(word)

        self.view.window().show_input_panel("Parameters", keyword, self.on_done, None, None)

    def on_done(self, keywords):
        os.system(self.cmd_path + " " + self.view.file_name() + " " + keywords)

class ExecuteWithCurrentWordAsParameterCommand(sublime_plugin.TextCommand):
    def run(self, edit, cmd_path):
        self.cmd_path = cmd_path

        for region in self.view.sel():
            if region.begin() == region.end():
               word = self.view.word(region)
            else:
                word = region

        if not word.empty():
            keyword = self.view.substr(word)

        os.system(self.cmd_path + " " + self.view.file_name() + " " + keyword)