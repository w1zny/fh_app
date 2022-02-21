import additions
import os
from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer


def msg(filename, folder):
    print(f"file {filename} was handled to {folder} folder")

# file handler class


class SchoolFilesHandler(FileSystemEventHandler):
    def on_modified(self, event):
        for filename in os.listdir(additions.main_school_folder):
            old_destination = f"{additions.main_school_folder}/{filename}"

            for i in range(len(additions.sf)):
                if filename[0:3] == additions.sf[i]:
                    folder = additions.sf[i].upper()
                    new_path_folder = additions.path_folder + folder
                    new_destination = f"{new_path_folder}/{filename}"
                    msg(filename, folder)
                else:
                    continue
                os.rename(old_destination, new_destination)


school_files_handler = SchoolFilesHandler()
school_file_observer = Observer()

school_file_observer.schedule(
    school_files_handler, additions.main_school_folder, recursive=False)
