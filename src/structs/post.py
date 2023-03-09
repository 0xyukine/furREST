class File:
	def __init__(self, file):
		self.width = file["width"]
		self.height = file["height"]
		self.ext = file["ext"]
		self.size = file["size"]
		self.md5 = file["md5"]
		self.url = file["url"]

class Tags:
	def __init__(self, tags):
		self.general = tags["general"]
		self.species = tags["species"]
		self.character = tags["character"]
		self.artist = tags["artist"]
		self.invalid = tags["invalid"]
		self.lore = tags["lore"]
		self.meta = tags["meta"]

class Flags:
	def __init__(self, flags):
		self.pending = flags["pending"]
		self.flagged = flags["flagged"]
		self.note_locked = flags["note_locked"]
		self.status_locked = flags["status_locked"]
		self.rating_locked = flags["rating_locked"]
		self.deleted = flags["deleted"]

class Preview:
	def __init__(self, preview):
		self.width = preview["width"]
		self.height = preview["height"]
		self.url = preview["url"]

class Sample:
	def __init__(self, sample):
		self.has = sample["has"]
		self.width = sample["width"]
		self.height = sample["height"]
		self.url = sample["url"]

class Score:
	def __init__(self, score):
		self.up = score["up"]
		self.down = score["down"]
		self.total = score["total"]

class Relationships:
	def __init__(self, relationships):
		self.parent_id = relationships["parent_id"]
		self.has_children = relationships["has_children"]
		self.has_active_children = relationships["has_active_children"]
		self.children = relationships["children"]

class Post:
	def __init__(self, dict):
		self.id = dict["id"]
		self.created = dict["created_at"]
		self.updated = dict["updated_at"]

		self.file = File(dict["file"])
		self.preview = Preview(dict["preview"])
		self.sample = Sample(dict["sample"])
		self.score = Score(dict["score"])
		self.tags = Tags(dict["tags"])
		self.flags = Flags(dict["flags"])
		self.relationships = Relationships(dict["relationships"])

		self.locked_tags = dict["locked_tags"]
		self.change_seq = dict["change_seq"]

		self.rating = dict["rating"]
		self.favs = dict["fav_count"]
		self.sources = dict["sources"]
		self.pools = dict["pools"]

		self.approver_id = dict["approver_id"]
		self.uploader_id = dict["uploader_id"]
		self.description = dict["description"]
		self.comment_count = dict["comment_count"]
		self.is_favourited = dict["is_favorited"]