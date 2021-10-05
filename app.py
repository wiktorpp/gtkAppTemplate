import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class Handler:
    def onDestroy(self, *args):
        Gtk.main_quit()

    def __getattr__(self, name):
        return lambda self, *args: print(
            f'Signal "{name}" '
            f'was sent by a {self.get_name()} '
            f'with arguments {args}'
        )

builder = Gtk.Builder()
builder.add_from_file("ui.glade")
builder.connect_signals(Handler())

window = builder.get_object("window")
window.show_all()
Gtk.main()
