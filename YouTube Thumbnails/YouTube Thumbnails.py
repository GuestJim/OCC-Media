#This version is Python only/does not need the Batch file

import sys, os

foldnam	=	"YouTube Thumbnails"
START	=	1

titleProjLong	=	"Review Playthrough"
#	Project Title for unedited videos
titleProjEdit	=	"Review"
#	Project Title edited videos

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

if len(sys.argv) == 3:
	if sys.argv[1].endswith(".svg"):
		droppedFile	=	sys.argv[1]
		with open(sys.argv[2], 'r') as LIST:
			NameList	=	LIST.read().splitlines()
	if sys.argv[1].endswith(".txt"):
		droppedFile	=	sys.argv[2]
		with open(sys.argv[1], 'r') as LIST:
			NameList	=	LIST.read().splitlines()
elif len(sys.argv) == 2:
	droppedFile	=	sys.argv[1]
	NameList	=	[]

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
	if not os.path.exists(titleFileList + " - " + Znam + ".png"):
		print(titleFileList + " - " + Znam + "\n")
		with open(droppedFile, 'r') as fref, open('Temp.svg', 'w') as fout:
			for line in fref:
				fout.write(REPLACE(line, titleProjLong, PART = place))
			fout.close()
		os.system('inkscape Temp.svg -C -z -h '+str(height)+' -e "'+titleFileList+' - '+Znam+'.png"')

for name in NameList:
	if not os.path.exists(titleProjEdit + " - " + name + ".png"):
		print(titleProjEdit + " - " + name + "\n")
		with open(droppedFile, 'r') as fref, open('Temp.svg', 'w') as fout:
			for line in fref:
				fout.write(REPLACE(line, titleProjLong, LIST = name))
			fout.close()
		os.system('inkscape Temp.svg -C -z -h '+str(height)+' -e "'+titleProjEdit+' - '+name+'.png"')

if os.path.exists("Temp.svg"):
	os.remove("Temp.svg")

# os.system("pause")