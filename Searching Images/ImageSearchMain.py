import pickle
import vocabulary
import sift
import imagesearch
from pysqlite2 import dbapi2 as sqlite

def __main__:
	
	nbr_images = len(imlist)
	featlist = [ imlist[i][:-3] + 'sif' for i in range(nbr_images))

	for i in range(nbr_images):
		sift.process_image(imlist[i],featlist[i])

	voc = vocabularly.Vocabulary('ukbenchtest')
	voc.train(featlist,1000,10)

	with open('vocabulary.pkl', 'wb') as f:
		pickle.dump(voc,f)
	print 'vocabulary is:', voc.name, voc.nbr_wods


	nbr_images = len(imlist)

	with open('vocabulary.pkl', 'rb') as f:
		voc = pickle.load(f)


	indx = imagesearch.Indexer('test.db',voc)
	indx.create_tables()

	for i in range(nbr_images)[:100]:
		locs,descr = sift.read_features_from_file(featlist[i])
		indx.add_to_index(imlist[i],descr)

	indx.db_commit()


	con = sqlite.connect('test.db')
	print con.execute('select count (filename) from imlist').fetchone()
	print con.execute('select * from imlist').fetchone()


	src = imagesearch.Searcher('test.db')
	locs,descr = sift.read_features_from_file(featlist[0])
	iw = voc.project(descr)

	print 'ask using a histogram...'
	print src.candidates_from_histogram(iw)[:10]

	print 'try a query...'
	print src.query(imlist[0])[:10]
