file = open("abcd.txt", "r")  # reading a file in python
print(file.read())  # printing its content

file1 = open("abcd.txt", "a") # this is to write in the file
file1.write("One more line")
file1.close()