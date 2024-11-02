from use_cases.note_use_cases import NoteUseCases
from core.entities.note import Note
from interface_adapters.mongo_note_repository import MongoNoteRepository
from frameworks.database import get_note_collection


def ui(use_cases):
    while True:
        print("\nGestión de Notas:")
        print("1. Agregar Nota")
        print("2. Ver Todas las Notas")
        print("3. Buscar Nota")
        print("4. Actualizar Nota")
        print("5. Eliminar Nota")
        print("6. Salir")
        choice = input("Selecciona una opción: ")

        if choice == "1":
            title = input("Título de la nota: ")
            content = input("Contenido de la nota: ")
            use_cases.add_note(title, content)
            print("Nota agregada exitosamente.")

        elif choice == "2":
            notes = use_cases.get_all_notes()
            for note in notes:
                print(f"ID: {note.id}, Título: {note.title}, Contenido: {note.content}")

        elif choice == "3":
            search_choice = input("¿Buscar por título (T) o ID (I)? ").strip().upper()
            if search_choice == "T":
                title = input("Título de la nota que deseas buscar: ")
                note = use_cases.find_note_by_title(title)
            elif search_choice == "I":
                note_id = input("ID de la nota que deseas buscar: ")
                note = use_cases.find_note_by_id(note_id)
            else:
                print("Opción inválida.")
                continue

            if note:
                print(f"ID: {note.id}, Título: {note.title}, Contenido: {note.content}")
            else:
                print("Nota no encontrada.")

        elif choice == "4":
            update_choice = input("¿Actualizar por título (T) o ID (I)? ").strip().upper()
            if update_choice == "T":
                title = input("Título de la nota que deseas actualizar: ")
                new_content = input("Nuevo contenido: ")
                updated_count = use_cases.update_note_content_by_title(title, new_content)
            elif update_choice == "I":
                note_id = input("ID de la nota que deseas actualizar: ")
                new_content = input("Nuevo contenido: ")
                updated_count = use_cases.update_note_content_by_id(note_id, new_content)
            else:
                print("Opción inválida.")
                continue

            print("Nota actualizada correctamente." if updated_count > 0 else "Nota no encontrada.")

        elif choice == "5":
            delete_choice = input("¿Eliminar por título (T) o ID (I)? ").strip().upper()
            if delete_choice == "T":
                title = input("Título de la nota que deseas eliminar: ")
                deleted_count = use_cases.delete_note_by_title(title)
            elif delete_choice == "I":
                note_id = input("ID de la nota que deseas eliminar: ")
                deleted_count = use_cases.delete_note_by_id(note_id)
            else:
                print("Opción inválida.")
                continue

            print("Nota eliminada exitosamente." if deleted_count > 0 else "Nota no encontrada.")

        elif choice == "6":
            print("Saliendo del programa.")
            break

        else:
            print("Opción no válida. Intenta de nuevo.")


