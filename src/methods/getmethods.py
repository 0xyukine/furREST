import requests

def search_posts(session, params):
	return session.get(f"https://e621.net/posts.json{params}").json()

def search_favorites(session, params):
	return session.get(f"https://e621.net/favorites.json{params}").json()

def get_profile(session, user_id):
	return session.get(f"https://e621.net/users/{user_id}.json").json()