class Note:
	def __init__(self, dict):
		self.id = dict["id"]
		self.created_at = dict["created_at"]
		self.updated_at = dict["updated_at"]
		self.creator_id = dict["creator_id"]
		self.x = dict["x"]
		self.y = dict["y"]
		self.width = dict["width"]
		self.height = dict["height"]
		self.version = dict["version"]
		self.is_active = dict["is_active"]
		self.post_id = dict["post_id"]
		self.body = dict["body"]
		self.creator_name = dict["creator_name"]