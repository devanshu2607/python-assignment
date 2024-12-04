##70.	Develop a simple task scheduler that runs functions at specified intervals.

import schedule # type: ignore
import time 

def task():
    print("task executed!")

schedule.every(2).seconds.do(task)

while True:
    schedule.run_pending()
    time.sleep(1)