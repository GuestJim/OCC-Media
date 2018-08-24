@echo off

set vidloc=%~dp0
::	this file should be in the same folder as the videos

set batloc=%vidloc%
set batloc=E:\Users\Jim\My Videos\FFMPEG Batch files
::	can have the FFmpeg instructions int he same folder but better to reference a different, generic location
::	by referencing a generic location, it is not necessary to keep a copy of the file in the same folder as this

set type=Re-encode - Sequence.bat
::	name of the BATCH file with the FFmpeg instructions

set input=Review 2018-08-24 13-04-56 Replay
::	the file name of the input
::		the assumption is made the input is in a mkv file
::		this can be changed by removing '.mkv' below and adding it to the input variable
set output=
::	set the name of the output file
set cut=-ss 00:04:14 -to 00:09:43
::	instructions for FFmpeg to cut the video
::		-ss hh:mm:ss is the start location
::		-to hh:mm:ss is the stop location
call "%batloc%\%type%" "%vidloc%\%input%.mkv" "%output%" "%cut%"
::	call will actually call the BATCH file, pointed to by "%batloc%\%type%"
::	the parts after the pointer to the BATCH file are passed to it as BATCH Parameters

::pause
