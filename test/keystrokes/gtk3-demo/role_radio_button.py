#!/usr/bin/python

"""Test of radio button output."""

from macaroon.playback import *
import utils

sequence = MacroSequence()

sequence.append(KeyComboAction("<Control>f"))
sequence.append(TypeAction("Printing"))
sequence.append(KeyComboAction("Return"))
sequence.append(PauseAction(3000))

sequence.append(utils.StartRecordingAction())
sequence.append(KeyComboAction("<Alt>a"))
sequence.append(utils.AssertPresentationAction(
    "1. All Pages radio button",
    ["BRAILLE LINE:  'gtk3-demo application Print dialog General page tab Range panel Range &=y All Pages radio button'",
     "     VISIBLE:  '&=y All Pages radio button', cursor=1",
     "SPEECH OUTPUT: 'General page tab'",
     "SPEECH OUTPUT: 'Range panel'",
     "SPEECH OUTPUT: 'All Pages selected radio button'"]))

sequence.append(utils.StartRecordingAction())
sequence.append(KeyComboAction("KP_Enter"))
sequence.append(utils.AssertPresentationAction(
    "2. All Pages radio button Where Am I",
    ["BRAILLE LINE:  'gtk3-demo application Print dialog General page tab Range panel Range &=y All Pages radio button'",
     "     VISIBLE:  '&=y All Pages radio button', cursor=1",
     "SPEECH OUTPUT: 'Range All Pages radio button selected 1 of 3.'",
     "SPEECH OUTPUT: 'Alt+A'"]))

sequence.append(KeyComboAction("Down"))
sequence.append(utils.StartRecordingAction())
sequence.append(KeyComboAction("<Shift>ISO_Left_Tab"))
sequence.append(utils.AssertPresentationAction(
    "3. Range radio button",
    ["BRAILLE LINE:  'gtk3-demo application Print dialog General page tab Range panel Range &=y Pages: radio button'",
     "     VISIBLE:  '&=y Pages: radio button', cursor=1",
     "SPEECH OUTPUT: 'Pages: selected radio button'"]))

sequence.append(utils.StartRecordingAction())
sequence.append(KeyComboAction("KP_Enter"))
sequence.append(utils.AssertPresentationAction(
    "4. Range radio button Where Am I",
    ["BRAILLE LINE:  'gtk3-demo application Print dialog General page tab Range panel Range &=y Pages: radio button'",
     "     VISIBLE:  '&=y Pages: radio button', cursor=1",
     "SPEECH OUTPUT: 'Range Pages: radio button selected 3 of 3.'",
     "SPEECH OUTPUT: 'Alt+E'",
     "SPEECH OUTPUT: 'Specify one or more page ranges,",
     " e.g. 1-3,7,11'"]))

sequence.append(KeyComboAction("<Alt>F4"))

sequence.append(utils.AssertionSummaryAction())
sequence.start()
