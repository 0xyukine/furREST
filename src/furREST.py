import requests
import methods.getmethods
import structs.post
import structs.profile

class FurREST:
	def __init__(self, username, api_key):
		self.username = username
		self.api_key = api_key
		self.session = requests.Session()
		self.session.auth = (username, api_key)
		self.session.headers.update({'User-Agent':'furREST wrapper - yukine.moe'})

	def search_raw(self, search, page_limit, post_limit):
		return methods.getmethods.search_posts(self.session, search, page_limit, post_limit)

	def search(self, search, page_limit, post_limit):
		posts = []
		for post in methods.getmethods.search_posts(self.session, search, page_limit, post_limit)["posts"]:
			posts.append(structs.post.Post(post))
		return posts

	def favorites_raw(self):
		return methods.getmethods.search_favorites(self.session)

	def favorites(self):
		posts = []
		for post in methods.getmethods.search_favorites(self.session)["posts"]:
			posts.append(structs.post.Post(post))
		return posts

	def get_profile_raw(self, user):
		return methods.getmethods.get_profile(self.session, user)

	def get_profile(self, user):
		return structs.profile.ProfileOther(methods.getmethods.get_profile(self.session, user))

	def profile(self):
		return structs.profile.ProfileSelf(methods.getmethods.get_profile(self.session, self.username))