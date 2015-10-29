import FWCore.ParameterSet.Config as cms
from RecoHI.HiJetAlgos.HiRecoJets_cff import *
from RecoHI.HiJetAlgos.HiRecoPFJets_cff import *

ak1PFJets = ak5PFJets.clone(rParam       = cms.double(0.1))
ak2PFJets = ak5PFJets.clone(rParam       = cms.double(0.2))
ak3PFJets = ak5PFJets.clone(rParam       = cms.double(0.3))
ak4PFJets = ak5PFJets.clone(rParam       = cms.double(0.4))
ak6PFJets = ak5PFJets.clone(rParam       = cms.double(0.6))
ak7PFJets = ak5PFJets.clone(rParam       = cms.double(0.7))

akVs1PFJets.jetPtMin = 1
akVs1PFJets.src = cms.InputTag("particleFlow")
akVs1CaloJets.jetPtMin = 1
akVs2PFJets.jetPtMin = 1
akVs2PFJets.src = cms.InputTag("particleFlow")
akVs2CaloJets.jetPtMin = 1
akVs3PFJets.jetPtMin = 1
akVs3PFJets.src = cms.InputTag("particleFlow")
akVs3CaloJets.jetPtMin = 1
akVs4PFJets.jetPtMin = 1
akVs4PFJets.src = cms.InputTag("particleFlow")
akVs4CaloJets.jetPtMin = 1
akVs5PFJets.jetPtMin = 1
akVs5PFJets.src = cms.InputTag("particleFlow")
akVs5CaloJets.jetPtMin = 1
akVs6PFJets.jetPtMin = 1
akVs6PFJets.src = cms.InputTag("particleFlow")
akVs6CaloJets.jetPtMin = 1
akVs7PFJets.jetPtMin = 1
akVs7PFJets.src = cms.InputTag("particleFlow")
akVs7CaloJets.jetPtMin = 1
akPu1PFJets.jetPtMin = 1
akPu1CaloJets.jetPtMin = 1
akPu2PFJets.jetPtMin = 1
akPu2CaloJets.jetPtMin = 1
akPu3PFJets.jetPtMin = 1
akPu3CaloJets.jetPtMin = 1
akPu4PFJets.jetPtMin = 1
akPu4CaloJets.jetPtMin = 1
akPu5PFJets.jetPtMin = 1
akPu5CaloJets.jetPtMin = 1
akPu6PFJets.jetPtMin = 1
akPu6CaloJets.jetPtMin = 1
akPu7PFJets.jetPtMin = 1
akPu7CaloJets.jetPtMin = 1
ak1PFJets.jetPtMin = 1
ak1PFJets.src = cms.InputTag("particleFlow")
ak1CaloJets.jetPtMin = 1
ak2PFJets.jetPtMin = 1
ak2PFJets.src = cms.InputTag("particleFlow")
ak2CaloJets.jetPtMin = 1
ak3PFJets.jetPtMin = 1
ak3PFJets.src = cms.InputTag("particleFlow")
ak3CaloJets.jetPtMin = 1
ak4PFJets.jetPtMin = 1
ak4PFJets.src = cms.InputTag("particleFlow")
ak4CaloJets.jetPtMin = 1
ak5PFJets.jetPtMin = 1
ak5PFJets.src = cms.InputTag("particleFlow")
ak5CaloJets.jetPtMin = 1
ak6PFJets.jetPtMin = 1
ak6PFJets.src = cms.InputTag("particleFlow")
ak6CaloJets.jetPtMin = 1
ak7PFJets.jetPtMin = 1
ak7PFJets.src = cms.InputTag("particleFlow")
ak7CaloJets.jetPtMin = 1

hiReRecoPFJets = cms.Sequence(
ak1PFJets
+
ak2PFJets
+
ak3PFJets
+
ak4PFJets
+
ak5PFJets
+
ak6PFJets
+
ak7PFJets
+
akPu1PFJets
+
akPu2PFJets
+
akPu3PFJets
+
akPu4PFJets
+
akPu5PFJets
+
akPu6PFJets
+
akPu7PFJets
+
akVs1PFJets
+
akVs2PFJets
+
akVs3PFJets
+
akVs4PFJets
+
akVs5PFJets
+
akVs6PFJets
+
akVs7PFJets
)

hiReRecoCaloJets = cms.Sequence(
ak1CaloJets
+
ak2CaloJets
+
ak3CaloJets
+
ak4CaloJets
+
ak5CaloJets
+
ak6CaloJets
+
ak7CaloJets
+
akPu1CaloJets
+
akPu2CaloJets
+
akPu3CaloJets
+
akPu4CaloJets
+
akPu5CaloJets
+
akPu6CaloJets
+
akPu7CaloJets
+
akVs1CaloJets
+
akVs2CaloJets
+
akVs3CaloJets
+
akVs4CaloJets
+
akVs5CaloJets
+
akVs6CaloJets
+
akVs7CaloJets
)
