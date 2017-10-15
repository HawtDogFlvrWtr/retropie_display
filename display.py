#!/usr/bin/python
# OBD2 Loop routine for metrics
# Created by Christopher Phipps (hawtdogflvrwtr@gmail.com)
# 7/12/2016
#

import sys
sys.path.append('/usr/local/lib/lcd')
from lcd import *
import psutil
import time
import syslog
import ConfigParser
import os.path
import string
import random
import requests
from datetime import datetime


def getCPUtemperature():
    res = os.popen('vcgencmd measure_temp').readline()
    return(res.replace("temp=",""))

initDisplay()
lcdSetContrast(60)  # Universal contrast value for most lcd's
lcdShowLogo()
time.sleep(2)
lcdClear()
while True:
  cpuload = psutil.cpu_percent()
  memused = psutil.virtual_memory()
  rootused = psutil.disk_usage('/')
  lcdDisplayText(0, 0, "   RetroPie  ")
  lcdDrawLine(0,8,84,8,1)
  lcdDisplayText(0, 12, "CPU  "+str(cpuload).split('.', 1)[0]+"%")
  lcdDisplayText(0, 20,"RAM  "+str(memused.percent).split('.', 1)[0]+"%")
  lcdDisplayText(0, 28, "DISK "+str(rootused.percent).split('.', 1)[0]+"%")
  lcdDisplayText(0, 36, "TEMP "+str(getCPUtemperature()))
  lcdDisplay()
  time.sleep(1)
