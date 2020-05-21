from threading import Thread as t
import threading
import wave,struct
import numpy as np
import matplotlib.pyplot as plot
def readfile(filename):
    wave_r = wave.open(filename,'r')
    ret = []
    length = wave_r.getnframes()
    while wave_r.tell() < length:
        decoded = struct.unpack("<hh",wave_r.readframes(1))
        ret.append(decoded)
    return ret
def plotSound(T,A,title):
    plot.title(title)
    plot.plot(T,A)
    plot.xlabel('time')
    plot.ylabel('A')
    plot.grid(True,which= 'both')
    plot.axhline(y=0,color ='k')
    plot.show()
w = np.array(readfile('./output.wav'))
T = np.arange(0,w.shape[0])
A = w[T]
plotSound(T,A[T,0],'left')
plotSound(T,A[T,1],'right')