import urwid

def exit_on_q(key):
    if key in ('q', 'Q'):
        raise urwid.ExitMainLoop()

valid_chars = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.' '+', ' ', '(', ')') # can you create malicious python with just these characters?

class QuestionBox(urwid.Filler):
    def keypress(self, size, key):
        if key != 'enter':
            return super(QuestionBox, self).keypress(size, key)
        text = edit.edit_text # ew, globals. is this valid? is there a better way?

        if not text: # empty string
            self.original_widget = urwid.Text("Please enter an expression next time. Press Q to exit.")
            return

        for char in text:
            if char not in valid_chars:
                self.original_widget = urwid.Text("Invalid string. Press Q to exit.")
                return

        self.original_widget = urwid.Text(f"{text} \n= {eval(text)}.\n\nPress Q to exit.")

edit = urwid.Edit("Enter your (addition-only, integers and floats ok) expression to be evaluated\n")
fill = QuestionBox(edit)
loop = urwid.MainLoop(fill, unhandled_input=exit_on_q)
loop.run()