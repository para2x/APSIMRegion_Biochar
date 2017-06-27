#!/usr/bin/env python
#==============================================================================
# Module that contains all management rules.
#==============================================================================

import lxml.etree as ET

def sowOnFixedDate_rule(folder,crop,name='Sow on a fixed date',shortcut=None,date='1-jan',density='10',depth='50',cultivar='',gclass='plant',row_spacing='500',occurrence='start_of_day'):
    ''' Rule for sowing on fixed date.'''

    if shortcut == None:
        rule = ET.SubElement(folder, 'manager', name=name)

        ui = ET.SubElement(rule, 'ui')
        ET.SubElement(ui, 'category', type='category', description='Sowing criteria')
        ET.SubElement(ui, 'date', type='text', description='Enter sowing date (dd-mmm) : ').text = date

        ET.SubElement(ui, 'category', type='category', description='Sowing parameters')
        ET.SubElement(ui, 'crop', type='crop', description='Enter name of crop to sow : ').text = crop
        ET.SubElement(ui, 'density', type='text', description='Enter sowing density (plants/m2) : ').text = density
        ET.SubElement(ui, 'depth', type='text', description = 'Enter sowing depth (mm) : ').text = depth
        ET.SubElement(ui, 'cultivar', type='cultivars', description='Enter cultivar : ').text = cultivar
        ET.SubElement(ui, 'class', type='classes', description='Enter crop growth class : ').text = gclass
        ET.SubElement(ui, 'row_spacing', type='text', description='Enter row spacing (mm) : ').text = row_spacing

        script = ET.SubElement(rule, 'script')
        ET.SubElement(script, 'text').text = '''
      if (today = date('[date]') then
              [crop] sow plants =[density], sowing_depth = [depth], cultivar = [cultivar], row_spacing = [row_spacing], crop_class = [class]
         endif
      '''
        ET.SubElement(script, 'event').text = occurrence
    else:
        rule = ET.SubElement(folder, 'manager', name=name, shortcut=shortcut+'/'+name)
    return rule

def sowUsingAVariable_rule(folder,crop,name='Sow using a variable rule',shortcut=None,start_date='',end_date='',must_sow='yes',raincrit='30',rainnumdays='3',esw_amount='200',density='3',depth='50',cultivar='usa_18leaf',gclass='plant',row_spacing='250',occurrence='start_of_day'):
    ''' Rule for sowing on a variable date.'''

    if shortcut == None:
        rule = ET.SubElement(folder, 'manager', name=name)

        ui = ET.SubElement(rule, 'ui')
        ET.SubElement(ui, 'category', type='category', description='Sowing criteria')
        ET.SubElement(ui, 'date1', type='ddmmmdate', description='Enter sowing window START date (dd-mmm) : ').text = start_date
        ET.SubElement(ui, 'date2', type='ddmmmdate', description='Enter sowing window END date (dd-mmm) : ').text = end_date
        ET.SubElement(ui, 'must_sow', type='yesno', description='Must sow? : ').text = must_sow
        ET.SubElement(ui, 'raincrit', type='text', description='Amount of rainfall : ').text = raincrit
        ET.SubElement(ui, 'rainnumdays', type='text', description='Number of days of rainfall : ').text = rainnumdays
        ET.SubElement(ui, 'esw_amount', type='text', description='Enter minimum allowable available soil water (mm) : ').text = esw_amount

        ET.SubElement(ui, 'category', type='category', description='Sowing parameters')
        ET.SubElement(ui, 'crop', type='crop', description='Enter name of crop to sow : ').text = crop
        ET.SubElement(ui, 'density', type='text', description='Enter sowing density (plants/m2) : ').text = density
        ET.SubElement(ui, 'depth', type='text', description = 'Enter sowing depth (mm) : ').text = depth
        ET.SubElement(ui, 'cultivar', type='cultivars', description='Enter cultivar : ').text = cultivar
        ET.SubElement(ui, 'class', type='classes', description='Enter crop growth class : ').text = gclass
        ET.SubElement(ui, 'row_spacing', type='text', description='Enter row spacing (mm) : ').text = row_spacing

        script = ET.SubElement(rule, 'script')
        ET.SubElement(script, 'text').text = '''
      if (paddock_is_fallow() = 1 and FallowIn <> 'yes' and (NextCrop = 0 or NextCrop = '[crop]')) then
         if (date_within('[date1], [date2]') = 1) then
            if (rain[[rainnumdays]] >= [raincrit] AND esw >= [esw_amount]) OR
                ('[must_sow]' = 'yes' AND today = date('[date2]'))) THEN
               ChooseNextCrop = 'yes'   ! for rotations
               [crop] sow plants =[density], sowing_depth = [depth], cultivar = [cultivar], row_spacing = [row_spacing], crop_class = [class]
            endif
            if today = date('[date2]') then
               ChooseNextCrop = 'yes'
            endif
         endif
      endif
      '''
        ET.SubElement(script, 'event').text = occurrence
        script = ET.SubElement(rule, 'script')
        ET.SubElement(script, 'text').text = '''
        nextcrop = 0
        fallowin = 0
        '''
        ET.SubElement(script, 'event').text = 'init'
    else:
        rule = ET.SubElement(folder, 'manager', name=name, shortcut=shortcut+'/'+name)
    return rule

def cotton_sowing_rule(folder,crop,name='Cotton sowing rule',shortcut=None,start_date='',end_date='',must_sow='yes',raincrit='30',rainnumdays='3',esw_amount='200',density='10',depth='30',cultivar='siok',row_spacing='1000',skiprow='0',occurrence='start_of_day'):
    ''' Rule for sowing cotton in a date range.'''

    if shortcut == None:
        rule = ET.SubElement(folder, 'manager', name=name)

        ui = ET.SubElement(rule, 'ui')
        ET.SubElement(ui, 'category', type='category', description='Sowing criteria')
        ET.SubElement(ui, 'date1', type='ddmmmdate', description='Enter sowing window START date (dd-mmm) : ').text = start_date
        ET.SubElement(ui, 'date2', type='ddmmmdate', description='Enter sowing window END date (dd-mmm) : ').text = end_date
        ET.SubElement(ui, 'must_sow', type='yesno', description='Must sow? : ').text = must_sow
        ET.SubElement(ui, 'raincrit', type='text', description='Amount of rainfall : ').text = raincrit
        ET.SubElement(ui, 'rainnumdays', type='text', description='Number of days of rainfall : ').text = rainnumdays
        ET.SubElement(ui, 'esw_amount', type='text', description='Enter minimum allowable available soil water (mm) : ').text = esw_amount

        ET.SubElement(ui, 'category', type='category', description='Sowing parameters')
        ET.SubElement(ui, 'crop', type='crop', description='Enter name of crop to sow : ').text = crop
        ET.SubElement(ui, 'density', type='text', description='Enter sowing density (plants/m2) : ').text = density
        ET.SubElement(ui, 'depth', type='text', description = 'Enter sowing depth (mm) : ').text = depth
        ET.SubElement(ui, 'cultivar', type='cultivars', description='Enter cultivar : ').text = cultivar
        ET.SubElement(ui, 'row_spacing', type='text', description='Enter row spacing (mm) : ').text = row_spacing
        ET.SubElement(ui, 'skiprow', type='list', listvalues='0,1,2', description='Skip row : ').text = skiprow

        script = ET.SubElement(rule, 'script')
        ET.SubElement(script, 'text').text = '''
      if (paddock_is_fallow() = 1 and FallowIn <> 'yes' and (NextCrop = 0 or NextCrop = '[crop]')) then
         if (date_within('[date1], [date2]') = 1) then
            if (rain[[rainnumdays]] >= [raincrit] AND esw >= [esw_amount]) OR
                ('[must_sow]' = 'yes' AND today = date('[date2]'))) THEN
               ChooseNextCrop = 'yes'   ! for rotations
               [crop] sow plants_pm =[density], sowing_depth = [depth], cultivar = [cultivar], row_spacing = [row_spacing], skiprow = [skiprow]
            endif
            if today = date('[date2]') then
               ChooseNextCrop = 'yes'
            endif
         endif
      endif
      '''
        ET.SubElement(script, 'event').text = occurrence
    else:
        rule = ET.SubElement(folder, 'manager', name=name, shortcut=shortcut+'/'+name)
    return rule

def cotton_fixed_date_sowing_rule(folder,crop,name='Cotton fixed date sowing rule',shortcut=None,date='',density='10',depth='30',cultivar='siok',row_spacing='1000',occurrence='start_of_day'):
    ''' Rule for sowing cotton on a fixed date.'''

    if shortcut == None:
        rule = ET.SubElement(folder, 'manager', name=name)

        ui = ET.SubElement(rule, 'ui')
        ET.SubElement(ui, 'category', type='category', description='Sowing criteria')
        ET.SubElement(ui, 'date', type='text', description='Enter sowing date (dd-mmm) : ').text = date

        ET.SubElement(ui, 'category', type='category', description='Sowing parameters')
        ET.SubElement(ui, 'crop', type='crop', description='Enter name of crop to sow : ').text = crop
        ET.SubElement(ui, 'density', type='text', description='Enter sowing density (plants/m2) : ').text = density
        ET.SubElement(ui, 'depth', type='text', description = 'Enter sowing depth (mm) : ').text = depth
        ET.SubElement(ui, 'cultivar', type='cultivars', description='Enter cultivar : ').text = cultivar
        ET.SubElement(ui, 'row_spacing', type='text', description='Enter row spacing (mm) : ').text = row_spacing

        script = ET.SubElement(rule, 'script')
        ET.SubElement(script, 'text').text = '''
      if (today = date('[date]') then
              [crop] sow plants_pm =[density], sowing_depth = [depth], cultivar = [cultivar], row_spacing = [row_spacing]
         endif
      '''
        ET.SubElement(script, 'event').text = occurrence
    else:
        rule = ET.SubElement(folder, 'manager', name=name, shortcut=shortcut+'/'+name)
    return rule

def sowingFertiliser_rule(folder, name='Sowing fertiliser', shortcut=None, eventname='sowing', fertiliser='fertiliser', fert_amount_sow='150', fert_type_sow='urea_N'):
    '''Rule for when to apply fertilizer.'''

    if shortcut == None:
        rule = ET.SubElement(folder, 'manager', name=name)

        ui = ET.SubElement(rule, 'ui')
        ET.SubElement(ui, 'category', type='category', description='When should fertiliser be applied')
        ET.SubElement(ui, 'eventname', type='text', description='On which event should fertiliser be applied : ').text = eventname
        ET.SubElement(ui, 'category', type='category', description='Fertiliser application details')
        ET.SubElement(ui, 'fertmodule', type='modulename', description='Module used to apply the fertiliser : ').text = fertiliser
        ET.SubElement(ui, 'fert_amount_sow', type='text', description='Amount of starter fertiliser at sowing (kg/ha) : ').text = fert_amount_sow
        ET.SubElement(ui, 'fert_type_sow', type='list', listvalues='NO3_N, NH4_N, NH4NO3, urea_N, urea_no3, urea, nh4so4_n, rock_p, banded_p, broadcast_p', description='Sowing fertiliser type : ').text = fert_type_sow

        script = ET.SubElement(rule, 'script')
        ET.SubElement(script, 'text').text = '''
        [fertmodule] apply amount = [fert_amount_sow] (kg/ha), depth = 50 (mm), type = [fert_type_sow]
        '''
        ET.SubElement(script, 'event').text = '[modulename].[eventname]'
    else:
        rule = ET.SubElement(folder, 'manager', name=name, shortcut=shortcut+'/'+name)
    return rule

def harvesting_rule(folder, crop, name='Harvesting rule', shortcut=None):
    ''' Rule for when to harvest the crop.'''

    if shortcut == None:
        rule = ET.SubElement(folder, 'manager', name=name)

        ui = ET.SubElement(rule, 'ui')
        ET.SubElement(ui, 'category', type='category', description='Harvesting criteria')
        ET.SubElement(ui, 'crop', type='text', description='Enter name of crop to harvest when ripe : ').text = crop

        script = ET.SubElement(rule, 'script')
        ET.SubElement(script, 'text').text = '''
           if ('[crop]' = 'cotton') then
              if ([crop].ozcot_status > 0) then
                  [crop] harvest
              endif
           elseif ([crop].StageName = 'harvest_ripe' or [crop].plant_status = 'dead') then
              [crop]  harvest
              [crop]  end_crop
           endif
           '''
        ET.SubElement(script, 'event').text = 'end_of_day'
    else:
        rule = ET.SubElement(folder, 'manager', name=name, shortcut=shortcut+'/'+name)
    return rule

def end_crop_on_fixed_date_rule(folder, crop, harvestDate='1-jan', name='End crop on a fixed date', shortcut=None):
    '''
    Rule for ending a crop on a fixed date.

    Parameters
    ----------
    folder : element tree object
        node to attach rule to
    crop : string
        crop to harvest
    harvestDate : string (dd-mmm)
        (optional) date to harvest crop
    name : string
        (optional) name of component to display in APSIM gui
    shortcut : string
        (optional) shortcut to link to

    Returns
    -------
    The management rule.
    '''
    if shortcut == None:
        rule = ET.SubElement(folder, 'manager', name=name)

        ui = ET.SubElement(rule, 'ui')
        ET.SubElement(ui, 'category', type='category', description='Harvesting criteria')
        ET.SubElement(ui, 'crop', type='crop', description='Enter name of crop to harvest when ripe : ').text = crop
        ET.SubElement(ui, 'date', type='text', description='Enter ending date (dd-mmm) : ').text = harvestDate

        script = ET.SubElement(rule, 'script')
        ET.SubElement(script, 'text').text = '''
           if (today = date('[date]') then
              [crop]  end_crop
           endif
           '''
        ET.SubElement(script, 'event').text = 'end_of_day'
    else:
        rule = ET.SubElement(folder, 'manager', name=name, shortcut=shortcut+'/'+name)
    return rule

def irrigate_on_sw_deficit_rule(folder, name='irrigate at sw deficit', shortcut=None, trigger='50', occurrence='start_of_day'):
    ''' Rule for when to irrigate, and under what conditions.'''

    if shortcut == None:
        rule = ET.SubElement(folder, 'manager', name=name)

        ui = ET.SubElement(rule, 'ui')
        ET.SubElement(ui, 'trigger', type='text', description='Enter sw deficit to irrigate at (mm)').text = trigger

        script = ET.SubElement(rule, 'script')
        ET.SubElement(script, 'text').text = '''
           '''
        ET.SubElement(script, 'event').text = 'init'

        script = ET.SubElement(rule, 'script')
        ET.SubElement(script, 'text').text = '''
        if sw_dep() > [trigger] then
            irrigation apply amount = [trigger]
            endif
           '''
        ET.SubElement(script, 'event').text = occurrence
    else:
        rule = ET.SubElement(folder, 'manager', name=name, shortcut=shortcut+'/'+name)
    return rule

def fertOnSoilNCriteria_rule(folder, name='FertOnSoilNCriteria', shortcut=None, FertAmtCriteria='50', FertDepthCriteria='75', FertDepth='50', FertAmt='25', FertType='urea_n'):
    ''' Rule for when to apply fertilizer with Manager 2.'''

    if shortcut == None:
        rule = ET.SubElement(folder, 'manager2', name=name)

        ui = ET.SubElement(rule, 'ui')
        ET.SubElement(ui, 'category', type='category', description="Test for the mineral N in the soil and don't apply the fertiliser if greater than X kgN/ha is stored in the soil above a depth of Y mm")
        ET.SubElement(ui, 'FertAmtCriteria', type='text', description="Don't add fertiliser if N in the soil to the depth below exceeds (kg/ha)").text = FertAmtCriteria
        ET.SubElement(ui, 'FertDepthCriteria', type='text', description="Depth to which the amount of N in the soil should be calculated (mm)").text = FertDepthCriteria
        ET.SubElement(ui, 'category', type='category', description="Fertiliser application details")
        ET.SubElement(ui, 'FertDepth', type='text', description="Depth at which to apply the fertiliser (mm)").text = FertDepth
        ET.SubElement(ui, 'FertAmt', type='text', description="Amount of fertiliser to add (kg N /ha)").text = FertAmt
        ET.SubElement(ui, 'FertType', type='list', listvalues="no3_n,nh4_n,nh4no3,urea_n,urea_no3,urea,nh4so4_n,rock_p,banded_p,broadcast_p", description="Fertiliser type - select from the list").text = FertType

        ET.SubElement(rule, 'text').text = '''Imports System
Imports ModelFramework

Public Class Script
   <Link()> Dim MyPaddock As Paddock
   <Link()> Dim Fert As Fertiliser

   'Parameters - user inputs from the Properties tab
   <Param> Private FertAmtCriteria As Single    'Don't apply fertiliser if the N stored in the soil is greater than this.  Disregard the test if the value is -ve
   <Param> Private FertDepthCriteria As Single  'Depth in the soil to calculate the N storage
   <Param> Private FertDepth As Single          'Depth in the soil that the fertilser will be applied
   <Param> Private FertAmt As Single            'Total annual application - needs to be split up between the various application dates listed
   <Param> Private FertType As String           'Type of fertliser to apply

   'Inputs - got by this Manager from elsewhere in APSIM
   <Input> Private Today As DateTime            'Today's date from APSIM
   <Input> Private dlayer As Single()           'Array of soil layer thicknesses - for calculation of mineral N in the soil
   <Input> Private no3 As Single()              'Array of nitrate-N (kg N /ha) for each soil layer - for calculation of mineral N in the soil
   <Input> Private nh4 As Single()              'Array of ammonium-N (kg N /ha) for each soil layer - for calculation of mineral N in the soil
   <Input> Private urea As Single()             'Array of urea-N (kg N /ha) for each soil layer - for calculation of mineral N in the soil

   'Outputs - calculated by this Manager and available to be output by the user
   <Output> Private CumSoilN As Single          'Mineral-N stored in the soil to a depth of FertDepthCriteria

   'Other variables that are calculated but not needed for outputs
   Private LayerWeights As Single()             'Weigthing of each layer for FertAmtCriteria calculation


   <EventHandler()> Public Sub OnInit2()
      '"OnInit2" is an event handler gets called once at the start of the simulation

      'nothing to do in here

   End Sub

   <EventHandler()> Public Sub OnPrepare()
      '"OnPrepare" is an event handler gets called once at the start of every day (before Prepare and Post)

      'Set the number of elements in the LayerWeights array to equal the number of soil layers - do this here because erosion can change the layering
      'Then move through the array and assign a LayerWeighting from 0 to 1 quantifying what proportion of the soil and mineral N in this layer is above FertDepthCriteria
      ReDim LayerWeights(dlayer.length - 1)
      Dim CumDepth As Single = 0.0
         For i As Integer = 0 To dlayer.Length - 1
            CumDepth += dlayer(i)
         If CumDepth <= FertDepthCriteria Then
            LayerWeights(i) = 1.0
         ElseIf (CumDepth - dlayer(i)) <= FertDepthCriteria Then
            LayerWeights(i) = (FertDepthCriteria - (CumDepth - dlayer(i))) / dlayer(i)
         Else
            LayerWeights(i) = 0.0
         End If
      Next

      'Add up the no3, nh4 and urea (all already in kg N /ha) in each layer and multiply by the layer weighting to get the total mineral N to the set depth
      CumSoilN = 0.0
      For i As Integer = 0 To dlayer.Length - 1
         CumSoilN += (no3(i) + nh4(i) + urea(i)) * LayerWeights(i)
      Next

      'If there is less mineral N in the soil than FertAmtCriteria then it is OK to add fertiliser
      '"Fert.Apply" send the command to apply the specified amount of fertiliser at the specified depth of the specified type of fertiliser
      If CumSoilN <= FertAmtCriteria Then
         Fert.Apply(FertAmt, FertDepth, FertType)
      End If

   End Sub

End Class
'''
    else:
        rule = ET.SubElement(folder, 'manager2', name=name, shortcut=shortcut+'/'+name)
    return rule

def BiocharApplication_rule(folder, name='Biochar5v3', shortcut=None, AppDate="04/02/1991", BAR='75000', Cfr='0.71', MRT1='0.5', MRT2='2',labfr="0.2"):
    ''' Rule for when to apply fertilizer with Manager 2.'''

    if shortcut == None:
        rule = ET.SubElement(folder, 'manager2', name=name)

        ui = ET.SubElement(rule, 'ui')
        ET.SubElement(ui, 'category', type='category', description="")
        ET.SubElement(ui, 'date_of_application', type='text', description="").text =AppDate
        ET.SubElement(ui, 'biochar_added', type='float', description="").text = BAR
        ET.SubElement(ui, 'frac_c_biochar', type='float', description="").text = Cfr
        ET.SubElement(ui, 'biochar_loss', type='float', description="").text = "0"
        ET.SubElement(ui, 'MRT1', type='float', description="").text = MRT1
        ET.SubElement(ui, 'MRT2', type='float', description="").text = MRT2
        ET.SubElement(ui, 'frac_labile', type='float', description="").text = labfr
        ET.SubElement(ui, 'ef_biochar', type='float', description="").text = "0.4"
        ET.SubElement(ui, 'fr_biochar_biom', type='float', description="").text = "0.05"
        ET.SubElement(ui, 'biochar_cn', type='float', description="").text = "100"
        ET.SubElement(ui, 'sand', type='float', description="").text = "0.7"
        ET.SubElement(ui, 'clay', type='float', description="").text = "0.3"
        ET.SubElement(ui, 'prim_biom', type='float', description="").text = "0"
        ET.SubElement(ui, 'prim_hum', type='float', description="").text = "0"
        ET.SubElement(ui, 'prim_cell', type='float', description="").text = "0"
        ET.SubElement(ui, 'prim_carb', type='float', description="").text = "0"
        ET.SubElement(ui, 'prim_lign', type='float', description="").text = "0"
        ET.SubElement(ui, 'prim_ef', type='float', description="").text = "0"
        ET.SubElement(ui, 'prim_fr', type='float', description="").text = "0"
        ET.SubElement(ui, 'prim_ef_fom', type='text', description="").text = "0"
        ET.SubElement(ui, 'prim_fr_fom', type='text', description="").text = "0"
        ET.SubElement(ui, 'biom_cn', type='text', description="").text = "8"
        ET.SubElement(ui, 'soil_cn', type='text', description="").text = "12"
        ET.SubElement(ui, 'incorp_depth', type='text', description="").text = "250"
        ET.SubElement(ui, 'dul_qual', type='text', description="").text = "0.3"
        ET.SubElement(ui, 'bd_qual', type='text', description="").text = "0.16"
        ET.SubElement(ui, 'bc_cce', type='text', description="").text = "50"
        ET.SubElement(ui, 'bc_cec', type='text', description="").text = "150"
        ET.SubElement(ui, 'cnrf_bc_coeff', type='text', description="").text = "0.693"
        ET.SubElement(ui, 'cnrf_bc_optcn', type='text', description="").text = "25"
        ET.SubElement(ui, 'bc_wfps_factor', type='text', description="").text = "1"
        ET.SubElement(ui, 'nh4_adsorption', type='text', description="").text = "0.006"
        ET.SubElement(ui, 'nh4_desorption', type='text', description="").text = "0.06"
        ET.SubElement(ui, 'tillage', type='text', description="").text = "0.8"
        ET.SubElement(ui, 'nclay_portion', type='text', description="").text = "0.95"
        ET.SubElement(ui, 'uph', type='text', description="").text = "8.6"
        ET.SubElement(ui, 'lph', type='text', description="").text = "3.5"
        ET.SubElement(ui, 'ab_val', type='text', description="").text = "0"
        ET.SubElement(ui, 'bot_slope', type='text', description="").text = "10"
        ET.SubElement(ui, 'decomp_switch', type='list', listvalues="on,off", description="").text = "on"
        ET.SubElement(ui, 'nitrification_switch', type='list', listvalues="on,off", description="").text = "on"
        ET.SubElement(ui, 'ph_switch', type='list', listvalues="on,off", description="").text = "on"
        ET.SubElement(ui, 'll_switch', type='list', listvalues="on,off", description="").text = "on"
        ET.SubElement(ui, 'dul_switch', type='list', listvalues="on,off", description="").text = "on"
        ET.SubElement(ui, 'xf_switch', type='list', listvalues="on,off", description="").text = "on"
        ET.SubElement(ui, 'kl_switch', type='list', listvalues="on,off", description="").text = "on"
        ET.SubElement(ui, 'bd_switch', type='list', listvalues="on,off", description="").text = "on"
        ET.SubElement(ui, 'biochar_c_switch', type='list', listvalues="on,off", description="").text = "on"
        ET.SubElement(ui, 'swcon_switch', type='list', listvalues="on,off", description="").text = "on"
        ET.SubElement(ui, 'ks_switch', type='list', listvalues="on,off", description="").text = "on"
        ET.SubElement(ui, 'sat_switch', type='list', listvalues="on,off", description="").text = "on"
        ET.SubElement(ui, 'category', type='category', description="")
        ET.SubElement(ui, 'soil_order', type='list', listvalues="Aridisol,Entisol,Gelisol,Inceptisol,Mollisol,Vertisol,Histosol,Alfisol,Oxisol,Spodosol,Ultisol", description="").text = "Mollisol"

        ET.SubElement(rule, 'text').text = '''using System;

using ModelFramework;

using CSGeneral;



public class Script
{
   [Link] Paddock MyPaddock; // Can be used to dynamically get access to simulation structure and variables
   [Link] Paddock pad; //Hamze-----Can be used to dynamically get access to simulation structure and variables
   [Input] DateTime Today; // Equates to the value of the current simulation date - value comes from CLOCK
   private string soil_name="Soil";
   [Input] double wf;      // Use the same water factor (SoilN)
   [Input] double[] oc; //Soil OC percent
   [Input] double[] ph; //Soil pH
   [Input] double[] nh4;
   [Input] double[] no3;
   [Input] double[] dlayer;
   [Input] double[] hum_c;
   [Input] double[] biom_c;
   [Input] double[] bd;
   [Input] double rain;
   [Input] double[] nit_tot;

   [Input] double[] no3_min; //Min NO3 in soil per layer
   [Input] double[] nh4_min; //Min NH4 in soil per layer
   double[] tf;      // Use the same temperature factor (SoilN)

   [Param] int biochar_added;      // in kg/ha
   [Param] double frac_c_biochar;  // C in biochar
   [Param] double biochar_loss;    // usually there is a loss during application that might impact calculations
   [Param] double MRT1;             // mean residence time for the labile biochar pool
   [Param] double MRT2;             // mean residence time for the resistant biochar pool
   [Param] double frac_labile;     // labile fraction of biochar; this depends on the biochar type - varies from 1 to 30%.
   [Param] double ef_biochar;      // efficiency of biochar retained in the system
   [Param] double fr_biochar_biom; // a small portion goes to BIOM (usually this is zero) and the rest goes to HUM
   [Param] double biochar_cn;         // CN ratio of the new biochar pool
   [Param] string date_of_application; //The date biochar was adde
   [Param] double sand; // Sand percent of soil
   [Param] double clay; //Clay percent of soil
   [Param] string decomp_switch; //Whether or not biochar affects decomposition
   [Param] string nitrification_switch; //Whether or not biochar affects nitrification
   [Param] string ph_switch; //whether biochar affects ph
   [Param] string ll_switch;
   [Param] string dul_switch;
   [Param] string xf_switch;
   [Param] string kl_switch;
   [Param] string bd_switch;
   [Param] string biochar_c_switch;
   [Param] string swcon_switch;
   [Param] string ks_switch;
   [Param] string sat_switch;
   [Param] double prim_hum;//priming effects
   [Param] double prim_biom;
   [Param] double prim_cell;
   [Param] double prim_carb;
   [Param] double prim_lign;
   [Param] double prim_fr;
   [Param] double prim_ef;
   [Param] double prim_fr_fom;
   [Param] double prim_ef_fom;
   //[Param] string soil_name;
   [Param] double soil_cn; //C:N ratio of soil (SoilN)
   [Param] double biom_cn;
   [Param] double incorp_depth;
   [Param] double tillage;
   [Param] double dul_qual;
   [Param] double bd_qual;
   [Param] string soil_order;
   [Param] double nclay_portion;
   [Param] double bc_cce;
   [Param] double bc_cec;
   [Param] double cnrf_bc_coeff;
   [Param] double cnrf_bc_optcn;
   [Param] double uph;
   [Param] double lph;
   [Param] double ab_val;
   [Param] double bot_slope;
   [Param] double bc_wfps_factor;

   [Param] double nh4_adsorption;
   [Param] double nh4_desorption;

   [Output] double[] BiocharC;             // BiocharC = biochar_added * frac_c_biochar * biochar_loss
   [Output] double BiocharC_total;    // Ammount of biochar c in each individual soil layer
   [Output] double[] dlt_c_min_biochar;    // here I use a douple exponential function instead of a first order decay
   [Output] double[] dlt_c_biochar_co2;    // 1 - efficiency
   [Output] double[] dlt_c_biochar_biom;   //
   [Output] double[] dlt_c_biochar_hum;
   [Output] double[] dlt_n_min_biochar;
   [Output] double[] n_demand_bc;
   [Output] double[] n_avail_bc;
   [Output] double[] bc_nh4;
   [Output] double[] BiocharC_labile;
   [Output] double[] BiocharC_resistant;
   [Output] double BiocharC_labile_total;
   [Output] double BiocharC_resistant_total;
   [Output] double rd_hum_fac = 0.0, rd_fr_fom_fac = 0.0, rd_ef_fom_fac = 0.0;
   [Output] double rd_biom_fac = 0.0, rd_carb_fac = 0.0, rd_cell_fac = 0.0, rd_lign_fac = 0.0, rd_ef_fac = 0.0, rd_fr_fac = 0.0;
   [Output] double[] saxon_bd;
   [Output] double[] saxon_sat;
   [Output] double[] till_bd;
   [Output] double[] till_sat;
   [Output] double[] cnr_bcf; //the cnrf_bc. called as such to avoid a name conflict with SurfaceOrganicMatter (need to look into)
   [Output] double[] scale_factor;
   [Output] double[] dlt_dlayer;
   [Output] double[] biochar_bd; //internal virtual bd for soil water
   [Output] double[] dlt_c_min_biochar_pot;
   [Output] double[] total_stress;

   private double[] init_soil_fac;

   //Debugging related output variables
   //How we communicate with other modules
   [Event] public event BiocharDecomposedDelegate BiocharDecomposed;
   [Event] public event BiocharAppliedDelegate BiocharApplied;

   private int dayApp;
   private int moApp;
   private int yearApp;

   //kb1 = labile pool, kb2 is resistant (decomp rate constants)
   private double kb1, kb2;

   //thisPH = conversion of soil pH, the rest are soil parameters
   private double[] thisPH, dul, ll15, sat, swcon, ks;
   //the date of application
   private DateTime date;
   //nh4 date
   private DateTime nh4_date;

   //The base titration value calcutated from default soil pH
   private double[] titrat_val;

   private double biochar_ph_value; //10^-(bc_ph)

   private double[] yesterday_oc; //OC from yesterday so we can compute delta
   private double rainAmt;
   private double[] initialBD;
   //The ratio of biochar mass in the soil to mass of that segment of soil
   private double[] MassComparison;
   //Respective mass of each layer, computed using bulk density on day 1
   private double[] LayerMass;

   private bool firstTill;



   private int till_depth_layer;
   private double q_ll;//Quality factors
   [Output] double[] soil_cec;
   [Output] double[] soil_cec_orig;

   [Output] double wfps_factor;


   // The following event handler will be called once at the beginning of the simulation
   [EventHandler] public void OnInitialised()
    {
      string[] names;
      double[] estimates;
      string[] stringSeparators = new string[] {" "};
      /// Hamze - I'm trying to find the soil name through looping all the childerns of the paddok (Maybe not very efficient but it's working for now)
      pad = MyPaddock.Parent.ChildPaddocks[0];
      foreach (Component s in pad.Children)      {
         if(s.Name.Contains("Water")){
            names = s.Name.Split(stringSeparators, StringSplitOptions.None);
            soil_name = names[0];
         }
      }

      bc_nh4 = new double[oc.Length];
      thisPH = new double[ph.Length];
      soil_cec = new double[oc.Length];
      soil_cec_orig = new double[oc.Length];
      titrat_val = new double[oc.Length];
      MassComparison = new double[oc.Length];
      LayerMass = new double[oc.Length];
      biochar_bd = bd;
      for(int i = 0; i < ph.Length; i++)
      {
         thisPH[i] = ph[i];
         soil_cec[i] = get_soil_CEC(i);
         titrat_val[i] = 216.51*Math.Exp(ph[i]*(-0.91));
         soil_cec_orig[i] = get_soil_CEC(i);
         LayerMass[i] = bd[i] * dlayer[i] * 10000;
      }
      biochar_ph_value = Math.Pow(10, -bc_cce);

      //To convert MRT to kb

      kb1 = Math.Log(2.0) / (MRT1 * 365);
      kb2 = Math.Log(2.0) / (MRT2 * 365);

      init_soil_fac = new double[oc.Length];
      for (int i = 0; i < oc.Length; i++)
      {
         init_soil_fac[i] = 100 / (dlayer[i] * bd[i]);
      }

      //Only works for USA format dates - change in future? Maybe change input format?
      dayApp = Convert.ToInt32(date_of_application.Substring(3, 2));
      moApp = Convert.ToInt32(date_of_application.Substring(0, 2));
      yearApp = Convert.ToInt32(date_of_application.Substring(6, 4));

      date = new DateTime(yearApp, moApp, dayApp);


      BiocharC_labile = new double[oc.Length];
      BiocharC_resistant = new double[oc.Length];
      BiocharC = new double[oc.Length];

      firstTill = false;

      //initialize a lot of things
      dlt_c_biochar_co2 = new double[oc.Length];
      dlt_c_biochar_biom = new double[oc.Length];
      dlt_c_biochar_hum = new double[oc.Length];
      dlt_c_min_biochar = new double[oc.Length];
      dlt_n_min_biochar = new double[oc.Length];
      n_demand_bc = new double[oc.Length];
      n_avail_bc = new double[oc.Length];
      yesterday_oc = new double[oc.Length];
      saxon_bd = new double[oc.Length];
      saxon_sat = new double[oc.Length];
      till_bd = new double[oc.Length];
      till_sat = new double[oc.Length];
      cnr_bcf = new double[oc.Length];
      scale_factor = new double[oc.Length];
      dlt_dlayer = new double[oc.Length];
      dlt_c_min_biochar_pot = new double[oc.Length];
      total_stress = new double[oc.Length];

      rainAmt = 0.0;
      initialBD = bd;
      q_ll = 0.01;

   }


   //Called each daily timestep


   [EventHandler] void OnProcess()
   {
      //Delta arrays for each variable
      rainAmt += rain;

      double[] dlt_ks = new double[oc.Length];
      double[] dlt_dul = new double[oc.Length];
      double[] dlt_ll = new double[oc.Length];
      double[] dlt_bd = new double[oc.Length];
      double[] dlt_swcon = new double[oc.Length];
      double[] dlt_sat = new double[oc.Length];
      double[] dlt_hum = new double[oc.Length];
      double[] dlt_biom = new double[oc.Length];
      double[] dlt_ph = new double[oc.Length];
      double[] dlt_n_avail = new double[oc.Length];
      double[] dlt_biochar_c = new double[oc.Length];
      double[] bc_nh4_dlt = new double[oc.Length];
      double[] dlt_kl = new double[oc.Length];



      for (int i = 0; i < oc.Length; i++)//Since kl's effect is multiplicative, its default needs to be 1
         dlt_kl[i] = 1.0;

      //computeDULandBD(out saxon_dul, out saxon_bd, 0);
      //saxon_ll = computeLL(0);
      //saxon_sat = giveSAT(0);
      if (Today < date)
      {
         for (int i = 0; i < dlayer.Length; i++)
         {
            saxon_bd[i] = bd[i];
         }
      }
      if (Today == date)
         //Step 1
         applyBiochar();
      if (Today > date)
      {
         for (int i = 0; i < oc.Length; i++)//try looping through all layers
         {
            MyPaddock.Get(soil_name + " Nitrogen.tf", out tf);//This si why soil name needs to be an input parameter

            MassComparison[i] = (BiocharC[i] / frac_c_biochar)/(LayerMass[i]);
            double n_demand, dlt_n_min_tot_bc;

         //double rd_hum_fac = 0.0, rd_biom_fac = 0.0, rd_carb_fac = 0.0, rd_cell_fac = 0.0, rd_lign_fac = 0.0, rd_ef_fac = 0.0, rd_fr_fac = 0.0;
            double nh4_change;

            double new_ph;
            //Local variables for this specific soil layer
            double new_layer_ll, new_layer_bd, new_layer_dul, new_layer_ks, new_layer_sat, new_layer_swcon = 0.0;
            //step 2
            //When biochar functionality is expanded, every instance of a '0' method argument or array index will be changed to a layer index, and layers that biochar
            //alters will be iterated over in a for loop, but for now biochar only changes the first layer
            dlt_c_min_biochar[i] = computeDailyBCCarbDecomp(i);
            //step 3
            computeDLTs(out dlt_c_biochar_biom[i], out dlt_c_biochar_hum[i], out dlt_c_biochar_co2[i], dlt_c_min_biochar[i]);
            //step 4 -inactive


            n_demand = getNDemand(dlt_c_biochar_biom[i], dlt_c_biochar_hum[i]);
            dlt_n_min_tot_bc = computeNFromDecomp(dlt_c_min_biochar[i]);

            n_demand_bc[i] = n_demand;
            n_avail_bc[i] = dlt_n_min_tot_bc;
            dlt_n_min_biochar[i] = dlt_n_min_tot_bc - n_demand; //This will get added to dlt_n_min_tot I think
            //Step 5 happens in model

            //Step 6

            get_rd_factors(out rd_hum_fac, out rd_biom_fac, out rd_carb_fac, out rd_cell_fac, out rd_lign_fac,
               out rd_ef_fac, out rd_fr_fac, out rd_ef_fom_fac, out rd_fr_fom_fac, i);

            //Step 7

            nh4_change = get_NH4_changes(i);
            //Step 8

            soil_cec[i] = get_new_cec(i);
            new_ph = get_new_ph(i);

            //For computing delta locally.

            getCurrentSoilWatValues();


            //Step 9
            new_layer_ll = computeLL(i);
            computeDULandBD(out new_layer_dul, out new_layer_bd, i);

            //new_layer_sat = giveSAT(i); //Active but not being used
            /**
            new_layer_swcon = computeSWCON(0, new_layer_sat, new_layer_bd);
            new_layer_ks = computeKS(0, new_layer_sat, new_layer_dul, new_layer_ll);
            **/


            //End of steps
            /**
            * The biochar decomposed event requires that changes be in terms of delta.
            * However, our equations give the total value, not the change, so we must compute
            * the change within this script.
            **/
            //dlt_ks[0] = new_layer_ks - ks[0];
            dlt_dul[i] = new_layer_dul;// -dul[i];
            dlt_ll[i] = new_layer_ll;// -ll15[i];



         //not actually a delta, model stops working if it is. Instead, is the next wanted value of bd
            if (BiocharC[i] != 0.0)
            {
               dlt_bd[i] = new_layer_bd + saxon_bd[i];
            }
            else
               dlt_bd[i] = initialBD[i];


            dlt_hum[i] = dlt_c_biochar_hum[i];
            dlt_biom[i] = dlt_c_biochar_biom[i];

            dlt_biochar_c[i] = dlt_c_min_biochar[i];

            dlt_ph[i] = new_ph - ph[i];

            dlt_n_avail[i] = dlt_n_min_biochar[i];

            bc_nh4_dlt[i] = nh4_change;
            if (kl_switch.Equals("on")) //So that kl does not go to 0
               dlt_kl[i] = 1; //what became of step 10


         }
            //End of loop
            //The data structure for our decomposition event
            BiocharDecomposedType BiocharDecomp = new BiocharDecomposedType();

         getCurrentSoilWatValues();
         //region for andales saxon mergeing - to later integrate with
         double[] andales_bd = AndalesBD();
         double[] bd_new = biggest_bd_dlt(dlt_bd, andales_bd);
         double[] sat_dlt_new = sat_in_terms_of_dlt(bd_new);

         for (int i = 0; i < oc.Length; i++)
         {
            double temp;
            saxon_sat[i] = (-(dlt_bd[i] - saxon_bd[i]) / 2.65) * 0.9 + sat[i];
            saxon_bd[i] = dlt_bd[i];
            till_bd[i] = andales_bd[i];
            till_sat[i] = ( -(andales_bd[i] - biochar_bd[i]) / 2.65) * 0.9 + sat[i];
            temp = 100 / (bd_new[i] * init_soil_fac[i]);
            dlt_dlayer[i] = temp - dlayer[i];
         }

         biochar_bd = bd_new;
            //Script control area
            if (dul_switch.Equals("on"))
            {
               BiocharDecomp.dlt_dul = dlt_dul;
            }
            if (ll_switch.Equals("on"))
            {
               BiocharDecomp.dlt_ll = dlt_ll;
            }
            if (sat_switch.Equals("on"))
            {
               BiocharDecomp.dlt_sat = sat_dlt_new;
            }
         //Since errors occur if bd is in terms of delta, we need to ensure that if bd is off, we still get what we want
            if(bd_switch.Equals("on"))
            {
            BiocharDecomp.dlt_bd = bd;
            //BiocharDecomp.dlt_bd = bd_new;
               //MyPaddock.Set("dlt_dlayer", dlt_dlayer);
            }
            else
            {
               BiocharDecomp.dlt_bd = bd;
            }
            if (swcon_switch.Equals("on"))
            {
               BiocharDecomp.dlt_swcon = dlt_swcon;
            }
            if (ks_switch.Equals("on"))
            {
               BiocharDecomp.dlt_ks = dlt_ks;
            }


            if (biochar_c_switch.Equals("on"))
            {
               BiocharDecomp.hum_c = dlt_hum;
               BiocharDecomp.biom_c = dlt_biom;
               BiocharDecomp.dlt_biochar_c = dlt_biochar_c;
            }

            if (nitrification_switch.Equals("on"))
            {
               BiocharDecomp.bc_nh4_change = bc_nh4_dlt;
            }

            if (decomp_switch.Equals("on"))
            {
               BiocharDecomp.dlt_rd_hum = rd_hum_fac;
               BiocharDecomp.dlt_rd_biom = rd_biom_fac;
               BiocharDecomp.dlt_rd_carb = rd_carb_fac;
               BiocharDecomp.dlt_rd_cell = rd_cell_fac;
               BiocharDecomp.dlt_rd_lign = rd_lign_fac;
               BiocharDecomp.dlt_rd_ef = rd_ef_fac;
               BiocharDecomp.dlt_rd_fr = rd_fr_fac;
            BiocharDecomp.dlt_rd_ef_fom = rd_ef_fom_fac;
            BiocharDecomp.dlt_rd_fr_fom = rd_fr_fom_fac;

            }


            BiocharDecomp.dlt_n_biochar = dlt_n_avail;
            if (ph_switch.Equals("on"))
            {
               BiocharDecomp.dlt_ph = dlt_ph;
            }

         BiocharDecomp.bc_wfps_factor = 1.0 - this.bc_wfps_factor;


            BiocharDecomp.dlt_kl = dlt_kl; //Since KL is a multiplicative effect, if we do not always assign this KL will go to 0
            //If uninitialized, it is 0 by default

            BiocharDecomposed.Invoke(BiocharDecomp);
         Console.WriteLine("Biochar bd: " + biochar_bd[0]);


      }


      for (int i = 0; i < oc.Length; i++)
         yesterday_oc[i] = oc[i]; //Make a deep copy


   }


   //Step 1 section
   private void applyBiochar()
   {
      /**
      * This puts the proper amount of biochar into the necessary soil layers
      * based off of how deeply the biochar was applied, assuming even distribution
      * of BC throughout its application range. Based off an implementation already
      * in APSIM.
      **/
      wfps_factor = 1.0 - bc_wfps_factor;
      double depth_so_far = 0.0;
      double depth_to_go;
      double frac_bc_layer;
      double layer_incorp_depth;
      for (int i = 0; i < dlayer.Length; i++)
      {
         depth_to_go = incorp_depth - depth_so_far;
         if (depth_to_go <= 0.0)
            depth_to_go = 0.0;
         layer_incorp_depth = Math.Min(depth_to_go, dlayer[i]);
         frac_bc_layer = layer_incorp_depth / incorp_depth;
         BiocharC[i] = biochar_added * frac_c_biochar * (1 - biochar_loss) * frac_bc_layer;
         BiocharC_labile[i] = BiocharC[i] * frac_labile;
         BiocharC_resistant[i] = BiocharC[i] * (1 - frac_labile);

         depth_so_far += dlayer[i];
      }
      BiocharAppliedType BioApp = new BiocharAppliedType();
      double[] bc_carb_applied = new double[oc.Length];
      for (int i = 0; i < bc_carb_applied.Length; i++)
         bc_carb_applied[i] = BiocharC[i];

      BioApp.bc_carbon_ammount = bc_carb_applied;
      BiocharApplied.Invoke(BioApp);

      Console.WriteLine("Biochar has been applied Ammount: " + biochar_added + " kg/ha" + "Depth: " + incorp_depth + " (mm)");
      sumSoilBCFirstTime();


   }
   //Step 2 section

   private double computeDailyBCCarbDecomp(int layer)
   {
      double pot_hum, pot_biom, pot_co2, pot_tot;
      cnr_bcf[layer] = calculateCNR_BCF(layer);
      calculatePotentialDecomp(layer, cnr_bcf[layer], out pot_hum, out pot_biom, out pot_co2, out pot_tot);
      scale_factor[layer] = calculateScale(layer, pot_biom, pot_hum, pot_tot);


      return calculateActualDecomp(layer, scale_factor[layer], cnr_bcf[layer]);
   }

   //Helper methods for biochar decomposition

   private double calculateCNR_BCF (int layer)
   {
      double cnr_bc; //Biochar cn ratio for decomposition
      double n_available_cnr; // Potential nitrogen available for bc decomposition?

      //bc available N + mineral N in layer
      n_available_cnr = (BiocharC_labile[layer] / biochar_cn) + nh4[layer] - nh4_min[layer] + no3[layer] - no3_min[layer];
      if (n_available_cnr != 0.0)
         cnr_bc = (BiocharC_labile[layer] / n_available_cnr);
      else
         cnr_bc = 0.0;


      double cnrf_bc = Math.Exp(-cnrf_bc_coeff * (cnr_bc - cnrf_bc_optcn) / cnrf_bc_optcn);
      if (cnrf_bc > 1)
         cnrf_bc = 1;
      if (cnrf_bc < 0)
         cnrf_bc = 0;

      return cnrf_bc;
   }

   private void calculatePotentialDecomp(int layer, double cnrf_bc, out double pot_hum, out double pot_biom, out double pot_co2, out double pot_tot)
   {
      double pot_labile = BiocharC_labile[layer] * kb1 * Math.Min( Math.Min(wf , tf[layer]) , cnrf_bc);
      double pot_resist = BiocharC_resistant[layer] * kb2 * Math.Min( Math.Min(wf , tf[layer]) , cnrf_bc);

      pot_tot = pot_labile + pot_resist;
      dlt_c_min_biochar_pot[layer] = BiocharC_labile[layer] * kb1 + BiocharC_resistant[layer] * kb2;
      total_stress[layer] = Math.Min( Math.Min(wf , tf[layer]) , cnrf_bc);
      pot_co2 = pot_tot * (1 - ef_biochar);
      pot_biom = pot_tot * ef_biochar * fr_biochar_biom;
      pot_hum = pot_tot * ef_biochar * (1 - fr_biochar_biom);
   }

   private double calculateScale(int layer, double pot_biom, double pot_hum, double pot_tot)
   {
      double bc_n_min_tot = pot_tot / biochar_cn;
      double n_demand = (pot_biom / biom_cn) + (pot_hum / soil_cn);
      //Calculate n available from mineral n
      double n_avail = nh4[layer] - nh4_min[layer] + no3[layer] - no3_min[layer] + bc_n_min_tot;

      double scale_of;

      if (n_demand > n_avail)
      {
         scale_of = (nit_tot[layer] / (n_demand - bc_n_min_tot));
         if (scale_of > 1)
            scale_of = 1;

      }
      else
         scale_of = 1;

      return scale_of;

   }

   //Performs the actual decomposition of biochar, based off of the limitations the potential runs into
   private double calculateActualDecomp(int layer, double scale_of, double cnrf_bc)
   {
      double decomp1 = BiocharC_labile[layer] * kb1 * Math.Min( Math.Min(wf , tf[layer]) , cnrf_bc) * scale_of;
      BiocharC_labile[layer] -= decomp1;
      double decomp2 = BiocharC_resistant[layer] * kb2 * Math.Min( Math.Min(wf , tf[layer]) , cnrf_bc) * scale_of;
      BiocharC_resistant[layer] -= decomp2;
      if (BiocharC_labile[layer] < 0)
         BiocharC_labile[layer] = 0;
      if (BiocharC_resistant[layer] < 0)
         BiocharC_resistant[layer] = 0;


      BiocharC[layer] = BiocharC_labile[layer] + BiocharC_resistant[layer]; //Remove decomposed ammount from biochar pool

      updateSoilBCTotals(layer);
      return decomp1 + decomp2;
   }

   //End of decomposition helper methods

   //Computes the changes in co2, biom c and humic c due to a change in biochar c

   //Step 3 section

   private void computeDLTs(out double dlt_c_biochar_biom, out double dlt_c_biochar_hum, out double dlt_c_biochar_co2, double dlt_c_min_biochar)
   {
      dlt_c_biochar_co2 = dlt_c_min_biochar * (1 - ef_biochar);
      dlt_c_biochar_biom = dlt_c_min_biochar * ef_biochar * fr_biochar_biom;
      dlt_c_biochar_hum = dlt_c_min_biochar * ef_biochar * (1 - fr_biochar_biom);


   }



   //Step 4 section

   private double getNDemand(double dlt_c_biochar_biom, double dlt_c_biochar_hum)
   {
      return (dlt_c_biochar_biom / biom_cn) + (dlt_c_biochar_hum / soil_cn);  // this biochar n demand, n_demand_bc
   }

   private double computeNFromDecomp(double dlt_c_min_biochar)
   {
      return (dlt_c_min_biochar / biochar_cn); // this is n released during biochar decomposition, n_avail_bc
   }



   //Step 5 happens within the apsim model itself

   //Step 6
   private void get_rd_factors(out double rd_hum_fac, out double rd_biom_fac, out double rd_carb_fac,
      out double rd_cell_fac, out double rd_lign_fac, out double rd_ef_fac, out double rd_fr_fac, out double rd_ef_fom_fac,
      out double rd_fr_fom_fac, int layer)
   {

         rd_hum_fac = (prim_hum * BiocharC_total / 10000);
         rd_biom_fac = (prim_biom * BiocharC_total / 10000);
         rd_carb_fac = (prim_carb * BiocharC_total / 10000);
         rd_cell_fac = (prim_cell * BiocharC_total / 10000);
         rd_lign_fac = (prim_lign * BiocharC_total / 10000);
         rd_ef_fac = (prim_ef * BiocharC_total / 10000);
         rd_fr_fac = (prim_fr * BiocharC_total / 10000);
         rd_ef_fom_fac = (prim_ef_fom * BiocharC_total / 10000);
         rd_fr_fom_fac = (prim_fr_fom * BiocharC_total / 10000);




   }

   //Step 7 big work here pretty sure does not matter ppm or kg/ha since both related by constant

   private double get_NH4_changes(int layer)
   {
      if (BiocharC[layer] > 0.0)
      {
         double cec_ratio = soil_cec[layer] / soil_cec_orig[layer];
         double nh4_absorbed = nh4[layer] * cec_ratio * nh4_adsorption / (1 + cec_ratio * nh4_adsorption);
         double nh4_desorbed = bc_nh4[layer] * cec_ratio * nh4_desorption / (1 + cec_ratio * nh4_desorption);
         double nh4_change = nh4_desorbed - nh4_absorbed;
         bc_nh4[layer] = bc_nh4[layer] - nh4_change;
         return nh4_change;
      }
      else
         return 0.0;
   }


   //Step 8
   private double get_new_ph(int layer)
   {
      return compute_ph_equation(soil_cec[layer], ab_val, layer) + compute_bc_limeing(layer);



   }


   //Step 9 area - Changes to DUL and LL and the like


   private double computeLL(int layer)
   {


      double dlt_oc = oc[layer] - yesterday_oc[layer];

      //double ll15_temp = -0.024 * sand + 0.487 * clay + 0.006 * om + 0.005 * sand * om - 0.013 * clay * om + 0.068 * sand * clay + 0.031;
      //ll15_temp = ll15_temp + 0.14 * ll15_temp - 0.02;
      if (BiocharC[layer] != 0.0)
      {
         return q_ll * (0.0118 + 0.0098 * sand - 0.0255 * clay) * dlt_oc;
      }
      else
         return 0.0;

   }

   //Returns a two element array containing values used in computing DUL and bd for a specific layer, as well as in sat
   private double[] computeDULMidway(int layer)
   {

      double om;
      //four temporary values needed
      double temp1, temp2, temp3, temp4;

      //Based off of documentation equations

     /**
      temp1 = -0.251 * sand + 0.195 * clay + 0.011 * om + 0.006 * sand * om - 0.027 * clay * om + 0.452 * sand * clay + 0.299;//dula
      temp1 = temp1 + (1.283 * temp1 * temp1 - 0.374 * temp1 - 0.015);//dulb
      temp2 = -0.097 * sand + 0.043;//dulc
      temp3 = 0.278 * sand + 0.034 * clay + 0.022 * om - 0.018 * sand * om - 0.027 * clay * om - 0.584 * sand * clay + 0.078;//duld
      temp3 = temp3 + (0.636 * temp3 - 0.107);//dule
      temp4 = temp1 + temp3;//dulf
      temp4 = temp4 + temp2;//dulg
      **/

      //Returns return[0] = DULh from documentation, return[1] = DULb from documentation, as both values are needed elsewhere
      return new double[] {0.0, 0.0};



   }

   //Computes DUL and BD based off of changes to soil OC due to biochar in that layer
   private void computeDULandBD(out double layer_dul, out double layer_bd, int layer)
   {


      double dlt_oc = oc[layer] - yesterday_oc[layer];

      double q_dul = 1.3067 * Math.Exp(-dul_qual * oc[layer]);
      double q_bd = 1.3067 * Math.Exp(-bd_qual * oc[layer]);
      /**
      midDUL = computeDULMidway(layer);
      BDa = midDUL[0] * df;

      gravels = ((BDa / 2.65) * gravelw) / (1 - gravelw * (1 - BDa / 2.65));
      **/
      if (BiocharC[layer] != 0.0)
      {
         layer_bd = q_bd * (-0.2332 + 0.115 * sand + 0.35 * clay) * dlt_oc;

         layer_dul = q_dul * (0.0261 + 0.0072 * sand - 0.0561 * clay) * dlt_oc;
      }
      else
      {
         layer_bd = 0.0;
         layer_dul = 0.0;
      }



   }

   //Gives the SAT for a given layer based off of the layer's newly computed bulk density
   /**
   private double giveSAT (int layer)
   {



      double dlt_oc = oc[layer] - yesterday_oc[layer];
      if (BiocharC[layer] != 0.0)
      {
         return ( 0.0836 - 0.0412 * sand - 0.1255 * clay)  * dlt_oc;
      }
      else
         return 0.0;
   }
   **/

   //deprecated
   private double computeKS(int layer, double layer_sat, double layer_dul, double layer_ll)
   {
      return 0.0;


   }
   //deprecated
   private double computeSWCON(int layer, double layer_sat, double layer_dul)
   {
      double SWCON = (layer_sat / 0.95 - layer_dul) / (layer_sat / 0.95);

      return SWCON;

   }

   //Gets the current values of various soil water associated variables so we can compute our dlts based off of the difference
   private void getCurrentSoilWatValues()
   {

      MyPaddock.Get(soil_name + " Water.dul", out dul);
      MyPaddock.Get(soil_name + " Water.ll15", out ll15);
      MyPaddock.Get(soil_name + " Water.sat", out sat);
      //MyPaddock.Get(soil_name + " Water.bd", out bd);
      MyPaddock.Get(soil_name + " Water.swcon", out swcon); //doesn't work
      MyPaddock.Get(soil_name + " Water.ks", out ks);
   }


   //Updates the total amount of soil biochar in the system. We need to make how this is done better, so it is only run once,
   //as it is a O(n) operation being run within a O(n) operation, making our whole daily algorithm O(n^2) when it doesn't
   //need to be. Done?
   private void updateSoilBCTotals(int layer)
   {
      if (layer == 0)//Zero all values the first time this is called each day
      {
         BiocharC_total = 0;
         BiocharC_labile_total = 0;
         BiocharC_resistant_total = 0;
      }
      BiocharC_total += BiocharC[layer];
      BiocharC_labile_total += BiocharC_labile[layer];
      BiocharC_resistant_total += BiocharC_resistant[layer];
   }


   //Special method that sums the total BC in the system. Used only during the apply biochar process.
   private void sumSoilBCFirstTime()
   {
      BiocharC_total = 0;
      BiocharC_labile_total = 0;
      BiocharC_resistant_total = 0;
      for (int i = 0; i < dlayer.Length; i++)
      {
         BiocharC_total += BiocharC[i];
         BiocharC_labile_total += BiocharC_labile[i];
         BiocharC_resistant_total += BiocharC_resistant[i];
      }

   }
   //For the andales methods of bd
   [EventHandler] void OnTillage(TillageType Till)
   {
      firstTill = true;

      rainAmt = 0.0;
      float depth = Till.tillage_depth;
      for (int i = 0; i < oc.Length; i++)
      {
         depth -= (float) dlayer[i];
         till_depth_layer = i;
         if ( depth <= 0)
         {
            break;
         }

      }
   }
   //Method that gives BD computed with the andales equation
   private double[] AndalesBD()
   {
      double[] ret = new double[oc.Length];
      double q_bd;
      double q_const = 1.3067;

      for (int layer = 0; layer < ret.Length; layer++)
      {
         if (oc[layer] < 0.5)
            q_const = 1.8067;
         if (firstTill && layer <= till_depth_layer)
         {
            q_bd = q_const * Math.Exp(-bd_qual * oc[layer]);
            ret[layer] = q_bd * (tillage * initialBD[layer] - initialBD[layer]) * Math.Exp(-(5 * (1 - 0.205 * oc[layer])) * rainAmt * 0.00217);//Based off of Andales equation
            ret[layer] = ret[layer] + initialBD[layer];
            if (ret[layer] < initialBD[layer] - ((1.0 - tillage) * initialBD[layer] * q_bd))//really confusing. basically if it is lower than it could possibly be (the andales equation fails to capture reality for oc > 4.8)
               ret[layer] = initialBD[layer] - ((1.0 - tillage) * initialBD[layer] * q_bd);// we set it to the lowest possible and regard it as (mostly) constant
         }
         else
            ret[layer] = initialBD[layer];
      }

      return ret;
   }
   //Computes the biggest delta associated with bd
   private double[] biggest_bd_dlt(double[] dlt_bd, double[] andales_bd)
   {
      double[] ret = new double[saxon_bd.Length];
      for (int layer = 0; layer < oc.Length; layer++)
      {
         if (Math.Abs(dlt_bd[layer] - initialBD[layer])>= Math.Abs(andales_bd[layer] - initialBD[layer]))
         {
            ret[layer] = dlt_bd[layer];
         }
         else
            ret[layer] = andales_bd[layer];
      }

      return ret;
   }

   private double[] sat_in_terms_of_dlt(double[] bd_new)
   {
      double[] ret = new double[bd_new.Length];
      if (bd_switch == "on")
      {
         for (int layer = 0; layer < bd_new.Length; layer++)
         {


            ret[layer] = (-(bd_new[layer] - biochar_bd[layer]) / 2.65) * 0.9;

         }
      }
      else//still need SAT estimation if no bd change... (old... maybe unneccessary with new change?? but then bd off is unmeaningful)
      {
         for (int layer = 0; layer < oc.Length; layer++)
         {
            double dlt_oc = oc[layer] - yesterday_oc[layer];
            if (BiocharC[layer] != 0.0)
            {
               ret[layer] = ( 0.0836 - 0.0412 * sand - 0.1255 * clay) * dlt_oc;
            }
            else
               ret[layer] = 0.0;

         }
      }
      return ret;
   }


   //Computes soil CEC on the first day of the simulation to have a constant value for soil CEC
   //Which is later used as a base for when BC is applied (i am not sure if we should maintain pH at all?)
   private double get_soil_CEC(int layer)
   {
      if (soil_order == "Aridisol")
      {
         return Math.Exp(0.042 * Math.Log(oc[layer]) + 0.828 * Math.Log(nclay_portion * clay * 100) + 0.236);
      }
      else if (soil_order == "Entisol")
      {
         return Math.Exp(0.078 * Math.Log(oc[layer]) + 0.873 * Math.Log(nclay_portion * clay * 100) + 0.084);
      }
      else if (soil_order == "Gelisol")
      {
         return Math.Exp(0.359 * Math.Log(oc[layer]) + 0.49 * Math.Log(nclay_portion * clay * 100) + 1.05);
      }
      else if (soil_order == "Inceptisol")
      {
         return Math.Exp(0.134 * Math.Log(oc[layer]) + 0.794 * Math.Log(nclay_portion * clay * 100) + 0.239);
      }
      else if (soil_order == "Mollisol")
      {
         if (oc[layer] < 0.3)
            return Math.Exp(0.932 * Math.Log(nclay_portion * clay * 100) - 0.174);
         else
            return Math.Exp(0.113 * Math.Log(oc[layer]) + 0.786 * Math.Log(nclay_portion * clay * 100) + 0.475);
      }
      else if (soil_order == "Vertisol")
      {
         return Math.Exp(0.059 * Math.Log(oc[layer]) + 0.86 * Math.Log(nclay_portion * clay * 100) + 0.312);
      }
      else if (soil_order == "Histosol")
      {
         return Math.Exp(0.319 * Math.Log(oc[layer]) + 0.497 * Math.Log(nclay_portion * clay * 100) + 1.075);
      }
      else if (soil_order == "Alfisol")
      {
         if (oc[layer] < 0.3)
            return Math.Exp(0.911 * Math.Log(nclay_portion * clay * 100) - 0.308);
         else
            return Math.Exp(0.158 * Math.Log(oc[layer]) + 0.805 * Math.Log(nclay_portion * clay * 100) + 0.216);
      }
      else if (soil_order == "Spodosol")
      {
         return Math.Exp(0.045 * Math.Log(oc[layer]) + 0.798 * Math.Log(nclay_portion * clay * 100) + 0.029);
      }
      else if (soil_order == "Ultisol")
      {
         return Math.Exp(0.184 * Math.Log(oc[layer]) + 0.57 * Math.Log(nclay_portion * clay * 100) + 0.365*Math.Log((1 - clay - sand)*100) - 0.906);
      }
      else if (soil_order == "Oxisol")
      {
         return 2.738 * oc[layer] + 0.103 * nclay_portion * clay * 100 + 0.123 * (100*(1 - clay - sand)) - 2.531;
      }
      else
         return 20.0;

   }
   //Computes a new biochar adjusted value for soil CEC
   private double get_new_cec(int layer)
   {
      return soil_cec_orig[layer] * (1 - MassComparison[layer]) + bc_cec * MassComparison[layer];
   }
   //Computes a value for soil pH based off of the given values for CEC and acid, using that layer's particular titration curve value
   private double compute_ph_equation(double cec_val, double acid, int layer)
   {
      return (uph - lph) / (1 + titrat_val[layer] * Math.Exp(-acid/cec_val)) + lph;
   }
   //Computes a value that describes the lime effect that biochar has on soils
   private double compute_bc_limeing(int layer)
   {
      double bc_alkaline = MassComparison[layer] * bc_cce;
      return bc_alkaline * (uph - thisPH[layer]) * (thisPH[layer] - lph) * bot_slope / ((uph - lph) * soil_cec[layer]);
   }


//TODO sand clay gravelw into arrays and gotten from simulation


}
'''
    else:
        rule = ET.SubElement(folder, 'manager2', name=name, shortcut=shortcut+'/'+name)
    return rule

def reset_on_fixed_date(folder, crop, soilmodule, reset_date, name='Reset water, nitrogen and surfaceOM on fixed date', shortcut=None, surfaceommodule='surface organic matter', resetWater='yes', resetNitrogen='yes', resetSurfaceOM='yes', occurrence='start_of_day'):
    '''
    Resets water, nitrogen, and surfaceOM on a fixed date.

    Parameters
    ----------

    Returns
    -------
    The management rule.
    '''
    if shortcut == None:
        rule = ET.SubElement(folder, 'manager', name=name)

        ui = ET.SubElement(rule, 'ui')
        ET.SubElement(ui, 'category', type='category', description="When should a reset be done")
        ET.SubElement(ui, 'reset_date', type='ddmmdate', description="Enter date of reset (dd-mmm)").text = reset_date
        ET.SubElement(ui, 'category', type='category', description="Reset details")
        ET.SubElement(ui, 'soilmodule', type='modulename', description="Name of your soil module : ").text = soilmodule
        ET.SubElement(ui, 'surfaceommodule', type='modulename', description="Name of your surface organic matter module : ").text = surfaceommodule
        ET.SubElement(ui, 'resetWater', type='yesno', description="Reset soil water?").text = resetWater
        ET.SubElement(ui, 'resetNitrogen', type='yesno', description="Reset soil nitrogen?").text = resetNitrogen
        ET.SubElement(ui, 'resetSurfaceOM', type='yesno', description="Reset surface organic matter?").text = resetSurfaceOM

        script = ET.SubElement(rule, 'script')
        ET.SubElement(script, 'text').text = '''
           if (today = date('[reset_date]')) then
            resetWater = '[resetWater]'
            resetNitrogen  = '[resetNitrogen]'
            resetSurfaceOM = '[resetSurfaceOM]'
            if (resetWater = 'yes') then
                '[soilmodule] Water' reset
            endif
            if (resetNitrogen = 'yes') then
                '[soilmodule] Nitrogen' reset
            endif
            if (resetSurfaceOM = 'yes') then
                '[surfaceommodule]' reset
            endif
            act_mods reseting
         endif
           '''
        ET.SubElement(script, 'event').text = occurrence
    else:
        rule = ET.SubElement(folder, 'manager', name=name, shortcut=shortcut+'/'+name)
    return rule

def reset_on_sowing(folder, crop, soilmodule, name='Reset water, nitrogen and surfaceOM on sowing', shortcut=None, surfaceommodule='surface organic matter', resetWater='yes', resetNitrogen='yes', resetSurfaceOM='yes', eventname='sowing'):
    '''
    Resets water, nitrogen, and surfaceOM on sowing.

    Parameters
    ----------

    Returns
    -------
    The management rule.
    '''
    if shortcut == None:
        rule = ET.SubElement(folder, 'manager', name=name)

        ui = ET.SubElement(rule, 'ui')
        ET.SubElement(ui, 'category', type='category', description="When should a reset be done")
        ET.SubElement(ui, 'modulename', type='modulename', description="The module the event is to come from : ").text = crop
        ET.SubElement(ui, 'eventname', type='text', description="On which event should a reset be done : ").text = eventname
        ET.SubElement(ui, 'category', type='category', description="Reset details")
        ET.SubElement(ui, 'soilmodule', type='modulename', description="Name of your soil module : ").text = soilmodule
        ET.SubElement(ui, 'surfaceommodule', type='modulename', description="Name of your surface organic matter module : ").text = surfaceommodule
        ET.SubElement(ui, 'resetWater', type='yesno', description="Reset soil water?").text = resetWater
        ET.SubElement(ui, 'resetNitrogen', type='yesno', description="Reset soil nitrogen?").text = resetNitrogen
        ET.SubElement(ui, 'resetSurfaceOM', type='yesno', description="Reset surface organic matter?").text = resetSurfaceOM

        script = ET.SubElement(rule, 'script')
        ET.SubElement(script, 'text').text = '''
            resetWater = '[resetWater]'
            resetNitrogen  = '[resetNitrogen]'
            resetSurfaceOM = '[resetSurfaceOM]'
            if (resetWater = 'yes') then
                '[soilmodule] Water' reset
            endif
            if (resetNitrogen = 'yes') then
                '[soilmodule] Nitrogen' reset
            endif
            if (resetSurfaceOM = 'yes') then
                '[surfaceommodule]' reset
            endif
            if (resetWater = 'yes' or resetNitrogen = 'yes' or resetSurfaceOM = 'yes') then
               act_mods reseting
            endif
           '''
        ET.SubElement(script, 'event').text = '[modulename].[eventname]'
    else:
        rule = ET.SubElement(folder, 'manager', name=name, shortcut=shortcut+'/'+name)
    return rule
