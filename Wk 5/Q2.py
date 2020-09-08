#Design a program which will ask the user to 
#enter the date in the form dd/mm/yyyy


input_date = input('Enter a date in DD/MM/YYY format')
list_date = input_date.split("/")

print('Day: ' + list_date[0])

print('Month: ' + list_date[1])

print('Year: ' + list_date[2])
