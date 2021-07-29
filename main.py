import urwid

def exit_on_q(key):
    if key in ('q', 'Q'):
        raise urwid.ExitMainLoop()
def on_exit_clicked(_):
    raise urwid.ExitMainLoop()

def button_click(button: urwid.Button):
    edit.edit_text += button.get_label()

def on_delete_clicked(_):
    if edit.edit_text:
        edit.edit_text = edit.edit_text[:-1]

valid_chars = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.', '+', ' ', '(', ')') # can you create malicious python with just these characters?

class QuestionBox(urwid.Filler):
    def keypress(self, size, key):
        if key != 'enter':
            return super(QuestionBox, self).keypress(size, key)
        self.evaluate()
    def evaluate(self, _ = None):
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

buttons = []
for i in range(10):
    button = urwid.Button(str(i))
    urwid.connect_signal(button, 'click', button_click)
    buttons.append(button)
plus = urwid.Button("+")
delete = urwid.Button("Delete")
equals = urwid.Button("=")
exit = urwid.Button("Exit")

div = urwid.Divider()
pile = urwid.Pile([edit, *buttons, plus, delete, equals, exit])

fill = QuestionBox(pile)
urwid.connect_signal(exit, 'click', on_exit_clicked)
urwid.connect_signal(plus, 'click', button_click)
urwid.connect_signal(delete, 'click', on_delete_clicked)
urwid.connect_signal(equals, 'click', fill.evaluate)

loop = urwid.MainLoop(fill, unhandled_input=exit_on_q)
loop.run()