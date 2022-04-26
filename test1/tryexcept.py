try:
    f = open("file.txt", "r")
    print('hello')
    a = 8 / 0
except Exception:
    print("Not Possible.")


try:
    f = open("file.txt", "r")
except FileNotFoundError:
    print('File Not Found')
finally:  # executes regardless the exception has been handled or not
    print("All exceptions have been handled.")