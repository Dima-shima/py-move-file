import os


def move_file(command: str) -> None:
    string = list(command.split())
    if len(string) == 3:
        command_from_string = string[0]
        file_in = string[1]
        file_out = string[2]
    if "/" not in file_out:
        os.rename(file_in, file_out)
    if "/" in file_out:
        path = ""
        while "/" in file_out:
            new_directory = file_out[0:(file_out.find("/"))]
            new_directory = path + new_directory
            if not os.path.isdir(new_directory):
                os.mkdir(new_directory)
            path = new_directory + "/"
            file_out = file_out[(file_out.find("/"))+1:]
        with open(file_in, "r") as file1, \
                open(path + file_out, "w") as file2:
            content = (file1.read())
            file2.write(content)
        os.remove(file_in)
