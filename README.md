# plot-cat

plot-cat is the python library for plotting live serial input. plotcat works on python 2.7 and later. plotcat comes handy when you want to plot live data that is coming form different sensors over the serial port. For example you have to plot the output of a temperature sensor that is coming from an [arduino](https://www.arduino.cc/) or any other microcontroller for that matter; plotcat comes handy for such tasks.

plotcat sits on the top of [matplotlib](matplotlib.org) and does all the initialization and drawing stuff itself. you just have to provide the list of values to be plotted.

plotcat works on linux osx and windows. plotcat also works well with [Raspberry Pi](https://www.raspberrypi.org/)

## install plotcat

```bash
git clone https://github.com/girish946/plot-cat.git

pip install -r requirements.txt

python install setup.py install

```


## useage

To plot the incomming input from serial device directly.

Assuming there is one value on one line in the serial input, ie. the format of the serial input is roughly like:

    val | \r | \n 
    -----|----|----

    python live_plot.py /dev/tty<device> baudrate

### plot-cat api


To use plot-cat api.

```python 
import serial
from plotcat import *

p = plotter()

#init serial device
ser = serial.Serial('/dev/ttyAMA0', 9600)

#the callback function for plotting
@p.plot_self
def update_plot():

  data = [ser.readline() for i in range(100)]
  p.lines[0][0].set_data(p.currentAxis, data)

p.set_call_back(update_plot)

```

this is the example to recive the data from arduino (given in the example->communication->SerialEvent of the arduino IDE.)
