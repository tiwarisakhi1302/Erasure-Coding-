

import os
from reedsolo import RSCodec
from pathlib import Path
import array

str1=""
file_name="input"
fli="./media/"+file_name+".txt"
f = open(fli, "r")
for i in f :
    str1=str1+(i)
f.close()

size_of_file=len(str1)

if(2*size_of_file > 254) :    #127
    rsc = RSCodec(254)
else :
    rsc = RSCodec(2*size_of_file)

b_str=bytes(str1, 'utf-8')

# print(b_str)

encoded_msg= rsc.encode(b_str)

# print(encoded_msg)

parity_block = encoded_msg.removeprefix(b_str)

# print(parity_block)

# print(size_of_file)
os.chdir('./media')
os.mkdir("user")
# fli1=file_name+"_original_len.txt"
fle="./user/"+file_name+"_encode.bin"
f = open(fle, "wb")

f.write(parity_block)

f.close()

size = str(size_of_file)

fli1="./user/"+file_name+"_original_len.txt"
# os.mkdir("user")
fli1=file_name+"_original_len.txt"
f=open(fli1, "w")
f.write(size)

print('File is Encoded successfully')



