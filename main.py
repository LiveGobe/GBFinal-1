import noteapp

def main():
    app = noteapp.NoteApp('notes.json')

    while True:
        print('1. View notes')
        print('2. Create note')
        print('3. Update note')
        print('4. Delete note')
        print('5. Quit')

        choice = input('Choose an option: ')

        if choice == '1':
            app.view_notes()
        elif choice == '2':
            title = input('Enter a title: ')
            body = input('Enter a body: ')
            app.create_note(title, body)
        elif choice == '3':
            id = input('Enter the id of the note to update: ')
            title = input('Enter a new title: ')
            body = input('Enter a new body: ')
            app.update_note(id, title, body)
        elif choice == '4':
            id = input('Enter the id of the note to delete: ')
            app.delete_note(id)
        elif choice == '5':
            break
        else:
            print('Invalid option')

if __name__ == '__main__':
    main()
