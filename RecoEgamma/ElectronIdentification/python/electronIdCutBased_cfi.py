import FWCore.ParameterSet.Config as cms

eidCutBased = cms.EDFilter("EleIdCutBasedRef",
    
    filter = cms.bool(False),
    threshold = cms.double(0.5),

    src = cms.InputTag("gsfElectrons"),
    verticesCollection = cms.InputTag("offlinePrimaryVerticesWithBS"),
    reducedBarrelRecHitCollection = cms.InputTag("ecalRecHit","EcalRecHitsEB"),
    reducedEndcapRecHitCollection = cms.InputTag("ecalRecHit","EcalRecHitsEE"),
    algorithm = cms.string('eIDCB'),

    #electronIDType can be robust or classbased
    #electronQuality can be loose,tight or highenergy but for the classedbased 
    #electronVersion can be retrived from the PSet name, no version means the last updated 
    electronIDType  = cms.string('robust'),
    electronQuality = cms.string('loose'),
    electronVersion = cms.string(''),
    etBinning = cms.bool(True),
    additionalCategories = cms.bool(True),
                           
    # variables H/E sigmaietaieta deltaphiin deltaetain e2x5/e5X5 e1x5/e5x5 isoTk ecalTk hcalTk(barrel/endcap)
    #Robust Loose Cuts
    #V00 CMSSW16X optimization 
    #V01 CMSSW22X optimization
    #V02 CMSSW33X optimization
    #V03-V04 CMSSW35X optimization      
    robustlooseEleIDCutsV00 = cms.PSet(
        barrel = cms.vdouble(0.115, 0.014, 0.09, 0.009, -1, -1, 9999., 9999., 9999., 9999., 9999.,9999., 0.000, -9999., 9999., 9999., 9999, -1, 0, 0),
        endcap = cms.vdouble(0.15, 0.0275, 0.092, 0.0105, -1, -1, 9999., 9999., 9999., 9999., 9999.,9999., 0.000, -9999., 9999., 9999., 9999, -1, 0, 0)
    ),
    robustlooseEleIDCutsV01 = cms.PSet(
       barrel = cms.vdouble(0.075, 0.0132, 0.058, 0.0077, -1, -1, 9999., 9999., 9999., 9999., 9999.,9999., 0.000, -9999., 9999., 9999., 9999, -1, 0, 0),
       endcap = cms.vdouble(0.083, 0.027, 0.042, 0.01, -1, -1, 9999., 9999., 9999., 9999., 9999.,9999., 0.000, -9999., 9999., 9999., 9999, -1, 0, 0)
    ),
    robustlooseEleIDCutsV02 = cms.PSet(
       barrel = cms.vdouble(0.05, 0.0103, 0.8, 0.00688, -1, -1, 7.33, 4.68, 9999., 9999., 9999.,9999., 0.000, -9999., 9999., 9999., 9999, -1, 0, 0),
       endcap = cms.vdouble(0.0389, 0.0307, 0.7, 0.00944, -1, -1, 7.76, 3.09, 2.23, 9999., 9999.,9999., 0.000, -9999., 9999., 9999., 9999, -1, 0, 0)
    ),
    robustlooseEleIDCutsV03 = cms.PSet(
       barrel = cms.vdouble(0.05, 0.0103, 0.8, 0.00688, -1, -1, 7.33, 4.68, 9999., 9999., 9999.,9999., 0.000, -9999., 9999., 9999., 9999, -1, 0, 0),
       endcap = cms.vdouble(0.0389, 0.0307, 0.7, 0.00944, -1, -1, 7.76, 3.09, 2.23, 9999., 9999.,9999., 0.000, -9999., 9999., 9999., 9999, -1, 0, 0)
    ),
    robustlooseEleIDCutsV04 = cms.PSet(
       barrel = cms.vdouble(0.05, 0.0103, 0.8, 0.00688, -1, -1, 7.33, 4.68, 9999., 9999., 9999.,9999., 0.000, -9999., 9999., 9999., 9999, -1, 0, 0),
       endcap = cms.vdouble(0.0389, 0.0307, 0.7, 0.00944, -1, -1, 7.76, 3.09, 2.23, 9999., 9999.,9999., 0.000, -9999., 9999., 9999., 9999, -1, 0, 0)
    ),
    robustlooseEleIDCuts = cms.PSet(
       barrel = cms.vdouble(0.05, 0.0103, 0.8, 0.00688, -1, -1, 7.33, 4.68, 9999., 9999., 9999.,9999., 0.000, -9999., 9999., 9999., 9999, -1, 0, 0),
       endcap = cms.vdouble(0.0389, 0.0307, 0.7, 0.00944, -1, -1, 7.76, 3.09, 2.23, 9999., 9999.,9999., 0.000, -9999., 9999., 9999., 9999, -1, 0, 0)
    ),
    
    #Robust Tight Cuts
    #V00 CMSSW16X optimization 
    #V01 CMSSW22X optimization
    #V02 CMSSW33X optimization
    #V03-V04 CMSSW35X optimization 
    robusttightEleIDCutsV00 = cms.PSet(
        barrel = cms.vdouble(0.015, 0.0092, 0.020, 0.0025, -1, -1, 9999., 9999., 9999., 9999., 9999.,9999.,9999., 9999.,9999., 9999., 9999.,9999., 9999., 0.000, -9999., 9999., 9999., 9999, -1, 0, 0),
        endcap = cms.vdouble(0.018, 0.025, 0.020, 0.0040, -1, -1, 9999., 9999., 9999., 9999., 9999.,9999.,9999., 9999.,9999., 9999., 9999.,9999., 9999., 0.000, -9999., 9999., 9999., 9999, -1, 0, 0)
    ),
    robusttightEleIDCutsV01 = cms.PSet(
        barrel = cms.vdouble(0.01, 0.0099, 0.025, 0.0040, -1, -1, 9999., 9999., 9999., 9999., 9999.,9999., 9999.,9999., 9999., 9999.,9999., 9999., 0.000, -9999., 9999., 9999., 9999, -1, 0, 0),
        endcap = cms.vdouble(0.01, 0.028, 0.020, 0.0066, -1, -1, 9999., 9999., 9999., 9999., 9999.,9999., 9999.,9999., 9999., 9999.,9999., 9999., 0.000, -9999., 9999., 9999., 9999, -1, 0, 0)
    ),
    robusttightEleIDCutsV02 = cms.PSet(
        barrel = cms.vdouble(0.0201, 0.0102, 0.0211, 0.00606, -1, -1, 2.34, 3.24, 4.51, 9999., 9999.,9999., 9999.,9999., 9999., 9999.,9999., 9999., 0.000, -9999., 9999., 9999., 9999, -1, 0, 0),
        endcap = cms.vdouble(0.00253, 0.0291, 0.022, 0.0032, -1, -1, 0.826, 2.7, 0.255, 9999., 9999.,9999., 9999.,9999., 9999., 9999.,9999., 9999., 0.000, -9999., 9999., 9999., 9999, -1, 0, 0)
    ),
    robusttightEleIDCutsV03 = cms.PSet(
        barrel = cms.vdouble(0.0201, 0.0102, 0.0211, 0.00606, -1, -1, 2.34, 3.24, 4.51, 9999., 9999.,9999., 9999.,9999., 9999., 9999.,9999., 9999., 0.000, -9999., 9999., 9999., 9999, -1, 0, 0),
        endcap = cms.vdouble(0.00253, 0.0291, 0.022, 0.0032, -1, -1, 0.826, 2.7, 0.255, 9999., 9999.,9999., 9999.,9999., 9999., 9999.,9999., 9999., 0.000, -9999., 9999., 9999., 9999, -1, 0, 0)
    ),
    robusttightEleIDCutsV04 = cms.PSet(
        barrel = cms.vdouble(0.0201, 0.0102, 0.0211, 0.00606, -1, -1, 2.34, 3.24, 4.51, 9999., 9999.,9999., 9999.,9999., 9999., 9999.,9999., 9999., 0.000, -9999., 9999., 9999., 9999, -1, 0, 0),
        endcap = cms.vdouble(0.00253, 0.0291, 0.022, 0.0032, -1, -1, 0.826, 2.7, 0.255, 9999., 9999.,9999., 9999.,9999., 9999., 9999.,9999., 9999., 0.000, -9999., 9999., 9999., 9999, -1, 0, 0)
    ),
    robusttightEleIDCuts = cms.PSet(
        barrel = cms.vdouble(0.0201, 0.0102, 0.0211, 0.00606, -1, -1, 2.34, 3.24, 4.51, 9999., 9999.,9999., 9999.,9999., 9999., 9999.,9999., 9999., 0.000, -9999., 9999., 9999., 9999, -1, 0, 0),
        endcap = cms.vdouble(0.00253, 0.0291, 0.022, 0.0032, -1, -1, 0.826, 2.7, 0.255, 9999., 9999.,9999., 9999.,9999., 9999., 9999.,9999., 9999., 0.000, -9999., 9999., 9999., 9999, -1, 0, 0)
    ),                                

    # variables H/E sigmaietaieta deltaphiin deltaetain e2x5/e5X5 e1x5/e5x5
    #           isoTk (ecalIso+hcal1)(a+b*Et) (ecalIso+hcal1)(a+b*(Et-50)) hcalIso2(barrel/endcap)   
    #Robust High Energy Cuts
    #V00 CMSSW16X optimization 
    #V01 CMSSW22X optimization
    #V02 CMSSW33X optimization
    #V03-V04 CMSSW35X optimization    
    robusthighenergyEleIDCutsV00 = cms.PSet(
        barrel = cms.vdouble(0.050,  0.011, 0.090, 0.005, -1, -1, 9999., 9999., 0, 9999.,9999., 9999.,9999., 9999., 9999.,9999., 0, 9999., 0.000, -9999., 9999., 9999., 9999, -1, 0, 0),
        endcap = cms.vdouble(0.100, 0.0275, 0.090, 0.007, -1, -1, 9999., 9999., 0, 9999.,9999., 9999.,9999., 9999., 9999.,9999., 0, 9999., 0.000, -9999., 9999., 9999., 9999, -1, 0, 0)
    ),
    robusthighenergyEleIDCutsV01 = cms.PSet(
        barrel = cms.vdouble(0.050,   9999, 0.090, 0.005, 0.94, 0.83, 9999., 9999., 0, 9999.,9999., 9999.,9999., 9999., 9999.,9999., 0, 9999., 0.000, -9999., 9999., 9999., 9999, -1, 0, 0),
        endcap = cms.vdouble(0.050, 0.0275, 0.090, 0.007,   -1,   -1, 9999., 9999., 0, 9999.,9999., 9999.,9999., 9999., 9999.,9999., 0, 9999., 0.000, -9999., 9999., 9999., 9999, -1, 0, 0)
    ),
    robusthighenergyEleIDCutsV02 = cms.PSet(
        barrel = cms.vdouble(0.050, 9999, 0.090, 0.005,   0.94, 0.83, 7.5,   2, 0.03, 9999.,  0, 9999.,9999., 9999.,9999., 9999., 9999.,9999., 0.000, -9999., 9999., 9999., 9999, -1, 0, 0),
        endcap = cms.vdouble(0.050, 0.03, 0.090, 0.007,     -1,   -1,  15, 2.5, 0.03,   2.5,  0, 0.5, 9999., 9999.,9999., 9999., 9999.,9999.,0.000, -9999., 9999., 9999., 9999, -1, 0, 0)
    ),
    robusthighenergyEleIDCutsV03 = cms.PSet(
        barrel = cms.vdouble(0.050, 9999, 0.090, 0.005,   0.94, 0.83, 7.5,   2, 0.03, 9999.,  0, 9999.,9999., 9999.,9999., 9999., 9999.,9999., 0.000, -9999., 9999., 9999., 9999, -1, 0, 0),
        endcap = cms.vdouble(0.050, 0.03, 0.090, 0.007,     -1,   -1,  15, 2.5, 0.03,   2.5,  0, 0.5,9999., 9999.,9999., 9999., 9999.,9999., 0.000, -9999., 9999., 9999., 9999, -1, 0, 0)
    ),
    robusthighenergyEleIDCutsV04 = cms.PSet(
        barrel = cms.vdouble(0.050, 9999, 0.090, 0.005,   0.94, 0.83, 7.5,   2, 0.03, 9999.,  0, 9999.,9999., 9999.,9999., 9999., 9999.,9999., 0.000, -9999., 9999., 9999., 9999, -1, 0, 0),
        endcap = cms.vdouble(0.050, 0.03, 0.090, 0.007,     -1,   -1,  15, 2.5, 0.03,   2.5,  0, 0.5,9999., 9999.,9999., 9999., 9999.,9999., 0.000, -9999., 9999., 9999., 9999, -1, 0, 0)
    ),
    robusthighenergyEleIDCuts = cms.PSet(
        barrel = cms.vdouble(0.050, 9999, 0.090, 0.005,   0.94, 0.83, 7.5,   2, 0.03, 9999.,  0, 9999.,9999., 9999.,9999., 9999., 9999.,9999., 0.000, -9999., 9999., 9999., 9999, -1, 0, 0),
        endcap = cms.vdouble(0.050, 0.03, 0.090, 0.007,     -1,   -1,  15, 2.5, 0.03,   2.5,  0, 0.5,9999., 9999.,9999., 9999., 9999.,9999., 0.000, -9999., 9999., 9999., 9999, -1, 0, 0)
    ),
          
    #Class Based Loose Cuts
    #V00 CMSSW16X optimization 
    #V01 CMSSW22X optimization
    #V02 CMSSW33X optimization 
    classbasedlooseEleIDCutsV00 = cms.PSet(
        deltaEtaIn   = cms.vdouble(0.009, 0.0045, 0.0085, 0.0, 0.0105, 0.0068, 0.01, 0.0),
        deltaPhiIn   = cms.vdouble(0.05, 0.025, 0.053, 0.09, 0.07, 0.03, 0.092, 0.092),
        eSeedOverPin = cms.vdouble(0.11, 0.91, 0.11, 0.0, 0.0, 0.85, 0.0, 0.0),
        hOverE       = cms.vdouble(0.115, 0.1, 0.055, 0.0, 0.145, 0.12, 0.15, 0.0),
        sigmaEtaEta  = cms.vdouble(0.014, 0.012, 0.0115, 0.0, 0.0275, 0.0265, 0.0265, 0.0)
        ),
    classbasedlooseEleIDCutsV01 = cms.PSet(
        deltaEtaIn   = cms.vdouble (0.0078, 0.00259, 0.0062, 0.0, 0.0078, 0.0061, 0.0061, 0.0),
        deltaPhiIn   = cms.vdouble (0.053, 0.0189, 0.059, 0.099, 0.0278, 0.0157, 0.042, 0.080),
        eSeedOverPin = cms.vdouble (0.30, 0.92, 0.211, 0.0, 0.42, 0.88, 0.68, 0.0),
        hOverE       = cms.vdouble (0.076, 0.033, 0.070, 0.0, 0.083, 0.0148, 0.033, 0.0),
        sigmaEtaEta  = cms.vdouble (0.0101, 0.0095, 0.0097, 0.0, 0.0271, 0.0267, 0.0259, 0.0)
        ),

    classbasedlooseEleIDCutsV02 = cms.PSet(
        cutdeta = cms.vdouble(
             9.58e-03, 4.06e-03, 1.22e-02, 1.37e-02, 8.37e-03, 1.27e-02,
             1.10e-02, 3.36e-03, 9.77e-03, 1.50e-02, 6.75e-03, 1.09e-02,
             1.40e-02, 5.08e-03, 1.09e-02, 1.46e-02, 5.06e-03, 1.27e-02),
        cutdphi = cms.vdouble(
             3.72e-02, 1.14e-01, 1.18e-01, 4.88e-02, 1.17e-01, 1.19e-01,
             6.06e-02, 5.48e-02, 1.17e-01, 7.00e-02, 3.55e-02, 1.17e-01,
             8.80e-02, 4.50e-02, 1.18e-01, 9.19e-02, 2.36e-02, 5.15e-02),
        cuteopin = cms.vdouble(
             8.78e-01, 8.02e-01, 8.14e-01, 9.42e-01, 7.35e-01, 7.74e-01,
             8.29e-01, 9.09e-01, 8.29e-01, 8.13e-01, 8.60e-01, 8.97e-01,
             8.17e-01, 8.31e-01, 8.18e-01, 8.61e-01, 7.87e-01, 7.89e-01),
        cuthoe = cms.vdouble(
             8.87e-02, 9.34e-02, 9.49e-02, 9.86e-02, 4.31e-02, 8.78e-02,
             9.70e-02, 5.09e-02, 9.80e-02, 9.91e-02, 3.21e-02, 9.28e-02,
             6.63e-02, 7.17e-02, 9.66e-02, 7.58e-02, 1.49e-02, 1.31e-02),
        cutip = cms.vdouble(
             2.46e-02, 7.60e-02, 9.66e-02, 8.85e-02, 4.41e-01, 2.05e-01,
             2.92e-02, 2.93e-02, 6.19e-02, 2.51e-02, 1.59e-01, 8.15e-02,
             7.29e+00, 1.06e-02, 5.76e+00, 6.89e+00, 1.27e+00, 5.89e+00),
        cutisoecal = cms.vdouble(
             3.34e+01, 2.81e+01, 7.32e+00, 2.74e+01, 7.33e+00, 2.17e+01,
             9.38e+01, 1.02e+02, 1.21e+01, 2.60e+01, 8.91e+00, 1.00e+01,
             1.61e+01, 3.13e+01, 1.69e+01, 1.54e+01, 1.33e+01, 3.77e+01),
        cutisohcal = cms.vdouble(
             1.35e+01, 9.93e+00, 7.56e+00, 1.48e+01, 8.10e+00, 1.08e+01,
             4.27e+01, 2.01e+01, 9.11e+00, 1.04e+01, 6.89e+00, 5.59e+00,
             8.53e+00, 9.59e+00, 2.42e+01, 2.78e+00, 8.67e+00, 2.88e-01),
        cutisotk = cms.vdouble(
             2.43e+01, 8.45e+00, 1.44e+01, 2.78e+01, 6.02e+00, 1.05e+01,
             1.41e+01, 1.02e+01, 1.45e+01, 1.91e+01, 6.10e+00, 1.41e+01,
             8.59e+00, 8.33e+00, 8.30e+00, 8.93e+00, 8.60e+00, 1.60e+01),
        cutmishits = cms.vdouble(
             5.50e+00, 1.50e+00, 5.50e+00, 2.50e+00, 2.50e+00, 2.50e+00,
             3.50e+00, 5.50e+00, 5.00e-01, 1.50e+00, 2.50e+00, 5.00e-01,
             1.50e+00, 1.50e+00, 5.00e-01, 5.00e-01, 5.00e-01, 5.00e-01),
        cutsee = cms.vdouble(
             1.72e-02, 1.15e-02, 1.43e-02, 3.44e-02, 2.95e-02, 3.04e-02,
             1.45e-02, 1.08e-02, 1.28e-02, 3.47e-02, 3.07e-02, 3.16e-02,
             1.80e-02, 1.10e-02, 1.32e-02, 3.49e-02, 3.10e-02, 3.27e-02)
        ),

    classbasedlooseEleIDCutsV03 = cms.PSet(
        cutdcotdist = cms.vdouble(
             3.93e-02, 3.92e-02, 3.97e-02, 3.94e-02, 3.93e-02, 3.90e-02, 3.78e-02, 3.88e-02, 3.82e-02,
             3.85e-02, 1.67e-02, 3.25e-03, 3.94e-02, 3.87e-02, 3.88e-02, 2.27e-02, 2.58e-02, 1.27e-02,
             2.98e-02, 3.00e-02, 9.46e-03, 3.90e-02, 2.31e-02, 2.78e-02, 1.62e-03, 3.67e-02, 1.99e-02),
        cutdetain = cms.vdouble(
             9.89e-03, 4.84e-03, 1.46e-02, 1.46e-02, 9.02e-03, 1.72e-02, 1.37e-02, 4.77e-02, 2.75e-02,
             9.67e-03, 3.77e-03, 9.24e-03, 1.30e-02, 6.66e-03, 1.23e-02, 1.25e-02, 2.28e-02, 1.12e-02,
             1.06e-02, 3.80e-03, 8.97e-03, 1.39e-02, 6.67e-03, 1.22e-02, 1.22e-02, 1.93e-02, 2.39e-03),
        cutdphiin = cms.vdouble(
             4.10e-02, 2.75e-01, 3.65e-01, 4.70e-02, 2.73e-01, 2.96e-01, 3.29e-01, 4.65e-01, 6.27e-01,
             5.81e-02, 9.54e-02, 3.27e-01, 7.02e-02, 5.82e-02, 2.79e-01, 1.17e-01, 3.18e-01, 2.46e-01,
             8.21e-02, 5.20e-02, 2.92e-01, 1.16e-01, 4.35e-02, 3.12e-01, 1.18e-01, 2.96e-01, 4.59e-02),
        cuteseedopcor = cms.vdouble(
             7.80e-01, 3.02e-01, 4.83e-01, 9.04e-01, 1.68e-01, 6.45e-01, 1.08e-01, 2.84e-01, 3.24e-01,
             5.91e-01, 2.86e-01, 4.88e-01, 8.13e-01, 7.91e-01, 6.72e-01, 3.98e-01, 8.34e-01, 8.78e-01,
             5.15e-01, 9.37e-01, 8.06e-01, 8.16e-01, 8.50e-01, 5.07e-01, 3.67e-01, 8.30e-01, 6.48e-01),
        cutet = cms.vdouble(
             -1.00e+05, -1.00e+05, -1.00e+05, -1.00e+05, -1.00e+05, -1.00e+05, -1.00e+05, -1.00e+05, -1.00e+05,
             -1.00e+05, -1.00e+05, -1.00e+05, -1.00e+05, -1.00e+05, -1.00e+05, -1.00e+05, -1.00e+05, -1.00e+05,
             1.20e+01, 1.20e+01, 1.20e+01, 1.20e+01, 1.20e+01, 1.20e+01, 1.20e+01, 1.20e+01, 1.25e+01),
        cutfmishits = cms.vdouble(
             4.50e+00, 1.50e+00, 1.50e+00, 2.50e+00, 2.50e+00, 1.50e+00, 2.50e+00, 2.50e+00, 1.50e+00,
             2.50e+00, 1.50e+00, 1.50e+00, 1.50e+00, 1.50e+00, 5.00e-01, 2.50e+00, 2.50e+00, 5.00e-01,
             2.50e+00, 1.50e+00, 5.00e-01, 1.50e+00, 1.50e+00, 5.00e-01, 2.50e+00, 5.00e-01, 5.00e-01),
        cuthoe = cms.vdouble(
             1.66e-01, 7.71e-02, 1.44e-01, 3.70e-01, 4.97e-02, 1.39e-01, 4.01e-01, 2.68e+00, 5.16e-01,
             2.34e-01, 5.56e-02, 1.44e-01, 3.68e-01, 3.10e-02, 1.20e-01, 6.02e-01, 2.01e+00, 1.05e+00,
             1.04e-01, 6.30e-02, 5.65e-02, 3.80e-01, 1.92e-02, 2.94e-02, 5.37e-01, 4.65e+00, 1.87e+00),
        cutip_gsf = cms.vdouble(
             4.31e-02, 7.67e-02, 1.39e-01, 1.01e-01, 1.49e-01, 1.54e-01, 9.32e-01, 1.50e-01, 1.24e-01,
             2.38e-02, 4.67e-02, 7.59e-02, 3.69e-02, 1.47e-01, 9.86e-02, 6.26e-02, 1.95e-01, 1.16e-01,
             1.22e-02, 1.25e-02, 6.93e-02, 1.62e-02, 8.90e-02, 6.73e-02, 4.67e-02, 6.51e-02, 2.21e-02),
        cutiso_sum = cms.vdouble(
             3.15e+01, 1.03e+01, 8.80e+00, 1.10e+01, 6.13e+00, 6.94e+00, 7.52e+00, 9.00e+00, 3.50e+00,
             1.00e+05, 1.00e+05, 1.00e+05, 1.00e+05, 1.00e+05, 1.00e+05, 1.00e+05, 1.00e+05, 1.00e+05,
             1.00e+05, 1.00e+05, 1.00e+05, 1.00e+05, 1.00e+05, 1.00e+05, 1.00e+05, 1.00e+05, 1.00e+05),
        cutiso_sumoet = cms.vdouble(
             2.89e+01, 1.53e+01, 1.20e+01, 1.83e+01, 7.17e+00, 9.42e+00, 1.10e+01, 9.81e+00, 3.94e+00,
             2.27e+01, 1.59e+01, 1.23e+01, 1.70e+01, 7.58e+00, 8.89e+00, 1.52e+01, 1.27e+01, 6.17e+00,
             2.08e+01, 2.12e+01, 1.72e+01, 1.55e+01, 9.37e+00, 1.06e+01, 1.98e+01, 2.21e+01, 1.56e+01),
        cutsee = cms.vdouble(
             1.75e-02, 1.27e-02, 1.77e-02, 3.73e-02, 3.14e-02, 3.29e-02, 1.57e-02, 4.09e-02, 1.40e-01,
             1.69e-02, 1.06e-02, 1.42e-02, 3.63e-02, 3.22e-02, 3.54e-02, 1.17e-02, 3.72e-02, 2.82e+01,
             1.71e-02, 1.13e-02, 1.40e-02, 4.03e-02, 3.23e-02, 4.11e-02, 1.04e-02, 4.36e-02, 1.14e-02)
        ),

    classbasedlooseEleIDCutsV04 = cms.PSet(
        cutdcotdist = cms.vdouble(
             3.93e-02, 3.92e-02, 3.97e-02, 3.94e-02, 3.93e-02, 3.90e-02, 3.78e-02, 3.88e-02, 3.82e-02,
             3.85e-02, 1.67e-02, 3.25e-03, 3.94e-02, 3.87e-02, 3.88e-02, 2.27e-02, 2.58e-02, 1.27e-02,
             2.98e-02, 3.00e-02, 9.46e-03, 3.90e-02, 2.31e-02, 2.78e-02, 1.62e-03, 3.67e-02, 1.99e-02),
        cutdetain = cms.vdouble(
             9.89e-03, 4.84e-03, 1.46e-02, 1.46e-02, 9.02e-03, 1.72e-02, 1.37e-02, 4.77e-02, 2.75e-02,
             9.67e-03, 3.77e-03, 9.24e-03, 1.30e-02, 6.66e-03, 1.23e-02, 1.25e-02, 2.28e-02, 1.12e-02,
             1.06e-02, 3.80e-03, 8.97e-03, 1.39e-02, 6.67e-03, 1.22e-02, 1.22e-02, 1.93e-02, 2.39e-03),
        cutdphiin = cms.vdouble(
             4.10e-02, 2.75e-01, 3.65e-01, 4.70e-02, 2.73e-01, 2.96e-01, 3.29e-01, 4.65e-01, 6.27e-01,
             5.81e-02, 9.54e-02, 3.27e-01, 7.02e-02, 5.82e-02, 2.79e-01, 1.17e-01, 3.18e-01, 2.46e-01,
             8.21e-02, 5.20e-02, 2.92e-01, 1.16e-01, 4.35e-02, 3.12e-01, 1.18e-01, 2.96e-01, 4.59e-02),
        cuteseedopcor = cms.vdouble(
             7.80e-01, 3.02e-01, 4.83e-01, 9.04e-01, 1.68e-01, 6.45e-01, 1.08e-01, 2.84e-01, 3.24e-01,
             5.91e-01, 2.86e-01, 4.88e-01, 8.13e-01, 7.91e-01, 6.72e-01, 3.98e-01, 8.34e-01, 8.78e-01,
             5.15e-01, 9.37e-01, 8.06e-01, 8.16e-01, 8.50e-01, 5.07e-01, 3.67e-01, 8.30e-01, 6.48e-01),
        cutet = cms.vdouble(
             -1.00e+05, -1.00e+05, -1.00e+05, -1.00e+05, -1.00e+05, -1.00e+05, -1.00e+05, -1.00e+05, -1.00e+05,
             -1.00e+05, -1.00e+05, -1.00e+05, -1.00e+05, -1.00e+05, -1.00e+05, -1.00e+05, -1.00e+05, -1.00e+05,
             1.20e+01, 1.20e+01, 1.20e+01, 1.20e+01, 1.20e+01, 1.20e+01, 1.20e+01, 1.20e+01, 1.25e+01),
        cutfmishits = cms.vdouble(
             4.50e+00, 1.50e+00, 1.50e+00, 2.50e+00, 2.50e+00, 1.50e+00, 2.50e+00, 2.50e+00, 1.50e+00,
             2.50e+00, 1.50e+00, 1.50e+00, 1.50e+00, 1.50e+00, 5.00e-01, 2.50e+00, 2.50e+00, 5.00e-01,
             2.50e+00, 1.50e+00, 5.00e-01, 1.50e+00, 1.50e+00, 5.00e-01, 2.50e+00, 5.00e-01, 5.00e-01),
        cuthoe = cms.vdouble(
             1.66e-01, 7.71e-02, 1.44e-01, 3.70e-01, 4.97e-02, 1.39e-01, 4.01e-01, 2.68e+00, 5.16e-01,
             2.34e-01, 5.56e-02, 1.44e-01, 3.68e-01, 3.10e-02, 1.20e-01, 6.02e-01, 2.01e+00, 1.05e+00,
             1.04e-01, 6.30e-02, 5.65e-02, 3.80e-01, 1.92e-02, 2.94e-02, 5.37e-01, 4.65e+00, 1.87e+00),
        cutip_gsf = cms.vdouble(
             4.31e-02, 7.67e-02, 1.39e-01, 1.01e-01, 1.49e-01, 1.54e-01, 9.32e-01, 1.50e-01, 1.24e-01,
             2.38e-02, 4.67e-02, 7.59e-02, 3.69e-02, 1.47e-01, 9.86e-02, 6.26e-02, 1.95e-01, 1.16e-01,
             1.22e-02, 1.25e-02, 6.93e-02, 1.62e-02, 8.90e-02, 6.73e-02, 4.67e-02, 6.51e-02, 2.21e-02),
        cutiso_sum = cms.vdouble(
             3.15e+01, 1.03e+01, 8.80e+00, 1.10e+01, 6.13e+00, 6.94e+00, 7.52e+00, 9.00e+00, 3.50e+00,
             1.00e+05, 1.00e+05, 1.00e+05, 1.00e+05, 1.00e+05, 1.00e+05, 1.00e+05, 1.00e+05, 1.00e+05,
             1.00e+05, 1.00e+05, 1.00e+05, 1.00e+05, 1.00e+05, 1.00e+05, 1.00e+05, 1.00e+05, 1.00e+05),
        cutiso_sumoet = cms.vdouble(
             2.89e+01, 1.53e+01, 1.20e+01, 1.83e+01, 7.17e+00, 9.42e+00, 1.10e+01, 9.81e+00, 3.94e+00,
             2.27e+01, 1.59e+01, 1.23e+01, 1.70e+01, 7.58e+00, 8.89e+00, 1.52e+01, 1.27e+01, 6.17e+00,
             2.08e+01, 2.12e+01, 1.72e+01, 1.55e+01, 9.37e+00, 1.06e+01, 1.98e+01, 2.21e+01, 1.56e+01),
        cutsee = cms.vdouble(
             1.75e-02, 1.27e-02, 1.77e-02, 3.73e-02, 3.14e-02, 3.29e-02, 1.57e-02, 4.09e-02, 1.40e-01,
             1.69e-02, 1.06e-02, 1.42e-02, 3.63e-02, 3.22e-02, 3.54e-02, 1.17e-02, 3.72e-02, 2.82e+01,
             1.71e-02, 1.13e-02, 1.40e-02, 4.03e-02, 3.23e-02, 4.11e-02, 1.04e-02, 4.36e-02, 1.14e-02)
        ),

    classbasedlooseEleIDCutsV06 = cms.PSet(
        cutdetain = cms.vdouble(1.37e-02, 6.78e-03, 2.41e-02, 1.87e-02, 1.61e-02, 2.24e-02, 2.52e-02, 3.08e-02, 2.73e-02),
        cutdetainl = cms.vdouble(1.24e-02, 5.03e-03, 2.57e-02, 2.28e-02, 1.18e-02, 1.78e-02, 1.88e-02, 1.40e-01, 2.40e-02),
        cutdphiin = cms.vdouble(8.97e-02, 2.62e-01, 3.53e-01, 1.16e-01, 3.57e-01, 3.19e-01, 3.42e-01, 4.04e-01, 3.36e-01),
        cutdphiinl = cms.vdouble(7.47e-02, 2.50e-01, 3.56e-01, 9.56e-02, 3.47e-01, 3.26e-01, 3.33e-01, 6.47e-01, 2.89e-01),
        cuteseedopcor = cms.vdouble(6.30e-01, 8.20e-01, 4.01e-01, 7.18e-01, 4.00e-01, 4.58e-01, 1.50e-01, 6.64e-01, 3.73e-01),
        cutfmishits = cms.vdouble(4.50e+00, 1.50e+00, 1.50e+00, 2.50e+00, 2.50e+00, 1.50e+00, 4.50e+00, 3.50e+00, 3.50e+00),
        cutdcotdist = cms.vdouble(9999., 9999., 9999., 9999., 9999., 9999., 9999., 9999., 9999.),
        cuthoe = cms.vdouble(2.47e-01, 1.37e-01, 1.47e-01, 3.71e-01, 5.88e-02, 1.47e-01, 5.20e-01, 4.52e-01, 4.04e-01),
        cuthoel = cms.vdouble(2.36e-01, 1.26e-01, 1.47e-01, 3.75e-01, 3.92e-02, 1.45e-01, 3.65e-01, 3.83e-01, 3.84e-01),
        cutip_gsf = cms.vdouble(5.51e-02, 7.65e-02, 1.43e-01, 8.74e-02, 5.94e-01, 3.70e-01, 9.13e-02, 1.15e+00, 2.31e-01),
        cutip_gsfl = cms.vdouble(1.86e-02, 7.59e-02, 1.38e-01, 4.73e-02, 6.20e-01, 3.04e-01, 1.09e-01, 7.75e-01, 4.79e-02),
        cutiso_sum = cms.vdouble(3.30e+01, 1.70e+01, 1.79e+01, 1.88e+01, 8.55e+00, 1.25e+01, 1.76e+01, 1.85e+01, 2.98e+00),
        cutiso_sumoet = cms.vdouble(3.45e+01, 1.27e+01, 1.21e+01, 1.99e+01, 6.35e+00, 8.85e+00, 1.40e+01, 1.05e+01, 9.74e+00),
        cutiso_sumoetl = cms.vdouble(1.13e+01, 9.05e+00, 9.07e+00, 9.94e+00, 5.25e+00, 6.15e+00, 1.07e+01, 1.08e+01, 4.40e+00),
        cutsee = cms.vdouble(1.76e-02, 1.25e-02, 1.81e-02, 4.15e-02, 3.64e-02, 4.18e-02, 1.46e-02, 6.78e-02, 1.33e-01),
        cutseel = cms.vdouble(1.64e-02, 1.18e-02, 1.50e-02, 5.23e-02, 3.26e-02, 4.56e-02, 1.85e-02, 5.89e-02, 5.44e-02)
        ),

    classbasedlooseEleIDCuts = cms.PSet(
        cutdetain = cms.vdouble(1.37e-02, 6.78e-03, 2.41e-02, 1.87e-02, 1.61e-02, 2.24e-02, 2.52e-02, 3.08e-02, 2.73e-02),
        cutdetainl = cms.vdouble(1.24e-02, 5.03e-03, 2.57e-02, 2.28e-02, 1.18e-02, 1.78e-02, 1.88e-02, 1.40e-01, 2.40e-02),
        cutdphiin = cms.vdouble(8.97e-02, 2.62e-01, 3.53e-01, 1.16e-01, 3.57e-01, 3.19e-01, 3.42e-01, 4.04e-01, 3.36e-01),
        cutdphiinl = cms.vdouble(7.47e-02, 2.50e-01, 3.56e-01, 9.56e-02, 3.47e-01, 3.26e-01, 3.33e-01, 6.47e-01, 2.89e-01),
        cuteseedopcor = cms.vdouble(6.30e-01, 8.20e-01, 4.01e-01, 7.18e-01, 4.00e-01, 4.58e-01, 1.50e-01, 6.64e-01, 3.73e-01),
        cutfmishits = cms.vdouble(4.50e+00, 1.50e+00, 1.50e+00, 2.50e+00, 2.50e+00, 1.50e+00, 4.50e+00, 3.50e+00, 3.50e+00),
        cutdcotdist = cms.vdouble(9999., 9999., 9999., 9999., 9999., 9999., 9999., 9999., 9999.),
        cuthoe = cms.vdouble(2.47e-01, 1.37e-01, 1.47e-01, 3.71e-01, 5.88e-02, 1.47e-01, 5.20e-01, 4.52e-01, 4.04e-01),
        cuthoel = cms.vdouble(2.36e-01, 1.26e-01, 1.47e-01, 3.75e-01, 3.92e-02, 1.45e-01, 3.65e-01, 3.83e-01, 3.84e-01),
        cutip_gsf = cms.vdouble(5.51e-02, 7.65e-02, 1.43e-01, 8.74e-02, 5.94e-01, 3.70e-01, 9.13e-02, 1.15e+00, 2.31e-01),
        cutip_gsfl = cms.vdouble(1.86e-02, 7.59e-02, 1.38e-01, 4.73e-02, 6.20e-01, 3.04e-01, 1.09e-01, 7.75e-01, 4.79e-02),
        cutiso_sum = cms.vdouble(3.30e+01, 1.70e+01, 1.79e+01, 1.88e+01, 8.55e+00, 1.25e+01, 1.76e+01, 1.85e+01, 2.98e+00),
        cutiso_sumoet = cms.vdouble(3.45e+01, 1.27e+01, 1.21e+01, 1.99e+01, 6.35e+00, 8.85e+00, 1.40e+01, 1.05e+01, 9.74e+00),
        cutiso_sumoetl = cms.vdouble(1.13e+01, 9.05e+00, 9.07e+00, 9.94e+00, 5.25e+00, 6.15e+00, 1.07e+01, 1.08e+01, 4.40e+00),
        cutsee = cms.vdouble(1.76e-02, 1.25e-02, 1.81e-02, 4.15e-02, 3.64e-02, 4.18e-02, 1.46e-02, 6.78e-02, 1.33e-01),
        cutseel = cms.vdouble(1.64e-02, 1.18e-02, 1.50e-02, 5.23e-02, 3.26e-02, 4.56e-02, 1.85e-02, 5.89e-02, 5.44e-02)
        ),

 
    #Class Based Tight Cuts
    #V00 CMSSW16X optimization 
    #V01 CMSSW22X optimization
    #V02 CMSSW33X optimization
    #V03-V04 CMSSW35X optimization
    classbasedtightEleIDCutsV00 = cms.PSet(
        deltaEtaIn   = cms.vdouble(0.0055, 0.003, 0.0065, 0.0, 0.006, 0.0055, 0.0075, 0.0),
        deltaPhiIn   = cms.vdouble(0.032, 0.016, 0.0525, 0.09, 0.025, 0.035, 0.065, 0.092),
        eSeedOverPin = cms.vdouble(0.24, 0.94, 0.11, 0.0, 0.32, 0.83, 0.0, 0.0),
        hOverE       = cms.vdouble(0.05, 0.042, 0.045, 0.0, 0.055, 0.037, 0.05, 0.0),
        sigmaEtaEta  = cms.vdouble(0.0125, 0.011, 0.01, 0.0, 0.0265, 0.0252, 0.026, 0.0)
    ),
    classbasedtightEleIDCutsV01 = cms.PSet(
        deltaEtaIn   = cms.vdouble (0.0043, 0.00282, 0.0036, 0.0, 0.0066, 0.0049, 0.0041, 0.0),
        deltaPhiIn   = cms.vdouble (0.0225, 0.0114, 0.0234, 0.039, 0.0215, 0.0095, 0.0148, 0.0167),
        eSeedOverPin = cms.vdouble (0.32, 0.94, 0.221, 0.0, 0.74, 0.89, 0.66, 0.0),
        hOverE       = cms.vdouble (0.056, 0.0221, 0.037, 0.0, 0.0268, 0.0102, 0.0104, 0.0),
        sigmaEtaEta  = cms.vdouble (0.0095, 0.0094, 0.0094, 0.0, 0.0260, 0.0257, 0.0246, 0.0)
    ),

    classbasedtightEleIDCutsV02 = cms.PSet(
        cutdeta = cms.vdouble(
              9.15e-03, 3.02e-03, 6.10e-03, 1.35e-02, 5.65e-03, 7.93e-03,
              1.02e-02, 2.66e-03, 1.06e-02, 9.03e-03, 7.66e-03, 7.23e-03,
              1.16e-02, 2.03e-03, 6.59e-03, 1.48e-02, 5.55e-03, 1.28e-02),
        cutdphi = cms.vdouble(
              3.69e-02, 3.07e-02, 1.17e-01, 4.75e-02, 2.16e-02, 1.17e-01,
              3.72e-02, 2.46e-02, 4.26e-02, 6.12e-02, 1.42e-02, 3.90e-02,
              7.37e-02, 5.66e-02, 3.59e-02, 1.87e-02, 1.20e-02, 3.58e-02),
        cuteopin = cms.vdouble(
              8.78e-01, 8.59e-01, 8.74e-01, 9.44e-01, 7.37e-01, 7.73e-01,
              8.60e-01, 9.67e-01, 9.17e-01, 8.12e-01, 9.15e-01, 1.01e+00,
              8.47e-01, 9.53e-01, 9.79e-01, 8.41e-01, 7.71e-01, 1.09e+00),
        cuthoe = cms.vdouble(
              8.71e-02, 2.89e-02, 7.83e-02, 9.46e-02, 2.45e-02, 3.63e-02,
              6.71e-02, 4.80e-02, 6.14e-02, 9.24e-02, 1.58e-02, 4.90e-02,
              3.82e-02, 9.15e-02, 4.51e-02, 4.52e-02, 1.96e-03, 4.30e-03),
        cutip = cms.vdouble(
              2.39e-02, 2.70e-02, 7.68e-02, 2.31e-02, 1.78e-01, 9.57e-02,
              1.02e-02, 1.68e-02, 4.30e-02, 1.66e-02, 5.94e-02, 3.08e-02,
              2.10e+00, 5.27e-03, 3.17e+00, 4.91e+00, 7.69e-01, 5.90e+00),
        cutisoecal = cms.vdouble(
              2.00e+01, 2.72e+01, 4.48e+00, 1.35e+01, 4.56e+00, 3.19e+00,
              1.22e+01, 1.31e+01, 7.42e+00, 7.67e+00, 4.12e+00, 4.85e+00,
              1.01e+01, 1.24e+01, 1.11e+01, 1.10e+01, 1.06e+01, 1.34e+01),
        cutisohcal = cms.vdouble(
              1.09e+01, 7.01e+00, 8.75e+00, 3.51e+00, 7.75e+00, 1.62e+00,
              1.16e+01, 9.90e+00, 4.97e+00, 5.33e+00, 3.18e+00, 2.32e+00,
              1.64e-01, 5.46e+00, 1.20e+01, 6.04e-03, 4.10e+00, 6.28e-04),
        cutisotk = cms.vdouble(
              6.53e+00, 4.60e+00, 6.00e+00, 8.63e+00, 3.11e+00, 7.77e+00,
              5.42e+00, 4.81e+00, 4.06e+00, 6.47e+00, 2.80e+00, 3.45e+00,
              5.29e+00, 5.18e+00, 1.54e+01, 5.38e+00, 4.47e+00, 3.47e-02),
        cutmishits = cms.vdouble(
              5.50e+00, 1.50e+00, 5.00e-01, 1.50e+00, 2.50e+00, 5.00e-01,
              3.50e+00, 5.50e+00, 5.00e-01, 5.00e-01, 5.00e-01, 5.00e-01,
              5.00e-01, 1.50e+00, 5.00e-01, 5.00e-01, 5.00e-01, 5.00e-01),
        cutsee = cms.vdouble(
              1.31e-02, 1.06e-02, 1.15e-02, 3.06e-02, 2.80e-02, 2.93e-02,
              1.31e-02, 1.06e-02, 1.15e-02, 3.17e-02, 2.90e-02, 2.89e-02,
              1.42e-02, 1.06e-02, 1.03e-02, 3.50e-02, 2.96e-02, 3.33e-02)
        ),


    classbasedtightEleIDCutsV03 = cms.PSet(
        cutdcotdist = cms.vdouble(
              3.93e-02, 2.56e-02, 6.91e-03, 3.94e-02, 3.86e-02, 3.90e-02, 3.25e-02, 3.84e-02, 3.82e-02,
              2.45e-02, 2.81e-04, 5.46e-05, 3.42e-02, 2.32e-02, 1.07e-03, 1.78e-02, 1.93e-02, 7.58e-04,
              1.08e-04, 2.48e-02, 4.58e-04, 1.29e-02, 1.19e-03, 1.82e-02, 4.53e-05, 1.89e-02, 9.28e-04),
        cutdetain = cms.vdouble(
              8.11e-03, 3.41e-03, 6.33e-03, 1.03e-02, 6.67e-03, 1.00e-02, 1.06e-02, 1.45e-02, 1.63e-02,
              7.60e-03, 2.59e-03, 5.11e-03, 9.41e-03, 4.30e-03, 8.57e-03, 1.20e-02, 1.69e-02, 1.72e-03,
              8.61e-03, 3.62e-03, 6.01e-03, 9.25e-03, 4.89e-03, 8.32e-03, 1.19e-02, 1.69e-02, 9.96e-04),
        cutdphiin = cms.vdouble(
              4.04e-02, 4.99e-02, 2.63e-01, 4.20e-02, 4.84e-02, 2.41e-01, 2.42e-01, 2.31e-01, 2.86e-01,
              5.52e-02, 3.38e-02, 1.54e-01, 6.23e-02, 1.83e-02, 3.92e-02, 5.47e-02, 5.88e-02, 6.54e-03,
              4.20e-02, 2.17e-02, 8.85e-02, 4.45e-02, 1.41e-02, 2.34e-02, 6.50e-02, 2.58e-02, 3.46e-02),
        cuteseedopcor = cms.vdouble(
              7.84e-01, 3.66e-01, 5.70e-01, 9.11e-01, 2.98e-01, 6.45e-01, 5.10e-01, 4.97e-01, 9.32e-01,
              8.35e-01, 9.68e-01, 9.69e-01, 9.23e-01, 8.98e-01, 9.80e-01, 6.30e-01, 9.71e-01, 1.00e+00,
              5.15e-01, 9.63e-01, 9.86e-01, 8.23e-01, 8.79e-01, 1.01e+00, 9.31e-01, 9.37e-01, 1.05e+00),
        cutet = cms.vdouble(
              -1.00e+05, -1.00e+05, -1.00e+05, -1.00e+05, -1.00e+05, -1.00e+05, -1.00e+05, -1.00e+05, -1.00e+05,
              -1.00e+05, -1.00e+05, -1.00e+05, -1.00e+05, -1.00e+05, -1.00e+05, -1.00e+05, -1.00e+05, -1.00e+05,
              1.37e+01, 1.32e+01, 1.36e+01, 1.42e+01, 1.41e+01, 1.39e+01, 1.29e+01, 1.49e+01, 1.77e+01),
        cutfmishits = cms.vdouble(
              2.50e+00, 1.50e+00, 1.50e+00, 1.50e+00, 1.50e+00, 5.00e-01, 2.50e+00, 5.00e-01, 5.00e-01,
              2.50e+00, 1.50e+00, 5.00e-01, 5.00e-01, 5.00e-01, 5.00e-01, 5.00e-01, 5.00e-01, -5.00e-01,
              2.50e+00, 1.50e+00, 5.00e-01, 5.00e-01, 5.00e-01, 5.00e-01, 5.00e-01, 5.00e-01, 5.00e-01),
        cuthoe = cms.vdouble(
              7.83e-02, 3.87e-02, 1.05e-01, 1.18e-01, 2.27e-02, 6.20e-02, 1.30e-01, 2.47e+00, 3.80e-01,
              8.88e-02, 5.03e-02, 9.55e-02, 7.41e-02, 1.50e-02, 3.00e-02, 5.89e-01, 1.13e+00, 6.12e-01,
              4.94e-02, 4.61e-02, 2.92e-02, 3.69e-02, 1.13e-02, 1.45e-02, 1.24e-01, 2.05e+00, 6.10e-01),
        cutip_gsf = cms.vdouble(
              2.13e-02, 4.22e-02, 6.32e-02, 3.61e-02, 7.30e-02, 1.26e-01, 1.71e-01, 1.19e-01, 3.72e-02,
              1.31e-02, 1.46e-02, 5.64e-02, 1.52e-02, 2.22e-02, 2.68e-02, 3.14e-02, 8.84e-02, 3.74e-03,
              8.52e-03, 7.61e-03, 1.43e-02, 1.06e-02, 1.27e-02, 1.19e-02, 1.23e-02, 2.35e-02, 3.63e-03),
        cutiso_sum = cms.vdouble(
              1.18e+01, 8.31e+00, 6.26e+00, 6.18e+00, 3.28e+00, 4.38e+00, 4.17e+00, 5.40e+00, 1.57e+00,
              1.00e+05, 1.00e+05, 1.00e+05, 1.00e+05, 1.00e+05, 1.00e+05, 1.00e+05, 1.00e+05, 1.00e+05,
              1.00e+05, 1.00e+05, 1.00e+05, 1.00e+05, 1.00e+05, 1.00e+05, 1.00e+05, 1.00e+05, 1.00e+05),
        cutiso_sumoet = cms.vdouble(
              1.37e+01, 1.16e+01, 7.14e+00, 9.98e+00, 3.52e+00, 4.87e+00, 6.24e+00, 7.96e+00, 2.53e+00,
              1.12e+01, 1.19e+01, 7.88e+00, 8.16e+00, 5.58e+00, 5.03e+00, 1.14e+01, 8.15e+00, 5.79e+00,
              1.04e+01, 1.11e+01, 1.04e+01, 7.47e+00, 5.08e+00, 5.90e+00, 1.18e+01, 1.41e+01, 1.17e+01),
        cutsee = cms.vdouble(
              1.43e-02, 1.05e-02, 1.23e-02, 3.24e-02, 3.07e-02, 3.01e-02, 1.09e-02, 2.70e-02, 2.92e-02,
              1.33e-02, 1.04e-02, 1.16e-02, 3.32e-02, 2.96e-02, 3.10e-02, 9.81e-03, 3.07e-02, 7.20e-02,
              1.49e-02, 1.05e-02, 1.10e-02, 3.42e-02, 3.07e-02, 3.03e-02, 9.54e-03, 2.65e-02, 1.01e-02)
        ),


    classbasedtightEleIDCutsV04 = cms.PSet(
        cutdcotdist = cms.vdouble(
              3.93e-02, 2.56e-02, 6.91e-03, 3.94e-02, 3.86e-02, 3.90e-02, 3.25e-02, 3.84e-02, 3.82e-02,
              2.45e-02, 2.81e-04, 5.46e-05, 3.42e-02, 2.32e-02, 1.07e-03, 1.78e-02, 1.93e-02, 7.58e-04,
              1.08e-04, 2.48e-02, 4.58e-04, 1.29e-02, 1.19e-03, 1.82e-02, 4.53e-05, 1.89e-02, 9.28e-04),
        cutdetain = cms.vdouble(
              8.11e-03, 3.41e-03, 6.33e-03, 1.03e-02, 6.67e-03, 1.00e-02, 1.06e-02, 1.45e-02, 1.63e-02,
              7.60e-03, 2.59e-03, 5.11e-03, 9.41e-03, 4.30e-03, 8.57e-03, 1.20e-02, 1.69e-02, 1.72e-03,
              8.61e-03, 3.62e-03, 6.01e-03, 9.25e-03, 4.89e-03, 8.32e-03, 1.19e-02, 1.69e-02, 9.96e-04),
        cutdphiin = cms.vdouble(
              4.04e-02, 4.99e-02, 2.63e-01, 4.20e-02, 4.84e-02, 2.41e-01, 2.42e-01, 2.31e-01, 2.86e-01,
              5.52e-02, 3.38e-02, 1.54e-01, 6.23e-02, 1.83e-02, 3.92e-02, 5.47e-02, 5.88e-02, 6.54e-03,
              4.20e-02, 2.17e-02, 8.85e-02, 4.45e-02, 1.41e-02, 2.34e-02, 6.50e-02, 2.58e-02, 3.46e-02),
        cuteseedopcor = cms.vdouble(
              7.84e-01, 3.66e-01, 5.70e-01, 9.11e-01, 2.98e-01, 6.45e-01, 5.10e-01, 4.97e-01, 9.32e-01,
              8.35e-01, 9.68e-01, 9.69e-01, 9.23e-01, 8.98e-01, 9.80e-01, 6.30e-01, 9.71e-01, 1.00e+00,
              5.15e-01, 9.63e-01, 9.86e-01, 8.23e-01, 8.79e-01, 1.01e+00, 9.31e-01, 9.37e-01, 1.05e+00),
        cutet = cms.vdouble(
              -1.00e+05, -1.00e+05, -1.00e+05, -1.00e+05, -1.00e+05, -1.00e+05, -1.00e+05, -1.00e+05, -1.00e+05,
              -1.00e+05, -1.00e+05, -1.00e+05, -1.00e+05, -1.00e+05, -1.00e+05, -1.00e+05, -1.00e+05, -1.00e+05,
              1.37e+01, 1.32e+01, 1.36e+01, 1.42e+01, 1.41e+01, 1.39e+01, 1.29e+01, 1.49e+01, 1.77e+01),
        cutfmishits = cms.vdouble(
             2.50e+00, 1.50e+00, 1.50e+00, 1.50e+00, 1.50e+00, 5.00e-01, 2.50e+00, 5.00e-01, 5.00e-01,
             2.50e+00, 1.50e+00, 5.00e-01, 5.00e-01, 5.00e-01, 5.00e-01, 5.00e-01, 5.00e-01, -5.00e-01,
             2.50e+00, 1.50e+00, 5.00e-01, 5.00e-01, 5.00e-01, 5.00e-01, 5.00e-01, 5.00e-01, 5.00e-01),
        cuthoe = cms.vdouble(
             7.83e-02, 3.87e-02, 1.05e-01, 1.18e-01, 2.27e-02, 6.20e-02, 1.30e-01, 2.47e+00, 3.80e-01,
             8.88e-02, 5.03e-02, 9.55e-02, 7.41e-02, 1.50e-02, 3.00e-02, 5.89e-01, 1.13e+00, 6.12e-01,
             4.94e-02, 4.61e-02, 2.92e-02, 3.69e-02, 1.13e-02, 1.45e-02, 1.24e-01, 2.05e+00, 6.10e-01),
        cutip_gsf = cms.vdouble(
             2.13e-02, 4.22e-02, 6.32e-02, 3.61e-02, 7.30e-02, 1.26e-01, 1.71e-01, 1.19e-01, 3.72e-02,
             1.31e-02, 1.46e-02, 5.64e-02, 1.52e-02, 2.22e-02, 2.68e-02, 3.14e-02, 8.84e-02, 3.74e-03,
             8.52e-03, 7.61e-03, 1.43e-02, 1.06e-02, 1.27e-02, 1.19e-02, 1.23e-02, 2.35e-02, 3.63e-03),
        cutiso_sum = cms.vdouble(
             1.18e+01, 8.31e+00, 6.26e+00, 6.18e+00, 3.28e+00, 4.38e+00, 4.17e+00, 5.40e+00, 1.57e+00,
             1.00e+05, 1.00e+05, 1.00e+05, 1.00e+05, 1.00e+05, 1.00e+05, 1.00e+05, 1.00e+05, 1.00e+05,
             1.00e+05, 1.00e+05, 1.00e+05, 1.00e+05, 1.00e+05, 1.00e+05, 1.00e+05, 1.00e+05, 1.00e+05),
        cutiso_sumoet = cms.vdouble(
             1.37e+01, 1.16e+01, 7.14e+00, 9.98e+00, 3.52e+00, 4.87e+00, 6.24e+00, 7.96e+00, 2.53e+00,
             1.12e+01, 1.19e+01, 7.88e+00, 8.16e+00, 5.58e+00, 5.03e+00, 1.14e+01, 8.15e+00, 5.79e+00,
             1.04e+01, 1.11e+01, 1.04e+01, 7.47e+00, 5.08e+00, 5.90e+00, 1.18e+01, 1.41e+01, 1.17e+01),
        cutsee = cms.vdouble(
             1.43e-02, 1.05e-02, 1.23e-02, 3.24e-02, 3.07e-02, 3.01e-02, 1.09e-02, 2.70e-02, 2.92e-02,
             1.33e-02, 1.04e-02, 1.16e-02, 3.32e-02, 2.96e-02, 3.10e-02, 9.81e-03, 3.07e-02, 7.20e-02,
             1.49e-02, 1.05e-02, 1.10e-02, 3.42e-02, 3.07e-02, 3.03e-02, 9.54e-03, 2.65e-02, 1.01e-02)
        ),

    classbasedtightEleIDCutsV06 = cms.PSet(
        cutdetain = cms.vdouble(1.16e-02, 4.49e-03, 9.38e-03, 1.84e-02, 6.78e-03, 1.09e-02, 2.52e-02, 2.68e-02, 1.39e-02),
        cutdetainl = cms.vdouble(8.16e-03, 4.01e-03, 8.10e-03, 1.90e-02, 5.88e-03, 8.93e-03, 1.71e-02, 4.34e-02, 1.43e-02),
        cutdphiin = cms.vdouble(8.97e-02, 9.93e-02, 2.95e-01, 9.79e-02, 1.51e-01, 2.52e-01, 3.41e-01, 3.08e-01, 3.28e-01),
        cutdphiinl = cms.vdouble(6.10e-02, 1.40e-01, 2.86e-01, 9.21e-02, 1.97e-01, 2.40e-01, 3.33e-01, 3.03e-01, 2.58e-01),
        cuteseedopcor = cms.vdouble(6.37e-01, 9.43e-01, 7.42e-01, 7.48e-01, 7.63e-01, 6.31e-01, 2.14e-01, 8.73e-01, 4.73e-01),
        cutfmishits = cms.vdouble(1.50e+00, 1.50e+00, 1.50e+00, 2.50e+00, 2.50e+00, 1.50e+00, 1.50e+00, 2.50e+00, 5.00e-01),
        cutdcotdist = cms.vdouble(9999., 9999., 9999., 9999., 9999., 9999., 9999., 9999., 9999.),
        cuthoe = cms.vdouble(2.15e-01, 6.08e-02, 1.47e-01, 3.69e-01, 3.49e-02, 1.02e-01, 5.20e-01, 4.22e-01, 4.04e-01),
        cuthoel = cms.vdouble(2.28e-01, 8.36e-02, 1.43e-01, 3.70e-01, 3.92e-02, 9.79e-02, 3.00e-01, 3.81e-01, 3.39e-01),
        cutip_gsf = cms.vdouble(1.31e-02, 5.86e-02, 8.39e-02, 3.66e-02, 4.52e-01, 2.04e-01, 9.13e-02, 8.02e-02, 7.31e-02),
        cutip_gsfl = cms.vdouble(1.19e-02, 5.27e-02, 4.71e-02, 2.12e-02, 2.33e-01, 2.67e-01, 1.09e-01, 1.22e-01, 4.79e-02),
        cutiso_sum = cms.vdouble(1.55e+01, 1.22e+01, 1.22e+01, 1.17e+01, 7.16e+00, 9.71e+00, 8.66e+00, 1.19e+01, 2.98e+00),
        cutiso_sumoet = cms.vdouble(1.19e+01, 7.81e+00, 6.28e+00, 8.92e+00, 4.65e+00, 5.49e+00, 9.36e+00, 8.84e+00, 5.94e+00),
        cutiso_sumoetl = cms.vdouble(6.21e+00, 6.81e+00, 5.30e+00, 5.39e+00, 2.73e+00, 4.73e+00, 4.84e+00, 3.46e+00, 3.73e+00),
        cutsee = cms.vdouble(1.45e-02, 1.16e-02, 1.20e-02, 3.90e-02, 2.97e-02, 3.11e-02, 9.87e-03, 3.47e-02, 9.17e-02),
        cutseel = cms.vdouble(1.32e-02, 1.17e-02, 1.12e-02, 3.87e-02, 2.81e-02, 2.87e-02, 9.87e-03, 2.96e-02, 5.44e-02)
        ),

   classbasedtightEleIDCuts = cms.PSet(
        cutdetain = cms.vdouble(1.16e-02, 4.49e-03, 9.38e-03, 1.84e-02, 6.78e-03, 1.09e-02, 2.52e-02, 2.68e-02, 1.39e-02),
        cutdetainl = cms.vdouble(8.16e-03, 4.01e-03, 8.10e-03, 1.90e-02, 5.88e-03, 8.93e-03, 1.71e-02, 4.34e-02, 1.43e-02),
        cutdphiin = cms.vdouble(8.97e-02, 9.93e-02, 2.95e-01, 9.79e-02, 1.51e-01, 2.52e-01, 3.41e-01, 3.08e-01, 3.28e-01),
        cutdphiinl = cms.vdouble(6.10e-02, 1.40e-01, 2.86e-01, 9.21e-02, 1.97e-01, 2.40e-01, 3.33e-01, 3.03e-01, 2.58e-01),
        cuteseedopcor = cms.vdouble(6.37e-01, 9.43e-01, 7.42e-01, 7.48e-01, 7.63e-01, 6.31e-01, 2.14e-01, 8.73e-01, 4.73e-01),
        cutfmishits = cms.vdouble(1.50e+00, 1.50e+00, 1.50e+00, 2.50e+00, 2.50e+00, 1.50e+00, 1.50e+00, 2.50e+00, 5.00e-01),
        cutdcotdist = cms.vdouble(9999., 9999., 9999., 9999., 9999., 9999., 9999., 9999., 9999.),
        cuthoe = cms.vdouble(2.15e-01, 6.08e-02, 1.47e-01, 3.69e-01, 3.49e-02, 1.02e-01, 5.20e-01, 4.22e-01, 4.04e-01),
        cuthoel = cms.vdouble(2.28e-01, 8.36e-02, 1.43e-01, 3.70e-01, 3.92e-02, 9.79e-02, 3.00e-01, 3.81e-01, 3.39e-01),
        cutip_gsf = cms.vdouble(1.31e-02, 5.86e-02, 8.39e-02, 3.66e-02, 4.52e-01, 2.04e-01, 9.13e-02, 8.02e-02, 7.31e-02),
        cutip_gsfl = cms.vdouble(1.19e-02, 5.27e-02, 4.71e-02, 2.12e-02, 2.33e-01, 2.67e-01, 1.09e-01, 1.22e-01, 4.79e-02),
        cutiso_sum = cms.vdouble(1.55e+01, 1.22e+01, 1.22e+01, 1.17e+01, 7.16e+00, 9.71e+00, 8.66e+00, 1.19e+01, 2.98e+00),
        cutiso_sumoet = cms.vdouble(1.19e+01, 7.81e+00, 6.28e+00, 8.92e+00, 4.65e+00, 5.49e+00, 9.36e+00, 8.84e+00, 5.94e+00),
        cutiso_sumoetl = cms.vdouble(6.21e+00, 6.81e+00, 5.30e+00, 5.39e+00, 2.73e+00, 4.73e+00, 4.84e+00, 3.46e+00, 3.73e+00),
        cutsee = cms.vdouble(1.45e-02, 1.16e-02, 1.20e-02, 3.90e-02, 2.97e-02, 3.11e-02, 9.87e-03, 3.47e-02, 9.17e-02),
        cutseel = cms.vdouble(1.32e-02, 1.17e-02, 1.12e-02, 3.87e-02, 2.81e-02, 2.87e-02, 9.87e-03, 2.96e-02, 5.44e-02)
        )
)
