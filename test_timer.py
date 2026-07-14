import time
from utils import *

timer = Timer()

timer.start()

time.sleep(2)

elapsed = timer.stop()

print(f"Elapsed Time: {elapsed:.2f} seconds")


@measure_time
def process():
    time.sleep(1)


process()


with TimerContext("Video Processing"):
    time.sleep(3)