
with open('/tmp/a.bin') as f:
	byte=f.read(1)
	while byte != "":
			byte=f.read(1)
			#print '{0:08b}'.format(ord(byte)),
			print byte,
