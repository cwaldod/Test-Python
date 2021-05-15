from pymodbus.client.sync import ModbusSerialClient as ModbusClient

client = ModbusClient(method='rtu', port='COM7', baudrate=19200, timeout=1)

client.connect()
read=client.read_input_registers(address = 2 ,count = 2,unit= 1) 
#Address is register address e.g 30222, 
#and count is number of registers to read, 
#so it will read values of register 30222 to 30232
#unit is slave address, for 1 device leave it 1

data=read.registers[int(2)] #reading register 30223 
print(read) #printing value read in above line