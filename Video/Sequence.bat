@echo off

set vidloc=%~dp0
set rate264=30M
set rate265=10M
set rateAV1=10M

set title=

REM CALL :FFcut "INPUT" "-ss 00:00:00 -to 00:09:59" ""
CALL :FFx264 "INPUT" "-ss 00:00:00 -to 00:09:59" ""
REM CALL :FFx265 "INPUT" "-ss 00:00:00 -to 00:09:59" ""
REM CALL :FFav1 "INPUT" "-ss 00:00:00 -to 00:09:59" ""

::pause

exit


:FOLDcheck <OUTfold>
if NOT EXIST "%~1" mkdir "%~1"
exit/B 0

:FFcut <input> <cut> <output>
set folder=Re-encode
CALL :FOLDcheck %folder%
ffmpeg -i "%vidloc%%~1" %~2 -map 0:v -map 0:a:1? ^
-c copy ^
-movflags faststart "%vidloc%%folder%\%title% - %~3.mp4" -n
exit /B 0

:FFx264 <input> <cut> <output>
set folder=Re-encode
CALL :FOLDcheck %folder%
ffmpeg -i "%vidloc%%~1" %~2 -map 0:v -map 0:a:1? ^
-vf "setpts=PTS-STARTPTS, format=pix_fmts=yuvj420p" ^
-c:v libx264 -crf 18 -maxrate %rate264% -bufsize %rate264% -preset slow ^
-c:a copy ^
-movflags faststart "%vidloc%%folder%\%title% - %~3.mp4" -n
exit /B 0

:FFx265 <input> <cut> <output>
set folder=Re-encode - x265
CALL :FOLDcheck %folder%
ffmpeg -i "%vidloc%%~1" %~2 -map 0:v -map 0:a:1? ^
-vf "setpts=PTS-STARTPTS, format=pix_fmts=yuvj420p" ^
-c:v libx265 -crf 18 -maxrate %rate265% -bufsize %rate265% -preset medium ^
-c:a copy ^
-movflags faststart "%vidloc%%folder%\%title% - %~3.mp4" -n
exit /B 0

:FFav1 <input> <cut> <output>
set folder=Re-encode - AV1
CALL :FOLDcheck %folder%
ffmpeg -i "%vidloc%%~1" %~2 -map 0:v -map 0:a:1? ^
-vf "setpts=PTS-STARTPTS, format=pix_fmts=yuvj420p" ^
-c:v libsvtav1 -crf 20 -preset 7 -svtav1-params tune=0:mbr=%rateAV1% ^
-c:a copy "%vidloc%%folder%\%title% - %~3.mkv" -n