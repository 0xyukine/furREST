import requests

BASE_URL = "https://e621.net"

def search_posts(session, params):
	return session.get(f"{BASE_URL}/posts.json{params}")

def search_favorites(session, params):
	return session.get(f"{BASE_URL}/favorites.json{params}").json()

def get_profile(session, user_id):
	return session.get(f"{BASE_URL}/{user_id}.json").json()

def get_popular(session, params):
	return session.get(f"{BASE_URL}/popular.json{params}").json()

def get_pools(session, params):
	return session.get(f"{BASE_URL}/pools.json{params}").json()

def get_pool(session, pool_id):
	return session.get(f"{BASE_URL}/pools/{pool_id}.json").json()

def get_sets(session, params):
	return session.get(f"{BASE_URL}/post_sets.json{params}").json()

def get_set(session, set_id):
	return session.get(f"{BASE_URL}/post_sets/{set_id}.json").json()