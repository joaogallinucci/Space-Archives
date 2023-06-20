# Space-Archives
The Space Archives is an open-source game inspired by Space Invaders, made entirely in Python. However, unlike the original Space Invaders, in this game, each enemy is a file from your computer. When you defeat an enemy, one of the files is deleted. But don't worry, the game only detects files that are in the same folder as the game.

Notice: This game is merely an experiment. If you wish to use it, you must select certain files and copy them into the game folder for it to detect them. Under no circumstances should you place important files within the game folder. I do not assume any responsibility for any damage caused to your files or your computer. Additionally, I do not assume any responsibility for other repositories that share the code of this game.

If you wish to play the game without having Python installed, simply extract the SI.7z file. Inside, you will find a pre-compiled Windows file. Just place the file in the main directory, and everything will work. If your antivirus raises any alerts, it is normal. It sometimes happens when something is compiled with PyInstaller :(

If you wish to compile the code yourself, you will need Python 3 and the following modules: pygame, random, os, pyinstaller. Once everything is ready, navigate to your game folder and execute the following command in the command prompt (CMD): 'pyinstaller --onefile -w SI.py'. After waiting for the compilation process to complete, your executable will be located in the 'dist' folder. Simply move it to the main directory.
