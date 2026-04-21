import numpy as np

# CONSTANTS                                                                                                                           
BASELINEDEFAULT = 2050
BASETOLERANCE = 1
RMSCUT = 2.


#inputs:
# wf -> waveform
# tickstart -> first tick for baseline calculation
# tickend -> last tick for baseline calculation
def GetBaselineAndRMS(wf,tickstart,tickend):
    base = 0
    rms = 0
    return base,rms

# find SPEs in a given tick range
# inputs:
# wf -> waveform
# tickstart -> where to start looking for pulses
# tickend -> where to stop looking for pulses
# threshold -> threshold to trigger a pulse ID
def FindSPE(wf,tickstart,tickend,threshold):
    pulsetick = 0
    return pulsetick


# once we have an SPE, is there enough of a buffer?
# make sure the buffer region does not have other SPEs
# inputs:
# wf -> waveform
# SPEtick -> tick at which spe is found
# deadtime -> how much dead-time to require after pulse
# threshold -> threshold for secondary pulses in deadtimedelay region
# deadtimedelay -> how many ticks to veto after SPEtick + deadime
def CheckDeadTime(wf,SPEtick,deadtime,threshold,deadtimedelay):
    return False

# record the waveform centered on the SPE peak
# inputs
# wf -> waveform
# SPEtick -> tick at peak of SPE
# bufferL -> how many ticks to save before the peak
# bufferR -> how many ticks to save after the peak
def SaveSPE(wf,SPEtick,bufferL,bufferR):
    return np.zeros(bufferL+bufferR)

# get Single Photo-Electrons
# input:
# waveform -> waveform
# BASELINECUT -> baseline value
# BASELINETOLERANCECUT -> tolerance on baseline
# RMSMAX -> Max RMS allowed
# returns:
# base, rms: baseline and rms for waveform
# spectr: how many SPEs were found on the waveform?
# SPE_ampl_v, SPE_tick_v, SPE_wf_v: arrays of amplitude, time-tick, and actual SPE waveform for identified SPEs
def GetSPE(waveform,BASELINECUT=BASELINEDEFAULT,BASELINETOLERANCECUT=BASETOLERANCE,RMSMAX=RMSCUT):

    base = 0
    rms = 0
    spectr = 0
    SPE_ampl_v = []
    SpE_tick_v = []
    SPE_wf_v = []
    return base, rms, spectr, SPE_ampl_v, SPE_tick_v, SPE_wf_v
