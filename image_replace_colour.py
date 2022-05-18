import os
import shutil
import sys
import numpy as np
from PIL import Image

file_extension = ["jpg", "bmp", "png"]
replace_color = [0,0,0,0]

def listAllFiles():
  filenames = []
  for root, dirs, files in os.walk("."):
    for dir in dirs:
      for root, dirs, files in os.walk(dir):
        for filename in files:
          filenames.append(dir+'/'+filename)
  return filenames

def listAllDirectory(sourceDirectoryName):
  dirss = []
  for root, dirs, files in os.walk(sourceDirectoryName):
    return dirs

def deleteDirectory(path):
  if os.path.exists(path) and os.path.isdir(path):
    shutil.rmtree(path)

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

# Replace colour program in python

# Prerequisite:
# pip install numpy
# pip install Pillow

# Description
# The sample project provide you an example to change specfic colours into new colours of images.
# Please put images in root directory.

for root, dirss, files in os.walk(".."):
  for filename in files:
    extension = filename.split(".")[-1]
    if (extension == "bmp" or extension == "jpg" or extension == "png"):
      print(filename)
      img = Image.open(filename)
      mordifiedImg = getFourGrayscaleColor(img)
      mordifiedImg.save(filename.split(".")[0] + "_modified" + "." + extension)
