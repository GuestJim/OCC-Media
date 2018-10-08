import sys, os
droppedFile = sys.argv[1]
droppedList = sys.argv[2]
NameStop = int(float(sys.argv[3]))
droppedPath = sys.argv[4]

if not droppedList == '':
	with open(droppedList, 'r') as LIST:
		NameList = LIST.read().splitlines()
else:
	NameList = []

foldnam = "YouTube Thumbnails"

height = 768

os.chdir(droppedPath)
if not os.path.exists(foldnam):
	os.mkdir(foldnam)
os.chdir(droppedPath + foldnam)

title = "Review Playthrough"

for name in range(1, NameStop + 1):
	Snam = str(name)
	Znam = format(name, '02')	
	if not os.path.exists("Thumbnail - " + Znam + ".png"):	
		with open(droppedFile, 'r') as fref, open('Temp.svg', 'w') as fout:
			for line in fref:
				fout.write(line.replace("!TYPE!", title).replace("!PART!", "Part " + Snam))
			fout.close()
		os.system('inkscape Temp.svg -C -z -h '+str(height)+' -e "Thumbnail - '+Znam+'.png"')

title = "Review"

for name in NameList:
	if not os.path.exists("Thumbnail - " + name + ".png"):	
		with open(droppedFile, 'r') as fref, open('Temp.svg', 'w') as fout:
			for line in fref:
				fout.write(line.replace("!TYPE!", title).replace("!PART!", name))
			fout.close()
		os.system('inkscape Temp.svg -C -z -h '+str(height)+' -e "Thumbnail - '+name+'.png"')

if os.path.exists("Temp.svg"):
	os.remove("Temp.svg")
