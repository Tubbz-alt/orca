#!/usr/bin/python

"""Test of menu checkbox output using the gtk-demo Application Main Window
   demo.
"""

from macaroon.playback.keypress_mimic import *

sequence = MacroSequence()

########################################################################
# We wait for the demo to come up and for focus to be on the tree table
#
sequence.append(WaitForWindowActivate("GTK+ Code Demos"))
sequence.append(WaitForFocus(acc_role=pyatspi.ROLE_TREE_TABLE))

########################################################################
# Once gtk-demo is running, invoke the Application Main Window demo
#
sequence.append(KeyComboAction("<Control>f"))
sequence.append(WaitForFocus(acc_role=pyatspi.ROLE_TEXT))
sequence.append(TypeAction("Application main window", 1000))
sequence.append(KeyComboAction("Return", 500))

########################################################################
# When the demo comes up, go to the Bold check menu item in the
# Preferences menu.
#
#sequence.append(WaitForWindowActivate("Application Window",None))
sequence.append(WaitForFocus("Open", acc_role=pyatspi.ROLE_PUSH_BUTTON))
sequence.append(KeyComboAction("<Alt>p"))

sequence.append(WaitForFocus("Color", acc_role=pyatspi.ROLE_MENU))
sequence.append(KeyComboAction("Up"))

########################################################################
# When the Bold check menu item gets focus, the following should be
# presented in speech and braille:
#
# BRAILLE LINE:  'gtk-demo Application Application Window Frame MenuBar <x> Bold CheckItem(Control b)'
#      VISIBLE:  '<x> Bold CheckItem(Control b)', cursor=1
#
# SPEECH OUTPUT: ''
# SPEECH OUTPUT: 'Bold check item checked Control b'
#
sequence.append(WaitForFocus("Bold", acc_role=pyatspi.ROLE_CHECK_MENU_ITEM))

########################################################################
# Do a basic "Where Am I" via KP_Enter.  The following should be
# presented in speech and braille:
# BRAILLE LINE:  'gtk-demo Application Application Window Frame MenuBar <x> Bold CheckItem(Control b)'
#      VISIBLE:  '<x> Bold CheckItem(Control b)', cursor=1
#
# SPEECH OUTPUT: 'Preferences menu'
# SPEECH OUTPUT: 'Bold'
# SPEECH OUTPUT: 'check item'
# SPEECH OUTPUT: 'checked'
# SPEECH OUTPUT: 'Control b'
# SPEECH OUTPUT: 'item 3 of 3'
# SPEECH OUTPUT: 'b'
#
sequence.append(KeyComboAction("KP_Enter"))

########################################################################
# Dismiss the menu and close the Application Window demo window
#
sequence.append(KeyComboAction("Escape", 3000))
sequence.append(WaitForFocus("Open", acc_role=pyatspi.ROLE_PUSH_BUTTON))
sequence.append(KeyComboAction("<Alt>F4", 500))

########################################################################
# Go back to the main gtk-demo window and reselect the
# "Application main window" menu.  Let the harness kill the app.
#
#sequence.append(WaitForWindowActivate("GTK+ Code Demos",None))
sequence.append(WaitForFocus(acc_role=pyatspi.ROLE_TREE_TABLE))

# Just a little extra wait to let some events get through.
#
sequence.append(WaitForFocus(acc_role=pyatspi.ROLE_INVALID, timeout=3000))

sequence.start()
