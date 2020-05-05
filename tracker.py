import os

# 'pytracker_test.py is outside of this directroy, so you can't see it in the Repo.
filetotrack = "pytracker_test.py"  # type the name of the python file whose changes you want to save

###########################################################################################################################################


def read(file):
    with open(file, "r") as f:
        return f.read()


def write(file, text):
    with open(file, "w") as f:
        f.write(text)


def create_everything():
    global filetotrack

    if "versions" not in os.listdir():
        os.system("mkdir versions")

    if f"{filetotrack}_changes.txt" not in os.listdir():
        os.system(f"touch {filetotrack}_changes.txt")

###########################################################################################################################################


def compare_versions(v1, v2):  # compare versions and write changes to .txt file
    pass


def add_version():  # add the version to versions
    global filetotrack
    version_num = len(os.listdir("versions")) + 1
    os.system(f"cp ../{filetotrack} versions/v{version_num}.py")


def reset_everything():  # reset everything
    os.system("rm -rf versions")


def get_structure(v):
    def how_many_spaces(line):
        counter = 0
        for i in line:
            if i == " ":
                counter += 1
            else:
                return counter
        return counter

    def remove_method_class_stuff(s):
        output = ""
        for i in s:
            if i != "(":
                output += i
            else:
                break

        output = output.replace("def", "method", 2)
        return output

    lines = read(f"versions/{v}").split("\n")
    l = []
    for line in lines:
        l.append((int(how_many_spaces(line)/4 + 1))*"- " + line[how_many_spaces(line):])

    # only classes and methods/functions
    l = [remove_method_class_stuff(item) for item in l if "class" in item or "def" in item]

    return l
