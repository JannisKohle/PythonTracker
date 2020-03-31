Description:
\n
PythonTracker is a program that keeps track of the changes you make to classes and methods in a python file.
\n
\n
\n
How to use it:
\n
-install python if you haven't already
\n
-install git if you haven't already
\n
-Clone this Repo into your Project directory.\n
 'cd path/to/your/project/directory'\n
 'git clone github.com/JannisKohle/PythonTracker'
\n
-open the file_to_track.json file in this Repo and change "name_of_your_file" to the name of your python file\n
 for example: 'atom PythonTracker/file_to_track' or 'nano PythonTracker/file_to_track' ...
\n
-when you want to save the current status of your python file, you need to run the file tracker.py\n
 'python3 PythonTracker/tracker.py'
\n
\n
\n
How to see the changes of your python file:
\n
-after you run tracker.py the first time, it should automatically create a file called {name_of_your_file}_changes.txt
 in which you can see a structured view of the classes and methods in your python file: (example)
\n
1.
-method xy\n
|-method xy\n
|-method xy
\n
-class xy\n
|-method xy\n
|-method xy
\n
-class xy\n
|-class xy\n
||-method xy\n
|-class xy\n
||-method xy\n
||-method xy\n
|-method xy\n
|-method xy\n
||-method xy\n
|-method xy
\n
-when you run tracker.py again, it will add your changes to the file: (example)
\n
2.\n
-added method xy to class xy\n
-changed method xy in class xy
\n
3.\n
-removed class xy\n
-changed method xy in method xy
