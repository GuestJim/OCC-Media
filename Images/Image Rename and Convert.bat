@echo off

set folder=Small

set	name=0
set pad=2

if NOT EXIST "%~dp1%folder%" (
mkdir "%~dp1%folder%"
)

magick convert "*_*_*.png" -write "%name%%%0%pad%d.png" -quality 95 -resize "1920x1080>" "%folder%\%name%%%0%pad%d.jpg"

::pause
