>**Note**: Please **fork** the current Udacity repository so that you will have a **remote** repository in **your** Github account. Clone the remote repository to your local machine. Later, as a part of the project "Post your Work on Github", you will push your proposed changes to the remote repository in your Github account.

### Date created
2023_08_07

### bikeshare.py

### Description
Imports bikeshare data from user selected city, then filters data based off user selected filters, then gives user various stats about the data. Can also display raw data 5 rows at a time.

### Files used
* bikeshare.py - Main program file
* chicago.csv - Raw bike data from Chicago
* new_york_city.csv - Raw bike data from New York City
* washington.csv - Raw bike data from New York City

### Imported Libraries
* sys --> Used for exiting the code if an error occurs
* pandas --> Used for importing data into dataframe
* time --> Used for getting time info to calcualte how long each data section takes to calculate
* dateutil.relativedelta --> Used to re-format the time stats to make it more readable (original author: Gustavo Niemeyer)

### Credits
- Used sample code from Udacity examples to help write functions
- https://stackoverflow.com/questions/60698147/how-to-drop-a-row-using-iloc-method --> Used this for how to drop a single row in a dataframe
- https://stackoverflow.com/questions/26164671/convert-seconds-to-readable-format-time --> Used this for formatting time
- https://stackoverflow.com/questions/43772362/how-to-print-a-specific-row-of-a-pandas-dataframe --> Used this for displaying specific dataframe rows

