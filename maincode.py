from reedsolo import RSCodec

n=10

# 3/5*len(string)

#3/5 * 5
#3

#dynamic Parity

#as for every parity block the 


rsc = RSCodec(n)  # n ecc symbols
#This can help in recover maximum of n/2 errors

# Encoding
# rsc.encode([1,2,3,4])

# rsc.encode(bytearray([1,2,3,4]))
message = b'hello Sakshi, I live in ghaziabad and studying in Jaypee University'
# print(len(message))
encoded_msg= rsc.encode(message)
# Decoding (repairing)

#The length of the wrong string should same as the original string

msg2=b'ejlbfjkbjbwjbfjowebg   wfEH    VFHIEVHFjbjobgofefbievfvevfobrwobgob'
parity_block = encoded_msg.removeprefix(message)
print(parity_block)
msg3= msg2+parity_block
print(msg3)
#print(msg3.removeprefix(msg2ṇ))

# tampered_msg = msg3
# decoded_msg, decoded_msgecc, errata_pos = rsc.decode(tampered_msg)

# print(decoded_msg)
# print(decoded_msgecc)

# print(errata_pos) 

# print(list(errata_pos)) #for printing the indices of the erratas in interger




