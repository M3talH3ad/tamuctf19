import base64

encrypted = 'XUBdTFdScw5XCVRGTglJXEpMSFpOQE5AVVxJBRpLT10aYBpIVwlbCVZATl1WTBpaTkBOQFVcSQdH'
decrypted = base64.b64decode(encrypted)

decrypted = "]@]LWRs\x0eW\tTFN\tI\\JLHZN@N@U\\I\x05\x1aKO]\x1a`\x1aHW\t[\tV@N]VL\x1aZN@N@U\\I\x07G"
known = 'gigem{'

# print (decrypted, known)
key = ''
for index,i in enumerate(known):
	c = chr(ord(decrypted[index]) ^ ord(i))
	key +=  c


key = ':)'

flag = ''
for index, i in enumerate(decrypted):
	c = chr(ord(decrypted[index]) ^ ord(key[index%2]))
	flag +=c

print(flag)