print("Hello, Python in Codespaces!")
#1)Opening a file_ex:1open a file in read mode
file=open("/workspaces/python-activity-template/.devcontainer/example1.txt","r")
print("file opened in read mode.")
file.close()
#ex:2open a file in write mode
file=open("/workspaces/python-activity-template/.devcontainer/example2.txt","w")
print("file opened in write mode.")
file.close()
#ex:3open a file in append mode
file=open("/workspaces/python-activity-template/.devcontainer/example3.txt","a")
print("file opened in append mode.")
file.close()
#2)reading from a file
#ex:1 read the entire file
file=open("/workspaces/python-activity-template/.devcontainer/example1.txt","r")
content=file.read()
print("File content:\n",content)
file.close()
#ex:2 read file line by line
file=open(".devcontainer/example1.txt","r")
for line in file:
    print("Line:",line.strip())
file.close()
#ex:3 read specific no of characters
file=open(".devcontainer/example1.txt","r")
content=file.read(3)
print("First 3 characters:",content)
file.close()
#3)Writing to a file
#ex:1write to a file in write mode
file=open("/workspaces/python-activity-template/.devcontainer/example2.txt","w")
file.write("Hello, python!\n")
file.write("Writing to a file.\n")
file.close()
#ex:2append data to a file
file=open("/workspaces/python-activity-template/.devcontainer/example3.txt","a")
file.write("Appending new data.\n")
file.close()
#ex:3overwrite existing file content
file=open("/workspaces/python-activity-template/.devcontainer/example2.txt","w")
file.write("This will overwrite the previous content.\n")
file.close()
#4)closing a file
#ex:1close a file after reading
file=open("/workspaces/python-activity-template/.devcontainer/example1.txt","r")
content=file.read()
file.close()
print("File closed after reading.")
#ex:2close a file after writing
file=open("/workspaces/python-activity-template/.devcontainer/example2.txt","w")
file.write("Closing the file after writing.\n")
file.close()
print("File closed after writing.")
#ex:3ensure file is closed using "with" statement
with open("/workspaces/python-activity-template/.devcontainer/example1.txt","r") as file:
    content=file.read()
print("File automatically closed after exiting the block")
#5)Handling errors with Try-Except
#ex:1handle file not found error
try:
    file=open("nonexistent.txt","r")
except FileNotFoundError:
    print("The file does not exist.")
#ex:2handle permission error
try:
    file=open("/root/protected.txt","r")
except PermissionError:
    print("You do not have permission to access this file.")
#ex:3general exception handling
try:
    file=open("/workspaces/python-activity-template/.devcontainer/example1.txt","r")
    content=file.read()
    file.close()
except Exception as e:
    print(f"An error occured: {e}")