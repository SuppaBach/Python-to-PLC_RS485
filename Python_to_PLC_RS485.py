#Python-to-PLC_RS485
#RS485Sender_and_DataLogger
#College of Nanotechnology Co-op Education
#TBR AI Image Recognition project of ThaiBev and CMKL University
#Code by NiNouNiaNaNoNa
#Copyright 2019, Suppawat Boonrach

#Library Import
import random #for random testing only
import time #about time :)
import serial #for serial port
import logging #for data logger

#Variable preparation
#i = 0 #for testing only

#Random Type Testing
bottle_type_list = ['A', 'B', 'C'] #for random testing only

#User Input Testing
#bottle_type = str(input('Enter your bottle type : ')) #for user input testing only
#i = 0 #for user input testing only

#RS232-Serial Preparation
#ser = serial.Serial('COM6', 9600)     #Change serial port and baud rate here!!!
#time.sleep(1)

#RS485 Preparation
#COM_Port = serial.Serial('COM10') # open the COM port and change it here!!!
#COM_Port.baudrate = 9600               # Change baud rate  here!!!
#COM_Port.bytesize = 8                  # Number of data bits = 8
#COM_Port.parity   = 'N'                # No parity
#COM_Port.stopbits = 1                  # Number of Stop bits = 1
#Controlling DTR and RTS pins to put USB2SERIAL in transmit mode
#COM_Port.setDTR(0)                     #DTR=0,~DTR=1 so DE = 1,Transmit mode enabled
#COM_Port.setRTS(0)                     #RTS=0,~RTS=1 (In FT232 RTS and DTR pins are inverted)

#print("connected to: " + COM_Port.portstr)

ser = serial.Serial(
    port='COM10', #COM Port
    baudrate=9600, #Baud Rate
    parity=serial.PARITY_NONE, #Parity
    stopbits=serial.STOPBITS_ONE, #Stop Bit
    bytesize=serial.EIGHTBITS, #Number of Bits
    timeout=1
)

print("connected to: " + ser.portstr) #Show COM Port

#bottle_type = 'A' #for force test

def dataLog_and_Send():
    logging.basicConfig(filename='SerialSender.log', filemode='w', format= '%(asctime)s - %(message)s')
    #print(bottle_type) #for testing only

    #In real system. Instead of print, You will send a logic to Microcontroller before PLC lol
    bottle_type = random.choice(bottle_type_list) #Looping random, for testing only
    if bottle_type == 'A':
        logging.warning('Type_A => Ignore...')
        print('Type_A => Ignore...') #for test
        #ser.write(b'A') #for test rs232
        data = bytearray(b'A')  #for test rs485
        #data = 1
        #data = bottle_type
    if bottle_type == 'B':
        logging.warning('Type_B => Reject with Pusher_1')
        print('Type_B => Reject with Pusher_1') #for test
        #ser.write(b'B') #for test rs232
        data = bytearray(b'B') #for test rs485
        #data = 2
        #data = bottle_type  
    if bottle_type == 'C':
        logging.warning('Type_C => Reject with Pusher_2')
        print('Type_C => Reject with Pusher_2') 
        #ser.write(b'C') #for real system        # for test rs232
        data = bytearray(b'C')                   # for test rs485, Convert Character to byte array 
        #data = 3
        #data = bottle_type
    #ascii_char = ord(bottle_type)
    #print(ascii_char)
    #data = bytearray(ascii_char)
    #NoOfBytes  = COM_Port.write(data)            # Write data to serial port
    #send = COM_Port.write(str.encode(data))
    send = ser.write(data)          # Write data to serial port

#Loop
while 1: #bottle_type != '0': #i >= 0:
    dataLog_and_Send()
    #COM_Port.close()                             # Close the Serial port
    #ser.close()                             # Close the Serial port
    time.sleep(1)
    #i += 1 #for testing only
