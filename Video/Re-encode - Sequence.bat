@echo off

set folder=Re-encode
::	sets the name of the folder that will be created for the output files
set rate=30M
::	sets the maximum bitrate of the output video

set input=%~1
set output=%~2
set cut=%~3
::	not strictly needed, but helpful for remembering

TITLE %input% to %output%
::	sets the title of the console window to show the input file name "to" the output file name

if NOT EXIST "%~dp1%folder%" (
mkdir "%~dp1%folder%"
)
::	checks if the output folder exists and makes it if necessary

ffmpeg -i "%~1" %cut% -map 0:v -map 0:a:1 ^
::	ffmpeg	-	calls FFmpeg
::	-i "%~1"	-	passes it the input file
::	%cut%	-	gives it seeking instructions for cutting the video
::		format is -ss hh:mm:ss -to hh:mm:ss
::	-map 0:v -map 0:a:1	-	states which video and audio tracks to use
::		-map 0:v identifies all video tracks in the first input file
::		-map 0:a:1 identifies the second audio track in the first input file
::			a:0	Game + Mic
::			a:1	Game audio
::			a:2	Mic audio
-vf "setpts=PTS-STARTPTS, format=pix_fmts=yuvj420p" ^
::	-vf	-	calls Video Filters (-vf)
::	setpts=PTS-STARTPTS	-	resets the Presentation Time Stamp which can fix some timing issues
::	format=pix_fmts=yuvj420p	-	makes the pixel format have 4:2:0 chroma subsampling, but full BT.709 colors
-c:v libx264 -crf 18 -maxrate %rate% -bufsize %rate% -preset slower ^
::	-c:v libx264	-	identifies the video encoder to use is x264
::	-crf 18	-	sets what the Constant Rate Factor for x264 should be
::		18 corresponds to what should be visually lossless
::	-maxrate %rate% -bufsize %rate%	-	sets a maximum bit rate, so CRF will not go above it
::	-present slower	-	identifies the encoding preset for x264
::		the slower the preset the more efficient compression
-c:a copy ^
::	-c:a copy	-	copies the audio tracks to the output
-movflags faststart "%~dp1%folder%\%~2.mp4"
::	-movflags faststart	-	places the atom metadata for the MP4 container at the front of the file instead of the end
::	"%~dp1%folder%\%~2.mp4"	-	identifies where the output should be saved, its name, and container

::pause
