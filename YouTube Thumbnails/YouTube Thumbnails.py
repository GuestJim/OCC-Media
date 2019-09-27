#This version is Python only/does not need the Batch file

import sys, os
#	loads different modules for Python

foldnam = "YouTube Thumbnails"
#	name for the folder the thumbnails should be saved in

titleProjLong = "Review Playthough"
#	Project Title for unedited videos
titleProjEdit = "Review"
#	Project Title edited videos

titleFilePart = "Stream"
#	File title for iterated thumbnails
titleFileList = "Review"
#	File title for named thumbnails

def	REPLACE(input, TYPE = titleProjLong, PART = "", LIST = ""):
	if type(PART) == int:
		PART	=	vidBreak + str(PART)
	return(input.replace("!TYPE!", TYPE).replace("!PART!", PART).replace("!LIST!", LIST));
#	custom function for applying the string replacements
#		can make things a little cleaner, by placing the multiple replace commands inside it and having default values

NameList	=	[]
#	creates an empty list for holding the list of names

for ARG in sys.argv:
	if ARG.endswith(".svg"):
		droppedFile	=	ARG
	if ARG.endswith(".txt"):
		with open(ARG, 'r') as LIST:
			NameList	=	LIST.read().splitlines()
#	goes through the list of arguments, assigning them to the proper variables depending on what the extensions are

droppedName = droppedFile.rsplit("\\",1)[1].split(".")[0]
#	pulls just the name from the droppedFile variable
droppedPath = droppedFile.rsplit("\\",1)[0] + "\\"
#	pulls just the location from the droppedFile variable and sticks the necessary \ at the end

NameStop = int(input("How many parts: ") or 0)
#	asks the user to state how many Part images to create
#	defaults to 0 if no input is provided

height = int(input("Image Height (default 768): ") or 768)
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
			fout.write(REPLACE(line, titleProjLong))
		fout.close()
	os.system('inkscape Temp.svg -C -z -h '+str(1152)+' -e "'+droppedName+' - Full.png"')
	os.system('inkscape Temp.svg -C -z -h '+str(height)+' -e "'+droppedName+'.png"')
#	creates a version of the thumbnail only identifying the Type
#	there is both a full resolution version for stream background and one sized for upload to YouTube

for place in range(1, NameStop + 1):
#	a For loop to go from 1 to the desired number passed to the scripts
#		The '+ 1' is necessary because Python excludes the top of the range
	Znam	=	format(place, '02')
#		creates a string from the place variable, with zero padding to 2 digits
	if not os.path.exists(titleFileList + " - " + Znam + ".png"):
#		checks if the thumbnail already exists and will skip if it does
		print(titleFileList + " - " + Znam + "\n")
#			prints a message identifying the thumbnail being generated
		with open(droppedFile, 'r') as fref, open('Temp.svg', 'w') as fout:
#			opens and reads the original SVG to the fref variable
#			opens the Temp.svg file for writing too, and calls it fout
			for line in fref:
#				reads through each line from the reference file
				fout.write(REPLACE(line, titleProjLong, PART = place))
#					uses the custom REPLACE command on every line in the reference file
#						it is not necessary to identify the PART argument, but it does not hurt
			fout.close()
#				closes fout, which finishes the file so it can be used
		os.system('inkscape Temp.svg -C -z -h '+str(height)+' -e "'+titleFileList+' - '+Znam+'.png"')
#			goes to the OS to run the provided command, in this case Inkscape
#				info on Inkscape commands:	https://inkscape.org/en/doc/inkscape-man.html

for name in NameList:
#	For loop going through the list of video names that can be given to the script
	if not os.path.exists(titleProjEdit + " - " + name + ".png"):
#		checks if the thumbnail already exists and will skip if it does
		print(titleProjEdit + " - " + name + "\n")
#			prints a message identifying the thumbnail being generated
		with open(droppedFile, 'r') as fref, open('Temp.svg', 'w') as fout:
#			opens and reads the original SVG to the fref variable
#			opens the Temp.svg file for writing too, and calls it fout
			for line in fref:
#				reads through each line from the reference file
				fout.write(REPLACE(line, titleProjLong, LIST = name))
#					uses the custom REPLACE command on every line in the reference file
#						it is necessary to identify the LIST argument
			fout.close()
#				closes fout, which finishes the file so it can be used
		os.system('inkscape Temp.svg -C -z -h '+str(height)+' -e "'+titleProjEdit+' - '+name+'.png"')
#			goes to the OS to run the provided command, in this case Inkscape
#				info on Inkscape commands:	https://inkscape.org/en/doc/inkscape-man.html

if os.path.exists("Temp.svg"):
	os.remove("Temp.svg")
#	checks if the Temp.svg file was made (if no Thumbnails are made, then neither is this) and removes it

#os.system("pause")
