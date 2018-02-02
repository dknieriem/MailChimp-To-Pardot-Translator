import sublime
import sublime_plugin
import re


class MailChimpToPardotCommand(sublime_plugin.TextCommand):

    settings = sublime.load_settings("MailChimpToPardot.sublime-settings")
    replacements = settings.get("replacements")

    def run(self, edit):
        
        #edit = self.view.begin_edit('MailChimpToPardot')
        currentFieldNumber = 0;
        for replacementField in MailChimpToPardotCommand.replacements:

            print("Field #", currentFieldNumber, ": ", replacementField[0])
            self.replaceField(edit, replacementField, currentFieldNumber)
            currentFieldNumber = currentFieldNumber + 1

    def replaceField(self, edit, replacementField, currentFieldNumber):
        searchValue = re.escape(replacementField[0])
        matches = self.view.find_all(searchValue)
        print("Found ", len(matches), " match(es)")
        currentMatchPosition = 0

        match = self.view.find(searchValue, currentMatchPosition)

        while match is not None and match.size() > 0 :
            currentMatchPosition = match.begin()
            print("Found at pos ", match.begin(), "-", match.end())
            #if match.size() > 0:
            self.view.replace(edit, match, replacementField[1])
            match = self.view.find(replacementField[0], currentMatchPosition)