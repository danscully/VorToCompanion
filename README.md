Simple script to take the feedback SACN signal from Vor, and use OSC to control a variable in Companion.

To use:
- Install Python3.  Tested with 3.10
- Copy the sacnListen and VorToCompanionHelper.command files locally on your machine.  The Desktop is fine.  (If not on the desktop, you need to fix the path in VorToCompanionHelper.command).
- You need to make the .command file executable (chmod +x VorToCompanionHelper.command).
- Create a custom variable in Companion called "vorrecord".
- Create a login item to run the "VorToCompanionHelper.command" at login.
- Turn on SACN feedback in Vor settings.
- Make sure the universe in the script matches the universe in Vor.
  
For your record button, add a feedback control where if "vorrecord" is > 128, change the background color.  This will get your button to pulse every second as Vor is recording.
