import numpy as np
import matplotlib.pyplot as plt
import scipy as sp


def raspi_import(path, channels=5):
    """
    Import data produced using adc_sampler.c.

    Parameters
    ----------
    path: str
        Path to file.
    channels: int, optional
        Number of channels in file.

    Returns
    -------
    sample_period: float
        Sample period
    data: ndarray, uint16
        Sampled data for each channel,
        in dimensions NUM_SAMPLES x NUM_CHANNELS.
    """

    with open(path, 'r') as fid:
        sample_period = np.fromfile(fid, count=1, dtype=float)[0]
        data = np.fromfile(fid, dtype=np.uint16)
        data = data.reshape((-1, channels))
    return sample_period, data


def modifyData(data, up_sample_factor=1):
    length = len(data[:, 0])
    new_data = np.zeros((length, 3))
    new_data = sp.signal.detrend(data[:, :3], axis=0, type="constant")

    if(up_sample_factor != 1):
        new_data = sp.signal.resample(
                   new_data, up_sample_factor*length, axis=0)
    return new_data


def get_delay(data):
    # 3x Crosscorrelation of the modified microphone data.
    Xc12 = np.correlate(data[:, 0], data[:, 1], mode='full')
    Xc13 = np.correlate(data[:, 0], data[:, 2], mode="full")
    Xc23 = np.correlate(data[:, 1], data[:, 2], mode="full")
    # 3x Casting from ndarray to list .
    listeXc12 = np.ndarray.tolist(Xc12)
    listeXc13 = np.ndarray.tolist(Xc13)
    listeXc23 = np.ndarray.tolist(Xc23)
    # 3x Finding the delay of the max value of the crosscorrelation
    Tau12 = int(listeXc12.index(max(Xc12))) - (int((len(Xc12))/2))
    Tau13 = int(listeXc13.index(max(Xc13))) - (int((len(Xc13))/2))
    Tau23 = int(listeXc23.index(max(Xc23))) - (int((len(Xc23))/2))
    # må ta lengda til Xc før crosscorrelation-1
    # fikse upsampling
    return Tau12, Tau13, Tau23


def xcorr_attributes(Xcorr, data):
    if (Xcorr == 12):
        Xc = np.correlate(data[:, 0], data[:, 1], mode='full')
        listeX = np.ndarray.tolist(Xc)
        print("The length of the crosscorrelation is :", len(Xc))
        print("The maximum value of the crosscorrelation is : ", max(Xc))
        print("The maximum value is located at index : ",
              listeX.index(max(Xc)))
        print("That corresponds to a delay of", int(listeX.index(max(Xc))) - (
              int((len(Xc))/2)), "samples")
    elif (Xcorr == 13):
        Xc = np.correlate(data[:, 0], data[:, 2], mode='full')
        listeX = np.ndarray.tolist(Xc)
        print("The length of the crosscorrelation is :", len(Xc))
        print("The maximum value of the crosscorrelation is : ", max(Xc))
        print("The maximum value is located at index : ",
              listeX.index(max(Xc)))
        print("That corresponds to a delay of", int(listeX.index(max(Xc))) - (
              int((len(Xc))/2)), "samples")
    elif (Xcorr == 23):
        Xc = np.correlate(data[:, 1], data[:, 2], mode='full')
        listeX = np.ndarray.tolist(Xc)
        print("The length of the crosscorrelation is :", len(Xc))
        print("The maximum value of the crosscorrelation is : ", max(Xc))
        print("The maximum value is located at index : ",

              listeX.index(max(Xc)))
        print("That corresponds to a delay of", int(listeX.index(max(Xc))) - (
              int((len(Xc))/2)), "samples")
    else:
        print("Choose between following Xcorrelations : 12 , 13 and 23")


def get_theta(T1, T2, T3):
    # Check if X is negtive
    a = 0.055       # Distance between mic in meters
    x = (-(np.sqrt(3)*a/3)*T1)+((np.sqrt(3)*a/3)*T2)+(np.sqrt(3)*a*T3)
    if (x < 0):
        theta = np.arctan(np.sqrt(3)*((T1+T2)/(T1-T2-2*T3)))
        theta_deg = (180/np.pi)*theta
    else:
        theta = np.arctan(np.sqrt(3)*((T1+T2)/(T1-T2-2*T3)))
        theta_deg = ((180/np.pi)*theta)+180
    if(theta_deg < 0):
        print("Angle of incident in degrees:", round(theta_deg+360, 2))
    else:
        print("Angle of incident in degrees:", round(theta_deg, 2))


def MakeComplex(data):
    InPhase = data[:, 0]                             # InPhase
    Quadrature = data[:, 1]                          # Quadrature
    X = InPhase + (Quadrature*1j)                    # Combines I and Q
    Xnew = sp.signal.detrend(
           X, axis=0, type="constant")             # Removes the DC-comp
    return Xnew


def plotData(data, time, scalingFactor):
    plt.plot(time[1:], scalingFactor*data[1:])
    plt.title("The sampled signal in time ", color="g")
    plt.ylabel("Magnitude[V]", color="b")
    plt.xlabel("Time[s]", color="r")
    plt.grid()
    plt.axis("tight")
    plt.show()


def plotVelocities(real, measured):
    plt.plot(real, measured, '*m-', linewidth=2, markersize=18)
    plt.title("Real velocity vs measured velocity", color="g")
    plt.ylabel("Real[m/s]", color="b")
    plt.xlabel("Measured[m/s]", color="r")
    plt.grid()
    plt.axis("tight")
    plt.show()


def plotFFT(data, frq, scalingFactor, length_of_data):
    FFT = (sp.fft(scalingFactor*data)/length_of_data)  # FFT
    plt.title("FFT of complex radardata ", color="g")
    plt.plot(frq, 20*np.log10(abs(FFT/766)))
    plt.ylabel("Magnitude[dB/1V]", color="b")
    plt.xlabel("frequency[Hz]", color="r")
    plt.xlim(-1000, 1000)
    plt.ylim(-10, 70)
    # plt.axis("tight")                             # fit all data barely
    plt.show()                                     # Show plot
    return FFT


def get_dopplerF(FFT, freq):
    max = np.argmax(np.abs(FFT))
    DopplerF = int(freq[max])
    print("Dopplerskiftet er : ", DopplerF, " Hz")
    return DopplerF


def get_velocity(HighestFftValueInSamples, lengde):
    C = 3*(10**8)                                   # Speed of sound
    BuiltInRadarFreq = 24.125*(10**9)               # Frequency of the radar
    V = HighestFftValueInSamples*C/(
        2*BuiltInRadarFreq)                         # Formula for velocity
    print("Hastigheten er: ", round(V, 3), " m/s")
    return V


def plotR(y, x,z):
    plt.plot(y, x[0, :], color="r")
    plt.title("The sampled signal from the red colours " + z, color="r")
    plt.ylabel("Magnitude[V]", color="r")
    plt.xlabel("Time[s]", color="r")
    plt.grid()
    plt.axis("tight")
    plt.show()


def plotG(y, x,z):
    plt.plot(y, x[1, :], color="g")
    plt.title("The sampled signal from the green colours "+ z, color="g")
    plt.ylabel("Magnitude[V]", color="g")
    plt.xlabel("Time[s]", color="g")
    plt.grid()
    plt.axis("tight")
    plt.show()


def plotB(y, x,z):
    plt.plot(y, x[2, :], color="b")
    plt.title("The sampled signal from the blue colours "+ z, color="b")
    plt.ylabel("Magnitude[V]", color="b")
    plt.xlabel("Time[s]", color="b")
    plt.grid()
    plt.axis("tight")
    plt.show()


def plotCameraFFT(f, data):
    FFT = sp.fft(data)/398  # FFT
    plt.title("FFT of PiCamera data", color="g")
    plt.plot(f, 20*np.log10(abs(FFT)))
    plt.ylabel("Magnitude[dB/1V]", color="b")
    plt.xlabel("frequency[Hz]", color="r")
    plt.axis("tight")                             # fit all data barely
    plt.show()                                     # Show plot
