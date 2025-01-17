import FWCore.ParameterSet.Config as cms
from GeneratorInterface.EvtGenInterface.EvtGenSetting_cff import *
from Configuration.Generator.Pythia8CommonSettings_cfi import *
from Configuration.Generator.MCTunes2017.PythiaCP5Settings_cfi import *

generator = cms.EDFilter("Pythia8HadronizerFilter",
    maxEventsToPrint = cms.untracked.int32(1),
    pythiaPylistVerbosity = cms.untracked.int32(1),
    pythiaHepMCVerbosity = cms.untracked.bool(True),
    comEnergy = cms.double(13000.0),

    PythiaParameters = cms.PSet(
        pythia8CommonSettingsBlock,
        pythia8CP5SettingsBlock,
        processParameters = cms.vstring( # put below any needed pythia parameter
            '541:m0 = 6.275',
            '541:tau0 = 0.153',
            #'ProcessLevel:all = off',
        ),
        parameterSets = cms.vstring(
            'pythia8CommonSettings',
            'pythia8CP5Settings',
            'processParameters',
        ),
    ),

    ExternalDecays = cms.PSet(
        EvtGen130 = cms.untracked.PSet(
            decay_table            = cms.string('GeneratorInterface/EvtGenInterface/data/DECAY_2014_NOLONGLIFE.DEC'),
            particle_property_file = cms.FileInPath('GeneratorInterface/EvtGenInterface/data/evt_2014.pdl'),
            list_forced_decays     = cms.vstring(
                'MyBc+',
                'MyBc-',
            ),
            operates_on_particles  = cms.vint32(541, -541),
            convertPythiaCodes     = cms.untracked.bool(False),
            user_decay_file        = cms.vstring('GeneratorInterface/ExternalDecays/data/BcToJpsiMuMuInclusive.dec'),

        ),
        parameterSets = cms.vstring('EvtGen130'),
    ),

)

jpsi_from_bc_filter = cms.EDFilter(
    "PythiaFilterMultiAncestor",
    ParticleID      = cms.untracked.int32 (443),
    MinPt           = cms.untracked.double( 6.),
    MinEta          = cms.untracked.double(-3.),
    MaxEta          = cms.untracked.double( 3.),
    MotherIDs       = cms.untracked.vint32([541]), 
    DaughterIDs     = cms.untracked.vint32([-13, 13]), 
    DaughterMinPts  = cms.untracked.vdouble([ 2.8 , 2.8  ]),
    DaughterMaxPts  = cms.untracked.vdouble([ 1.e6,  1.e6]),
    DaughterMinEtas = cms.untracked.vdouble([-2.52 , -2.52 ]),
    DaughterMaxEtas = cms.untracked.vdouble([ 2.52 ,  2.52 ]),
)

ProductionFilterSequence = cms.Sequence(generator*jpsi_from_bc_filter)

