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

	def search(self, search="", page=1, post_limit=75, raw=False):	
		tags = '+'.join(search)
		params = f"?tags={tags}&page={str(page)}&limit={post_limit}"
		if raw == True:
			return methods.getmethods.search_posts(self.session, params)
		elif raw == False:
			posts = []
			for post in methods.getmethods.search_posts(self.session, params)["posts"]:
				posts.append(structs.post.Post(post))
			return posts

	def favorites(self, page=1, post_limit=75, raw=False):
		params = f"?page={str(page)}&limit={post_limit}"
		if raw == True:
			return methods.getmethods.search_favorites(self.session, params)
		elif raw == False:
			posts = []
			for post in methods.getmethods.search_favorites(self.session, params)["posts"]:
				posts.append(structs.post.Post(post))
			return posts

	def get_profile(self, user, raw=False):
		if raw == True:
			return methods.getmethods.get_profile(self.session, user)
		elif raw == False:
			return structs.profile.ProfileOther(methods.getmethods.get_profile(self.session, user))

	def profile(self):
		return structs.profile.ProfileSelf(methods.getmethods.get_profile(self.session, self.username))