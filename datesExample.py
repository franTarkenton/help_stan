import datetime

# create a datetime object for whatever the time is now
date1 = datetime.datetime.now()
# create a datetime object for 2020, may 17
date2 =  datetime.datetime(2020, 5, 17)

# create some other datetime objects for comparing
inbetween_1 = datetime.datetime(2021, 5, 17)
inbetween_2 = datetime.datetime(2019, 5, 17)


# testing if the date inbetween_1 is inbetween date2 and date1
if inbetween_1 > date2 and inbetween_1 < date1:
    print(f"yes its inbetween")
else:
    print("nope")

# ditto as above but testing for inbetween_2
if inbetween_2 > date2 and inbetween_2 < date1:
    print(f"yes its inbetween")
else:
    print("nope")


