"""
List of input variables from MxAODs
TODO: Make this a yaml config file (Bad practice to use a .py file for configs)
"""
variables_dictionary = {"TauTracks": [

                                      # "TauTracks.dEta",
                                      # "TauTracks.dPhi",
                                      "TauTracks.nInnermostPixelHits",
                                      "TauTracks.nPixelHits",
                                      "TauTracks.nSCTHits",
                                      # "TauTracks.chargedScoreRNN",
                                      # "TauTracks.isolationScoreRNN",
                                      # "TauTracks.conversionScoreRNN",
                                      # "TauTracks.fakeScoreRNN",

                                      "TauTracks.pt",
                                      "TauTracks.dphiECal",
                                      "TauTracks.detaECal",
                                      "TauTracks.jetpt",
                                      "TauTracks.d0TJVA",
                                      "TauTracks.d0SigTJVA",
                                      "TauTracks.z0sinthetaTJVA",
                                      "TauTracks.z0sinthetaSigTJVA"

                                      ],

                        "ConvTrack": ["ConvTrack.dphiECal",
                                      "ConvTrack.dphi",
                                      "ConvTrack.detaECal",
                                      "ConvTrack.deta",
                                      "ConvTrack.pt",
                                      "ConvTrack.jetpt",
                                      "ConvTrack.d0TJVA",
                                      "ConvTrack.d0SigTJVA",
                                      "ConvTrack.z0sinthetaTJVA",
                                      "ConvTrack.z0sinthetaSigTJVA"],

                        "ShotPFO": ["ShotPFO.dphiECal",
                                    "ShotPFO.dphi",
                                    "ShotPFO.detaECal",
                                    "ShotPFO.deta",
                                    "ShotPFO.pt",
                                    "ShotPFO.jetpt"],

                        "NeutralPFO": [#"NeutralPFO.dphiECal",
                                       #"NeutralPFO.dphi",
                                       #"NeutralPFO.detaECal",
                                       #"NeutralPFO.deta",
                                       "NeutralPFO.pt",
                                       "NeutralPFO.jetpt",
                                       #"NeutralPFO.FIRST_ETA",
                                       "NeutralPFO.SECOND_R",
                                       #"NeutralPFO.DELTA_THETA",
                                       "NeutralPFO.CENTER_LAMBDA",
                                       #"NeutralPFO.LONGITUDINAL",
                                       "NeutralPFO.SECOND_ENG_DENS",
                                       #"NeutralPFO.ENG_FRAC_CORE",
                                       "NeutralPFO.NPosECells_EM1",
                                       "NeutralPFO.NPosECells_EM2",
                                       "NeutralPFO.energy_EM1",
                                       "NeutralPFO.energy_EM2",
                                       #"NeutralPFO.EM1CoreFrac",
                                       #"NeutralPFO.firstEtaWRTClusterPosition_EM1",
                                       #"NeutralPFO.firstEtaWRTClusterPosition_EM2",
                                       #"NeutralPFO.secondEtaWRTClusterPosition_EM1",
                                       #"NeutralPFO.secondEtaWRTClusterPosition_EM2",
                                       ],

                        "TauJets": ["TauJets.centFrac",
                                    "TauJets.etOverPtLeadTrk",
                                    "TauJets.dRmax",
                                    "TauJets.SumPtTrkFrac",
                                    "TauJets.ptRatioEflowApprox",
                                    #"TauJets.ptIntermediateAxis",
                                    "TauJets.mEflowApprox",
                                    "TauJets.ptJetSeed",
                                    "TauJets.etaJetSeed",
                                    #"TauJets.phiJetSeed",
                                    ],

                        "DecayMode": ["TauJets.truthDecayMode"],
                        "Prong": ["TauJets.truthProng"],
                        "Weight": ["TauJets.ptJetSeed"]}




variables_list = ["TauTracks.dEta",
                    "TauTracks.dPhi",
                    "TauTracks.nInnermostPixelHits",
                    "TauTracks.nPixelHits",
                    "TauTracks.nSCTHits",
                    "TauTracks.pt",
                    "TauTracks.d0TJVA",
                    "TauTracks.d0SigTJVA",
                    "TauTracks.z0sinthetaTJVA",
                    "TauTracks.z0sinthetaSigTJVA",
                    "ConvTrack.dphiECal",
                    "ConvTrack.dphi",
                    "ConvTrack.detaECal",
                    "ConvTrack.deta",
                    "ConvTrack.pt",
                    "ConvTrack.jetpt",
                    "ConvTrack.d0TJVA",
                    "ConvTrack.d0SigTJVA",
                    "ConvTrack.z0sinthetaTJVA",
                    "ConvTrack.z0sinthetaSigTJVA",
                    "ShotPFO.dphiECal",
                     "ShotPFO.dphi",
                     "ShotPFO.detaECal",
                     "ShotPFO.deta",
                     "ShotPFO.pt",
                     "ShotPFO.jetpt",
                    "NeutralPFO.dphiECal",
                    "NeutralPFO.dphi",
                    "NeutralPFO.detaECal",
                    "NeutralPFO.deta",
                    "NeutralPFO.pt",
                    "NeutralPFO.jetpt",
                    "NeutralPFO.FIRST_ETA",
                    "NeutralPFO.SECOND_R",
                    "NeutralPFO.DELTA_THETA",
                    "NeutralPFO.CENTER_LAMBDA",
                    "NeutralPFO.LONGITUDINAL",
                    "NeutralPFO.SECOND_ENG_DENS",
                    "NeutralPFO.ENG_FRAC_CORE",
                    "NeutralPFO.NPosECells_EM1",
                    "NeutralPFO.NPosECells_EM2",
                    "NeutralPFO.energy_EM1",
                    "NeutralPFO.energy_EM2",
                    "NeutralPFO.EM1CoreFrac",
                    "NeutralPFO.firstEtaWRTClusterPosition_EM1",
                    "NeutralPFO.firstEtaWRTClusterPosition_EM2",
                    "NeutralPFO.secondEtaWRTClusterPosition_EM1",
                    "NeutralPFO.secondEtaWRTClusterPosition_EM2",
                    "TauJets.centFrac",
                    "TauJets.etOverPtLeadTrk",
                    "TauJets.dRmax",
                    "TauJets.SumPtTrkFrac",
                    "TauJets.ptRatioEflowApprox",
                    "TauJets.ptIntermediateAxis",
                    "TauJets.ptJetSeed",
                    "TauJets.etaJetSeed",
                    "TauJets.phiJetSeed",]


var_lims =  {"ConvTrack.d0SigTJVA" : 8,
             "ConvTrack.d0TJVA" : 6,
             "ConvTrack.deta" : 8,
             "ConvTrack.detaECal" : 8,
             "ConvTrack.dphi" : 8,
             "ConvTrack.dphiECal" : 8,
             "ConvTrack.jetpt" : 8,
             "ConvTrack.pt": 15,
             "ConvTrack.z0sinthetaSigTJVA": 15,
             "ConvTrack.z0sinthetaTJVA": 15,


             "NeutralPFO.CENTER_LAMBDA" : 15,
             "NeutralPFO.DELTA_THETA" : 8,
             "NeutralPFO.deta" : 3.5,
             "NeutralPFO.detaECal" : 3.5,
             "NeutralPFO.dphi" : 3.5,
             "NeutralPFO.dphiECal" : 4,
             "NeutralPFO.EM1CoreFrac" : 3,
             "NeutralPFO.energy_EM1" : 25,
             "NeutralPFO.energy_EM2" : 45,
             "NeutralPFO.ENG_FRAC_CORE" : 5,
             "NeutralPFO.FIRST_ETA" : 3,
             "NeutralPFO.firstEtaWRTClusterPosition_EM1" : 45,
             "NeutralPFO.firstEtaWRTClusterPosition_EM2" : 45,
             "NeutralPFO.jetpt" : 35,
             "NeutralPFO.LONGITUDINAL" : 2,
             "NeutralPFO.NPosECells_EM1" : 15,
             "NeutralPFO.NPosECells_EM2" : 15,
             "NeutralPFO.pt" : 25,
             "NeutralPFO.SECOND_ENG_DENS" : 30,
             "NeutralPFO.SECOND_R" : 15,
             "NeutralPFO.secondEtaWRTClusterPosition_EM1" : 15,
             "NeutralPFO.secondEtaWRTClusterPosition_EM2" : 15,

             "ShotPFO.deta" : 15,
             "ShotPFO.detaECal" : 20,
             "ShotPFO.dphi" : 10,
             "ShotPFO.dphiECal" : 15,
             "ShotPFO.jetpt" : 45,
             "ShotPFO.pt" : 25,

             "TauTracks.d0SigTJVA" : 30,
             "TauTracks.d0TJVA" : 15,
             "TauTracks.dEta" : 10,
             "TauTracks.dPhi" : 10,
             "TauTracks.nPixelHits" : 10,
             "TauTracks.nSCTHits" : 15,
             "TauTracks.pt" : 40,
             "TauTracks.z0sinthetaSigTJVA" : 45,
             "TauTracks.z0sinthetaTJVA" : 45
 }






