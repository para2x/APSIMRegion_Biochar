#!/usr/bin/env python
# -*- coding: utf-8 -*-
#==============================================================================
# main file for creating apsimRegion experiments
#==============================================================================

import os
from apsimRegions.preprocess.configMaker import create_many_config_files
from apsimRegions.preprocess.apsimPreprocess import preprocess_many
from apsimRegions.preprocess.batch import create_run_all_batchfile

def main():
    experimentName = 'Test'
    outputDir = 'C:/Users/Para2x/Dropbox/Hamze Dokoohaki/Projects/Large-scale APSIM Simulation/apsimRegions-Revised/Example-factorial/{0}'.format(experimentName)

    # validArgs are 'resolution','crop','model','crit_fr_asw', 'sowStart', or 'soilName'
    #factorials = {'soilName':['auto','HCGEN0001','HCGEN0003','HCGEN0007','HCGEN0010','HCGEN0011','HCGEN0013','HCGEN0014','HCGEN0015','HCGEN0016','HCGEN0017','HCGEN0025']}
    #factorials = {'sowStart':['auto']}
    factorials = {'BAR':['10000','20000']}
    #factorials = {'crit_fr_asw':['0.0','0.05','0.15','0.25','0.50','0.75','0.95','1.0']}

    otherArgs = {'metFileDir':'C:/Users/Para2x/Dropbox/Hamze Dokoohaki/Projects/Large-scale APSIM Simulation/apsimRegions-Revised/Example-factorial/metfiles/%(met)s',\
                'gridLutPath':'C:/Users/Para2x/Dropbox/Hamze Dokoohaki/Projects/Large-scale APSIM Simulation/apsimRegions-Revised/Example-factorial/exampleLookupTable.csv',\
                'apsimModelDir':'C:/Program Files (x86)/Apsim77-r3632/Model',\
                'soilDataPath':'C:/Program Files (x86)/Apsim77-r3632/UserInterface/ToolBoxes/hc27_v1_1.soils',\
                'model':'NARR32',\
                'clockStart':'1/1/1991',\
                'clockEnd':'31/12/1993', \
                'crop':'maize', \
                'density':'8',\
                'depth':'30',\
                'cultivar':'usa_18leaf',\
                'row_spacing':'760',\
                'outputVariables':'mm/dd/yyyy as date, yield, biomass, lai'}

    # create directory if it doesn't exist
    if not os.path.isdir(outputDir):
        os.mkdir(outputDir)

    # create config files
    print 'Creating configuration files...'
    runs = create_many_config_files(outputDir, factorials, otherArgs)

    # create apsim files
    print 'Saving .apsim and .bat files...'
    preprocess_many(outputDir, runs.keys()[0], runs.keys()[-1])

    # create run all batchfile
    create_run_all_batchfile(outputDir, runs, experimentName)

    # feedback
    print 'All files saved to:\r', outputDir
    print '\nFolder', ': Variable'
    for key in runs.keys():
        print '{0:6} : {1}'.format(key, runs[key])

    # save text file of run data
    if not os.path.isfile(os.path.join(outputDir,'readme.txt')):
        mode = 'w'
    else:
        mode = 'a'

    with open(os.path.join(outputDir,'readme.txt'),mode=mode) as f:
        f.write('Folder : Variable')
        for key in runs.keys():
            f.write('\n{0:6} : {1}'.format(key, runs[key]))
        f.write('\n')

    print '\n***** Done! *****'

# Run main() if module is run as a program
if __name__ == '__main__':
    main()
