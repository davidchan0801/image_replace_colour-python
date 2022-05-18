import os
import shutil
import numpy as np
from PIL import Image

# Replace colour program in python

# Prerequisite:
# pip install numpy
# pip install Pillow

# Description
# The sample project provide you an example to change specfic colours into new colours of images.
# Please put images in root directory.


file_extension = ["jpg", "bmp", "png"]
replace_color = [0,0,0,0]

def replaceColor(img, targetColor, newColor):
  data = np.array(img)
  rgb = data[:,:,:3]
  mask = np.all(rgb == targetColor, axis = -1)
  data[mask] = newColor
  return Image.fromarray(data)

def getFourGrayscaleColor(img):
  for i in range(0,42):
    img = replaceColor(img, [i,i,i], [0,0,0])
  for i in range(42,128):
    img = replaceColor(img, [i,i,i], [85,85,85])
  for i in range(128,212):
    img = replaceColor(img, [i,i,i], [170,170,170])
  for i in range(212,256):
    img = replaceColor(img, [i,i,i], [255,255,255])
  return img

def saveFourGrayscaleColor(img,path):
  for ext in file_extension:
    if (path.endswith("."+ext)):
      getFourGrayscaleColor(img).save(path.replace("."+ext,'.bmp'))
      break

if (os.path.isdir("output")):
  shutil.rmtree("output")
os.mkdir("output")

for entry in os.scandir('.'):
  if entry.is_file():
    filename = entry.name
    for ext in file_extension:
      if (filename.endswith("."+ext)):
        img = Image.open(filename)
        img = getFourGrayscaleColor(img)
        img.save("output/" + filename.split(".")[0] + "." + ext)
