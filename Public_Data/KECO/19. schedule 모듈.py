# https://eva-codingnote.tistory.com/38
# pip install schedule
# Schedule Library imported
import schedule
import time
# Functions setup


def sec():
    print("1초에 한번씩")


def min():
    print("10분에 한번씩")


def hour():
    print("1시간에 한번씩")


def day():
    print('하루에 한번씩')


def zero():
    print('00:00')


def func():
    print('5~10')


def mon():
    print('monday')


def half_hour():
    print('35분')


# Task scheduling
# After every 1second sec() is called.
schedule.every(1).second.do(sec)

# After every 10mins min() is called.
schedule.every(10).minutes.do(min)

# After every hour hour() is called.
schedule.every().hour.do(hour)

# Every day at 12am or 00:00 time zero() is called.
schedule.every().day.at("00:00").do(zero)

# After every 5 to 10mins in between run func()
schedule.every(5).to(10).minutes.do(func)

# Every monday mon() is called
schedule.every().monday.do(mon)

# Loop so that the scheduling task
# keeps on running all time.
while True:

    # Checks whether a scheduled task
    # is pending to run or not
    schedule.run_pending()
    time.sleep(1)
