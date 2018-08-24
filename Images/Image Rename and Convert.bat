@echo off

set folder=Small
::	sets the name of the output folder

set	prefix=0
::	prefix characters to make identifying groups easier
set pad=2
::	the number of digits to pad to

if NOT EXIST "%~dp1%folder%" (
mkdir "%~dp1%folder%"
)
::	creates a new folder for the converted images to go to

magick convert "*_*_*.png" -write "%prefix%%%0%pad%d.png" -quality 95 -resize "1920x1080>" "%folder%\%prefix%%%0%pad%d.jpg"
::	magick convert	-	calls the convert tool of Imagemagick
::	"*_*_*.png"	-	accepts only the input PNG files that have three sets of characters with underscores between
::		this is the formatting Steam uses for screenshots and is to avoid doing this to any other images in the folder
::		can use "*.png" if we do not need to work on only Steam screenshots
::	-write "%prefix%%%0%pad%d.png"	-	writes a copy of the input to a file with a new name to match the converted output
::	-quality 95 -resize "1920x1080>"	-	sets the JPG compression to quality 95 and resizes the image to be no larger than 1920x1080
::	"%folder%\%prefix%%%0%pad%d.jpg"	-	the output file path, name, and file type

::pause
