import cv2

im2 = cv2.imread(imgPath)
im = cv2.cvtColor(im2, cv2.COLOR_BGR2GRAY)
surfDetector = cv2.FeatureDetector_create("SURF")
surfDescriptorExtractor = cv2.DescriptorExtractor_create("SURF")
keypoints = surfDetector.detect(im)
(keypoints, descriptors) = surfDescriptorExtractor.compute(im,keypoints)
