#This version is Python only/does not need the Batch file

import sys, os

foldnam = "YouTube Thumbnails"

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

droppedSVG = None
droppedTXT = None

for file in sys.argv[1:]:
	#if ".svg" in file:
	if files.endswith(".svg"):
		droppedSVG = file
	#if ".txt" in file:
	if files.endswith(".txt"):
		droppedTXT = file

droppedFile = droppedSVG
droppedName = droppedFile.rsplit("\\",1)[1].split(".")[0]
droppedPath = droppedFile.rsplit("\\",1)[0] + "\\"

print(droppedSVG)
print(droppedTXT)

if droppedTXT is not None:
	with open(droppedTXT, 'r') as LIST:
		NameList = LIST.read().splitlines()
else:
	NameList = []

NameStop = int(input("How many parts: ") or 0)

# if NameStop == '':
	# NameStop = 0
# else:
	# NameStop = int(NameStop)

height = int(input("Image Height (default 768): ") or 768)

# if height == '':
	# height = 768
# else:
	# height = int(height)

os.chdir(droppedPath)
if not os.path.exists(foldnam):
	os.mkdir(foldnam)
os.chdir(droppedPath + foldnam)

if not os.path.exists(droppedName + ".png"):
	with open(droppedFile, 'r') as fref, open('Temp.svg', 'w') as fout:
		for line in fref:
			fout.write(line.replace("!TYPE!", titleProjLong).replace("!PART!", "").replace("!LIST!", ""))
		fout.close()
	os.system('inkscape Temp.svg -C -z -h '+str(1152)+' -e "'+droppedName+' - Full.png"')
	os.system('inkscape Temp.svg -C -z -h '+str(height)+' -e "'+droppedName+'.png"')

for name in range(1, NameStop + 1):
	Snam = str(name)
	Znam = format(name, '02')
	if not os.path.exists(titleFilePart + " - " + Znam + ".png"):
		print(titleFilePart + " - " + Znam + "\n")
		with open(droppedFile, 'r') as fref, open('Temp.svg', 'w') as fout:
			for line in fref:
				if droppedTXT is not None:
					fout.write(line.replace("!TYPE!", titleProjLong).replace("!PART!", vidBreak + " " + Snam).replace("!LIST!", NameList[name - 1]))
				else:
					fout.write(line.replace("!TYPE!", titleProjLong).replace("!PART!", vidBreak + " " + Snam))
			fout.close()
		os.system('inkscape Temp.svg -C -z -h '+str(height)+' -e "'+titleFilePart+' - '+Znam+'.png"')

if os.path.exists("Temp.svg"):
	os.remove("Temp.svg")

#os.system("pause")
