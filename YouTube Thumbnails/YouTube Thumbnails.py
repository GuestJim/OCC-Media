#This version is Python only/does not need the Batch file

import sys, os

foldnam	=	"YouTube Thumbnails"
START	=	1

titleProjLong	=	"Review Playthrough"
#	Project Title for unedited videos

titleFilePart	=	"Stream"
#	File title for iterated thumbnails
titleFileList	=	"Review"
#	File title for named thumbnails

vidBreak		=	"Part "
#	how the videos break (Part, Chapter, etc)

def	REPLACE(input, TYPE = titleProjLong, PART = "", LIST = ""):
	if type(PART) == int:
		PART	=	vidBreak + str(PART)
	return(input.replace("!TYPE!", TYPE).replace("!PART!", PART).replace("!LIST!", LIST));

NameList	=	[]

for ARG in sys.argv:
	if ARG.endswith(".svg"):
		droppedFile	=	ARG
	if ARG.endswith(".txt"):
		with open(ARG, 'r') as LIST:
			NameList	=	LIST.read().splitlines()

droppedName	=	droppedFile.rsplit("\\",1)[1].split(".")[0]
droppedPath	=	droppedFile.rsplit("\\",1)[0] + "\\"

NameStop	=	int(input("How many parts: ") or 0)

height		=	int(input("Image Height (default 768): ") or 768)

os.chdir(droppedPath)
if not os.path.exists(foldnam):
	os.mkdir(foldnam)
os.chdir(droppedPath + foldnam)


if not os.path.exists(droppedName + ".png"):
	with open(droppedFile, 'r') as fref, open('Temp.svg', 'w') as fout:
		for line in fref:
			fout.write(REPLACE(line, titleProjLong))
		fout.close()
	os.system('inkscape Temp.svg -C -z -h '+str(1152)+' -e "'+droppedName+' - Full.png"')
	os.system('inkscape Temp.svg -C -z -h '+str(height)+' -e "'+droppedName+'.png"')

for place in range(1, NameStop + 1):
	Znam	=	format(place, '02')
	if not os.path.exists(titleFilePart + " - " + Znam + ".png"):
		print(titleFilePart + " - " + Znam + "\n")
		with open(droppedFile, 'r') as fref, open('Temp.svg', 'w') as fout:
			for line in fref:
				fout.write(REPLACE(line, titleProjLong, PART = place))
			fout.close()
		os.system('inkscape Temp.svg -C -z -h '+str(height)+' -e "'+titleFilePart+' - '+Znam+'.png"')

for name in NameList:
	if not os.path.exists(titleFileList + " - " + name + ".png"):
		print(titleFileList + " - " + name + "\n")
		with open(droppedFile, 'r') as fref, open('Temp.svg', 'w') as fout:
			for line in fref:
				fout.write(REPLACE(line, titleProjLong, LIST = name))
			fout.close()
		os.system('inkscape Temp.svg -C -z -h '+str(height)+' -e "'+titleFileList+' - '+name+'.png"')

if os.path.exists("Temp.svg"):
	os.remove("Temp.svg")

# os.system("pause")
