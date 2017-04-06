#!/usr/bin/env python2
# -*- coding: utf-8 -*-
'''
psychopy OSC receiver debugging
wade022216

'''

from __future__ import division  # so that 1/3=0.333 instead of 1/3=0
from psychopy import locale_setup, visual, core, data, event, logging, sound, gui
from psychopy.constants import *  # things like STARTED, FINISHED
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import sin, cos, tan, log, log10, pi, average, sqrt, std, deg2rad, rad2deg, linspace, asarray
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys # to get file system encoding

#####
##OSC
from OSC import OSCServer, ThreadingOSCServer, ForkingOSCServer, OSCClient, OSCMessage, OSCBundle
import time, threading

#setup()
win = visual.Window(size=(128, 128), fullscr=False, screen=0, allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True,
    )

##globals
fixation = 0
timestamp = 0

#####
##OSC
server = OSCServer( ("127.0.0.1", 12345) )
server.addDefaultHandlers()
server.timeout = 0

#####
##OSC
def eyetech_handler(addr, tags, stuff, source): 
    print "---"
    ##print "received new osc msg from %s" % getUrlStr(source)
    print "with addr : %s" % addr
    print "typetags %s" % tags
    print "data %s" % stuff
    print "---"
    
    global fixation
    global timestamp
    fixation = stuff[0]
    timestamp = stuff[1]
    
    ##debug
    #print "%s\n" % str(fixation)
    #print "%s\n" % str(timestamp)
   

#####
##OSC
server.addMsgHandler("/eyetech", eyetech_handler)

#####
##OSC
# List registered callback handlers
print "Registered Callback-functions are :"
for addr in server.getOSCAddressSpace():
    print addr

#####
##OSC
# Start OSCServer
print "\nStarting threaded OSCServer. Use ESC to join and close\n"
st = threading.Thread( target = server.serve_forever )
st.start()


#main()
continueRoutine = True
while continueRoutine:

    #draw something to the window
    
    # set fixation back to zero
    #loop >> check fixation
        # if fixation do something
       
    
    
    win.flip()
    
    while 1:
        if fixation:
            print "RECEIVED"
            fixation = 0
            
    
    
    # check for quit (the Esc key)
    if event.getKeys(keyList=["escape"]):
        #####
        ##OSC
        print "\nClosing OSCServer."
        server.close()
        print "Waiting for Server-thread to finish"
        st.join()
        
        core.quit()
    
    # refresh the screen
    if continueRoutine: 
        win.flip()

#exit()
thisExp.saveAsPickle(filename)
logging.flush()

win.close()
core.quit()
