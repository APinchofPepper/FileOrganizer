import os
import importlib
from utils.logger import setup_logging

def list_organizers():
    organizer_dir = os.path.join(os.path.dirname(__file__), 'organizers')
    return [f[:-3] for f in os.listdir(organizer_dir) if f.endswith('.py') and f != '__init__.py']

def main():
    setup_logging()
    print("Welcome to the File Organizer!")
    
    organizers = list_organizers()
    print("\nAvailable organization methods:")
    for idx, organizer in enumerate(organizers, 1):
        print(f"{idx}. {organizer.replace('_', ' ').title()}")

    choice = input("\nChoose an organizer by number: ").strip()
    if not choice.isdigit() or int(choice) < 1 or int(choice) > len(organizers):
        print("Invalid choice. Exiting.")
        return

    selected_organizer = organizers[int(choice) - 1]
    module = importlib.import_module(f'organizers.{selected_organizer}')

    target_directory = input("\nEnter the directory to organize: ").strip()
    if not os.path.exists(target_directory):
        print("Invalid directory. Exiting.")
        return

    print(f"\nRunning organizer: {selected_organizer.replace('_', ' ').title()}")
    module.run(target_directory)

if __name__ == "__main__":
    main()
