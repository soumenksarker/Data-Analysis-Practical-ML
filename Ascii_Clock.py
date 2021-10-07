#! python3 #delete other two lines if you are a Windows User

import time
import os
from Digits import Digits
def MakeTime(x,y):
    X = x.split("\n")
    Y = y.split("\n")
    R = ""
    l = len(X)
    for i in range(l):
        if(i==l-1):
            R += (X[i]+Y[i])
        else:
            R += (X[i]+Y[i]+"\n")
    return R
hour = -1
Hour = ""
min = -1
Min =""
sec = -1
Sec =""
HourMin =""
try:
    while True:
        if((time.localtime().tm_hour%12 != hour) or (time.localtime().tm_min != min)):
            hour = time.localtime().tm_hour%12
            Hour = MakeTime(Digits.Select(int(hour/10)),Digits.Select(int(hour%10)))
            min = time.localtime().tm_min
            Min = MakeTime(Digits.Select(int(min/10)),Digits.Select(int(min%10)))
            HourMin = ""
            HourMin = MakeTime(Hour,Digits.Separetor())
            HourMin = MakeTime(HourMin,Min)
            HourMin = MakeTime(HourMin,Digits.Separetor())
            #print("reachead here")
        sec = time.localtime().tm_sec
        Sec = MakeTime(Digits.Select(int(sec/10)),Digits.Select(int(sec%10)))
        print(MakeTime(HourMin,Sec))
        time.sleep(1)
        os.system("echo '\033c'")

except KeyboardInterrupt:
    os._exit(0)


