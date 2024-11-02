from core.entities.note import Note
from core.repositories.note_repository import NoteRepository
from typing import List, Optional


class NoteUseCases:
    def __init__(self, repository: NoteRepository):
        self.repository = repository

    def add_note(self, title: str, content: str) -> str:
        note = Note(title, content)
        return self.repository.add(note)

    def get_all_notes(self) -> List[Note]:
        return self.repository.get_all()

    def find_note_by_title(self, title: str) -> Optional[Note]:
        return self.repository.find_by_title(title)

    def find_note_by_id(self, note_id: str) -> Optional[Note]:
        return self.repository.find_by_id(note_id)

    def update_note_content_by_title(self, title: str, new_content: str) -> int:
        return self.repository.update_content_by_title(title, new_content)

    def update_note_content_by_id(self, note_id: str, new_content: str) -> int:
        return self.repository.update_content_by_id(note_id, new_content)

    def delete_note_by_title(self, title: str) -> int:
        return self.repository.delete_by_title(title)

    def delete_note_by_id(self, note_id: str) -> int:
        return self.repository.delete_by_id(note_id)
