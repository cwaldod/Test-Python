import pymodbus  
import time  
from pymodbus.pdu import ModbusRequest
from pymodbus.client.sync import ModbusSerialClient as ModbusClient
#initialize a serial RTU client instance
from pymodbus.transaction import ModbusRtuFramer
#count= the number of registers to read
#unit= the slave unit this request is targeting
#address= the starting address to read from
for _ in range(5): 
#This is a comment
# This is a test after installing git  
    client = ModbusClient(method = 'rtu', port='com2',timout=1,stopbits=1, parity='N', baudrate= 19200)
#Connect to the serial modbus server
    connection = client.connect()
#Starting add, num of reg to read, slave unit.
#read = client.read_holding_registers(address = 0x000,count =2, unit=1)
    #read3 = client.read_coils(address = 0x060,count =1, unit=1)
    #read2 = client.read_input_registers(address = 0x059,count =10, unit=1)
    read = client.read_holding_registers(address = 0x000,count =63, unit=1)
   #This writes to motor current
    #client.write_register(address = 0x001, value=700,unit=1)
   #This writes to the leaving chilled water setpoint
    #client.write_register(address = 0x000, value=440,unit=1)
    #client.write_register(address = 0x061, value=1, unit=1)
    data = read.registers
   # data2 = read2.registers
    #data3 = read3.registers
    print(connection)
    print(data)
   # print(data2)
    #print(data3)
    leaving_chill = data[0] /10
    motor_amps = data[1] /10
    leaving_liquid = data[4] /10
    both = f"{leaving_chill} {motor_amps}"
    print(f"This Is Both",both)
    print(f"Leaving Chill Water temp set point",leaving_chill)
    print(f"Leaving Liquid",leaving_liquid)
    print(f"Motor Amps set point ",motor_amps)
    if leaving_chill > 15:
        print("yes it is greater than 15")
    time.sleep(2)
#Closes the underlying socket connection
client.close()
