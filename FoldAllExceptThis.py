import sublime_plugin


class FoldAllExceptThisCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		view              = self.view
		tabSize           = view.settings().get("tab_size")
		currentLine       = view.substr(view.line(view.sel()[0].begin())).replace("\t", " " * tabSize)

		leadingSpaceCount = 0
		for a in currentLine:
			if a == " ":
				leadingSpaceCount += 1
			else:
				break

		indentLevel  = leadingSpaceCount / tabSize
		foldingLevel = int(indentLevel * 9 / 10)
		print("# fold_all_except_this, level: ", foldingLevel)

		view.run_command("unfold_all")
		view.run_command("fold_by_level", {"level": foldingLevel})
