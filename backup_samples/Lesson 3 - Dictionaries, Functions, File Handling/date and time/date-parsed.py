import datetime

date_string = "1996-12-27"
parsed_date = datetime.datetime.strptime(date_string, "%Y-%m-%d")
print(parsed_date) # Prints the current parsed date
# Output
# 1996-12-27 00:00:00