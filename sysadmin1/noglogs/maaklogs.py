#!/usr/bin/python3


import random
import datetime

for tel in range(random.randint(1000,2000)):
    trekking = random.randint(1,1000)
    trekking2 = random.randint(1,1000)
    if trekking < trekking2:
        print("{}:MINDER {} {}".format(datetime.datetime.now().isoformat(), trekking, trekking2))
    elif trekking > trekking2:
        print("{}:MEER wie sou nou ooit kon ding {} {}".format(datetime.datetime.now().isoformat(), trekking, trekking2))
    else:
        print("{}:ERROR".format(datetime.datetime.now().isoformat()))


