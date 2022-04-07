/************* 
 * Try1 Test *
 *************/


// store info about the experiment session:
let expName = 'TRY1';  // from the Builder filename that created this script
let expInfo = {'participant': '', 'session': '001'};

// Start code blocks for 'Before Experiment'
// init psychoJS:
const psychoJS = new PsychoJS({
  debug: true
});

// open window:
psychoJS.openWindow({
  fullscr: true,
  color: new util.Color([0,0,0]),
  units: 'height',
  waitBlanking: true
});
// schedule the experiment:
psychoJS.schedule(psychoJS.gui.DlgFromDict({
  dictionary: expInfo,
  title: expName
}));

const flowScheduler = new Scheduler(psychoJS);
const dialogCancelScheduler = new Scheduler(psychoJS);
psychoJS.scheduleCondition(function() { return (psychoJS.gui.dialogComponent.button === 'OK'); }, flowScheduler, dialogCancelScheduler);

// flowScheduler gets run if the participants presses OK
flowScheduler.add(updateInfo); // add timeStamp
flowScheduler.add(experimentInit);
flowScheduler.add(InstructionsRoutineBegin());
flowScheduler.add(InstructionsRoutineEachFrame());
flowScheduler.add(InstructionsRoutineEnd());
const questionsLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(questionsLoopBegin(questionsLoopScheduler));
flowScheduler.add(questionsLoopScheduler);
flowScheduler.add(questionsLoopEnd);
flowScheduler.add(quitPsychoJS, '', true);

// quit if user presses Cancel in dialog box:
dialogCancelScheduler.add(quitPsychoJS, '', false);

psychoJS.start({
  expName: expName,
  expInfo: expInfo,
  resources: [
    {'name': '../../../../../../Desktop/instructions/Slide1.JPG', 'path': '../../../../../../Desktop/instructions/Slide1.JPG'},
    {'name': '../../../questions.xlsx', 'path': '../../../questions.xlsx'},
    {'name': '../../../NOhebYardenSHORT.wav', 'path': '../../../NOhebYardenSHORT.wav'},
    {'name': '../../../stim_words.xlsx', 'path': '../../../stim_words.xlsx'},
    {'name': '../../../PinkNoise.wav', 'path': '../../../PinkNoise.wav'},
    {'name': '../../../YEShebYardenSHORT.wav', 'path': '../../../YEShebYardenSHORT.wav'}
  ]
});

psychoJS.experimentLogger.setLevel(core.Logger.ServerLevel.EXP);


var frameDur;
async function updateInfo() {
  expInfo['date'] = util.MonotonicClock.getDateStr();  // add a simple timestamp
  expInfo['expName'] = expName;
  expInfo['psychopyVersion'] = '2022.1.1';
  expInfo['OS'] = window.navigator.platform;

  psychoJS.experiment.dataFileName = (("." + "/") + `data/${expInfo["participant"]}_${expName}_${expInfo["date"]}`);

  // store frame rate of monitor if we can measure it successfully
  expInfo['frameRate'] = psychoJS.window.getActualFrameRate();
  if (typeof expInfo['frameRate'] !== 'undefined')
    frameDur = 1.0 / Math.round(expInfo['frameRate']);
  else
    frameDur = 1.0 / 60.0; // couldn't get a reliable measure so guess

  // add info from the URL:
  util.addInfoFromUrl(expInfo);
  
  return Scheduler.Event.NEXT;
}


var InstructionsClock;
var image;
var key_resp;
var questionClock;
var target_quest;
var crossClock;
var polygon;
var trialClock;
var target_word;
var target_sound;
var globalClock;
var routineTimer;
async function experimentInit() {
  // Initialize components for Routine "Instructions"
  InstructionsClock = new util.Clock();
  image = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image', units : undefined, 
    image : 'C:/Users/yarde/Desktop/instructions/Slide1.JPG', mask : undefined,
    ori : 0.0, pos : [0, 0], size : [2, 2],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : 0.0 
  });
  key_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "question"
  questionClock = new util.Clock();
  target_quest = new visual.TextStim({
    win: psychoJS.window,
    name: 'target_quest',
    text: '',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('black'),  opacity: undefined,
    depth: 0.0 
  });
  
  // Initialize components for Routine "cross"
  crossClock = new util.Clock();
  polygon = new visual.ShapeStim ({
    win: psychoJS.window, name: 'polygon', 
    vertices: 'cross', size:[0.25, 0.25],
    ori: 0.0, pos: [0, 0],
    lineWidth: 1.0, lineColor: new util.Color([(- 1.0), (- 1.0), (- 1.0)]),
    fillColor: new util.Color([(- 1.0), (- 1.0), (- 1.0)]),
    opacity: undefined, depth: 0, interpolate: true,
  });
  
  // Initialize components for Routine "trial"
  trialClock = new util.Clock();
  target_word = new visual.TextStim({
    win: psychoJS.window,
    name: 'target_word',
    text: '',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.2,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('black'),  opacity: undefined,
    depth: 0.0 
  });
  
  target_sound = new sound.Sound({
    win: psychoJS.window,
    value: 'A',
    secs: 0.7,
    });
  target_sound.setVolume(1.0);
  // Create some handy timers
  globalClock = new util.Clock();  // to track the time since experiment started
  routineTimer = new util.CountdownTimer();  // to track time remaining of each (non-slip) routine
  
  return Scheduler.Event.NEXT;
}


var t;
var frameN;
var continueRoutine;
var _key_resp_allKeys;
var InstructionsComponents;
function InstructionsRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'Instructions'-------
    t = 0;
    InstructionsClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    key_resp.keys = undefined;
    key_resp.rt = undefined;
    _key_resp_allKeys = [];
    // keep track of which components have finished
    InstructionsComponents = [];
    InstructionsComponents.push(image);
    InstructionsComponents.push(key_resp);
    
    InstructionsComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function InstructionsRoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'Instructions'-------
    // get current time
    t = InstructionsClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *image* updates
    if (t >= 0 && image.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      image.tStart = t;  // (not accounting for frame time here)
      image.frameNStart = frameN;  // exact frame index
      
      image.setAutoDraw(true);
    }

    
    // *key_resp* updates
    if (t >= 0.0 && key_resp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp.tStart = t;  // (not accounting for frame time here)
      key_resp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp.clearEvents(); });
    }

    if (key_resp.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp.getKeys({keyList: [], waitRelease: false});
      _key_resp_allKeys = _key_resp_allKeys.concat(theseKeys);
      if (_key_resp_allKeys.length > 0) {
        key_resp.keys = _key_resp_allKeys[_key_resp_allKeys.length - 1].name;  // just the last key pressed
        key_resp.rt = _key_resp_allKeys[_key_resp_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    InstructionsComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function InstructionsRoutineEnd() {
  return async function () {
    //------Ending Routine 'Instructions'-------
    InstructionsComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp.corr, level);
    }
    psychoJS.experiment.addData('key_resp.keys', key_resp.keys);
    if (typeof key_resp.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp.rt', key_resp.rt);
        routineTimer.reset();
        }
    
    key_resp.stop();
    // the Routine "Instructions" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var questions;
var currentLoop;
function questionsLoopBegin(questionsLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    questions = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.FULLRANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: 'C:/Users/yarde/Documents/GitHub/BCI4ALS-MI/questions.xlsx',
      seed: undefined, name: 'questions'
    });
    psychoJS.experiment.addLoop(questions); // add the loop to the experiment
    currentLoop = questions;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    questions.forEach(function() {
      const snapshot = questions.getSnapshot();
    
      questionsLoopScheduler.add(importConditions(snapshot));
      questionsLoopScheduler.add(questionRoutineBegin(snapshot));
      questionsLoopScheduler.add(questionRoutineEachFrame());
      questionsLoopScheduler.add(questionRoutineEnd());
      const trialsLoopScheduler = new Scheduler(psychoJS);
      questionsLoopScheduler.add(trialsLoopBegin(trialsLoopScheduler, snapshot));
      questionsLoopScheduler.add(trialsLoopScheduler);
      questionsLoopScheduler.add(trialsLoopEnd);
      questionsLoopScheduler.add(endLoopIteration(questionsLoopScheduler, snapshot));
    });
    
    return Scheduler.Event.NEXT;
  }
}


var trials;
function trialsLoopBegin(trialsLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    trials = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 2, method: TrialHandler.Method.FULLRANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: 'C:/Users/yarde/Documents/GitHub/BCI4ALS-MI/stim_words.xlsx',
      seed: undefined, name: 'trials'
    });
    psychoJS.experiment.addLoop(trials); // add the loop to the experiment
    currentLoop = trials;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    trials.forEach(function() {
      const snapshot = trials.getSnapshot();
    
      trialsLoopScheduler.add(importConditions(snapshot));
      trialsLoopScheduler.add(crossRoutineBegin(snapshot));
      trialsLoopScheduler.add(crossRoutineEachFrame());
      trialsLoopScheduler.add(crossRoutineEnd());
      trialsLoopScheduler.add(trialRoutineBegin(snapshot));
      trialsLoopScheduler.add(trialRoutineEachFrame());
      trialsLoopScheduler.add(trialRoutineEnd());
      trialsLoopScheduler.add(endLoopIteration(trialsLoopScheduler, snapshot));
    });
    
    return Scheduler.Event.NEXT;
  }
}


async function trialsLoopEnd() {
  psychoJS.experiment.removeLoop(trials);

  return Scheduler.Event.NEXT;
}


async function questionsLoopEnd() {
  psychoJS.experiment.removeLoop(questions);

  return Scheduler.Event.NEXT;
}


var questionComponents;
function questionRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'question'-------
    t = 0;
    questionClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(1.500000);
    // update component parameters for each repeat
    target_quest.setText(Question_stim);
    // keep track of which components have finished
    questionComponents = [];
    questionComponents.push(target_quest);
    
    questionComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


var frameRemains;
function questionRoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'question'-------
    // get current time
    t = questionClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *target_quest* updates
    if (t >= 0.0 && target_quest.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      target_quest.tStart = t;  // (not accounting for frame time here)
      target_quest.frameNStart = frameN;  // exact frame index
      
      target_quest.setAutoDraw(true);
    }

    frameRemains = 0.0 + 1.5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (target_quest.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      target_quest.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    questionComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function questionRoutineEnd() {
  return async function () {
    //------Ending Routine 'question'-------
    questionComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    return Scheduler.Event.NEXT;
  };
}


var crossComponents;
function crossRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'cross'-------
    t = 0;
    crossClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(2.000000);
    // update component parameters for each repeat
    // keep track of which components have finished
    crossComponents = [];
    crossComponents.push(polygon);
    
    crossComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function crossRoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'cross'-------
    // get current time
    t = crossClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *polygon* updates
    if (t >= 0 && polygon.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      polygon.tStart = t;  // (not accounting for frame time here)
      polygon.frameNStart = frameN;  // exact frame index
      
      polygon.setAutoDraw(true);
    }

    frameRemains = 0 + 2 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (polygon.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      polygon.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    crossComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function crossRoutineEnd() {
  return async function () {
    //------Ending Routine 'cross'-------
    crossComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    return Scheduler.Event.NEXT;
  };
}


var trialComponents;
function trialRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'trial'-------
    t = 0;
    trialClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(0.700000);
    // update component parameters for each repeat
    target_word.setText(word);
    target_sound = new sound.Sound({
    win: psychoJS.window,
    value: sound_target,
    secs: 0.7,
    });
    target_sound.secs=0.7;
    target_sound.setVolume(1.0);
    // keep track of which components have finished
    trialComponents = [];
    trialComponents.push(target_word);
    trialComponents.push(target_sound);
    
    trialComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function trialRoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'trial'-------
    // get current time
    t = trialClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *target_word* updates
    if (t >= 0.0 && target_word.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      target_word.tStart = t;  // (not accounting for frame time here)
      target_word.frameNStart = frameN;  // exact frame index
      
      target_word.setAutoDraw(true);
    }

    frameRemains = 0.0 + 0.7 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (target_word.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      target_word.setAutoDraw(false);
    }
    // start/stop target_sound
    if (t >= 0.0 && target_sound.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      target_sound.tStart = t;  // (not accounting for frame time here)
      target_sound.frameNStart = frameN;  // exact frame index
      
      psychoJS.window.callOnFlip(function(){ target_sound.play(); });  // screen flip
      target_sound.status = PsychoJS.Status.STARTED;
    }
    frameRemains = 0.0 + 0.7 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (target_sound.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      if (0.7 > 0.5) {
        target_sound.stop();  // stop the sound (if longer than duration)
      }
      target_sound.status = PsychoJS.Status.FINISHED;
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    trialComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function trialRoutineEnd() {
  return async function () {
    //------Ending Routine 'trial'-------
    trialComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    target_sound.stop();  // ensure sound has stopped at end of routine
    return Scheduler.Event.NEXT;
  };
}


function endLoopIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        const thisTrial = snapshot.getCurrentTrial();
        if (typeof thisTrial === 'undefined' || !('isTrials' in thisTrial) || thisTrial.isTrials) {
          psychoJS.experiment.nextEntry(snapshot);
        }
      }
    return Scheduler.Event.NEXT;
    }
  };
}


function importConditions(currentLoop) {
  return async function () {
    psychoJS.importAttributes(currentLoop.getCurrentTrial());
    return Scheduler.Event.NEXT;
    };
}


async function quitPsychoJS(message, isCompleted) {
  // Check for and save orphaned data
  if (psychoJS.experiment.isEntryEmpty()) {
    psychoJS.experiment.nextEntry();
  }
  psychoJS.window.close();
  psychoJS.quit({message: message, isCompleted: isCompleted});
  
  return Scheduler.Event.QUIT;
}
