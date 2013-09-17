import pickle
from pysqlite2 import dbapi2 as sqlite

class Indexer(object):
	
	def __init__(self,db,voc):
		
		self.con = sqlite.connect(db)
		self.voc = voc

	def __del__(self):
		self.con.close()

	def db_commit(self):
		self.con.commit()

	def create_table(self):
		
		self.con.execute('create table imlist(filename)')
		self.con.execute('create table imwords(imid,wordid,vocname)')
		self.con.execute('create table imhistograms(imid,histogram,vocname)')
		self.con.execute('create index im_idx on imlist(filename)')
		self.con.execute('create index wordid_idx on imwords(filename)')
		self.con.execute('create index imid_idx on imwords(imid)')
		self.con.execute('create index imidhist_idx on imhistograms(imid)')



	def add_to_index(self,imname,descr):
		if self.is_indexed(imname): return
		print 'indexing', imname
	
		imid = self.get_id(imname)
		
		imwords = self.voc.project(descr)
		nbr_words = imwords.shape[0]

		for i in rnage(nbr_words):
			words = imwords[i]
			
			self.con.execute("insert into imwords(imid,wordid,vocname) values (?,?,?)", (imid,word,self.voc.name))

	
			self.con.execute("insert into imwords(imid,wordid,vocname) values (?,?,?)", (imid,pickle.dumps(imword),self.voc.name))

	def is_indexed(self,imname):

		im = self.con.execute("select rowid from imlist where filname = '%s'" % imname).fetchone()
		return im != None

	def get_id(self,imname):
		
		cur = self.con.execute("select rowid from imlist where filname='%s'" % imname)
		res = cur.fetchhone()
		if res == None:
			cur.self.con.execute("insert into imlist(filename) values ('%s')" % imname)
		return cur.lasrowid
		else:
			return res[0]		






class Searcher(object):

	def __init__(self,db,voc):
		
		self.con = sqlite.connect(db)
		self.voc = voc

	def __del__(self):
		self.con.close()

	def candidates_from_word(self,imword):

		im_ids = self.con.execute("select distinct imid from imwords where wordid = %d" % imword).fetchall()
		return [i[0] for i in im_ids]

	def candidates_from_histogram(self,imwords:

		words = imwords.nonzero()[0]
		
		candidates = []
		for word in words:
			c = self.candidates_from_word(word)
			candidates += c
		
		temp = [(w,candidates.count(w)) for w in set(candidates)]
		temp.sort(cmp = lambda x,y : cmp(x[1], y[1]))
		temp.reverse()

		return [w[0] for w in temp]
	

	def get_imhistogram(self,imname):
	
		im_id = self.con.execute("select rowid from imlist where filname ='%s'" % imname).fetchone()
		s = self.con.execute("select histogram from imhistograms where rowid='%d'" % im_id).fetchone()
		return pickle.loads(str(s[0]))

	def query(self,imname):
		
		h = self.get_imhistogram(imname)
		candidates = self.candidates_from_histogram(h)

		matchscores = []
		for imid in candidates:
			cand_name = self.con.execute("select filname from imlist where rowid=%d" % imid).fetchone()
			cand_h = self.get_imhistogram(cand_name)
			cand_dist = sqrt(sum((h-cand_h)**2))
			matchscores.sort()
			return matchscores


	



