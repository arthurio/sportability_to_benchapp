# General

This script is made to import your calendar from sportability to benchapp.

# Download your Team's schedule from sportability

1. Go to [sportability](http://www.sportability.com/spx/Leagues/Client.asp?ClientID=130)
2. Click on your league
3. Click on "view complete schedule"
4. Select your Team in the "Show" dropdown filter at the top
5. Click on "Export schedule (iCal or vCal)" and follow the steps to get it sent to your email address. Make sure to use iCal
6. Once you get the email, save the file as "schedule.ics" in this folder.

# Convert your .ics to .csv

You need python to be installed on your machine but it usually comes with new Mac OS versions.

1. install the requirements `pip install -r requirements.txt`
2. run the script `python convert_ics_to_csv.py`

# Import your schedule in benchapp

1. Go to [benchapp import page](https://www.benchapp.com/schedule/import/)
2. Upload your .csv file
3. Make sure everything looks good
4. Voilà :D

Note: the dates are converted from UTC to PST, you need to update the script with your timezone if it's different.