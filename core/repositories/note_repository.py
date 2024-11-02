from abc import ABC, abstractmethod
from core.entities.note import Note
from typing import List, Optional


class NoteRepository(ABC):
    @abstractmethod
    def add(self, note: Note) -> str:
        pass

    @abstractmethod
    def get_all(self) -> List[Note]:
        pass

    @abstractmethod
    def find_by_title(self, title: str) -> Optional[Note]:
        pass

    @abstractmethod
    def find_by_id(self, note_id: str) -> Optional[Note]:
        pass

    @abstractmethod
    def update_content_by_title(self, title: str, new_content: str) -> int:
        pass

    @abstractmethod
    def update_content_by_id(self, note_id: str, new_content: str) -> int:
        pass

    @abstractmethod
    def delete_by_title(self, title: str) -> int:
        pass

    @abstractmethod
    def delete_by_id(self, note_id: str) -> int:
        pass
