import urwid

def exit_on_q(key):
    if key in ('q', 'Q'):
        raise urwid.ExitMainLoop()

calcpalette = [
    ('bg', 'white', 'black'),
    ('numpad', 'black', 'light blue'),
    ('display', 'green', 'dark gray')
]