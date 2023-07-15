f = open("test.txt", "w")
f.write("Woops! I have deleted the content!")
f.close()

# Open and read the file after the overwriting.
f = open("test.txt", "r")
print(f.read())
