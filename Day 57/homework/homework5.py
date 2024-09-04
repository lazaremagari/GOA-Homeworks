def travel(age, year, time_to_travel, past_or_future):
    if past_or_future == "future":
        return "your age is" + str(age + time_to_travel) + "year is" + str(year + time_to_travel)
    else:
        return "your age is" + str(age - time_to_travel) + "year is" + str(year - time_to_travel)
print(travel(int(input("enter your age -> ")), int(input("enter year -> ")), int(input("enter time to travel -> ")), input("past or future -> ")))