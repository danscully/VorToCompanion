Simple script to take the feedback SACN signal from Vor, and use OSC to control a variable in Companion.

To use:
- Install Python3.  Tested with 3.10
- Create a custom variable in Companion called "vorrecord".
- Create a login item to run the "VorToCompanionHelper.command" at login.
- You need to make the .command file executable (chmod +x VorToCompanionHelper.command).
- Turn on SACN feedback in Vor settings.
- Make sure the universe in the script matches the universe in Vor.
  \
For your record button, add a feedback control where if "vorrecord" is > 128, change the background color.  This will get your button to pulse every second as Vor is recording.
