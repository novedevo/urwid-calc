import urwid

def exit_on_q(key):
    if key in ('q', 'Q'):
        raise urwid.ExitMainLoop()

class QuestionBox(urwid.Filler):
    def keypress(self, size, key):
        if key != 'enter':
            if key in tuple(map(lambda x: str(x), range(0,9))) or key == '+':
                return super(QuestionBox, self).keypress(size, key)
            return
        self.original_widget = urwid.Text(f"= \n{eval(edit.edit_text)}.\n\nPress Q to exit.")

edit = urwid.Edit("Enter your expression to be evaluated\n")
fill = QuestionBox(edit)
loop = urwid.MainLoop(fill, unhandled_input=exit_on_q)
loop.run()