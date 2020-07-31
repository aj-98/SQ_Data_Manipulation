import sqlite3 as sq
import pandas as pd
import tkinter as tk
import csv
import sys
import os
from tkinter import filedialog
from sqlite3 import Error


''' This is a Python script to manipulate raw excel data for canvassing results.
It specifically moves the column"VAN ID" to its correct position(the first column) and
splits the data into two separate csv files based on if the
attempt to contact the voter was successful or not. '''

# Open User Interface
window = tk.Tk()

def openfile():
    file = filedialog.askopenfilename(parent=window, initialdir="C:/", title="Select an Excel or CSV File to Upload", filetypes=[("Excel Files","*.xlsx")
        ,("Csv Files","*.csv")])
    return file


# Creation of Button to Initiate Path Retrieval
#file_bttn = tk.Button(window, text='Path of File', command=openfile)
#file_bttn.pack()

# Receive User Input
xl_path = openfile()
pd_data = None
# Open User Interface
# window.mainloop()

# Creation of DataFrame Using Pandas
if (xl_path != None) and (xl_path != ''):
    try:
        pd_data = pd.read_excel(xl_path, sheet_name='HubDialer 7.25.20', header=0)
    except Error as e:
        print(e)
else:
    print("Please Choose a File")
    xl_path = openfile()

if (xl_path == None) or (xl_path == ''):
    print("User has failed to pick a file. Try Again.")
    sys.exit(0)


data_path = input("What Folder Do You Want to Store the Database in? It Can Be Any Folder That Exists on Your Computer."
                  " \nFor Example, You Can Enter C:/Data/Campaign/ if that folder exists on your computer. \n"
                  "Make sure to include a / at the end of the file path that you enter: \n")

data_path += "jowa.db"

# Creation of Connection to Database
try:
    # conn = sq.connect('C:\\Users\\Arianna\\DevProj\\JoWa_Camp\\jowa_venv\\sqData\\jowa.db')
    conn = sq.connect(data_path)
except Error as e:
    print(e)
    print("Connection to Database Could Not Be Made. Make Sure That the Path You Provided Exists. Make Sure the Path "
          "Includes a / at the End of the Path and Try Again.")
    sys.exit(0)

# Establish cursor object to execute commands for the database
cursor = conn.cursor()

# Remove VAN ID Column
col_name = "VAN ID"
# Temporarily Store Removed Column
first_col = pd_data.pop(col_name)
# Move VAN ID Column to First Column
pd_data.insert(0, col_name, first_col)
# Remove Duplicate Email Column
remove_col = "Email"
pd_data.pop(remove_col)
# Clean up Column Names
pd_data.columns = pd_data.columns.str.strip().str.replace(" ", "_").str.replace("#", "Num").str.replace("?", "")\
    .str.replace(":", "").str.replace("{","").str.replace("}", "").str.replace("(", "").str.replace(")", "").\
    str.replace("&", "and").str.replace("\"", "").str.replace("1", "One").str.replace("\n", "").str.replace(",", "")


# Give instructions for initializing DataStructure for SQL
# print("For Each Column, Enter the Type of Value it Accepts. Enter i for Integers(e.g. 1,2,3,...). Enter d for "
#      "Decimal Numbers(e.g. 1.23, 4.0, 5.9099...). Enter t for text(e.g human, H5gtr33, john doe...)")

# Initialize DataFrame with blank
# dt_struct = ""

# Set Up Data Structure
#for col in pd_data.columns:
#    typ = input("What Type of Value Does %s Accept?" % col)
#    if (typ == 'i') or (typ == 'I'):
#        val_typ = 'INTEGER'
#    elif (typ == 'd') or (typ == 'D'):
#        val_typ = 'REAL'
#    elif (typ == 't') or (typ == 'T'):
#        val_typ = 'TEXT'
#    else:
#        typ = input("Invalid Input. What does %s accept? Enter i for integer, d for decimal, or t for text" % col)
#        if (typ == 'i') or (typ == 'I'):
#            val_typ = 'INTEGER'
#        elif (typ == 'd') or (typ == 'D'):
#            val_typ = 'REAL'
#           val_typ = 'TEXT'

#   dt_struct += ("%s %s,\n" % (col, val_typ))


# Establish VANID as Primary Key
# dt_struct += "PRIMARY KEY(VAN_ID)"

# Create 3 SQL DataTables. Initial is Untouched Data. Two Other Tables are Splits of Initial Data
# cursor.execute(('''CREATE TABLE IF NOT EXISTS jul25(%s);''' % dt_struct))
init_tbl_name = input("When was information for this file collected? Answer with the month abbreviation(lowercase) "
                      "followed by the date and the last two digits of the year.\nFor example, if the data was "
                      "collected on July 25, 2020, you should enter jul2520: ")

cursor.execute('''CREATE TABLE IF NOT EXISTS %s(VAN_ID INTEGER,
Campaign_ID INTEGER,
Household_ID INTEGER,
HUBID INTEGER,
Pass_Num INTEGER,
Phone_Number TEXT,
First_Name TEXT,
Middle_Name TEXT,
Last_Name TEXT,
Email_Address TEXT,
Address_One TEXT,
City TEXT,
State TEXT,
Zip INTEGER,
Sex TEXT,
Age INTEGER,
Cell_Phone TEXT,
RaceName TEXT,
Status TEXT,
Call_ID TEXT,
Agent_Session_Number INTEGER,
Agent TEXT,
Date TEXT,
Time TEXT,
Call_Duration INTEGER,
Patch_Number INTEGER,
Patch_Status TEXT,
Patch_Duration INTEGER,
Notes TEXT,
We_have_masks_we_can_deliver_free_of_charge_if_you_would_like_one TEXT,
IF_YES_TO_MASK_QUESTIONHow_many_would_you_like___Is_Address_Line_One_a_good_place_to_leave_them_if_not_put_in_notesCan_we_leave_them_in_a_mailbox_or_anything_like_that_IF_NO_Where_would_be_a_good_place_to_leave_them_PLEASE_PUT_NOTES_ABOUT_MASKS_and_GENERAL_NOTES_FROM_CONVERSATION_IN_NOTES_ON_LEFT_HAND_SIDE INTEGER,
What_issues_are_on_your_mind TEXT,
Would_you_like_Jonathan_to_give_you_a_call_to_discuss_these_issues TEXT,
PRIMARY KEY(VAN_ID));''' % init_tbl_name)

# Second Table's Creation
pass_tbl_name = init_tbl_name + "_pass"
cursor.execute('''CREATE TABLE IF NOT EXISTS %s(VAN_ID INTEGER,
Campaign_ID INTEGER,
Household_ID INTEGER,
HUBID INTEGER,
Pass_Num INTEGER,
Phone_Number TEXT,
First_Name TEXT,
Middle_Name TEXT,
Last_Name TEXT,
Email_Address TEXT,
Address_One TEXT,
City TEXT,
State TEXT,
Zip INTEGER,
Sex TEXT,
Age INTEGER,
Cell_Phone TEXT,
RaceName TEXT,
Status TEXT,
Call_ID TEXT,
Agent_Session_Number INTEGER,
Agent TEXT,
Date TEXT,
Time TEXT,
Call_Duration INTEGER,
Patch_Number INTEGER,
Patch_Status TEXT,
Patch_Duration INTEGER,
Notes TEXT,
We_have_masks_we_can_deliver_free_of_charge_if_you_would_like_one TEXT,
IF_YES_TO_MASK_QUESTIONHow_many_would_you_like___Is_Address_Line_One_a_good_place_to_leave_them_if_not_put_in_notesCan_we_leave_them_in_a_mailbox_or_anything_like_that_IF_NO_Where_would_be_a_good_place_to_leave_them_PLEASE_PUT_NOTES_ABOUT_MASKS_and_GENERAL_NOTES_FROM_CONVERSATION_IN_NOTES_ON_LEFT_HAND_SIDE INTEGER,
What_issues_are_on_your_mind TEXT,
Would_you_like_Jonathan_to_give_you_a_call_to_discuss_these_issues TEXT,
PRIMARY KEY(VAN_ID));''' % pass_tbl_name)

# Third Table's Creation
# cursor.execute('''CREATE TABLE IF NOT EXISTS jul25fail(%s);''' % dt_struct)
fail_tbl_name = init_tbl_name + "_fail"
cursor.execute('''CREATE TABLE IF NOT EXISTS %s(VAN_ID INTEGER,
Campaign_ID INTEGER,
Household_ID INTEGER,
HUBID INTEGER,
Pass_Num INTEGER,
Phone_Number TEXT,
First_Name TEXT,
Middle_Name TEXT,
Last_Name TEXT,
Email_Address TEXT,
Address_One TEXT,
City TEXT,
State TEXT,
Zip INTEGER,
Sex TEXT,
Age INTEGER,
Cell_Phone TEXT,
RaceName TEXT,
Status TEXT,
Call_ID TEXT,
Agent_Session_Number INTEGER,
Agent TEXT,
Date TEXT,
Time TEXT,
Call_Duration INTEGER,
Patch_Number INTEGER,
Patch_Status TEXT,
Patch_Duration INTEGER,
Notes TEXT,
We_have_masks_we_can_deliver_free_of_charge_if_you_would_like_one TEXT,
IF_YES_TO_MASK_QUESTIONHow_many_would_you_like___Is_Address_Line_One_a_good_place_to_leave_them_if_not_put_in_notesCan_we_leave_them_in_a_mailbox_or_anything_like_that_IF_NO_Where_would_be_a_good_place_to_leave_them_PLEASE_PUT_NOTES_ABOUT_MASKS_and_GENERAL_NOTES_FROM_CONVERSATION_IN_NOTES_ON_LEFT_HAND_SIDE INTEGER,
What_issues_are_on_your_mind TEXT,
Would_you_like_Jonathan_to_give_you_a_call_to_discuss_these_issues TEXT,
PRIMARY KEY(VAN_ID));''' % fail_tbl_name)

# Import Initial Data to First SQL DataTable
pd_data.to_sql(init_tbl_name, conn, if_exists='append', index=False)


# Search Initial Data for Successful Attempts at Contact
cursor.execute("SELECT * FROM %s where status='Human'" % init_tbl_name)
# Store Successful Attempts at Contact
contact_succ = cursor.fetchall()
# Upload Successful Attempts at Contact into Separate DataTable
cursor.executemany("INSERT INTO %s VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)"
                   ";" % pass_tbl_name, contact_succ)


# Search Initial Data for Unsuccessful Attempts at Contact
cursor.execute("SELECT * FROM %s where status!='Human'" % init_tbl_name)
# Store Unsuccessful Attempts at Contact into Separate DataTable
contact_fail = cursor.fetchall()
# Upload Unsuccessful Attempts at Contact Into Separate DataTable
cursor.executemany("INSERT INTO %s VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)"
                   ";" % fail_tbl_name, contact_fail)

# Isolate Data from Successful Contact Attempts
succ_data = cursor.execute("select * from %s" % pass_tbl_name)
# Convert to CSV File
with open(init_tbl_name + "_succ.csv", "w", newline="") as csv_file:
    csv_writer = csv.writer(csv_file, delimiter=",")
    csv_writer .writerow([i[0] for i in cursor.description])
    csv_writer.writerows(succ_data)

# Save CSV "Success" Data in Users Current Directory
contact_succ_csv = os.getcwd() + "/%s_succ.csv" % init_tbl_name
print("Data Exported Successfully into {}".format(contact_succ_csv))

# Isolate Date from Failed Contact Attempts
fail_data = cursor.execute("select * from %s" % fail_tbl_name)
# Convert to CSV File
with open(init_tbl_name + "_fail.csv", "w", newline="") as csv_file:
    csv_writer = csv.writer(csv_file, delimiter=",")
    csv_writer .writerow([i[0] for i in cursor.description])
    csv_writer.writerows(fail_data)

# Save CSV "Fail" Data in Users Current Directory
contact_fail_csv = os.getcwd() + "/%s_fail.csv" % init_tbl_name
print("Data Exported Successfully into {}".format(contact_fail_csv))

# Commit Uploads
conn.commit()

# View Full Structured Database
# print(dt_struct)

# Close Cursor and Connection
cursor.close()
conn.close()









