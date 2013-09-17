import numpy #Numpy is a Mathematics package primarily for linear algebra and scientific calculations
import scipy #Scipy builds on Numpy and, most relevantly, adds signal processing
import PIL #Python Image Library

from numpy import *
from scipy import *
from PIL import Image
from scipy.ndimage import measurements,morphology

#Loading the image and threshold and ensuring it's a binary
im = array(Image.open('DowntownStreet.jpg').convert('L'))
im = 1*(im<128)

labels, nbr_objects = measurements.label(im)
print "Number of objects:", nbr_objects
