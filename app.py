import pygsheets
import datetime

gc = pygsheets.authorize(outh_file='client_secret.json', outh_nonlocal=True)
now = datetime.datetime.now()
# Constants
date_formatted = "%Y-%m-%d-%H_%M"
formatted_date = now.strftimed(date_formatted)

# sheet_name = '{}'.format(formatted_date)
sheet_name = formatted_date

# Open spreadsheet or create
try:
    sheet = gc.open(sheet_name)
except pygsheets.SpreadsheetNotFound:
    sheet = gc.create(sheet_name)

if sheet:
    worksheet = sheet.sheet1
    
def create_headers():
    pass