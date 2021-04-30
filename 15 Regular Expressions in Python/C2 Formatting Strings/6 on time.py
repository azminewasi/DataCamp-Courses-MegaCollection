"""On time
Lastly, you want to rewrite an old real estate prediction project. At the time, you obtained historical information about house prices and used it to make a prediction on future values.

The date was in the datetime format: datetime.datetime(1990, 3, 17) but to print it out, you format it as 3-17-1990. You also remember that you defined a dictionary for each neighborhood. Now, you believe that you can handle both type of data better with f-strings.

Two dictionaries, east and west, both with the keys date and price, have already been loaded. You can use print() to view them in the IPython Shell.

Instructions 1/2
50 XP
Instructions 1/2
50 XP
1
Inside the f-string, access the values of the keys price and date in east dictionary. Format the date to month-day-year.


Take Hint (-15 XP)
2
Inside the f-string, access the values of the keys price and date in west dictionary. Format the date to month-day-year."""


# Access values of date and price in east dictionary
print(f"The price for a house in the east neighborhood was ${east['price']} in {east['date']:%m-%d-%Y}")


# Access values of date and price in west dictionary
print(f"The price for a house in the west neighborhood was ${west['price']} in {west['date']:%m-%d-%Y}.")