DO NOT ALTER THIS SCRIPT IN ANY WAY.
PURPOSE:
xlsplit.py is a Python script to manipulate raw canvassing results. It specifically moves the column
"VAN ID" to its correct position(the first column) and splits the data into two separate csv files based on if the
attempt to contact the voter was successful or not.


REQUIREMENTS BEFORE RUNNING:
Before running this script, the FOLLOWING REQUIREMENTS MUST BE MET:
1) Python 3 must be installed on the computer that is running this script. It can be downloaded via www.python.org
2) Open your command prompt (CMD on Windows, Linux on Mac). Clone these files by entering this command: git clone https://github.com/aj-98/SQ_Data_Manipulation
3) Enter this command: cd SQ_Data_Manipulation
4) Run this command: pip install -r requirements.txt OR
pip3 install -r requirements.txt  .If you are operating in Linux(Mac), enter: sudo 

HOW TO RUN:
This script may be run using a Python IDE, such as PyCharm, or through the command line (Command Prompt on Windows,
Linux on Mac). If running through the command line, start the script using the following command: python xlsplit.py

USER INPUT:
Once the script has been run, the user will be asked to:
1) Select the file that holds the data they want to manipulate. The file can be an excel file or a csv file.
2) Enter the FULL PATH to an existing folder that is already on your computer.
The path must end with a /    An example of what the user's input can look like: C:/Path/To/Existing/Folder/
3) Enter the date that the data was collected using the month abbreviation(lowercase), the date, and the last two digits of the
year. Example: If data was collected on July 25, 2020, the user should enter jul2520
4) The resulting excel files will be added to the directory you're in.






