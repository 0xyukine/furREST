import methods.handling
import methods.getmethods
import structs.exceptions
import structs.profile
import structs.post
import structs.pool
import structs.set

import requests
import time
import os

class FurREST:
	def __init__(self, username, api_key):
		self.username = username
		self.api_key = api_key
		self.session = requests.Session()
		self.session.auth = (username, api_key)
		self.session.headers.update({'User-Agent':'furREST wrapper - yukine.moe'})

	def search(self, search="", page=1, post_limit=75, raw=False):
		"""
		Returns posts with optional search parameters

		Parameters
		----------
		search : str or list
			Single tag or a list of tags to be searched
		page : int, default=1
			The page of the search results to be returned
		post_limiit : int, default=75
			The number of posts to be returned per page
		raw : bool, default=False
			Whether to return as a list of class instances or the raw json return

		Returns
		-------
		posts (formatted) : list
			A list of post class instances
		posts (raw) : dict
			A list of posts in json form
		"""

		if (check_return := methods.handling.check_search(search)) != True:
			raise TypeError(f"Bad search query: {check_return}")

		if type(page) == int:
			if page < 0:
				raise ValueError("page argument must be a positive integer")
		else:
			raise TypeError("page argument is not of type int")

		if type(post_limit) == int:
			if post_limit >= 320:
				raise ValueError("Post limit exceeds 320")
			elif post_limit < 0:
				raise ValueError("Post limit must be a positive integer")
		else:
			raise TypeError("post_limit argument is not of type int")

		if not type(raw) == bool:
			raise TypeError("raw argument is not of type bool")

		if type(search) == list:
			tags = '+'.join(search)
		else:
			tags = search
		params = f"?tags={tags}&page={str(page)}&limit={post_limit}"

		listing = methods.getmethods.search_posts(self.session, params)
		if listing.status_code == 200:
			listing = listing.json()
			if raw == True:
				return listing
			elif raw == False:
				posts = []
				for post in listing["posts"]:
					posts.append(structs.post.Post(post))
				return posts
		else:
			raise structs.exceptions.HttpException(methods.handling.http_status_response(listing.status_code))

	def favorites(self, page=1, post_limit=75, raw=False):
		"""
		Returns the user's favourited posts

		Parameters
		----------
		page : int, default=1
			The page of the searh results to be returned
		post_limit : int, default=75
			The number of posts to be returned per page
		raw : bool, default=False
			Whether to return as a list of class instances or the raw json return

		Returns
		-------
		posts (formatted) : list
			A list of post class instances
		posts (raw) : dict
			A list of posts in json form
		"""

		if (check_return := methods.handling.check_search(search)) != True:
			raise TypeError(f"Bad search query: {check_return}")

		if type(page) == int:
			if page < 0:
				raise ValueError("page argument must be a positive integer")
		else:
			raise TypeError("page argument is not of type int")

		if type(post_limit) == int:
			if post_limit >= 320:
				raise ValueError("Post limit exceeds 320")
			elif post_limit < 0:
				raise ValueError("Post limit must be a positive integer")
		else:
			raise TypeError("post_limit argument is not of type int")

		if not type(raw) == bool:
			raise TypeError("raw argument is not of type bool")

		listing = methods.getmethods.search_favorites(self.session, params)
		if listing.status_code == 200:
			listing = listing.json()
			if raw == True:
				return listing
			elif raw == False:
				posts = []
				for post in listing["posts"]:
					posts.append(structs.post.Post(post))
				return posts
		else:
			raise structs.exceptions.HttpException(methods.handling.http_status_response(listing.status_code))

	def get_profile(self, user, raw=False):
		"""
		Returns the specified user's profile

		Parameters
		----------
		user : int or str
			The ID or username of the user who's profile you want to get
		raw: bool, default=False
			Whether to return the profile as a json or as profile class instance

		Returns
		-------
		profile (formatted) : profile instance
			An instance of the profile class with the relevant user information
		profile (raw) : dict
			The json returned by the request

		"""

		response = methods.getmethods.get_profile(self.session, user)
		if response.status_code == 200:
			response = response.json()
			if raw == True:
				return response
			elif raw == False:
				return structs.profile.ProfileOther(response)
		else:
			raise structs.exceptions.HttpException(methods.handling.http_status_response(response.status_code))

	def profile(self):
		"""
		Returns the profile of the connected user

		Returns
		-------
		profile : profile instance
			An instance of the profile class containing all of the user's information
		"""

		response = methods.getmethods.get_profile(self.session, self.username)
		if response.status_code == 200:
			response = response.json()
			return structs.profile.ProfileSelf(response)
		else:
			structs.exceptions.HttpException(methods.handling.http_status_response(respone.status_code))

	def get_pools(self, name="", pool_id="", desc="", creator="", creator_id="", active="", category="", order="", page=1, limit=75, raw=False):
		"""
		Returns pools with optional search parameters

		Parameters
		----------
		name : str
			Match name of pools
		pool_id : int
			Match pools with id
		desc : str
			Match pools with description
		creator : str
			Match pools by creator name
		creator : int
			Match pools by creator id
		active : bool
			Match pools by active or not
		category : {"series", "collection"}
			Match pools by their category
		order : {"name", "created_at", "updated_at", "post_count"}
			Sort pools by a specified order
		page : int, default=1
			Page of results to be returned
		limit : int, default=75
			Number of pools to be returned per search
		raw : bool, default=False
			Whether to return as a list of class instances or the raw json return

		Returns
		-------
		pools (formatted) : list
			A list of of pool class instances
		pools (raw) : dict
			A list of pools in json form
		"""

		params = "?"\
			f"search[name_matches]={name}&"\
			f"search[id]={pool_id}&"\
			f"search[description_matches]={desc}&"\
			f"search[creator_name]={creator}&"\
			f"search[creator_id]={creator_id}&"\
			f"search[is_active]={active}&"\
			f"search[category]={category}&"\
			f"search[order]={order}&"\
			f"page={page}&"\
			f"limit={limit}"

		print("Getting pools: " + params)

		if raw == True:
			return methods.getmethods.get_pools(self.session, params)
		elif raw == False:
			pools = []
			for pool in methods.getmethods.get_pools(self.session, params):
				pools.append(structs.pool.Pool(pool))
			return pools

	def get_sets(self, name="", set_id="", shortname="", creator="", creator_id="", order="", page=1, limit=75, raw=False):
		"""
		Returns sets with optional search parameters

		Parameters
		----------
		name : str
			Match name of sets
		set_id : int
			Match sets with id
		shortname : str
			Match sets by shortname
		creator : str
			Match sets by creator name
		creator : int
			Match sets by creator id
		order : {"name", "shortname" "created_at", "updated_at", "post_count"}
			Sort sets by a specified order
		page : int, default=1
			Page of results to be returned
		limit : int, default=75
			Number of sets to be returned per search
		raw : bool, default=False
			Whether to return as a list of class instances or the raw json return

		Returns
		-------
		sets (formatted) : list
			A list of of pool class instances
		sets (raw) : dict
			A list of pools in json form
		"""

		params = "?"\
			f"search[name]={name}&"\
			f"search[id]={set_id}&"\
			f"search[shortname]={shortname}&"\
			f"search[order]={order}&"\
			f"search[creator_name]={creator}&"\
			f"search[creator_id]={creator_id}&"\
			f"page={page}&"\
			f"limit={limit}"

		print("Getting sets: " + params)

		if raw == True:
			return methods.getmethods.get_sets(self.session, params)
		elif raw == False:
			sets = []
			for set in methods.getmethods.get_sets(self.session, params):
				sets.append(structs.set.Set(set))
			return sets

	def get_popular(self, date=time.gmtime(), scale="day", raw=False):
		"""
		Returns popular posts for a given date and timescale

		Parameters
		----------
		date : time.date, default=system's current date
			The date to retrieve popular posts from
		scale : {"day", "week", "month"}
			The daterange to retrieve popular posts from
		raw : bool, default=False
			Whether to return as a list of class instances or the raw json return

		Returns
		-------
		posts (formatted) : list
			A list of post class instances
		posts (raw) : dict
			A list of posts in json form
		"""

		params = f"?date={time.strftime('%Y-%m-%d',date)}&scale={scale}"

		if raw == True:
			return methods.getmethods.get_popular(self.session, params)
		elif raw == False:
			posts = []
			for post in methods.getmethods.get_popular(self.session, params)["posts"]:
				posts.append(structs.post.Post(post))
			return posts

	def save_image(self, post, path, filename):
		image = self.session.get(post.file.url).content
		os.makedirs(os.path.dirname(f"{path}/{post.file.url.split('/')[2:]}"), exist_ok=True)
		with open(f"{post.id}.{post.file.ext}", 'wb') as handler:
			handler.write(image)