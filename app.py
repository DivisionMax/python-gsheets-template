import pygsheets

gc = pygsheets.authorize(outh_file='client_secret.json', outh_nonlocal=True)

# Open spreadsheet and then workseet
sh = gc.open('my new ssheet')
wks = sh.sheet1

wks.update_cell('A1', "Hey yank this numpy array")