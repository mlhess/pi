import RPi.GPIO as GPIO  
GPIO.setmode(GPIO.BCM)    
GPIO.setwarnings(False)
GPIO.setup(28, GPIO.OUT)  
GPIO.setup(29, GPIO.OUT)  
GPIO.setup(30, GPIO.OUT)  
GPIO.setup(31, GPIO.OUT)  

import os, time

while 1:
  (mode, ino, dev, nlink, uid, gid, size, atime, mtime, ctime) = os.stat('/tmp/myfile')

  diff = time.time() - mtime
  diff = diff/60
  if diff > 5:
    print "off"
    GPIO.output(28,False)
    GPIO.output(29,False)
    GPIO.output(30,False)
    GPIO.output(31,False)
    
    
    time.sleep(10)
#t = datetime.datetime.strptime(s, "%b %d %H:%M:%S")


