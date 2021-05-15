import time
from urllib.parse import urlencode
from urllib.request import Request

from pymodbus.client.sync import ModbusClient



from pymodbus.constants import Defaults
Defaults.RetryOnEmpty = True
Defaults.Timeout = 5
Defaults.Retries = 5
client = ModbusClient (method='rtu', port='com2', timout=2, stopbits= 1, bytesize = 8, baudrate=19200)
client.connect()

while True:
    hh = client.read_holding_registers(address=5, count=8, unit=1)

    h2 = hh.registers[7]/10
    batTemp = hh.registers[0]/10
    hd = client.read_holding_registers(address=23, count=1, unit=1)
    chargeVol = hd.registers[0]/10
    print (h2)
    print (batTemp)
    print (chargeVol)
    time.sleep(2)

