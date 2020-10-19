Requirement: 
Use the RSS feed to determine which diseases have no activity for the given time frame(days).

Resources Used:
1. RSS feed of the site clinicaltrials.gov
2. Python Modules(feedparser: to extract data from the given feed, datetime: to calculate the days past, and unittest: to write test cases for the script created.)

Steps:
1. Collected and created 2 lists of all diseases on the site(a main list for all diseases, second small list for testing the script)
2. Created disease_monitor() function which takes days as in parameter.
3. Iterate the example list for getting disease name one-by-one.
4. With the string formatting, updated the RSS url on run-time.(Append days & disease name)
5. Collect the generated content in a dictionary object, and check for the number of item(s) present.
6. With a looping & conditional statement, print the title of disease where item is None.
7. Created test class to write test cases.

Thus achieving the task objective to determine which disease had no activity for a given number of days.
