@echo off

set folder=Re-encode
set rate=30M

set input=%~1
set output=%~2
set cut=%~3
::	not strictly needed, but helpful for remembering

TITLE %input% to %output%

if NOT EXIST "%~dp1%folder%" (
mkdir "%~dp1%folder%"
)

ffmpeg -i "%~1" %cut% -map 0:v -map 0:a:1 ^
-vf "setpts=PTS-STARTPTS, format=pix_fmts=yuvj420p" ^
-c:v libx264 -crf 18 -maxrate %rate% -bufsize %rate% -preset slower ^
-c:a copy ^
-movflags faststart "%~dp1%folder%\%~2.mp4"

::pause
