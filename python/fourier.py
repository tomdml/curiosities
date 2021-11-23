import numpy as np
import matplotlib.pyplot as plotter

samplingFrequency = 100
samplingInterval = 1 / samplingFrequency

beginTime = 0
endTime = 10

signal1Frequency = 4
signal2Frequency = 7

time = np.arange(beginTime, endTime, samplingInterval)

amplitude1 = np.sin(2 * np.pi * signal1Frequency * time)
amplitude2 = np.sin(2 * np.pi * signal2Frequency * time)

figure, axis = plotter.subplots(4, 1)
plotter.subplots_adjust(hspace=1)

axis[0].set_title('Sine wave with a frequency of 4 Hz')
axis[0].plot(time, amplitude1)
axis[0].set_xlabel('Time')
axis[0].set_ylabel('Amplitude')


axis[1].set_title('Sine wave with a frequency of 7 Hz')
axis[1].plot(time, amplitude2)
axis[1].set_xlabel('Time')
axis[1].set_ylabel('Amplitude')

amplitude = amplitude1 + amplitude2

axis[2].set_title('Sine wave with multiple frequencies')
axis[2].plot(time, amplitude)
axis[2].set_xlabel('Time')
axis[2].set_ylabel('Amplitude')

fourierTransform = np.fft.fft(amplitude) / len(amplitude)
fourierTransform = fourierTransform[range(len(amplitude) // 2)]

tpCount = len(amplitude)
values = np.arange(tpCount // 2)
timePeriod = tpCount / samplingFrequency
frequencies = values / timePeriod

axis[3].set_title('Fourier transform depicting the frequency components')
axis[3].plot(frequencies, abs(fourierTransform))
axis[3].set_xlabel('Frequency')
axis[3].set_ylabel('Amplitude')

plotter.show()
