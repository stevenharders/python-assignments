from datetime import datetime

birthday = "01-May-12"
date_format = "%d-%B-%y"

parsed_date = datetime.strptime(birthday, date_format)
date_str = parsed_date.strftime("%-d/%w/%Y") # 01/11/17
print(date_str) 

