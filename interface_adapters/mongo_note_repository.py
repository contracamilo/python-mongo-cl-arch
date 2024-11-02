from bson import ObjectId
from core.entities.note import Note
from core.repositories.note_repository import NoteRepository
from pymongo.collection import Collection
from typing import List, Optional


class MongoNoteRepository(NoteRepository):
    def __init__(self, collection: Collection):
        self.collection = collection

    def add(self, note: Note) -> str:
        result = self.collection.insert_one(note.to_dict())
        return str(result.inserted_id)

    def get_all(self) -> List[Note]:
        notes = self.collection.find()
        return [Note.from_dict(note) for note in notes]

    def find_by_title(self, title: str) -> Optional[Note]:
        note_data = self.collection.find_one({"title": title})
        if note_data:
            return Note.from_dict(note_data)
        return None

    def find_by_id(self, note_id: str) -> Optional[Note]:
        note_data = self.collection.find_one({"_id": ObjectId(note_id)})
        if note_data:
            return Note.from_dict(note_data)
        return None

    def update_content_by_title(self, title: str, new_content: str) -> int:
        result = self.collection.update_one(
            {"title": title},
            {"$set": {"content": new_content}}
        )
        return result.modified_count

    def update_content_by_id(self, note_id: str, new_content: str) -> int:
        result = self.collection.update_one(
            {"_id": ObjectId(note_id)},
            {"$set": {"content": new_content}}
        )
        return result.modified_count

    def delete_by_title(self, title: str) -> int:
        result = self.collection.delete_one({"title": title})
        return result.deleted_count

    def delete_by_id(self, note_id: str) -> int:
        result = self.collection.delete_one({"_id": ObjectId(note_id)})
        return result.deleted_count
