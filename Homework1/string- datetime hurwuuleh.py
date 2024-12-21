#"2024/12/15" string- datetime hurwuuleh
from datetime import datetime, timedelta



date_sting = '2024/12/15'
date_format = '%Y/%m/%d'
new_date =datetime.datetime.strptime(date_sting, date_format)
print(new_date)

new_date_doloo = new_date + timedelta(days=7)
print(new_date_doloo)

new_string = datetime.strftime(new_date_doloo, "%B %d, %Y")
print(new_string)