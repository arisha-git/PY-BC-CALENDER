def julianleapyear(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def daysjulianmonth(year, month):
    if month == 2:
        return 29 if julianleapyear(year) else 28
    elif month in {4, 6, 9, 11}:
        return 30
    else:
        return 31

def monthstart(year, month):
    ref_year = 1900
    ref_start_day = 0
    total_days = 0

    for y in range(ref_year, year):
        total_days += 366 if julianleapyear(y) else 365

    for m in range(1, month):
        total_days += daysjulianmonth(year, m)

    return (ref_start_day + total_days) % 7

class JulianCalendar:
    month_names = ["January", "February", "March", "April", "May", "June",
                   "July", "August", "September", "October", "November", "December"]

    def __init__(self, year, month):
        self.year = year
        self.month = month

    def display_month(self):
        month_name = self.month_names[self.month - 1]
        print(f"{month_name} {self.year}")
        print("Mon Tue Wed Thu Fri Sat Sun")

        start_day = monthstart(self.year, self.month)
        days_in_month = daysjulianmonth(self.year, self.month)

        current_position = 0

        for _ in range(start_day):
            print("      ", end="  ")
            current_position += 1

        for day in range(1, days_in_month + 1):
            print(f" {day:2} ", end="  ")
            current_position += 1
            if current_position % 7 == 0:
                print()

        if current_position % 7 != 0:
            print()

        print("\n")

    def next_month(self):
        if self.month == 12:
            self.month = 1
            self.year += 1
        else:
            self.month += 1

    def previous_month(self):
        if self.month == 1:
            self.month = 12
            self.year -= 1
        else:
            self.month -= 1

def main():
    year = int(input("Enter year: "))
    month = int(input("Enter month (1-12): "))

    calendar_obj = JulianCalendar(year, month)

    while True:
        calendar_obj.display_month()
        command = input("Enter 'next', 'previous', or 'exit': ").lower()

        if command == "next":
            calendar_obj.next_month()
        elif command == "previous":
            calendar_obj.previous_month()
        elif command == "exit":
            break
        else:
            print("Invalid command. Please enter 'next', 'previous', or 'exit'.")

if __name__ == "__main__":
    main()
