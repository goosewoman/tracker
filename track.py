import os
import urllib2

file = open("files/blockedservers", "w")
for line in urllib2.urlopen("https://sessionserver.mojang.com/blockedservers"):
	found = False
	for dict_line in open("dictionary.txt", "r"):
		if line.strip() in dict_line.strip():
			file.write(dict_line.strip() + "\n")
			found = True

	if not found:
		file.write(line.strip() + "\n")

os.system("git add .")
os.system("git commit -a -m \"Automatic update\"")
os.system("git push -u origin master")
