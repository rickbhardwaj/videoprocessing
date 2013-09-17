#A possible source of error in my code was too much blanket importation so I will comment out excessive import statements and move accordingly

#import numpy
#import scipy
#import PIL

import sys
import os
#import matplotlib

from numpy import *
#from numpy import arrange #Clearly, I should not need this import statement. However, arrange() is not being recognized.
#from scipy import *
from pylab import * #Sub-directory of Scipy, Page 27
from PIL import Image

#Page 38. Applies the SIFT Algoritihim to the given image
#When just this image is run, you will only see a grayscale image (unless you print out the .pickle()) as the Grayscale Law holds true- everything must be normalized if you want to do anything with it
def process_image(imagename, resultname, params="--edge-thresh 10 --peak-thresh 5"):

	if imagename[-3:] != 'pgm':
		im = Image.open(imagename).convert('L')
		im.save('temp.pgm')
		imagename = 'temp.pgm'

	cmmd = str("~/Downloads/etc/vlfeat-0.9.16/bin/glnxa64/sift " + imagename + " --output=" + resultname + " " + params)
	os.system(cmmd)
	print 'processed', imagename, 'to', resultname


#Page 38 (Part of my ongoing experiments in storing images as different formats. Given my limited linear algebra experience, this is incredible to me.
#In C++, we had Mat, Image, cvImage, etc.
#In Python, with just Numpy, Scipy, and PIL, we have pickles and a consistent array representation for images (espciailly useful for signal processing)
def read_features_from_file(filename):
	
	f = loadtxt(filename)
	return f[:,:4],f[:,4:]


#I have to write my own range function that uses floats as steps (see use in plot_features())

def frange(x, y, step):
	while(x < y):
		yield x
		x += step



#Page 39. Making the analysis graphical
#If circle=true, blue circles overlayed as per the SIFT edges detected
def plot_features(im, locs, circle=False):
	
	def draw_circle(c, r):
		#t = numpy.arrange(0,1.01,.01) * 2 * pi #Seems to be a Numpy/Scipy circle object
		#t = range(0,1.01,.01) * 2 * pi #My Numpy directory can't find the arrange function- hopefully I can get by with the local range function
		#t = frange(0, 1.01, 0.01) #My replacement for numpy.arrange()	

		#With every option failing, I shall implement a for loop
		t = 0
		while(t <= 1):
			x = r * cos(t)
			y = r * sin(t)
			plot(x, y, 'b', linewidth=2) #Potentially from Python's native drawing library or PIL
			t += 0.1
	
	imshow(im)
	if circle:
		for p in locs:
			#print("Printing circle...")
			draw_circle(p[:2], p[2])
	
	else:
		#print("Plotting...")
		plot(locs[:,0], locs[:,1], 'ob')
	axis('on')

def main():
	#Book's addition to the main
	#imname = 'DowntownStreet.jpg'
	#Switching to Lenna so I have a smaller size
	imname = 'Biology.jpg'
	im1 = array(Image.open(imname).convert('L'))
	#process_image(imname, 'DowntownStreetBLUECIRCLES.sift')
	process_image(imname, 'BiologySIFT.jpg')
	
	#My simple and workign main
	#Raises some natural questions
	#process_image("DowntownStreet.jpg", "DowntownStreetSIFT.sift")

	#Blue Circles
	#l1,d1 = read_features_from_file('DowntownStreetBLUECIRCLES.sift')

	#l1,d1 = read_features_from_file('temp.pgm')
	l1,d1 = read_features_from_file('BiologySIFT.jpg')
	figure()
	gray()
	plot_features(im1, l1, circle=True)
	show()

if __name__ == "__main__":
	main()
