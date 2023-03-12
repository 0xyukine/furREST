import requests
import methods.getmethods
import structs.post
import structs.profile
import structs.pool
import structs.set

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

	def get_pools(self, name="", pool_id="", desc="", creator="", creator_id="", active="", category="", order="", limit=75, raw=False):
		params = "?"\
			f"search[name_matches]={name}&"\
			f"search[id]={pool_id}&"\
			f"search[description_matches]={desc}&"\
			f"search[creator_name]={creator}&"\
			f"search[creator_id]={creator_id}&"\
			f"search[is_active]={active}&"\
			f"search[category]={category}&"\
			f"search[order]={order}&"\
			f"limit={limit}"

		print(params)

		if raw == True:
			return methods.getmethods.get_pools(self.session, params)
		elif raw == False:
			pools = []
			for pool in methods.getmethods.get_pools(self.session, params):
				pools.append(structs.pool.Pool(pool))
			return pools