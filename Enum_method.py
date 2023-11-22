from enum import Enum


class WeekDay(Enum):
    monday = 1
    tuesday = 2
    wenesday = 3
    thrusday = 4
    friday = 5
    saturday = 6
    sunday = 7
#check given day is weekend or weekday
def checkday(value) -> str:
    result : str = ""
    match(value):
        case WeekDay.monday.value:
            result = "weekday"

        case WeekDay.tuesday.value:
            result = "weekday"

        case WeekDay.wenesday.value:
            result = "weekday"

        case WeekDay.thrusday.value:
            result = "weekday"

        case WeekDay.friday.value:
            result = "weekday"

        case WeekDay.saturday.value:
            result = "weekday"

        case WeekDay.sunday.value:
            result = "weekend"

    return result
day=int(input("Enterday value: 1 monday...:"))
print(checkday(day))

print(type(WeekDay))
print(WeekDay.monday)
print(WeekDay.monday.value)
print(WeekDay.monday.name)




