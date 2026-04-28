import numpy as np


# CONSTANTS
BASELINEDEFAULT = 2050
BASETOLERANCE = 1
RMSMAX = 2.
DEADTIME = 150
BUFFER = 10
SPETHRESHOLD = 10.
DEADTHRESHOLD = 3.
DEADTIMEDELAY = 10
TICKLENGTH = 500

PEMIN = 5
PEMAX = 100

# return the baseline and RMS of a waveform within a given tick-range
def GetBaselineAndRMS(wf,tickstart,tickend):
    baseline = wf[tickstart:tickend]
    return np.mean(baseline),np.std(baseline)

# Find Single Photo-Electrons within a given tick-range
def FindSPE(wf,tickstart,tickend,threshold):
    subwf = wf[tickstart:tickend]
    foundstart = False
    starttick = 0
    thistick = 0
    maxticks = len(subwf)-1
    while ( (foundstart == False) and (thistick < maxticks) ):
        if (subwf[thistick] > threshold):
            starttick = thistick
            foundstart = True
        thistick += 1
    return starttick + tickstart

# once we have an SPE, is there enough of a buffer?
# make sure the buffer region does not have other SPEs
def CheckDeadTime(wf,SPEtick,deadtime,threshold,deadtimedelay):
    wfsub = wf[SPEtick+deadtimedelay:SPEtick+deadtimedelay+deadtime]
    #fig = plt.figure(figsize=(6,6))
    #plt.plot(wfsub)
    #plt.title('CheckDeadTime')
    #plt.show()
    if (np.max(wfsub) > threshold):
        #print ('wf max is %i'%np.max(wfsub))
        return False
    return True

# record the waveform centered on the SPE peak
def SaveSPE(wf,SPEtick,bufferL,bufferR):
    return wf[SPEtick+bufferL:SPEtick+bufferR]


# get Single Photo-Electrons
def GetSPE(waveform,BASELINECUT=BASELINEDEFAULT,\
           BASELINETOLERANCECUT=BASETOLERANCE,DEBUG=False):

    spectr = 0

    waveform = waveform.astype(float)
    base,rms = GetBaselineAndRMS(waveform,0,20)
    baseE,rmsE = GetBaselineAndRMS(waveform,1500-21,1500-1)

    if(DEBUG):
        print("baseline: %.02f\t RMS: %.02f"%(base,rms))
    
    if (rms == 0 or base == 0):
        raise ValueError("ERROR: could not compute baseline or RMS")
    

    # veto waveforms with baseline not within spec
    if ( (base < BASELINECUT-BASETOLERANCE) or (base > BASELINECUT+BASETOLERANCE) ):
        raise ValueError("Baseline not within tolerance")
    # veto waveforms with RMS not within spec
    if ( rms > RMSMAX ):
        raise ValueError("RMS not within tolerance")
    # veto waveforms with start/end baseline or RMS not agreeing
    if ( (abs(base-baseE) > 0.5) or (abs(rms-rmsE) > 0.5) ):
        raise ValueError('RMS/baseline start-end disagree')
    # veto waveforms with large pulses
    if ( np.max(waveform) > (base+40) ):
        raise ValueError('Large Pulse!')

    # baseline subtracted waveform
    anawf = waveform - base

    # current index of potential SPE peak
    SPEtick = 20

    SPE_ampl_v = []
    SPE_tick_v = []
    SPE_wf_v = []

    PULSEFINDINGSTART = 20

    while (SPEtick < 1500-DEADTIME-BUFFER):

        if(DEBUG):
            print("\tSearch for a pulse starting from tick %i"%PULSEFINDINGSTART)
        
        # find time-tick of SPE
        SPEtick = FindSPE(anawf,PULSEFINDINGSTART,1500-DEADTIME,SPETHRESHOLD)

        if (DEBUG):
            print("Found SPE at tick %i"%SPEtick)

        if (SPEtick == PULSEFINDINGSTART): break
    
        if (CheckDeadTime(anawf,SPEtick,DEADTIME,DEADTHRESHOLD,DEADTIMEDELAY) == True):
        
            spe_wf = SaveSPE(anawf,SPEtick,-BUFFER,DEADTIME-BUFFER)

            SPEmax = np.amax(spe_wf)
            
            SPE_tick_v.append(SPEtick)
            SPE_ampl_v.append(SPEmax)
            SPE_wf_v.append(spe_wf)
            spectr += 1

        PULSEFINDINGSTART = SPEtick + DEADTIME
            
    return base, rms, spectr, SPE_ampl_v, SPE_tick_v, SPE_wf_v
