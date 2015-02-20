#!/usr/bin/python

"""Test of menu accelerator label output."""

from macaroon.playback import *
import utils

sequence = MacroSequence()

sequence.append(KeyComboAction("<Control>f"))
sequence.append(TypeAction("Application class"))
sequence.append(KeyComboAction("Return"))
sequence.append(KeyComboAction("Return"))
sequence.append(PauseAction(3000))

sequence.append(utils.StartRecordingAction())
sequence.append(KeyComboAction("<Alt>p"))
sequence.append(utils.AssertPresentationAction(
    "1. Initial menu and menu item",
    ["BRAILLE LINE:  'gtk3-demo-application application Application Class frame Preferences menu'",
     "     VISIBLE:  'Preferences menu', cursor=1",
     "BRAILLE LINE:  'gtk3-demo-application application Application Class frame < > Prefer Dark Theme check menu item'",
     "     VISIBLE:  '< > Prefer Dark Theme check menu', cursor=1",
     "SPEECH OUTPUT: 'Preferences menu'",
     "SPEECH OUTPUT: 'Prefer Dark Theme check menu item not checked'"]))

sequence.append(utils.StartRecordingAction())
sequence.append(KeyComboAction("Down"))
sequence.append(utils.AssertPresentationAction(
    "2. Next menu item",
    ["BRAILLE LINE:  'gtk3-demo-application application Application Class frame < > Hide Titlebar when maximized check menu item'",
     "     VISIBLE:  '< > Hide Titlebar when maximized', cursor=1",
     "SPEECH OUTPUT: 'Hide Titlebar when maximized check menu item not checked'"]))

sequence.append(utils.StartRecordingAction())
sequence.append(KeyComboAction("Down"))
sequence.append(utils.AssertPresentationAction(
    "3. Next menu item",
    ["BRAILLE LINE:  'gtk3-demo-application application Application Class frame Color menu'",
     "     VISIBLE:  'Color menu', cursor=1",
     "SPEECH OUTPUT: 'Color menu'"]))

sequence.append(utils.StartRecordingAction())
sequence.append(KeyComboAction("KP_Enter"))
sequence.append(utils.AssertPresentationAction(
    "4. Where Am I",
    ["BRAILLE LINE:  'gtk3-demo-application application Application Class frame Color menu'",
     "     VISIBLE:  'Color menu', cursor=1",
     "SPEECH OUTPUT: 'Application Class frame'",
     "SPEECH OUTPUT: 'Preferences menu'",
     "SPEECH OUTPUT: 'Color menu 3 of 5.'",
     "SPEECH OUTPUT: 'C'"]))

sequence.append(KeyComboAction("Escape"))
sequence.append(KeyComboAction("<Alt>F4"))

sequence.append(utils.AssertionSummaryAction())
sequence.start()
