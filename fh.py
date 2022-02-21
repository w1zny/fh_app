import time
import school_files as sf
import course_files as cf

observers = [cf.course_file_observer, sf.school_file_observer]

for observer in observers:
    observer.start()


try:
    print("HANDLING")
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print("\n\nDONE\n")
    for observer in observers:
        observer.stop()
for observer in observers:
    observer.join()
