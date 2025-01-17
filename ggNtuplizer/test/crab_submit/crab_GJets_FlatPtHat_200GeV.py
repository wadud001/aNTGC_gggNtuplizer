#!/usr/bin/env python

from CRABClient.UserUtilities import config
from CRABAPI.RawCommand import crabCommand
from CRABClient.ClientExceptions import ClientException
from httplib import HTTPException

from datetime import date

def submit(config):
    try:
        crabCommand('submit', config = config)
    except HTTPException as hte:
        print "Failed submitting task: %s" % (hte.headers)
    except ClientException as cle:
        print "Failed submitting task: %s" % (cle)


# workarea                              = '/afs/hep.wisc.edu/user/wadud/private/CMSSW_10_6_24/src/ggAnalysis/ggNtuplizer/test/crab_submit//jobs//jobsUL2017v1/GJets_FlatPtHat_200/'
# mainOutputDir                         = '/store/user/mwadud/aNTGCmet/ntuples/UL2017/jobsUL2017v1/'

workarea                              = '/afs/hep.wisc.edu/user/wadud/private/CMSSW_10_6_24/src/ggAnalysis/ggNtuplizer/test/crab_submit//jobs//jobsUL2017v1Xsecs/GJets_FlatPtHat_200/'
mainOutputDir                         = '/store/user/mwadud/aNTGCmet/ntuples/UL2017/jobsUL2017v1Xsecs/'

config                                = config()

config.General.requestName            = 'GJets_FlatPtHat_200'
config.General.transferLogs           = True
config.General.workArea               = '%s' % workarea
config.General.transferOutputs = False
config.General.transferLogs = False

config.Site.storageSite               = 'T2_US_Wisconsin'
config.Site.whitelist                 = ['T3_US_UCR','T3_US_FNALLPC','T3_US_Rice','T3_US_Rutgers','T3_US_FIT','T3_US_PSC','T3_US_OSU','T3_US_TAMU','T3_US_UMD','T3_US_VC3_NotreDame','T3_US_SDSC','T3_US_Colorado','T3_US_OSG','T3_US_Princeton_ICSE','T3_US_NERSC','T3_US_Baylor','T2_US_Nebraska','T2_US_UCSD','T2_US_Wisconsin','T2_US_MIT','T3_US_TACC','T3_US_UMiss','T2_US_Caltech','T2_US_Florida','T2_US_Vanderbilt']
config.Site.blacklist                 = ['T2_US_Purdue']


# config.JobType.psetName               = '/afs/hep.wisc.edu/user/wadud/private/CMSSW_10_6_24/src/ggAnalysis/ggNtuplizer/test/run_mc2017_106X.py'
config.JobType.psetName               = '/afs/hep.wisc.edu/user/wadud/private/CMSSW_10_6_24/src/ggAnalysis/ggNtuplizer/test/ana.py'
config.JobType.pluginName             = 'Analysis'
config.JobType.maxMemoryMB             = 2600
config.JobType.maxJobRuntimeMin        = 5000

config.Data.userInputFiles            = open('/afs/hep.wisc.edu/user/wadud/private/CMSSW_10_6_24/src/ggAnalysis/ggNtuplizer/test/crab_submit/GJets_FlatPtHat_200GeV_MINIAOD.txt').readlines()
config.Data.outputPrimaryDataset      = 'GJets_FlatPtHat_200'
config.Data.publication               = False
config.Data.allowNonValidInputDataset = True
config.Data.outLFNDirBase             = '%s' % mainOutputDir
config.Data.splitting                 = 'FileBased'
# config.Data.unitsPerJob               = 20
config.Data.unitsPerJob               = 20000
config.Data.totalUnits                = 100000
config.Data.ignoreLocality            = True
config.Data.totalUnits                = 50000

submit(config)