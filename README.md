# PythonTracker

PythonTracker is a program that keeps track of the changes you make to classes and methods in a python file.
It is very similar to git, just not for Repositories but it's optimized for python files.

## How to use it: (It is not working yet. This is just what I would like it to be.)

- install git and python if you haven't already

- Clone this Repo into your Project directory:
```cd path/to/your/projects/directory```,
```git clone https://www.github.com/JannisKohle/PythonTracker.git```

- Specify file to track: ```pytracker filename {name_of_your_python_file}```

- create the first version: ```pytracker init``` (If you do this later, it will delete all versions and start everything from the start) This will also create the text file and write the structure-view of the first version.

### Other commands:

- Save current status of file: ```pytracker save {version-name}```

- reset everything (all the older versions will be lost): ```pytracker reset yes``` <- if you type ```no```, it doesn't reset

- print current structure view of classes and methods: ```pytracker structure-view``` To get the structure-view of a specific version, do ```pytracker structure-view {version-name}```

- change the python file to older version: ```pytracker go-to {version-name}``` To go back to the latest version, do ```pytracker go-to-latest```

- print out all versions: ```pytracker history```

- combine two versions which are next to each other on a timeline: ```pytracker combine {v1-name} {v2-name} {new-name}```

### How combining works:

With combining, you can combine two versions into one version. It's important that the versions are next to each other and in the right order.

### How to see the changes:

After you run tracker.py the first time, it will automatically create a file called '{name_of_your_python_file}_changes.txt'.
In the file you can see a structured view of your classes and methods. Example:

```
- method xy1

- class xy2

- - method xy3

- - method xy4

- class xy5

- - method xy6

- - - method xy7

- - method xy8
```

As you can see, the methods xy3 and xy4 are in the class xy2, the methods xy6 and xy8 are in the class xy5
and the method xy7 is in the method xy6. So that's what you see after running tracker.py the first time.

If you run tracker.py after that, it is going to append something like this to your file:
Examples:

```created method xy1 in class xy2```, ```removed class xy3```, ```changed method xy4 in class xy5```, ...

------------------------

After you saved the status of your python file a few times, it should like similar to this example:

```
1.

- method xy0

- class xy1

- - method xy2

- - method xy3

2.

-created class xy4

-created method xy5 in class xy4

-changed method xy3 in class xy1

3.

-changed method xy5 in class xy4

-created method xy6 in class xy4

4.

-changed method xy2 in class xy1

-changed method xy6 in class xy4

-changed method xy0
```


If we print out the structure view (```pytracker structure-view```) now, we will see this:

```

- method xy0

- class xy1

- - method xy2

- - method xy3

- class xy4

- - method xy5

- - method xy6

```



## File Structure:

-your Project:

--filename.py

--filename_changes.txt

--PythonTracker:

---README.md

---tracker.py

---latest-version.json

---.git:

----.....

----.....

---versions:

----init_version.py

----changed_something.py

----another_change.py

----...

## How the program can get the changes of 2 versions (not important for users):

To get the changes of two versions, we need to do two things because there are two kinds of changes:

1. First, we have to know if there are new classes / methods, or classes / methods got removed.
   This part is easier because you don't need to look inside functions or classes. You can just
   use the structure view.

-----------------------

2. To see if changes have been made inside of methods, the structure view is not enough.
   We need to look at methods which are in both versions. Here we don't have to look at classes
   because in classes there are just methods. -> If something changed in a class, that means
   something changed in a method in the class.
