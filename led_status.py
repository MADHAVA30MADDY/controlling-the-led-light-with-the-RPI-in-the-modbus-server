import time
import RPi.GPIO as GPIO

# Modbus Client
from pyModbusTCP.server import ModbusServer, DataBank
from pyModbusTCP.client import ModbusClient
from  time import sleep
from random import uniform
import time
 
server = ModbusServer("192.168.1.46", 7878, no_block=True)  
client = ModbusClient(host='192.168.1.46', port=7878, unit_id=1)

print("Start server...")
server.start()
print("Server is online")


GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(4,GPIO.OUT)


def turn_on(status):
   
    if(status == 1):
        print ("LED on")
        GPIO.output(4,GPIO.HIGH)
    else:
        print ("LED off")
        GPIO.output(4,GPIO.LOW) 

    return status


print ("Lights ON/OFF")


try:

  while True:
        
    # Modbus Codes
    
    

    read_status = client.read_holding_registers(0x00,1)
    print(read_status)
    turn_on(read_status)
    	
    print (f"Light Status {read_status}")  
    
    #server.data_bank.set_holding_registers(0, [read_status]) 
 
    time.sleep(1)

except KeyboardInterrupt:
  
  GPIO.cleanup()
  
  
  

