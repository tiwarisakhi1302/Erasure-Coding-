from reedsolo import RSCodec
from pathlib import Path
# from encode import size_of_file

file_name="input"

fli = "./media/"+file_name+".txt"

fle="./media/"+file_name+"_encode.bin"

f = open(fle, 'rb')

parity=f.read()

f.close()

fle_s ="./media/"+file_name+"_original_len.txt"
f = open(fle_s, 'r')
size = f.read()

size_of_file = int(size)

f.close()
# print(parity)

temp=""

for i in range(size_of_file) :
    temp = temp + 'X';

t = bytes(temp, encoding='latin-1')

# print(t)

if(2*size_of_file> 254) :    #127
    rsc = RSCodec(254)
else :
    rsc = RSCodec(2*size_of_file)

temp1 = t + parity

# print(temp1)

# Decoding (repairing)

decoded_msg, decoded_msgecc, errata_pos = rsc.decode(temp1)

# print(decoded_msg)

data = str(decoded_msg)

data = data.removeprefix("bytearray(b'")
data = data.removesuffix("')")

# print(data)

fli="./media/"+file_name+".txt"
f = open(fli, "w")
f.write(data)

print('File is decoded successfully')

# print(data)
