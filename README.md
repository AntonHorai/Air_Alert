# Air_Alert
Project for Orange Pi Zero (Raspberry Pi) running Armbian, that integrates "Vellez ПМН-8"(fire alarm system) extension pult with "Air Alert" app from Stfalcon.
When PI recives alert from "Air Alert", it simulates pressing of the corresponding button on the pult, that turns amplifiers on, and plays the message. Then, outer siren turns on for 1 min. 
Another message is played when alert ends.
Also, there is a Telegram bot, that allows users to manually turn siren on and off and play messages through plants alarm system speakers.
# Necessary files are:
- alert_1.py (main script);
- AL_main.mp3 and OK.mp3 (alert and OK messages);
- remote.py (Telegram bot main file);
- dosomething.py (actions, called from remote.py);
- users.txt (authorized users and their Telegram ID's).
# Other files:
- IO.jpg (typical GPIO-to-24DCV relay connection);
- Morning.mp3 (Notice before alarm system test);
- configs.txt (Content of /etc/rc.local and other files, that are used to autostart our scripts);
