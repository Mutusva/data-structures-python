import turtle
import struct
import numpy as np
from scipy import signal as sg

#gp = turtle.Turtle()
#gp.forward(100)


sampling_rate = 44100 
freq = 344 
samples = 44100

x = np.arange(samples)


y = 100 * sg.square(2 * np.pi * freq * x / sampling_rate)

f = open('Aflatoxin.wav', 'wb')

for i in y:
    f.write(struct.pack('b', int(i)))

f.close()


