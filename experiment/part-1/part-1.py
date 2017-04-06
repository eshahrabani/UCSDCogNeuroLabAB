#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.83.01), January 11, 2016, at 14:24
If you publish work using this script please cite the relevant PsychoPy publications
  Peirce, JW (2007) PsychoPy - Psychophysics software in Python. Journal of Neuroscience Methods, 162(1-2), 8-13.
  Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy. Frontiers in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008
"""

from __future__ import division  # so that 1/3=0.333 instead of 1/3=0
from datetime import datetime
from psychopy import locale_setup, visual, core, data, event, logging, sound, gui
from psychopy.constants import *  # things like STARTED, FINISHED
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import sin, cos, tan, log, log10, pi, average, sqrt, std, deg2rad, rad2deg, linspace, asarray
from numpy.random import random, randint, normal, shuffle, uniform, seed
import os  # handy system and path functions
import sys # to get file system encoding

# Delete outdated constants after testing new ones.
'''foveal_angle = 5.0                               # degrees
peripheral_angle = 11.6
distance_from_screen = 177.8                     # centimeters (65 in)
cm_per_pixel = (56.5*2.54)/1920.0                # cm/pixel as per physical measurements 
width_of_screen = 1920.0 * cm_per_pixel          # 143.51 cm
height_of_screen = 1080.0 * cm_per_pixel         # 80.72  cm

foveal_radius = 7.76          # should be calculated by hand        
max_image_width =  18.06*1.5  # from peripheral angle
peripheral_radius = height_of_screen/2.0 - (max_image_width/2.0)'''


### EXPERIMENTAL CONSTANTS ###

# Constants relevant to part 1 only.
fixation_mark_duration = 1.0 # seconds
stim_duration = 0.130 # seconds (130 ms)
time_to_respond = 4.0 # seconds (time to respond to stim after it disappears)

total_trial_duration = fixation_mark_duration + stim_duration + time_to_respond

# Universal constants.
foveal_angle = 6.0 # degrees

pixel_width_of_screen = 1920 # pixels
width_of_screen = 143.51 # centimeters

pixel_height_of_screen = 1080 # pixels
distance_from_screen = 177.8 # centimeters (65 in.)
### END EXPERIMENTAL CONSTANTS ###


### CALCULATIONS OF OTHER EXPERIMENTAL CONSTANTS ###
### DO NOT MODIFY UNLESS EXPERIMENT PROTOCOLS CHANGE ###
cm_per_pixel = (143.51 / 1920.0) # units: cm/pixel

height_of_screen = 1080.0 * cm_per_pixel # cm

foveal_radius = 9.32 # should be calculated by hand on a calculator: r = dist * tan(f_r / 2)
max_image_width = 2*foveal_radius # cm

#peripheral_radius = height_of_screen/2.0 - (max_image_width/2.0) # cm
peripheral_radius = 20.0

### END CALCULATIONS OF OTHER EXPERIMENTAL CONSTANTS ###

# Generate foveal coordinates.
def foveal():
    r = 0
    t = uniform(0.0, 360.0)
    
    x = r*cos(t)
    y = r*sin(t)
    
    #x_pix = (1920.0/2)+(x/cm_per_pixel)
    #y_pix = (1080.0/2)-(y/cm_per_pixel)
    
    return [x, y]
    
# Generate peripheral coordinates.
def peripheral():
    r = peripheral_radius
    t = uniform(0.0, 360.0)
    
    x = r*cos(t)
    y = r*sin(t)
    
    #x_pix = (1920.0/2)+(x/cm_zper_pixel)
    #y_pix = (1080.0/2)-(y/cm_per_pixel)
    
    return [x, y]

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__)).decode(sys.getfilesystemencoding())
os.chdir(_thisDir)

# Store info about the experiment session
expName = 'Peripheral and Foveal Attention, Part 1'  # from the Builder filename that created this script
expInfo = {u'session': u'001', u'participant': u''}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False: core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etco
subject_folder_name = 'data/%s_%s/' %(expInfo['participant'], expInfo['date'])
os.makedirs(_thisDir + os.sep + subject_folder_name)
filename = _thisDir + os.sep + subject_folder_name + '%s_%s_%s' %(expInfo['participant'], expName, expInfo['date'])


trialLogFile = open(filename + '_trialLog.csv', 'w')
headers = 'trial,trialStartTime,image,emotion,locationPF,locationCoord,key_presses,key_presses_response_times,accuracy\n'
trialLogFile.write(headers)

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath=None,
    savePickle=True, saveWideText=True,
    dataFileName=filename)
#save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(size=(1920, 1080), fullscr=False, screen=0, allowGUI=True, allowStencil=False,
    monitor='SONY TV', color=[-1.000,-1.000,-1.000], colorSpace='rgb',
    blendMode='avg', useFBO=True,
    )
# store frame rate of monitor if we can measure it successfully
expInfo['frameRate']=win.getActualFrameRate()
if expInfo['frameRate']!=None:
    frameDur = 1.0/round(expInfo['frameRate'])
else:
    frameDur = 1.0/60.0 # couldn't get a reliable measure so guess

# Initialize components for Routine "Instructions"
InstructionsClock = core.Clock()
instr = visual.TextStim(win=win, ori=0, name='instr',
    text='Please state when you are ready to begin.',    font='Arial',
    pos=[0, 0], height=0.15, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "trial"
trialClock = core.Clock()
ISI = core.StaticPeriod(win=win, screenHz=expInfo['frameRate'], name='ISI')

### Set up the image stimulus. ###
face = visual.ImageStim(win=win, name='face',units='cm', 
    image='sin', mask=None,
    ori=0, pos=[0,0], size=[max_image_width, max_image_width],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)

### Set up the fixation mark. ###
text = visual.TextStim(win=win, ori=0, name='text',
    text='+',    font='Arial',
    pos=[0, 0], height=0.15, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-3.0)

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

#------Prepare to start Routine "Instructions"-------
t = 0
InstructionsClock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
key_resp_2 = event.BuilderKeyResponse()  # create an object of type KeyResponse
key_resp_2.status = NOT_STARTED
# keep track of which components have finished
InstructionsComponents = []
InstructionsComponents.append(instr)
InstructionsComponents.append(key_resp_2)
for thisComponent in InstructionsComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "Instructions"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = InstructionsClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instr* updates
    if t >= 0.0 and instr.status == NOT_STARTED:
        # keep track of start time/frame for later
        instr.tStart = t  # underestimates by a little under one frame
        instr.frameNStart = frameN  # exact frame index
        instr.setAutoDraw(True)
    
    # *key_resp_2* updates
    if t >= 0.0 and key_resp_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_2.tStart = t  # underestimates by a little under one frame
        key_resp_2.frameNStart = frameN  # exact frame index
        key_resp_2.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if key_resp_2.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in InstructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "Instructions"-------
for thisComponent in InstructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "Instructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=30, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('conditions.xlsx'),
    seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb=thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial.keys():
        exec(paramName + '= thisTrial.' + paramName)

nTrial = 0
correctResponses = 0
for thisTrial in trials:
    nTrial += 1
    print "Starting trial #" + str(nTrial)
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial.keys():
            exec(paramName + '= thisTrial.' + paramName)
    
    #------Prepare to start Routine "trial"-------
    t = 0
    trialClock.reset()  # clock 
    frameN = -1

    # Add the total trial duration to the routine timer.
    # The trial will end if the timer runs out of time.
    routineTimer.add(total_trial_duration)
    
    # update component parameters for each repeat
    imageLocation = location
    if location == 'fovea':
        # generate location in fovea.
        location = foveal()
    else:
        # generate location in periphery.
        location = peripheral()
        
    # randomly select image from dir.
    neutralDir = 'images\\neutral\\'
    angryDir = 'images\\angry\\'
    
    imageEmotion = image
    if image == 'neutral':
        images = os.listdir(neutralDir)
        image = neutralDir + images[randint(0, len(images))]
    else:
        images = os.listdir(angryDir)
        image = angryDir + images[randint(0, len(images))]
    
    face.setPos(location)
    face.setImage(image)
    key_resp_3 = event.BuilderKeyResponse()  # create an object of type KeyResponse
    key_resp_3.status = NOT_STARTED
    # keep track of which components have finished
    trialComponents = []
    trialComponents.append(ISI)
    trialComponents.append(face)
    trialComponents.append(key_resp_3)
    trialComponents.append(text)
    for thisComponent in trialComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "trial"-------
    # Set the trial start time in local 24HR system time
    trialStartTime = datetime.now().time()
    continueRoutine = True
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = trialClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # Updates face stimuli.
        if t >= fixation_mark_duration and face.status == NOT_STARTED:
            # keep track of start time/frame for later
            face.tStart = t  # underestimates by a little under one frame
            face.frameNStart = frameN  # exact frame index
            face.setAutoDraw(True)
        if face.status == STARTED and t >= (fixation_mark_duration + (stim_duration-win.monitorFramePeriod*0.75)): #most of one frame period left
            face.setAutoDraw(False)                                                    
        
        # Record keyboard responses as soon as the face disappears.
        if t >= (fixation_mark_duration + stim_duration) and key_resp_3.status == NOT_STARTED:
            # keep track of start time/frame for later
            key_resp_3.tStart = t  # underestimates by a little under one frame
            key_resp_3.frameNStart = frameN  # exact frame index
            key_resp_3.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(key_resp_3.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')
        if key_resp_3.status == STARTED and t >= (fixation_mark_duration + (time_to_respond-win.monitorFramePeriod*0.75)): #most of one frame period left
            key_resp_3.status = STOPPED
        if key_resp_3.status == STARTED:
            theseKeys = event.getKeys(keyList=['z', 'c'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                for key in theseKeys:
                    key_resp_3.keys.append(key)
                key_resp_3.rt.append(key_resp_3.clock.getTime())
                
                # was this 'correct'?
                if (key_resp_3.keys == str(correctAnswer)) or (key_resp_3.keys == correctAnswer):
                    key_resp_3.corr = 1
                else:
                    key_resp_3.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # *text* updates
        if t >= 0.0 and text.status == NOT_STARTED:
            # keep track of start time/frame for later
            text.tStart = t  # underestimates by a little under one frame
            text.frameNStart = frameN  # exact frame index
            text.setAutoDraw(True)
        if text.status == STARTED and t >= (0.0 + (fixation_mark_duration-win.monitorFramePeriod*0.75)): #most of one frame period left
            text.setAutoDraw(False)
        # *ISI* period
        if t >= 0.0 and ISI.status == NOT_STARTED:
            # keep track of start time/frame for later
            ISI.tStart = t  # underestimates by a little under one frame
            ISI.frameNStart = frameN  # exact frame index
            ISI.start(0.5)
        elif ISI.status == STARTED: #one frame should pass before updating params and completing
            ISI.complete() #finish the static period
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "trial"-------
    for thisComponent in trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if key_resp_3.keys in ['', [], None]:  # No response was made
       key_resp_3.keys=None
       # was no response the correct answer?!
       if str(correctAnswer).lower() == 'none': key_resp_3.corr = 1  # correct non-response
       else: key_resp_3.corr = 0  # failed to respond (incorrectly)
    # store data for trials (TrialHandler)
    trials.addData('key_resp_3.keys',key_resp_3.keys)
    trials.addData('key_resp_3.corr', key_resp_3.corr)
    if key_resp_3.keys != None:  # we had a response
        trials.addData('key_resp_3.rt', key_resp_3.rt)
        
        
    # output accuracy up until this trial
    if key_resp_3.keys != None:
        if imageEmotion == 'neutral' and 'z' in key_resp_3.keys:
            correctResponses +=1
        else:
            if imageEmotion == 'angry' and 'c' in key_resp_3.keys:
                correctResponses += 1
    
    accuracy = correctResponses/nTrial
    print "Accuracy: " + str(accuracy)
    print "\n\n"
    
    
    # record our data
    # headers: 'trial,trialStartTime,image,emotion,locationPF,locationCoord,key_presses,key_presses_response_times,accuracy'

    trialData = str(nTrial) + ',' + str(trialStartTime) + ',' + image + ',' + imageEmotion + ',' + imageLocation + ',' + str(location) + ',' + str(key_resp_3.keys) + ',' + str(key_resp_3.rt) +  ',' + str(accuracy) + '\n'
    trialLogFile.write(trialData)
    
    
    thisExp.nextEntry()
    
# completed 30 repeats of 'trials'

win.close()
core.quit()
