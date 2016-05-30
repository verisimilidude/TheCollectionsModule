The Collections Module
======================


This talk is about the collections module.  It has some useful specialized
data structures which I hope in the next 10 minutes to show you.  In Python
2.7 there are only 5 objects in it. This talk covers just the five data
structure classes that are common to both.  They are the deque (the double
ended queue), the counter, the defaultdict,the OrderedDict, and the
namedtuple.   Python 3 added one new data structure, the ChainMap and a number
of objects useful for creating other derivitive data structures.  I won't be
talking about the Python 3 parts.

None of the data structures in the collections module would be hard for anyone
who has had a data structures class to create.  And if you were rolling your
own you might just use a dictionary or list and write a method or two and not
bother subclassing the base object.  The advantage in using the standard
library is that the code is tested.  You won't break on an edge case, you
won't have to debug, and your code will be immediately understood by other
Python programmers who know the standard library.

To motivate this discussion and let you guys look at some real code I am going
to used these data structures to analyze the City of Chicago Building Permits
dataset that I downloaded from the city's data portal.

Let's go to Idle and bring up the first program.  This is just going to get
the number of rows in the file.  To do the counting I used the Counter object.
This is a sort of dictionary that is specialized for holding integers
associated with a hashable object key.  So in this code I create the counter,
open the file, add one to the counter for every line read (notice that I
didn't have to initialize the counter) and finally I print the number of lines
read and end the program.  So let's run it and we see we have almost a half
million building permits in this file.

(Open analysis2.py) Let's find out a bit more about these building permits.
The data is in Character Seperated Value (CSV) format and there is another
standard library for dealing with this kind of data.  So some changes here, I
am using a with statment to open the file.  This will automatically close the
file when the block ends.  And then I pass this open file to create a
csv_reader which allows me to read in a line as a list of fields rather than
just a string.  So in addition to totalling lines I am now using the permit
type (the second element) string as a counter name and incrementing that.
Then when the file has been read I sort these permit types and print out the
result. (run it)

And we see that the most common type of permit is for electric wiring (about
1/3rd) closely followed by the easy permit which is for small projects that
don't require blueprints (about 1/4).  "Permit Type" shows up with a
single occurance because that is what is in the header for the column.  It
shows up first because it has blanks around it so sorts high.  Looks like a
nice column name though.

(bring up analysis4.py) So about that header.  We can use that along with the
namedtuple structure to get rid of the magic numbers we used to refer to the
columns in the csv file.  So we have a function here that reads a line from
the file, removes blanks around the column names and returns a list of
columns.

Now in our main routine we add a call to create a namedtuple object that we
see returns a function.  The function takes a sequence of objects and applies 
the names to the values in the call.  (a digression on the *line - building
permit expects to get its values explicitly listed.  Since the values are in a
list we put * before the list to specify that it should unpack the list.)

So now we can refer to fields.permit_type and fields.amount_paid which is much
clearer than offset numbers.  So lets run this and see how much money the city
has pulled in for each permit type. (run analysis4.py)

Looks like renovations bring in half the building permit money. Total is just
above 263 million for the ten years this data covers.  For a city with a ten 
billion dollar per year budget this is pretty small potatoes.

(bring up analysis5.py) So lets see now which contractors pull the most
permits.  We will calculate the top 10 contractors two ways.  The first way
can be expressed as a one-liner.  We will be using two additional structures
from the collections class, the defaultdict and the deque.

First let's look at the main loop.  lead_contractors is defined as a
defaultdict.  The parameter to the constructor is a function that returns an
instance of the default value.  When you pull something out of the dictionary
at a key that does not yet exist the key is created and its value is
initialized to the return from the function passed to the initializer.  In
this case when the default is 0 (which is what you get when you create an int)
we could have used another Counter.  So now we see that we create a dictionary
with each key being a contractor's name and the value being the number of
times that contractor appeared as the lead contractor.

So now lets look at the two methods for calculation of the top 10.  The first
is a one-liner. We sort all the items in the dictionary by the count and take
the first ten.

The second method utilizes a deque structure.  In this case we create the
queue with a maximum length so that when we push the eleventh element onto the
queue the other end is popped off and disappears.  Now we iterate through the
dictionary and every time we find a contractor with a count larger than the
current minimum count we push it onto the deque and change what the current
minimum is.  Finally we sort the ten that remain and return them.

Now which is faster, and by how much.  To find out I am using the timeit
module to call each calculation 1000 times and return how long it took.

Now we run it and see that the two methods returned the same results, and then
after a pause we see the times and the second method is over 4 times faster.

(Bring up analysis6.py) Now for the final data structure in collections, the
OrderedDict.  This type of dictionary remembers the order in which keys were
created and allows you to easily iterate over the keys and associated
elements.

To see why we need the OrderedDict lets try this routine without it.  I want
to see how many Building Permits were issued each year.  So first I try with a
standard dictionary,  create default values for each key and run the file.
Now see what happens:

The dictionary fields are returned in a random order.  Now we chage dict to
OrderedDict and run again.  This time when we iterate over the dictionary keys
come out in the order they went in.

So that is the five data structures in the collections module and examples of
how you use them.
(run the program once with a standard dict and one with OrderedDict) 
