from typing import Dict, Optional
from bson import ObjectId


class Note:
    def __init__(self, title: str, content: str, note_id: Optional[ObjectId] = None):
        self.id = note_id
        self.title = title
        self.content = content

    def to_dict(self) -> Dict:
        note_data = {
            "title": self.title,
            "content": self.content
        }
        if self.id:
            note_data["_id"] = self.id
        return note_data

    @staticmethod
    def from_dict(data: Dict):
        return Note(
            title=data["title"],
            content=data["content"],
            note_id=data.get("_id")
        )
