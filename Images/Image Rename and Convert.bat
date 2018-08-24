@echo off

set folder=Small

set prefix=0
set pad=2

if NOT EXIST "%~dp1%folder%" (
mkdir "%~dp1%folder%"
)

magick convert "*_*_*.png" -write "%prefix%%%0%pad%d.png" -quality 95 -resize "1920x1080>" "%folder%\%prefix%%%0%pad%d.jpg"

::pause
