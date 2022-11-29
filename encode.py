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

size_of_file=len(str1);

if(2*size_of_file > 254) :    #127
    rsc = RSCodec(254)
else :
    rsc = RSCodec(2*size_of_file)

b_str=bytearray(str1, 'utf-8');

encoded_msg= rsc.encode(b_str)

# print(encoded_msg)

parity_block = encoded_msg.removeprefix(b_str)

parity_block_str = str(parity_block)

parity_block_str = parity_block_str.removeprefix("bytearray(b'")

parity_block_str = parity_block_str.removesuffix("')")

# print(parity_block_str)


fle="./media/"+file_name+"_encode.txt"

f = open(fle, "w")

f.write("")

f.close()

f = open(fle, "a")

f.write(parity_block_str + '\n')

f.write(str(size_of_file))

f.close()

# recover the original

# decoded_msg, decoded_msgecc, errata_pos = rsc.decode()





