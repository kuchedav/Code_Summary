def WriteTreePathFile(PathObserve,FolderNamesList):
	import glob
	with open(PathObserve + '.treePath.txt', 'a') as the_file:
		debth = '*'
		for j in FolderNamesList:
			dir = PathObserve + j
			for i in range(1,30):
				for filename in glob.iglob(dir  + debth + "JPG", recursive=True):
					print(the_file.write(filename + "\n"))
			debth = debth + "/*"