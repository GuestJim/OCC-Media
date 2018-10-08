@echo off

pushd %~dp0

set /p num="How Many Parts: "
::	Allows the user to pass a number to the scripts, for how many of the Part # thumbnails to create

python "YouTube Thumbnails.py" "%~1" "%~2" %num% "%~dp1
::	curiously I cannot close for the path
::	this will open the script and pass it those three arguments
::		full file path and name, file name, file path
::	these arguments are then passed through as sys.argv which can be called in Python

::pause
::	pause is useful for troubleshooting so I tend to leave it commented out for future use
