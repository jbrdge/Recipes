from PIL import Image
import os

path = "/Volumes/Backup/09_29/09_29_sorted/10_04/new_images/hips_up"

for root, directories, files in os.walk(path):
    for name in files:
	im = Image.open("/".join((root,name)))
	hi, wi = im.size
	print(hi)
	if hi<400:
	    os.remove("/".join((root,name)))

