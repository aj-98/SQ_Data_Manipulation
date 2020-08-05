DO NOT ALTER THIS SCRIPT IN ANY WAY.

PURPOSE:
xlsplit.py is a Python script to manipulate raw canvassing results. It specifically moves the column
"VAN ID" to its correct position(the first column) and splits the data into two separate csv files based on if the
attempt to contact the voter was successful or not.


REQUIREMENTS BEFORE RUNNING:
Before running this script, the FOLLOWING REQUIREMENTS MUST BE MET:
1) Python 3 must be installed on the computer that is running this script. It can be downloaded via www.python.org
2) Open your command prompt (CMD on Windows, Linux on Mac). Clone these files by entering this command: git clone https://github.com/aj-98/SQ_Data_Manipulation
3) Run this command: cd SQ_Data_Manipulation
4) Run this command: pip3 install -r requirements.txt
5) Run this command: python xlsplit.py


USER INPUT:
Once the script has been run, the user will be asked to:
1) Select the excel or csv file that they want to manipulate
2) Enter the FULL PATH to an existing folder that is already on their computer. The path must end with a /  .An example of what the user's input can look like: C:/Path/To/Existing/Folder/
3) Enter the date that the data was collected using the month's abbreviation(all lowercase), the two digit date, and the last two digits of the
year. Example: If this data was collected on July 25, 2020, the user should enter jul2520 .If collected on July 07, 2020, the user should enter jul0720
4) The resulting excel files will be added to the directory you're in. type this command to view them: dir 






