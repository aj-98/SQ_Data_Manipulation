PURPOSE:
xlsplit.py is a Python script to manipulate raw excel data for canvassing results. It specifically moves the column
"VAN ID" to its correct position(the first column) and splits the data into two separate csv files based on if the
attempt to contact the voter was successful or not.
DO NOT ALTER THIS SCRIPT IN ANY WAY.

REQUIREMENTS BEFORE RUNNING:
Before running this script, the FOLLOWING REQUIREMENTS MUST BE MET:
1) Python 3 must be installed on the computer that is running this script. It can be downloaded via www.python.org
2) Make sure user is in the same directory that the python(.py) file is in
3) *Suggested but not Necessary* Activate virtual environment by running jowa_venv/Scripts/activate (Windows)
4) All other necessary requirements can be filled by running the following command: pip install -r requirements.txt OR
pip3 install -r requirements.txt

HOW TO RUN:
This script may be run using a Python IDE, such as PyCharm, or through the command line (Command Prompt on Windows,
Linux on Mac). If running through the command line, start the script using the following command: python xlsplit.py

USER INPUT:
Once the script has been run, the user will be asked to:
1) Select the file that holds the data they want to manipulate. The file selected can be an excel file or a csv file.
2) Enter the FULL PATH to an existing folder. This folder will be used to contain a database.
The path must end with a /    An example of what the user's input should look like: C:/Path/To/Existing/Folder/
3) Enter the date that the data was collected using the month abbreviation(lowercase), the date, and the last two digits of the
year. Example: If data was collected on July 25, 2020, the user should enter jul2520
4) That's it.






