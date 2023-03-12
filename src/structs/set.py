class Set:
	def __init__(self, dict):
		self.id = dict["id"]
		self.created_at = dict["created_at"]
		self.updated_at = dict["updated_at"]
		self.creator_id = dict["creator_id"]
		self.is_public = dict["is_public"]
		self.name = dict["name"]
		self.shortname = dict["shortname"]
		self.description = dict["description"]
		self.post_count = dict["post_count"]
		self.transfer_on_delete = dict["transfer_on_delete"]
		self.post_ids = dict["post_ids"]