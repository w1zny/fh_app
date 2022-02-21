import time
import school_files as sf
import course_files as cf

cf.course_file_observer.start()
sf.chool_file_observer.start()


try:
    print("HANDLING")
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print("\n\nDONE\n")
    sf.school_file_observer.stop()
    cf.course_file_observer.stop()
sf.school_file_observer.join()
cf.course_file_observer.join()
