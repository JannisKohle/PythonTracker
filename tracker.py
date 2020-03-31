filetotrack = ""  # type the name of the python file whose changes you want to save

###########################################################################################################################################


def read_current_version():
    global filetotrack
    return read(f"../{filetotrack}")


def read(file):
    with open(file), "r") as f:
        return f.read()

def write(file, text):
    with open(file), "w") as f:
        f.write(text)

###########################################################################################################################################

def compare_versions(v1, v2):  # compare versions and write changes to .txt file
    pass


def add_version(v):  # add the version to data
    pass


def reset_everything():  # reset everything
    pass


def get_structure(v):
    def how_many_spaces(line):
        counter=0
        for i in line:
            if i == " ":
                counter += 1
            else:
                return counter
        return counter

    def remove_method_class_stuff(s):
        output=""
        for i in s:
            if i != "(":
                output += i
            else:
                break

        output.replace("def", "method", 1)
        return output


    lines=read(f"data/{v}").split("\n")
    l=[]
    for line in lines:
        l.append((how_many_spaces(line)/4 + 1) * "-" + line[how_many_spaces(line):])

    # only classes and methods/functions
    l=[remove_method_class_stuff(item) for item in l if "class" in item or "def" in item]


# Main Part:
