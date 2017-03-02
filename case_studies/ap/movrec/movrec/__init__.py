import pickle
import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

# Local Imports
from conf import *

class Movrec():
	def __init__(self, only_ids=False):
		# Movie info files
		if only_ids:
			self.mif = None
		else:
			self.mif = pd.read_csv(INFO_PATH, sep='|', names=MIFNAMES)

		# Ratings file
		self.mra = pd.read_csv(RATINGS_PATH, sep='\t', names=MRANAMES)
		self.ratings = None

		self.meta(only_ids)

	def save(self):
	    with open(UIX_PATH, 'wb') as file_pointer:
	        pickle.dump(self.user_similarity, file_pointer)
	    with open(MIX_PATH, 'wb') as file_pointer:
	        pickle.dump(self.item_similarity, file_pointer)

	def load(self):
	    with open(UIX_PATH, 'rb') as file_pointer:
	    	self.user_similarity = pickle.load(file_pointer)
	    with open(MIX_PATH, 'rb') as file_pointer:
	    	self.item_similarity = pickle.load(file_pointer)

	def meta(self, only_ids=False):
		self.n_users = self.mra.user_id.unique().shape[0]
		self.n_movies = self.mra.movie_id.unique().shape[0]

		if self.ratings is None:
			# self.ratings = np.zeros((self.n_users, self.n_movies))
			self.ratings = np.zeros((self.n_movies, self.n_users))
			self.populate()

		if not only_ids:
			self.sparsity = float(len(self.ratings.nonzero()[0]))
			self.sparsity /= (self.ratings.shape[0] * self.ratings.shape[1])
			self.sparsity *= 100

			print str(self.n_users) + ' users'
			print str(self.n_movies) + ' movies'
			print 'Sparsity: {:4.2f}%'.format(self.sparsity)

	def populate(self):
		for row in self.mra.itertuples():
		    # self.ratings[row[1]-1, row[2]-1] = row[3]
		    self.ratings[row[2]-1, row[1]-1] = row[3]

	def learn(self):
		# To calculate similarity cosine matrix
		user_cos = cosine_similarity(self.ratings)
		movie_cos = cosine_similarity(self.ratings.T)

		# To fill in the mising values
		self.user_similarity = user_cos.dot(self.ratings) / np.array([np.abs(user_cos).sum(axis=1)]).T
		self.item_similarity = self.ratings.dot(movie_cos) / np.array([np.abs(movie_cos).sum(axis=1)])

	def similar_movies(self, movie_id, k=6):
		movies = np.argsort(self.item_similarity[movie_id,:])[:-k-1:-1]
		movies = self.get_names(movies)
		return movies

	def similar_movies_via_user_behaviour(self, movie_id, k=6):
		movies = np.argsort(self.user_similarity[movie_id,:])[:-k-1:-1]
		movies = self.get_names(movies)
		return movies

	def movie_name(self, movie_id):
		if self.mif is None:
			return movie_id
		else:
			return str(self.mif.id[movie_id])

	def get_names(self, arr):
		for a in arr:
			print self.movie_name(a+1)

	def movies(self):
		if self.mif is None:
			print "No movies loaded"
		else:
			for row in self.mif.itertuples():
				print 'ID: ' + str(row[0][0]) + ', NAME: ' + str(row[0][1])
