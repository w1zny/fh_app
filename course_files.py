import additions
import os
from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer


def msg(filename, folder):
    print(f"file {filename} was handled to {folder} folder")

# file handler class


class CoursesFilesHandler(FileSystemEventHandler):
    def on_modified(self, event):
        for filename in os.listdir(additions.main_courses_folder):
            old_destination = f"{additions.main_courses_folder}/{filename}"
            folder = "courses"
            if filename.endswith(".mp4"):
                new_destination = f"{additions.courses_folder}/{filename}"
                msg(filename, folder)
            else:
                continue
            os.rename(old_destination, new_destination)


courses_files_handler = CoursesFilesHandler()
course_file_observer = Observer()

course_file_observer.schedule(
    courses_files_handler, additions.main_courses_folder, recursive=False)
