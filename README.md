# Headspin_Assignments
## How to run python the program
* To run python files you need to have python installed on your Pc.

* After installation,  check the version of python installed.
           

           python --version

           Python 3.7.3


* Run the files using command line, ie, *Teriminal* in MacOs and Linux and *Command Prompt* in Windows.

* Navigate into the the directory, in which the files are located using *cd* command. eg:
         
           cd Desktop

* Run the program using commands below. eg.

           1sudoku.py
## Numpy

Numpy is a library used specifically for advanced and faster data manipulation in Python. It allows us to effectively manage and manipulate our datasets with minimal programming. In this document, we will have a look at what are the most commonly used features of Numpy and how can we exploit them to optimize our Python programming. 
### Arrays

#### 2-D Arrays

We can create 2-D Numpy arrays as `a = np.array([[1,2,3], [4,5,6]])` and this would lead to a 2 dimensional array with 2 rows and 3 columns. 

On this object, the attribute `shape` represents the dimensions. It can be used as `a.shape` to return `(2,3)` meaning **2 rows** and **3 columns** exist in this 2D array.
## Collections
Collections in Python are containers that are used to store collections of data, for example, list, dict, set, tuple etc. These are built-in collections. Several modules have been developed that provide additional data structures to store collections of data. One such module is the Python collections module.
### Counter
A counter is a map from values to their frequencies. If you initialize a counter with a string, you get a map from each letter to the number of times it appears. If two words are anagrams, they yield equal Counters, so you can use Counters to test anagrams in linear time.
You have to import the Counter class before you can create a counter instance.

                   `from collections import Counter`
