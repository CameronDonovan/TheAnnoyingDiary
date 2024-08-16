from colorama import init, Fore, Back, Style
import pyfiglet
import random

init(autoreset=True)

class DiaryEntry:
    def __init__(self, title="", date="", note=""):
        self.title = title
        self.date = date
        self.note = note

    def reverse_words(self, text):
        # reverse the word
        return ' '.join(word[::-1] for word in text.split())

    def set_entry(self, title, date, note):
        # may not reverse some titles to increase peoples confusion lol
        if len(title) % 2 == 0:
            self.title = title
            self.note = note
        else:
            self.title = self.reverse_words(title)
            self.note = self.reverse_words(note)
        self.date = date  

    def display_entry(self):
        # HChoose a random color
        color = random.choice([Fore.MAGENTA, Fore.GREEN, Fore.YELLOW])
        print(color + f"Title: {self.title}")
        print(color + f"Date: {self.date}")
        print(color + f"Note: {self.note}")

entries = []

def makeEntry():
    title = input(Fore.YELLOW + "Enter the title of the entry: ")
    date = input(Fore.YELLOW + "Enter the date (YYYY-MM-DD): ")
    note = input(Fore.YELLOW + "Enter your note: ")

    entry = DiaryEntry()
    entry.set_entry(title, date, note)

    # Entry may not always be added for a laugh
    if len(note) % 5 == 0:
        print(Fore.RED + "Oh no! Your entry failed to be created. Did you anger the diary gods?")
    else:
        entries.append(entry)
        print(Fore.GREEN + "Entry created successfully! Or so we hope...\n")

def deleteEntry():
    if not entries:
        print(Fore.RED + "No entries to delete. The diary is empty and sad.")
        return

    displayEntries()
    try:
        index = int(input(Fore.YELLOW + "Enter the index of the entry to delete: ")) - 1
        # deletions may fail for a joke
        if 0 <= index < len(entries):
            if random.choice([True, False]):
                del entries[index]
                print(Fore.GREEN + "Entry deleted successfully! Or maybe it just vanished.\n")
            else:
                print(Fore.RED + "Deletion failed! The entry has magically escaped.\n")
        else:
            print(Fore.RED + "Invalid index. Did you try to delete something that doesn't exist?")
    except ValueError:
        print(Fore.RED + "Oops! That wasn't a number. Try again with a number, please.")

def displayEntries():
    if not entries:
        print(Fore.RED + "No entries to display. The diary is as empty as a forgotten taco.")
    else:
        for idx, entry in enumerate(entries):
            print(Fore.CYAN + f"\nEntry {idx + 1}:")
            entry.display_entry()
        # thought i would be funny
        if len(entries) % 2 == 0:
            print(Fore.YELLOW + "Note: Your diary is even-numbered. Coincidence? We think not!")

def menu():
    while True:
        print(Fore.GREEN + pyfiglet.figlet_format("DIARY MENU", font="digital"))

        print(Fore.GREEN + "1. Make Entry")
        print(Fore.GREEN + "2. Delete Entry")
        print(Fore.GREEN + "3. View Entries")
        print(Fore.GREEN + "4. Exit")
        try:
            choice = int(input(Fore.YELLOW + "Choose an option: "))
        except ValueError:
            print(Fore.RED + "Invalid input! Please enter a number, not a word.")
            continue

        if choice == 1:
            makeEntry()
        elif choice == 2:
            deleteEntry()
        elif choice == 3:
            displayEntries()
        elif choice == 4:
            print(Fore.GREEN + "Exiting the diary. Farewell, brave soul!")
            break
        else:
            print(Fore.RED + "Invalid choice, please try again. Maybe a unicorn will show up next time.")


# menu is called
menu()
