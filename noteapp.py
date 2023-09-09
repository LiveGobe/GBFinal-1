import json
import datetime

class Note:
    def __init__(self, id, title, body):
        self.id = id
        self.title = title
        self.body = body
        self.created_at = datetime.datetime.now().isoformat()
        self.updated_at = self.created_at

    def update(self, title, body):
        self.title = title
        self.body = body
        self.updated_at = datetime.datetime.now().isoformat()

    def to_dict(self):
        return self.__dict__

class NoteApp:
    def __init__(self, filename):
        self.filename = filename
        self.notes = self.load_notes()

    def load_notes(self):
        try:
            with open(self.filename, 'r') as f:
                notes_dict = json.load(f)
            return {id: Note(id, note_dict['title'], note_dict['body']) for id, note_dict in notes_dict.items()}
        except FileNotFoundError:
            return {}

    def save_notes(self):
        with open(self.filename, 'w') as f:
            json.dump({id: note.to_dict() for id, note in self.notes.items()}, f)

    def create_note(self, title, body):
        id = str(len(self.notes) + 1)
        self.notes[id] = Note(id, title, body)
        self.save_notes()

    def update_note(self, id, title, body):
        if id in self.notes:
            self.notes[id].update(title, body)
            self.save_notes()
        else:
            print(f'Note with id {id} not found.')

    def delete_note(self, id):
        if id in self.notes:
            del self.notes[id]
            self.save_notes()
        else:
            print(f'Note with id {id} not found.')

    def view_notes(self):
        for id, note in self.notes.items():
            print(f'ID: {id}\nTitle: {note.title}\nBody: {note.body}\nCreated at: {note.created_at}\nUpdated at: {note.updated_at}\n---')
