import sys, os
droppedFile = sys.argv[1]
droppedName = droppedFile.rsplit("\\",1)[1].split(".")[0]
droppedList = sys.argv[2]
if not sys.argv[3] == '':
	NameStop = int(float(sys.argv[3]))
else:
	NameStop = 0
if not sys.argv[4] == '':
	height = int(float(sys.argv[4]))
else:
	height = 768
droppedPath = sys.argv[5] 

if not droppedList == '':
	with open(droppedList, 'r') as LIST:
		NameList = LIST.read().splitlines()
else:
	NameList = []

foldnam = "YouTube Thumbnails"

os.chdir(droppedPath)
if not os.path.exists(foldnam):
	os.mkdir(foldnam)
os.chdir(droppedPath + foldnam)

title = "Review Playthrough"

if not os.path.exists(droppedName + ".png"):	
	with open(droppedFile, 'r') as fref, open('Temp.svg', 'w') as fout:
		for line in fref:
			fout.write(line.replace("!TYPE!", "").replace("!PART!", ""))
		fout.close()
	os.system('inkscape Temp.svg -C -z -h '+str(height)+' -e "'+droppedName+'.png"')

for name in range(1, NameStop + 1):
	Snam = str(name)
	Znam = format(name, '02')	
	if not os.path.exists("Stream - " + Znam + ".png"):	
		with open(droppedFile, 'r') as fref, open('Temp.svg', 'w') as fout:
			for line in fref:
				fout.write(line.replace("!TYPE!", title).replace("!PART!", "Part " + Snam))
			fout.close()
		os.system('inkscape Temp.svg -C -z -h '+str(height)+' -e "Stream - '+Znam+'.png"')

title = "Review"

for name in NameList:
	if not os.path.exists("Review - " + name + ".png"):	
		with open(droppedFile, 'r') as fref, open('Temp.svg', 'w') as fout:
			for line in fref:
				fout.write(line.replace("!TYPE!", title).replace("!PART!", name))
			fout.close()
		os.system('inkscape Temp.svg -C -z -h '+str(height)+' -e "Review - '+name+'.png"')

if os.path.exists("Temp.svg"):
	os.remove("Temp.svg")
