import os
import json

# 'pytracker_test.py is outside of this directroy, so you can't see it in the Repo.
filetotrack = "pytracker_test.py"

###########################################################################################################################################


def read(file):
    with open(file, "r") as f:
        return f.read()


def write(file, text):
    with open(file, "w") as f:
        f.write(text)


def get_latest_version():
    with open("latest_version.json", "r") as f:
        return json.load(f)["latest_version"]


def create_everything():
    global filetotrack

    if "versions" not in os.listdir():
        os.system("mkdir versions")

    if f"{filetotrack}_changes.txt" not in os.listdir():
        os.system(f"touch {filetotrack}_changes.txt")

###########################################################################################################################################


def compare_versions(v1, v2):  # compare versions and write changes to .txt file
    pass


def init():
    global filetotrack
    os.system(f"cp ../{filetotrack} versions/init_version.py")

    with open("latest_version.json", "w") as f:
        json.dump({"latest_version": "init_version.py"}, f)


def add_version(vname):  # add the version to versions
    global filetotrack

    # if latest version == current version
    if read(f"versions/{get_latest_version()}") != read(f"../{filetotrack}"):
        os.system(f"cp ../{filetotrack} versions/{vname}.py")

        with open("latest_version.json", "w") as f:
            towrite = {"latest_version": vname+".py"}
            json.dump(towrite, f)
    else:
        return "No changes to save"


def reset_everything():  # reset everything
    os.system("rm -rf versions")


def get_structure(vname):
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
