import serial 
from datetime import datetime
import io


ser = serial.Serial(
	port='/dev/ttyUSB0',
	baudrate=9600,
	bytesize=serial.EIGHTBITS,
	parity=serial.PARITY_NONE,
	stopbits=serial.STOPBITS_ONE
)

print(ser.read(size=8))
6
sio = io.TextIOWrapper(io.BufferedRWPair(ser, ser, 1), encoding='ascii', newline='\r')
sio._CHUNK_SIZE =1

while ser.isOpen():
	datastring = ser.read(size=8)
	print(datetime.utcnow().isoformat(), datastring)
	
with open(outfile, 'a') as f:
	while ser.isOpen():
		datastring = sio.readline()
		f.write(datetime.utcnow().isoformat() + '\t' + datastring + '\n')
		f.flush()
	
ser.close()
	


while ser.isOpen():
	datastring = sio.readline()
	print(datetime.utcnow().isoformat(), datastring) 
