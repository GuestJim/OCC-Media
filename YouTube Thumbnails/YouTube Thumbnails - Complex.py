#This version is Python only/does not need the Batch file

import sys, os
#	loads different modules for Python

foldnam = "YouTube Thumbnails"
#	name for the folder the thumbnails should be saved in

titleProjLong = "Review Playthough"
#	Project Title for unedited videos
titleProjEdit = "Review"
#	Project Title edited videos

titleFilePart = "Part"
#	File title for iterated thumbnails
titleFileList = "Review"
#	File title for named thumbnails

vidBreak = "Part"
#	how the videos break (Part, Chapter, etc)

droppedFile = sys.argv[1]
#	the location of the file dropped onto the script is stored in sys.argv[1]
#		sys.argv[0] is the location of the script
droppedName = droppedFile.rsplit("\\",1)[1].split(".")[0]
#	pulls just the name from the droppedFile variable
droppedPath = droppedFile.rsplit("\\",1)[0] + "\\"
#	pulls just the location from the droppedFile variable and sticks the necessary \ at the end

try:
	with open(sys.argv[2], 'r') as LIST:
		NameList = LIST.read().splitlines()
except:
	NameList = []
#	tries to grab a second dropped filed and then read its contents into a list
#	if there is no second dropped file, it makes the list empty
	
NameStop = int(input("How many parts: ")) or 0
#	asks the user to state how many Part images to create
#	defaults to 0 if no input is provided

height = int(input("Image Height (default 768): ")) or 768
#	asks the user to state how many Part images to create
#	defaults to 768 if no input is provided

os.chdir(droppedPath)
#	sets the working directory to that of the SVG file dropped onto the Batch script
if not os.path.exists(foldnam):
	os.mkdir(foldnam)
#	checks and then creates, if necessary, the YouTube Thumbnails folder
os.chdir(droppedPath + foldnam)
#	sets the working directory to be the YouTube Thumbnails folder, or whatever foldnam is

if not os.path.exists(droppedName + ".png"):
	with open(droppedFile, 'r') as fref, open('Temp.svg', 'w') as fout:
		for line in fref:
			fout.write(line.replace("!TYPE!", titleProjLong).replace("!PART!", "").replace("!LIST!", ""))
		fout.close()
	os.system('inkscape Temp.svg -C -z -h '+str(1152)+' -e "'+droppedName+' - Full.png"')
	os.system('inkscape Temp.svg -C -z -h '+str(height)+' -e "'+droppedName+'.png"')
#	creates a version of the thumbnail only identifying the Type
#	there is both a full resolution version for stream background and one sized for upload to YouTube

for name in range(1, NameStop + 1):
#	a For loop to go from 1 to the desired number passed to the scripts
#		The '+ 1' is necessary because Python excludes the top of the range
	Snam = str(name)
#		string version of the name for easy line replacement
	Znam = format(name, '02')	
	#		zero-padded version of the name for export file names
	if not os.path.exists(titleFilePart + " - " + Znam + ".png"):
#		checks if the thumbnail already exists and will skip if it does	
		with open(droppedFile, 'r') as fref, open('Temp.svg', 'w') as fout:
#			opens and reads the original SVG to the fref variable
#			opens the Temp.svg file for writing too, and calls it fout
			for line in fref:
#				reads through each line from the reference file
				fout.write(line.replace("!TYPE!", titleProjLong).replace("!PART!", vidBreak + " " + Snam).replace("!LIST!", NameList[name - 1]))
#					replaces the !TYPE!, !PART!, and !LIST! text in the reference SVG file with the 'titleProjLong' and 'Snam' variables and lines from the list you provide
#						note it is writing to fout, not fref, so the reference file is never changed
#						a new version of Temp.svg is made each time
			fout.close()
#				closes fout, which finishes the file so it can be used
		os.system('inkscape Temp.svg -C -z -h '+str(height)+' -e "'+titleFilePart+' - '+Znam+'.png"')
#			goes to the OS to run the provided command, in this case Inkscape
#				info on Inkscape commands:	https://inkscape.org/en/doc/inkscape-man.html

if os.path.exists("Temp.svg"):
	os.remove("Temp.svg")

#os.system("pause")