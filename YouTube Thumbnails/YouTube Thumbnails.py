import sys, os
#	loads different modules for Python

droppedFile = sys.argv[1]
droppedList = sys.argv[2]
if not sys.argv[3] == '':
	NameStop = int(float(sys.argv[3]))
else:
	NameStop = 0
#	this is the variable for the Part # and needs to be converted from type String to a number
# 	the If/Else is so one can skip providing a number without error
if not sys.argv[4] == '':
	height = int(float(sys.argv[4]))
else:
	height = 768
#	this allows a custom height for the PNG to be passed to this script from the BATCH file
# 	the If/Else is so one can skip providing a number without error
droppedPath = sys.argv[5]
#	assigns the values of the Batch Parameters passed to the Python script to these variables

if not droppedList == '':
	with open(droppedList, 'r') as LIST:
		NameList = LIST.read().splitlines()
else:
	NameList = []
#	allows the script to take a plain text file for a list of thumbnail titles
#	the If/Else is so one does not need to provide a list
	
foldnam = "YouTube Thumbnails"
#	folder name variable

os.chdir(droppedPath)
#	sets the working directory to that of the SVG file dropped onto the Batch script
if not os.path.exists(foldnam):
	os.mkdir(foldnam)
#	checks and then creates, if necessary, the YouTube Thumbnails folder
os.chdir(droppedPath + foldnam)
#	sets the working directory to be the YouTube Thumbnails folder, or whatever foldnam is

title = "Review Playthrough"
#	the title for the Part # thumbnails
#		it is a separate variable for easier editing, if ever needed

for name in range(1, NameStop + 1):
#	a For loop to go from 1 to the desired number passed to the scripts
#		The '+ 1' is necessary because Python excludes the top of the range
	Snam = str(name)
#		string version of the name for easy line replacement
	Znam = format(name, '02')	
#		zero-padded version of the name for export file names
	if not os.path.exists("Thumbnail - " + Znam + ".png"):
#		checks if the thumbnail already exists and will skip if it does
		with open(droppedFile, 'r') as fref, open('Temp.svg', 'w') as fout:
#			opens and reads the original SVG to the fref variable
#			opens the Temp.svg file for writing too, and calls it fout
			for line in fref:
#				reads through each line from the reference file
				fout.write(line.replace("!TYPE!", title).replace("!PART!", "Part " + Snam))
#					replaces the !TYPE! and !PART! text in the reference file with the 'title' and 'Snam' variables
#						note it is writing to fout, not fref, so the reference file is never changed
#						a new version of Temp.svg is made each time
			fout.close()
#				closes fout, which finishes the file so it can be used
		os.system('inkscape Temp.svg -C -z -h '+str(height)+' -e "Thumbnail - '+Znam+'.png"')
#			goes to the OS to run the provided command, in this case Inkscape
#				info on Inkscape commands:	https://inkscape.org/en/doc/inkscape-man.html
		
title = "Review"
#	this section is to produce thumbnails with a custom name, not just Part #, so Review instead of Review Playthrough is the proper title

for name in NameList:
#	For loop going through the list of video names that can be given to the script
	if not os.path.exists("Thumbnail - " + name + ".png"):
#		checks if the thumbnail already exists and will skip if it does
		with open(droppedFile, 'r') as fref, open('Temp.svg', 'w') as fout:
#			opens and reads the original SVG to the fref variable
#			opens the Temp.svg file for writing too, and calls it fout
			for line in fref:
#				reads through each line from the reference file
				fout.write(line.replace("!TYPE!", title).replace("!PART!", "Part " + Snam))
#					replaces the !TYPE! and !PART! text in the reference file with the 'title' and 'Snam' variables
#						note it is writing to fout, not fref, so the reference file is never changed
#						a new version of Temp.svg is made each time
			fout.close()
#				closes fout, which finishes the file so it can be used
		os.system('inkscape Temp.svg -C -z -h '+str(height)+' -e "Thumbnail - '+Znam+'.png"')
#			goes to the OS to run the provided command, in this case Inkscape
#				info on Inkscape commands:	https://inkscape.org/en/doc/inkscape-man.html

if os.path.exists("Temp.svg"):
	os.remove("Temp.svg")
#	checks if the Temp.svg file was made (if no Thumbnails are made, then neither is this) and removes it
