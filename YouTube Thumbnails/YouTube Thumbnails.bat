@echo off

pushd %~dp0

set /p hei="Image Height (default 768): "
::	Allows the user to pass a number to the scripts, for the height of the output images
::		the default of 768 is set in the Python file

python "YouTube Thumbnails.py" "%~1" "%~2" "%num%" "%hei%" "%~dp1
::	it is necessary to surround each variable with quotes, in case any are blank

::	curiously I cannot close for the path
::	this will open the script and pass it those three arguments
::		full file path and name, file name, file path
::	these arguments are then passed through as sys.argv which can be called in Python

::pause
::	pause is useful for troubleshooting so I tend to leave it commented out for future use
