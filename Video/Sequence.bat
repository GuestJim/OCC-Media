@echo off

set vidloc=%~dp0
::	this file should be in the same folder as the videos

set batloc=%vidloc%
set batloc=E:\Users\Jim\My Videos\FFMPEG Batch files
::	can have the FFmpeg instructions int he same folder but better to reference a different, generic location

set type=Re-encode - Sequence.bat

set input=Review 2018-08-24 13-04-56 Replay
set output=F1 2018 - Practice Programs - Tires and Fuel
set cut=-ss 00:04:14 -to 00:09:43
call "%batloc%\%type%" "%vidloc%\%input%.mkv" "%output%" "%cut%"

::pause
