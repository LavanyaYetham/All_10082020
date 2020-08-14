#!/usr/local/bin/python3.8
import os
a='df -h /root'
a=(os.system(a))
a=str(a)
print (a)
