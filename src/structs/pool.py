class Pool:
	def __init__(self, dict):
		self.id = dict["id"]
		self.name = dict["name"]
		self.created_at = dict["created_at"]
		self.updated_at = dict["updated_at"]
		self.creator_id = dict["creator_id"]
		self.description = dict["description"]
		self.is_active = dict["is_active"]
		self.category = dict["category"]
		self.post_ids = dict["post_ids"]
		self.creator_name = dict["creator_name"]
		self.post_count = dict["post_count"]