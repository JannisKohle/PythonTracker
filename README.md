PythonTracker:



Description:

PythonTracker is a program that keeps track of the changes you make to classes and methods in a python file.



How to use it:

-install python if you haven't already

-install git if you haven't already

-Clone this Repo into your Project directory.
 'cd path/to/your/project/directory'
 'git clone github.com/JannisKohle/PythonTracker'

-open the file_to_track.json file in this Repo and change "name_of_your_file" to the name of your python file
 for example: 'atom PythonTracker/file_to_track' or 'nano PythonTracker/file_to_track' ...

-when you want to save the current status of your python file, you need to run the file tracker.py
 'python3 PythonTracker/tracker.py'



How to see the changes of your python file:

-after you run tracker.py the first time, it should automatically create a file called {name_of_your_file}_changes.txt
 in which you can see a structured view of the classes and methods in your python file: (example)

1.
-method xy
|-method xy
|-method xy

-class xy
|-method xy
|-method xy

-class xy
|-class xy
||-method xy
|-class xy
||-method xy
||-method xy
|-method xy
|-method xy
||-method xy
|-method xy

-when you run tracker.py again, it will add your changes to the file: (example)

2.
-added method xy to class xy
-changed method xy in class xy

3.
-removed class xy
-changed method xy in method xy
