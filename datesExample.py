import datetime


date1 = datetime.datetime.now()
date2 =  datetime.datetime(2020, 5, 17)

inbetween_1 = datetime.datetime(2021, 5, 17)
inbetween_2 = datetime.datetime(2019, 5, 17)



if inbetween_1 > date2 and inbetween_1 < date1:
    print(f"yes its inbetween")
else:
    print("nope")

if inbetween_2 > date2 and inbetween_2 < date1:
    print(f"yes its inbetween")
else:
    print("nope")


