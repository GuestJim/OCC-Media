#This version is Python only/does not need the Batch file

import sys, os

foldnam = "YouTube Thumbnails"

titleProjLong = "Review Playthough"
#	Project Title for unedited videos
titleProjEdit = "Review"
#	Project Title edited videos

titleFilePart = "Stream"
#	File title for iterated thumbnails
titleFileList = "Review"
#	File title for named thumbnails

vidBreak = "Part"
#	how the videos break (Part, Chapter, etc)

droppedFile = sys.argv[1]
droppedName = droppedFile.rsplit("\\",1)[1].split(".")[0]
droppedPath = droppedFile.rsplit("\\",1)[0] + "\\"

try:
	with open(sys.argv[2], 'r') as LIST:
		NameList = LIST.read().splitlines()
except:
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
			fout.write(line.replace("!TYPE!", titleProjLong).replace("!PART!", ""))
		fout.close()
	os.system('inkscape Temp.svg -C -z -h '+str(1152)+' -e "'+droppedName+' - Full.png"')
	os.system('inkscape Temp.svg -C -z -h '+str(height)+' -e "'+droppedName+'.png"')

for name in range(1, NameStop + 1):
	Snam = str(name)
	Znam = format(name, '02')	
	if not os.path.exists(titleFilePart + " - " + Znam + ".png"):	
		with open(droppedFile, 'r') as fref, open('Temp.svg', 'w') as fout:
			for line in fref:
				fout.write(line.replace("!TYPE!", titleProjLong).replace("!PART!", vidBreak + " " + Snam))
			fout.close()
		os.system('inkscape Temp.svg -C -z -h '+str(height)+' -e "'+titleFilePart+' - '+Znam+'.png"')

for name in NameList:
	if not os.path.exists(titleFileList + " - " + name + ".png"):	
		with open(droppedFile, 'r') as fref, open('Temp.svg', 'w') as fout:
			for line in fref:
				fout.write(line.replace("!TYPE!", titleProjEdit).replace("!PART!", name))
			fout.close()
		os.system('inkscape Temp.svg -C -z -h '+str(height)+' -e "'+titleFileList+' - '+name+'.png"')

if os.path.exists("Temp.svg"):
	os.remove("Temp.svg")

# os.system("pause")