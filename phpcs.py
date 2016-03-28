import sublime
import sublime_plugin
import os
import os.path
import threading

class PhpcsCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        view = self.view;
        fileName = view.file_name();
        suffix =  os.path.splitext(fileName)[1][1:]
        if suffix == 'php':
            fix(fileName)

def fix(phpFile):
    if not os.path.exists(phpFile):
        return;
    command = 'phpcs fix ' + phpFile;
    os.system(command);

'''
class AutoAlign(sublime_plugin.EventListener):
    def on_post_save(self, view):
        thread = HandlerThread(view)
        thread.start()
'''

class HandlerThread(threading.Thread):
    def __init__(self, view):
        self.view = view
        threading.Thread.__init__(self)

    def run(self):
        fileName = self.view.file_name();
        suffix =  os.path.splitext(fileName)[1][1:]
        if suffix == 'php':
            fix(fileName)
