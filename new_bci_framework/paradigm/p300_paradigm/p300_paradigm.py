from __future__ import absolute_import, division

import multiprocessing.managers
from queue import Empty

from ..paradigm import Paradigm
from ...config.config import Config
from ...recorder.recorder import Recorder
import os
from new_bci_framework.paradigm.p300_paradigm.create_pseudoRand import create_pseudo_rand


class RecorderManager(multiprocessing.managers.BaseManager):
    pass

FILE_DIR =os.path.dirname(os.path.abspath(__file__))
RESCOURCES_DIR = os.path.join(FILE_DIR, "res")
# os.chdir(FILE_PATH)


class P300Paradigm(Paradigm):
    """
    Paradigm subclass for the p300 paradigm.
    """

    LABEL_TARGET = "Target"
    LABEL_DISTRACTOR = "Distractor"

    def __init__(self, config: Config):
        super(P300Paradigm, self).__init__(config)
        self.stim_labels = {self.LABEL_TARGET: 100, self.LABEL_DISTRACTOR: 200}
        for k, v in self.stim_labels.items():
            config.TRIAL_LABELS[v] = k

        self.questions_file = 'questions_everyone.xlsx'

    def run_expreriment_with_queue(self, q: multiprocessing.Queue):
        recorder = q[-1]
        self.psychopy_exp(recorder)



    def start(self, recorder: Recorder):
        # RecorderManager.register('Recorder', lambda: recorder)
        # with multiprocessing.Manager() as m:
        #     l = m.list()
        #     l.append(recorder)
            # q.put(recorder)
        q = multiprocessing.Queue()
        proc = multiprocessing.Process(target=self.psychopy_exp, args=(q,))
        proc.start()
        while proc.is_alive():
            try:
                marker = q.get(timeout=0.5)
                recorder.push_marker(marker)
            except Empty:
                continue
            except OSError:
                break
            except ValueError:
                break
        if proc.is_alive():
            proc.join()
        # self.psychopy_exp(recorder)
        # start a trial
        # recorder.push_marker("this trial's marker")

    def psychopy_exp(self, q: multiprocessing.Queue):
        """
        This experiment was created using PsychoPy3 Experiment Builder (v2021.2.3),
            on April 04, 2022, at 19:43
        If you publish work using this script the most relevant publication is:

            Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019)
                PsychoPy2: Experiments in behavior made easy Behav Res 51: 195.
                https://doi.org/10.3758/s13428-018-01193-y

        """

        from psychopy import sound, gui, visual, core, data, logging
        from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                        STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

        import os  # handy system and path functions

        from psychopy.hardware import keyboard

        # Store info about the experiment session
        psychopyVersion = '2021.2.3'
        expName = 'TRY_rec'  # from the Builder filename that created this script
        expInfo = {'participant': '', 'session': '001'}
        dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
        if dlg.OK == False:
            # win.close() #core.quit()()  # user pressed cancel
            return
        expInfo['date'] = data.getDateStr()  # add a simple timestamp
        expInfo['expName'] = expName
        expInfo['psychopyVersion'] = psychopyVersion

        # Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
        filename = FILE_DIR + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

        # An ExperimentHandler isn't essential but helps with data saving
        thisExp = data.ExperimentHandler(name=expName, version='',
                                         extraInfo=expInfo, runtimeInfo=None,
                                         originPath='TRY_rec.py',
                                         savePickle=True, saveWideText=True,
                                         dataFileName=filename)
        # save a log file for detail verbose info
        logFile = logging.LogFile(filename + '.log', level=logging.EXP)
        logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

        endExpNow = False  # flag for 'escape' or other condition => quit the exp
        frameTolerance = 0.001  # how close to onset before 'same' frame

        # Start Code - component code to be run after the window creation

        # Setup the Window
        win = visual.Window(
            size=[1920, 1080], fullscr=True, screen=0,
            winType='pyglet', allowGUI=False, allowStencil=False,
            monitor='testMonitor', color=[0, 0, 0], colorSpace='rgb',
            blendMode='avg', useFBO=True)
        # store frame rate of monitor if we can measure it
        expInfo['frameRate'] = win.getActualFrameRate()
        if expInfo['frameRate'] != None:
            frameDur = 1.0 / round(expInfo['frameRate'])
        else:
            frameDur = 1.0 / 60.0  # could not measure, so guess

        # Setup eyetracking
        ioDevice = ioConfig = ioSession = ioServer = eyetracker = None

        # create a default keyboard (e.g. to check for escape)
        defaultKeyboard = keyboard.Keyboard()

        # Initialize components for Routine "start_closed_eyes"
        start_closed_eyesClock = core.Clock()
        image_2 = visual.ImageStim(
            win=win,
            name='image_2',
            image=os.path.join(RESCOURCES_DIR, 'start_closed_eyes.png'), mask=None,
            ori=0.0, pos=(0, 0), size=(2, 2),
            color=[1,1,1], colorSpace='rgb', opacity=None,
            flipHoriz=False, flipVert=False,
            texRes=128.0, interpolate=True, depth=0.0)
        key_resp_2 = keyboard.Keyboard()

        # Initialize components for Routine "grey_screen"
        grey_screenClock = core.Clock()
        text = visual.TextStim(win=win, name='text',
                               text=None,
                               font='Open Sans',
                               pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0,
                               color='white', colorSpace='rgb', opacity=None,
                               languageStyle='RTL',
                               depth=0.0)
        key_resp = keyboard.Keyboard()

        # Initialize components for Routine "beep"
        beepClock = core.Clock()
        sound_1 = sound.Sound(os.path.join(RESCOURCES_DIR, 'Beep.wav'), secs=1.0, stereo=True, hamming=True,
                              name='sound_1')
        sound_1.setVolume(1.0)

        # Initialize components for Routine "Instructions"
        InstructionsClock = core.Clock()
        image = visual.ImageStim(
            win=win,
            name='image',
            image=os.path.join(RESCOURCES_DIR, 'Instructions_image.PNG'), mask=None,
            ori=0.0, pos=(0, 0), size=(2, 2),
            color=[1,1,1], colorSpace='rgb', opacity=None,
            flipHoriz=False, flipVert=False,
            texRes=128.0, interpolate=True, depth=0.0)
        key_resp_3 = keyboard.Keyboard()

        # Initialize components for Routine "question"
        questionClock = core.Clock()
        target_quest = visual.TextStim(win=win, name='target_quest',
                                       text='',
                                       font='Open Sans',
                                       pos=(0, 0), height=0.15, wrapWidth=None, ori=0.0,
                                       color='black', colorSpace='rgb', opacity=None,
                                       languageStyle='RTL',
                                       depth=0.0)

        # Initialize components for Routine "cross"
        crossClock = core.Clock()
        polygon = visual.ShapeStim(
            win=win, name='polygon', vertices='cross',
            size=(0.25, 0.25),
            ori=0.0, pos=(0, 0),
            lineWidth=1.0, colorSpace='rgb', lineColor=[1,1,1], fillColor=[1,1,1],
            opacity=None, depth=0.0, interpolate=True)

        # Initialize components for Routine "trial"
        trialClock = core.Clock()
        target_word = visual.TextStim(win=win, name='target_word',
                                      text='',
                                      font='Open Sans',
                                      pos=(0, 0), height=0.2, wrapWidth=None, ori=0.0,
                                      color='black', colorSpace='rgb', opacity=None,
                                      languageStyle='RTL',
                                      depth=0.0)
        target_sound = sound.Sound('A', secs=1, stereo=True, hamming=True,
                                   name='target_sound')
        target_sound.setVolume(1.0)

        # Initialize components for Routine "finished"
        questionCounter = 0
        totalQuestions = 0
        finishedClock = core.Clock()
        how_much = visual.TextStim(win=win, name='how_much',
                                   text=f'{questionCounter}/{totalQuestions}',
                                   font='Open Sans',
                                   pos=(0, 0), height=0.15, wrapWidth=None, ori=0.0,
                                   color='white', colorSpace='rgb', opacity=None,
                                   languageStyle='RTL',
                                   depth=0.0)

        # Create some handy timers
        globalClock = core.Clock()  # to track the time since experiment started
        routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine

        # ------Prepare to start Routine "start_closed_eyes"-------
        continueRoutine = True
        # update component parameters for each repeat
        key_resp_2.keys = []
        key_resp_2.rt = []
        _key_resp_2_allKeys = []
        # keep track of which components have finished
        start_closed_eyesComponents = [image_2, key_resp_2]
        for thisComponent in start_closed_eyesComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        start_closed_eyesClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1

        # -------Run Routine "start_closed_eyes"-------
        while continueRoutine:
            # get current time
            t = start_closed_eyesClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=start_closed_eyesClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame

            # *image_2* updates
            if image_2.status == NOT_STARTED and tThisFlip >= 0 - frameTolerance:
                # keep track of start time/frame for later
                image_2.frameNStart = frameN  # exact frame index
                image_2.tStart = t  # local t and not account for scr refresh
                image_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image_2, 'tStartRefresh')  # time at next scr refresh
                image_2.setAutoDraw(True)
            if image_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > image_2.tStartRefresh + 4 - frameTolerance:
                    # keep track of stop time/frame for later
                    image_2.tStop = t  # not accounting for scr refresh
                    image_2.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(image_2, 'tStopRefresh')  # time at next scr refresh
                    image_2.setAutoDraw(False)

            # *key_resp_2* updates
            waitOnFlip = False
            if key_resp_2.status == NOT_STARTED and tThisFlip >= 0.0 - frameTolerance:
                # keep track of start time/frame for later
                key_resp_2.frameNStart = frameN  # exact frame index
                key_resp_2.tStart = t  # local t and not account for scr refresh
                key_resp_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_2, 'tStartRefresh')  # time at next scr refresh
                key_resp_2.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_2.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp_2.clearEvents,
                               eventType='keyboard')  # clear events on next screen flip
            if key_resp_2.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_2.getKeys(keyList=['y', 'n', 'left', 'right', 'space'],
                                               waitRelease=False)
                _key_resp_2_allKeys.extend(theseKeys)
                if len(_key_resp_2_allKeys):
                    key_resp_2.keys = _key_resp_2_allKeys[-1].name  # just the last key pressed
                    key_resp_2.rt = _key_resp_2_allKeys[-1].rt
                    # a response ends the routine
                    continueRoutine = False

            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                win.close() #core.quit()()
                return

            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in start_closed_eyesComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished

            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()

        # -------Ending Routine "start_closed_eyes"-------
        for thisComponent in start_closed_eyesComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('image_2.started', image_2.tStartRefresh)
        thisExp.addData('image_2.stopped', image_2.tStopRefresh)
        # check responses
        if key_resp_2.keys in ['', [], None]:  # No response was made
            key_resp_2.keys = None
        thisExp.addData('key_resp_2.keys', key_resp_2.keys)
        if key_resp_2.keys != None:  # we had a response
            thisExp.addData('key_resp_2.rt', key_resp_2.rt)
        thisExp.addData('key_resp_2.started', key_resp_2.tStartRefresh)
        thisExp.addData('key_resp_2.stopped', key_resp_2.tStopRefresh)
        thisExp.nextEntry()
        # the Routine "start_closed_eyes" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()

        # ------Prepare to start Routine "grey_screen"-------
        continueRoutine = True
        # update component parameters for each repeat
        key_resp.keys = []
        key_resp.rt = []
        _key_resp_allKeys = []
        # keep track of which components have finished
        grey_screenComponents = [text, key_resp]
        for thisComponent in grey_screenComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        grey_screenClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1

        # -------Run Routine "grey_screen"-------
        while continueRoutine:
            # get current time
            t = grey_screenClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=grey_screenClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame

            # *text* updates
            if text.status == NOT_STARTED and tThisFlip >= 0.0 - frameTolerance:
                # keep track of start time/frame for later
                text.frameNStart = frameN  # exact frame index
                text.tStart = t  # local t and not account for scr refresh
                text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
                text.setAutoDraw(True)
            if text.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > text.tStartRefresh + 240 - frameTolerance:
                    # keep track of stop time/frame for later
                    text.tStop = t  # not accounting for scr refresh
                    text.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(text, 'tStopRefresh')  # time at next scr refresh
                    text.setAutoDraw(False)

            # *key_resp* updates
            waitOnFlip = False
            if key_resp.status == NOT_STARTED and tThisFlip >= 0.0 - frameTolerance:
                # keep track of start time/frame for later
                key_resp.frameNStart = frameN  # exact frame index
                key_resp.tStart = t  # local t and not account for scr refresh
                key_resp.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
                key_resp.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp.clearEvents,
                               eventType='keyboard')  # clear events on next screen flip
            if key_resp.status == STARTED and not waitOnFlip:
                theseKeys = key_resp.getKeys(keyList=['y', 'n', 'left', 'right', 'space'], waitRelease=False)
                _key_resp_allKeys.extend(theseKeys)
                if len(_key_resp_allKeys):
                    key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
                    key_resp.rt = _key_resp_allKeys[-1].rt
                    # a response ends the routine
                    continueRoutine = False

            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                win.close() #core.quit()()
                return

            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in grey_screenComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished

            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()

        # -------Ending Routine "grey_screen"-------
        for thisComponent in grey_screenComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('text.started', text.tStartRefresh)
        thisExp.addData('text.stopped', text.tStopRefresh)
        # check responses
        if key_resp.keys in ['', [], None]:  # No response was made
            key_resp.keys = None
        thisExp.addData('key_resp.keys', key_resp.keys)
        if key_resp.keys != None:  # we had a response
            thisExp.addData('key_resp.rt', key_resp.rt)
        thisExp.addData('key_resp.started', key_resp.tStartRefresh)
        thisExp.addData('key_resp.stopped', key_resp.tStopRefresh)
        thisExp.nextEntry()
        # the Routine "grey_screen" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()

        # ------Prepare to start Routine "beep"-------
        continueRoutine = True
        routineTimer.add(1.000000)
        # update component parameters for each repeat
        sound_1.setSound(os.path.join(RESCOURCES_DIR, 'Beep.wav'), secs=1.0, hamming=True)
        sound_1.setVolume(1.0, log=False)
        # keep track of which components have finished
        beepComponents = [sound_1]
        for thisComponent in beepComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        beepClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1

        # -------Run Routine "beep"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = beepClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=beepClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            # start/stop sound_1
            if sound_1.status == NOT_STARTED and tThisFlip >= 0.0 - frameTolerance:
                # keep track of start time/frame for later
                sound_1.frameNStart = frameN  # exact frame index
                sound_1.tStart = t  # local t and not account for scr refresh
                sound_1.tStartRefresh = tThisFlipGlobal  # on global time
                sound_1.play(when=win)  # sync with win flip
            if sound_1.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound_1.tStartRefresh + 1.0 - frameTolerance:
                    # keep track of stop time/frame for later
                    sound_1.tStop = t  # not accounting for scr refresh
                    sound_1.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(sound_1, 'tStopRefresh')  # time at next scr refresh
                    sound_1.stop()

            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                win.close() #core.quit()()
                return

            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in beepComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished

            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()

        # -------Ending Routine "beep"-------
        for thisComponent in beepComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        sound_1.stop()  # ensure sound has stopped at end of routine
        thisExp.addData('sound_1.started', sound_1.tStartRefresh)
        thisExp.addData('sound_1.stopped', sound_1.tStopRefresh)

        # ------Prepare to start Routine "Instructions"-------
        continueRoutine = True
        # update component parameters for each repeat
        key_resp_3.keys = []
        key_resp_3.rt = []
        _key_resp_3_allKeys = []
        # keep track of which components have finished
        InstructionsComponents = [image, key_resp_3]
        for thisComponent in InstructionsComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        InstructionsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1

        # -------Run Routine "Instructions"-------
        while continueRoutine:
            # get current time
            t = InstructionsClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=InstructionsClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame

            # *image* updates
            if image.status == NOT_STARTED and tThisFlip >= 0 - frameTolerance:
                # keep track of start time/frame for later
                image.frameNStart = frameN  # exact frame index
                image.tStart = t  # local t and not account for scr refresh
                image.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image, 'tStartRefresh')  # time at next scr refresh
                image.setAutoDraw(True)
            if image.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > image.tStartRefresh + 10 - frameTolerance:
                    # keep track of stop time/frame for later
                    image.tStop = t  # not accounting for scr refresh
                    image.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(image, 'tStopRefresh')  # time at next scr refresh
                    image.setAutoDraw(False)

            # *key_resp_3* updates
            waitOnFlip = False
            if key_resp_3.status == NOT_STARTED and tThisFlip >= 0.0 - frameTolerance:
                # keep track of start time/frame for later
                key_resp_3.frameNStart = frameN  # exact frame index
                key_resp_3.tStart = t  # local t and not account for scr refresh
                key_resp_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_3, 'tStartRefresh')  # time at next scr refresh
                key_resp_3.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_3.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp_3.clearEvents,
                               eventType='keyboard')  # clear events on next screen flip
            if key_resp_3.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_3.getKeys(keyList=['y', 'n', 'left', 'right', 'space'],
                                               waitRelease=False)
                _key_resp_3_allKeys.extend(theseKeys)
                if len(_key_resp_3_allKeys):
                    key_resp_3.keys = _key_resp_3_allKeys[-1].name  # just the last key pressed
                    key_resp_3.rt = _key_resp_3_allKeys[-1].rt
                    # a response ends the routine
                    continueRoutine = False

            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                win.close() #core.quit()()
                return

            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in InstructionsComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished

            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()

        # -------Ending Routine "Instructions"-------
        for thisComponent in InstructionsComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('image.started', image.tStartRefresh)
        thisExp.addData('image.stopped', image.tStopRefresh)
        # check responses
        if key_resp_3.keys in ['', [], None]:  # No response was made
            key_resp_3.keys = None
        thisExp.addData('key_resp_3.keys', key_resp_3.keys)
        if key_resp_3.keys != None:  # we had a response
            thisExp.addData('key_resp_3.rt', key_resp_3.rt)
        thisExp.addData('key_resp_3.started', key_resp_3.tStartRefresh)
        thisExp.addData('key_resp_3.stopped', key_resp_3.tStopRefresh)
        thisExp.nextEntry()
        # the Routine "Instructions" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()

        # set up handler to look after randomisation of conditions etc
        questions = data.TrialHandler(nReps=1.0, method='fullRandom',
                                      extraInfo=expInfo, originPath=-1,
                                      trialList=data.importConditions(os.path.join(RESCOURCES_DIR, self.questions_file)),
                                      seed=None, name='questions')
        totalQuestions = len(questions.trialList)
        thisExp.addLoop(questions)  # add the loop to the experiment
        thisQuestion = questions.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisQuestion.rgb)
        if thisQuestion != None:
            for paramName in thisQuestion:
                self.__setattr__(paramName, thisQuestion[paramName])
                # exec('{} = thisQuestion[paramName]'.format(paramName), __locals=locals())

        for thisQuestion in questions:
            currentLoop = questions
            # abbreviate parameter names if possible (e.g. rgb = thisQuestion.rgb)
            if thisQuestion != None:
                for paramName in thisQuestion:
                    self.__setattr__(paramName, thisQuestion[paramName])
                    # exec('{} = thisQuestion[paramName]'.format(paramName), __locals=locals())

            # ------Prepare to start Routine "question"-------
            continueRoutine = True
            routineTimer.add(2.000000)
            # update component parameters for each repeat
            target_quest.setText(self.Question_stim)
            # keep track of which components have finished
            questionComponents = [target_quest]
            for thisComponent in questionComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            questionClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
            frameN = -1

            # -------Run Routine "question"-------
            while continueRoutine and routineTimer.getTime() > 0:
                # get current time
                t = questionClock.getTime()
                tThisFlip = win.getFutureFlipTime(clock=questionClock)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame

                # *target_quest* updates
                if target_quest.status == NOT_STARTED and tThisFlip >= 0.0 - frameTolerance:
                    # keep track of start time/frame for later
                    target_quest.frameNStart = frameN  # exact frame index
                    target_quest.tStart = t  # local t and not account for scr refresh
                    target_quest.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(target_quest, 'tStartRefresh')  # time at next scr refresh
                    target_quest.setAutoDraw(True)
                if target_quest.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > target_quest.tStartRefresh + 2 - frameTolerance:
                        # keep track of stop time/frame for later
                        target_quest.tStop = t  # not accounting for scr refresh
                        target_quest.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(target_quest, 'tStopRefresh')  # time at next scr refresh
                        target_quest.setAutoDraw(False)

                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    win.close() #core.quit()()
                    return

                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in questionComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished

                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()

            # -------Ending Routine "question"-------
            for thisComponent in questionComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            questions.addData('target_quest.started', target_quest.tStartRefresh)
            questions.addData('target_quest.stopped', target_quest.tStopRefresh)

            # set up handler to look after randomisation of conditions etc
            trials = data.TrialHandler(nReps=1.0, method='sequential',
                                       extraInfo=expInfo, originPath=-1,
                                       trialList=create_pseudo_rand(
                                           data.importConditions(os.path.join(RESCOURCES_DIR, 'only_stim_words.xlsx')), self._config.MIN_TARGET_APPEARANCES),
                                       seed=None, name='trials')
            thisExp.addLoop(trials)  # add the loop to the experiment
            thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
            # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
            if thisTrial != None:
                for paramName in thisTrial:
                    self.__setattr__(paramName, thisTrial[paramName])
                    # exec('{} = thisTrial[paramName]'.format(paramName), __locals=locals())

            for thisTrial in trials:
                currentLoop = trials
                # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
                if thisTrial != None:
                    for paramName in thisTrial:
                        self.__setattr__(paramName, thisTrial[paramName])
                        # exec('{} = thisTrial[paramName]'.format(paramName), __locals=locals())

                # ------Prepare to start Routine "cross"-------
                continueRoutine = True
                routineTimer.add(0.700000)
                # update component parameters for each repeat
                # keep track of which components have finished
                crossComponents = [polygon]
                for thisComponent in crossComponents:
                    thisComponent.tStart = None
                    thisComponent.tStop = None
                    thisComponent.tStartRefresh = None
                    thisComponent.tStopRefresh = None
                    if hasattr(thisComponent, 'status'):
                        thisComponent.status = NOT_STARTED
                # reset timers
                t = 0
                _timeToFirstFrame = win.getFutureFlipTime(clock="now")
                crossClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
                frameN = -1

                # -------Run Routine "cross"-------
                while continueRoutine and routineTimer.getTime() > 0:
                    # get current time
                    t = crossClock.getTime()
                    tThisFlip = win.getFutureFlipTime(clock=crossClock)
                    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                    # update/draw components on each frame

                    # *polygon* updates
                    if polygon.status == NOT_STARTED and tThisFlip >= 0 - frameTolerance:
                        # keep track of start time/frame for later
                        polygon.frameNStart = frameN  # exact frame index
                        polygon.tStart = t  # local t and not account for scr refresh
                        polygon.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(polygon, 'tStartRefresh')  # time at next scr refresh
                        polygon.setAutoDraw(True)
                    if polygon.status == STARTED:
                        # is it time to stop? (based on global clock, using actual start)
                        if tThisFlipGlobal > polygon.tStartRefresh + 0.7 - frameTolerance:
                            # keep track of stop time/frame for later
                            polygon.tStop = t  # not accounting for scr refresh
                            polygon.frameNStop = frameN  # exact frame index
                            win.timeOnFlip(polygon, 'tStopRefresh')  # time at next scr refresh
                            polygon.setAutoDraw(False)

                    # check for quit (typically the Esc key)
                    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                        win.close() #core.quit()()
                        return

                    # check if all components have finished
                    if not continueRoutine:  # a component has requested a forced-end of Routine
                        break
                    continueRoutine = False  # will revert to True if at least one component still running
                    for thisComponent in crossComponents:
                        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                            continueRoutine = True
                            break  # at least one component has not yet finished


                    # refresh the screen
                    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                        win.flip()

                # -------Ending Routine "cross"-------
                for thisComponent in crossComponents:
                    if hasattr(thisComponent, "setAutoDraw"):
                        thisComponent.setAutoDraw(False)
                trials.addData('polygon.started', polygon.tStartRefresh)
                trials.addData('polygon.stopped', polygon.tStopRefresh)

                # ------Prepare to start Routine "trial"-------
                continueRoutine = True
                routineTimer.add(1.000000)
                # update component parameters for each repeat
                target_word.setText(self.word)
                target_sound.setSound(os.path.join(RESCOURCES_DIR, self.sound_target), secs=1, hamming=True)
                target_sound.setVolume(1.0, log=False)
                # keep track of which components have finished
                trialComponents = [target_word, target_sound]
                for thisComponent in trialComponents:
                    thisComponent.tStart = None
                    thisComponent.tStop = None
                    thisComponent.tStartRefresh = None
                    thisComponent.tStopRefresh = None
                    if hasattr(thisComponent, 'status'):
                        thisComponent.status = NOT_STARTED
                # reset timers
                t = 0
                _timeToFirstFrame = win.getFutureFlipTime(clock="now")
                trialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
                frameN = -1

                # -------Run Routine "trial"-------
                while continueRoutine and routineTimer.getTime() > 0:
                    # get current time
                    t = trialClock.getTime()
                    tThisFlip = win.getFutureFlipTime(clock=trialClock)
                    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                    # update/draw components on each frame

                    target = thisQuestion['answer']
                    marker = 0


                    # *target_word* updates
                    if target_word.status == NOT_STARTED and tThisFlip >= 0.0 - frameTolerance:
                        # keep track of start time/frame for later
                        target_word.frameNStart = frameN  # exact frame index
                        target_word.tStart = t  # local t and not account for scr refresh
                        target_word.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(target_word, 'tStartRefresh')  # time at next scr refresh
                        target_word.setAutoDraw(True)
                    if target_word.status == STARTED:
                        # is it time to stop? (based on global clock, using actual start)
                        if tThisFlipGlobal > target_word.tStartRefresh + 1 - frameTolerance:
                            # keep track of stop time/frame for later
                            target_word.tStop = t  # not accounting for scr refresh
                            target_word.frameNStop = frameN  # exact frame index
                            win.timeOnFlip(target_word, 'tStopRefresh')  # time at next scr refresh
                            target_word.setAutoDraw(False)
                    # start/stop target_sound
                    if target_sound.status == NOT_STARTED and tThisFlip >= 0.0 - frameTolerance:
                        # keep track of start time/frame for later
                        target_sound.frameNStart = frameN  # exact frame index
                        target_sound.tStart = t  # local t and not account for scr refresh
                        target_sound.tStartRefresh = tThisFlipGlobal  # on global time
                        target_sound.play(when=win)  # sync with win flip

                        marker = self.stim_labels[self.LABEL_TARGET] if target == thisTrial['stim'] else \
                            self.stim_labels[self.LABEL_DISTRACTOR]
                    if target_sound.status == STARTED:
                        # is it time to stop? (based on global clock, using actual start)
                        if tThisFlipGlobal > target_sound.tStartRefresh + 1 - frameTolerance:
                            # keep track of stop time/frame for later
                            target_sound.tStop = t  # not accounting for scr refresh
                            target_sound.frameNStop = frameN  # exact frame index
                            win.timeOnFlip(target_sound, 'tStopRefresh')  # time at next scr refresh
                            target_sound.stop()

                    # check for quit (typically the Esc key)
                    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                        win.close() #core.quit()()
                        return

                    # check if all components have finished
                    if not continueRoutine:  # a component has requested a forced-end of Routine
                        break
                    continueRoutine = False  # will revert to True if at least one component still running
                    for thisComponent in trialComponents:
                        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                            continueRoutine = True
                            break  # at least one component has not yet finished

                    # refresh the screen
                    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                        q.put(marker)
                        win.flip()

                # -------Ending Routine "trial"-------
                for thisComponent in trialComponents:
                    if hasattr(thisComponent, "setAutoDraw"):
                        thisComponent.setAutoDraw(False)
                trials.addData('target_word.started', target_word.tStartRefresh)
                trials.addData('target_word.stopped', target_word.tStopRefresh)
                target_sound.stop()  # ensure sound has stopped at end of routine
                trials.addData('target_sound.started', target_sound.tStartRefresh)
                trials.addData('target_sound.stopped', target_sound.tStopRefresh)
                thisExp.nextEntry()

            # completed 1.0 repeats of 'trials'

            # ------Prepare to start Routine "finished"-------
            continueRoutine = True
            routineTimer.add(1.500000)
            # update component parameters for each repeat
            # keep track of which components have finished
            finishedComponents = [how_much]
            for thisComponent in finishedComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            finishedClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
            frameN = -1

            # -------Run Routine "finished"-------
            questionCounter += 1
            how_much.setText(f"{questionCounter}/{totalQuestions}")
            while continueRoutine and routineTimer.getTime() > 0:
                # get current time
                t = finishedClock.getTime()
                tThisFlip = win.getFutureFlipTime(clock=finishedClock)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame

                # *how_much* updates
                if how_much.status == NOT_STARTED and tThisFlip >= 0.0 - frameTolerance:
                    # keep track of start time/frame for later
                    how_much.frameNStart = frameN  # exact frame index
                    how_much.tStart = t  # local t and not account for scr refresh
                    how_much.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(how_much, 'tStartRefresh')  # time at next scr refresh
                    how_much.setAutoDraw(True)
                if how_much.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > how_much.tStartRefresh + 1.5 - frameTolerance:
                        # keep track of stop time/frame for later
                        how_much.tStop = t  # not accounting for scr refresh
                        how_much.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(how_much, 'tStopRefresh')  # time at next scr refresh
                        how_much.setAutoDraw(False)

                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    win.close() #core.quit()()
                    return

                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in finishedComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished

                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()

            # -------Ending Routine "finished"-------
            for thisComponent in finishedComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            questions.addData('how_much.started', how_much.tStartRefresh)
            questions.addData('how_much.stopped', how_much.tStopRefresh)
            thisExp.nextEntry()

        # completed 1.0 repeats of 'questions'

        # Flip one final time so any remaining win.callOnFlip()
        # and win.timeOnFlip() tasks get executed before quitting
        win.flip()

        # these shouldn't be strictly necessary (should auto-save)
        thisExp.saveAsWideText(filename + '.csv', delim='auto')
        thisExp.saveAsPickle(filename)
        logging.flush()
        # make sure everything is closed down
        thisExp.abort()  # or data files will save again on exit
        win.close()
        q.close()
        # win.close() #
        core.quit()
