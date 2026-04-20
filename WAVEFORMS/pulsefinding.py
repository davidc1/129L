
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
def GetSPE(waveform,BASELINECUT=BASELINEDEFAULT,BASELINETOLERANCECUT=BASETOLERANCE):

    spectr = 0
    wfctr = 0
    baseline_v = []
    rms_v = []
    spe_ampl_v = []

    spe_avg_v = np.zeros(DEADTIME)

    waveform = waveform.astype(float)

    base,rms = GetBaselineAndRMS(waveform,0,20)

    if (rms == 0 or base == 0):
        continue

    baseline_v.append(base)
    rms_v.append(rms)


    if ( (base < BASELINECUT-BASETOLERANCE) or (base > BASELINECUT+BASETOLERANCE) ):
        continue
    if ( rms > RMSMAX ):
        continue

    anawf = waveform - base
    
    SPEtick = FindSPE(anawf,20,1500-DEADTIME,SPETHRESHOLD)

    if (SPEtick == 20): continue
    
    if (CheckDeadTime(anawf,SPEtick,DEADTIME,DEADTHRESHOLD,DEADTIMEDELAY) == True):
        
        spe_wf = SaveSPE(anawf,SPEtick,-BUFFER,DEADTIME-BUFFER)

        SPEmax = np.amax(spe_wf)
            
        spe_avg_v += spe_wf
        spectr += 1 
            
        spe_ampl_v.append(SPEmax)

    return spe_avg_v,spectr,baseline_v,rms_v,spe_ampl_v
