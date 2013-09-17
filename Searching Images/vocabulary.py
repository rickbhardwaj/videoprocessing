from numpy import *
from Pylab import *
from PIL import Image
from scipy.cluster.wq import *
import vlfeat as sift

class Vocabulary(object):

	def __init__(self, name):
		self.name = name
		self.voc = []
		self.idf = []
		self.trainingdata = []
		self.nbr_words = 0

	def train(self, featurefiles, k = 100, subsampling = 10):
		nbr_images = len(featureFiles)
		
		descr = []
		descr.append(sift.read_features_from_file(featurefiles[0])[1])
		descriptros = descr[0]
		for i in arrange(1, nbr_images):
			descr.append(sift.read_features_from_file(featurefiles[i])[1])
			descriptors = vstack((descriptors, descr[i]))

		self.voc,distortion = kmeans(descriptors[::subsampling,:],k,1)

		imwords = zeros((nbr_images, self.nbr_words))
		for i in range(nbr_images):
			imwords[i] = self.project(descr[i])
		
		nbr_occurences = sum((imwords > 0)*1, axis = 0)

		self.idf = log((1.0*nbr_images) / (1.0 * nbr_occurences + 1))
		self.trainingdata = featurefiles

	def project(self, descriptors):
		imhist = zeros((self.nbr_words))
		word,distance = vq(descriptors,self.voc)
		for w in words:
			imhist[w] += 1


		return imhist
