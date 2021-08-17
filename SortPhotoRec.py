#!/usr/bin/python3
'''this program was originally designed to sort photorec recovered file however,
it will now sort anything that you throw at it.
Note this program will create a duplicate of all the files make sure you have
Enough space to do this. This part is on you not the program.
This program is filed under the IDC (I don't care) License.'''
import os
import shutil
import sys

__version__ = "4.1"


# This will make a destination directory if it does not exist
def check_dest(path):
    if os.path.isdir(dest_file):
        print("There is a valid destination directory")
    elif not os.path.isdir(dest_file):
        print("Could not find directory. Creating one.")
        os.mkdir(dest_file)
    else:
        print("Dont know how you got here")


# This will check the size and return it
def check_size(path):
    # I feel bad for using duplicate code ill fix this later
    files_in_source_dir = os.listdir(path)
    global total_size
    global filePathList
    for file_in_source_dir in files_in_source_dir:
        new_path = os.path.join(path, file_in_source_dir)
        if os.path.isdir(new_path):
            check_size(new_path)
        else:
            total_size = total_size + os.path.getsize(new_path)
            filePathList.append(new_path)


def get_human_read(size):
    suffixes = ['B', 'KB', 'MB', 'GB', 'TB']
    suffixIndex = 0
    while size > 1024 and suffixIndex < 4:
        suffixIndex += 1  # increment the index of the suffix
        size = size / 1024.0  # apply the division
    return "%.2f%s" % (size, suffixes[suffixIndex])


# This is the iterative function that goes through the list of files
def progressor():
    global filePathList
    for file_in_source_dir in filePathList:
        # if the file_extension does not exsit it creals a null value
        filename, file_extension = os.path.splitext(file_in_source_dir)
        # handles the null value
        if file_extension == '':
            file_extension = "extensionNotFound"
        elif file_extension[0] == '.':
            file_extension = file_extension.lstrip('.')
        if os.path.isdir(os.path.join(dest_file, file_extension)):
            shutil.copy(file_in_source_dir, os.path.join(dest_file, file_extension))
        # handles if there is no directory to sort into
        else:
            os.mkdir(os.path.join(dest_file, file_extension))
            shutil.copy(file_in_source_dir, os.path.join(dest_file, file_extension))
        update_size(file_in_source_dir)


# displays how much more the program has left to go
def update_size(path):
    size = os.path.getsize(path)
    global done_size
    done_size += size
    remaining = (done_size / total_size) * 100
    print("\r", "%.2f" % remaining, "% done", end="")


# main method
def main():
    global filePathList
    check_dest(dest_file)
    check_size(source_file)
    print("The file size is: ", get_human_read(total_size),
          "do you want to continue? (y/N)")
    cont = input()
    if cont is not "y":
        sys.exit()
    progressor()

# main function I'm used to this type of programming
if __name__ == "__main__":
    source_file = input("Enter the source file full path ending with /: ")
    dest_file = input("Enter the destination file fill path ending with /: ")
    total_size = 0
    done_size = 0
    filePathList = []
    main()

