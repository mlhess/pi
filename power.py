import RPi.GPIO as GPIO  
GPIO.setmode(GPIO.BCM)    
GPIO.setwarnings(False)
GPIO.setup(28, GPIO.OUT)  
GPIO.setup(29, GPIO.OUT)  
GPIO.setup(30, GPIO.OUT)  
GPIO.setup(31, GPIO.OUT)  
GPIO.output(28,False) 
GPIO.output(29,True) 
GPIO.output(30,False) 
GPIO.output(31,False) 

