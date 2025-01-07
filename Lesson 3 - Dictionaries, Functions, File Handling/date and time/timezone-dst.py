#install pytz
# pip install pytz

import datetime
import pytz

date = datetime.datetime.now()
timezone = pytz.timezone('America/New_York')
localized_date = timezone.localize(date)

print(localized_date) # Prints the localized date