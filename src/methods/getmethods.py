import requests

def search_posts(session, search, page, post_limit):
	return session.get("https://e621.net/posts.json?page={}&tags={}&limit={}".format(page, search, post_limit)).json()

def search_favorites(session):
	return session.get("https://e621.net/favorites.json").json()