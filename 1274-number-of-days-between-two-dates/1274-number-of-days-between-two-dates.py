class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        
        def isLeap(year:int) ->bool:
            if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
                return True
            return False

        def days_from_1900(year:int, month: int, day:int) -> int:
            days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
            days = 0
            for y in range(1971, year):
                days += 366 if isLeap(y) else 365
            for m in range(1,month):
                if m == 2 and isLeap(year):
                    days+= 29
                else:
                    days += days_in_month[m-1]
            days += day
            return days



        Ay, Am, Ad = date1.split('-')
        By, Bm, Bd = date2.split('-')

        return abs(days_from_1900(int(Ay), int(Am), int(Ad) - days_from_1900(int(By), int(Bm), int(Bd))))




