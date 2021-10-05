import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class Handler:
    def onDestroy(self, *args):
        Gtk.main_quit()

    def __getattr__(self, name, *args):
        return lambda *args: print({"name": name, "args": args})

builder = Gtk.Builder()
builder.add_from_file("ui.glade")
builder.connect_signals(Handler())

window = builder.get_object("window")

hb = builder.get_object("headerBar")
hb.get_parent().remove(hb)
window.set_titlebar(hb)

window.show_all()
Gtk.main()
