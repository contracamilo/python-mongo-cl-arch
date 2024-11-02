import os
from dotenv import load_dotenv
from frameworks.database import get_note_collection
from interface_adapters.mongo_note_repository import MongoNoteRepository
from use_cases.note_use_cases import NoteUseCases
from frameworks.cli import ui


def initialize_environment():
    load_dotenv()
    mongo_collection = get_note_collection()
    repository = MongoNoteRepository(mongo_collection)
    note_use_cases = NoteUseCases(repository)
    return note_use_cases


if __name__ == "__main__":
    use_cases = initialize_environment()
    ui(use_cases)
