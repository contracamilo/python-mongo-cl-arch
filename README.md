# Note Management System

A simple, modularized note management application built using Python and MongoDB. This project follows the **Clean Architecture** pattern, making it easy to scale and maintain. Users can add, view, search, update, and delete notes by either title or unique ID.

## Features

- **Add Notes**: Create new notes with a title and content.
- **View All Notes**: Retrieve and display all notes.
- **Search Notes**: Search for notes by title or ID.
- **Update Notes**: Update the content of an existing note by title or ID.
- **Delete Notes**: Remove notes from the database by title or ID.

## Project Structure

The project is structured based on **Clean Architecture** principles, separating different layers of the application for better scalability and maintainability.
   ```bash
   note_manager/
   ├── .venv/                         # Virtual environment
   ├── core/
   │   ├── __init__.py
   │   ├── entities/
   │   │   ├── __init__.py
   │   │   └── note.py                # Note model
   │   └── repositories/
   │       ├── __init__.py
   │       └── note_repository.py     # Repository interface for notes
   ├── use_cases/
   │   ├── __init__.py
   │   └── note_use_cases.py          # Business logic and use cases (CRUD)
   ├── interface_adapters/
   │   ├── __init__.py
   │   └── mongo_note_repository.py   # MongoDB repository implementation for notes
   ├── frameworks/
   │   ├── __init__.py
   │   ├── database.py                # MongoDB configuration and connection
   │   └── cli.py                     # Command-line interface (CLI)
   ├── main.py                        # Entry point for the application
   └── requirements.txt               # Python dependencies
   ```

## Requirements

- Python 3.9 or higher
- MongoDB server running locally or remotely
- `python-dotenv` for environment variable management
- `pymongo` for MongoDB interaction

## Setup Instructions

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/note-manager.git
   cd note-manager


2. **Create a Virtual Environment**:
    ```bash
    python3 -m venv .venv
    source .venv/bin/activate


3. **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    Configure Environment Variables:

4. **Create a .env file in the project root with the following content**:
    ```plaintext
    MONGO_URI=<your-connection-string>
    DATABASE_NAME=<your-db-name>

5. **Run the Application**:
    ```bash
    python main.py

## Usage
The application provides a command-line interface with the following options:

Gestión de Notas:
1. Agregar Nota
2. Ver Todas las Notas
3. Buscar Nota
4. Actualizar Nota
5. Eliminar Nota
6. Salir
   Selecciona una opción: 


