Python 3.5.1 (v3.5.1:37a07cee5969, Dec  6 2015, 01:54:25) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import datetime as dt
>>> import time
>>> print(time.time())
1487147647.0475805
>>> example =time.time()
>>> print(examle)
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    print(examle)
NameError: name 'examle' is not defined
>>> print(example)
1487147692.357569
>>> print(dt.datetime.fromtimestamp(example))
2017-02-15 14:34:52.357569
>>> 
