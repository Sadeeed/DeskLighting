import serial
import time
import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

def write_read(x):
    mcuSerial.reset_input_buffer()
    mcuSerial.write(bytes(x, 'utf-8'))
    data = mcuSerial.readline()
    return data

class Handler:
    def onDestroy(self, *args):
        Gtk.main_quit()

    def onHueChange(self, *args):
        hue = str(int(hueSlider.get_value())) + "H"
        print(hue)
        # write_read(hue)
        print(write_read(hue))

    def onSaturationChange(self, *args):
        saturation = str(int(saturationSlider.get_value())) + "S"
        print(saturation)
        # write_read(saturation)
        print(write_read(saturation))

    def onValueChange(self, *args):
        value = str(int(valueSlider.get_value())) + "V"
        print(value)
        # write_read(value)
        print(write_read(value))


mcuSerial = serial.Serial(port="/dev/ttyACM0", baudrate=9600, timeout=0.5)
# load glade UI xml
builder = Gtk.Builder()
uiFile = "data/ui/LightApp.glade"
builder.add_from_file(uiFile)
builder.connect_signals(Handler())
window = builder.get_object("MainWindow")

hueSlider = builder.get_object("hueSlider")
saturationSlider = builder.get_object("saturationSlider")
valueSlider = builder.get_object("valueSlider")

window.show_all()
Gtk.main()
