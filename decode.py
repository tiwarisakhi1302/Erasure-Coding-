from reedsolo import RSCodec
from pathlib import Path
import array

file_name="input"

#  first go to the user folder
#  Then find the file he/she is demanding
# input : this is variable and will be come from

fle="./media/"+file_name+"_encode.txt"

f2 = open(fle)

parity = ""

for i in f2 :
    print(i)
    
    # parity = parity + i;

l=[l.rstrip() for l in f2]

# f2.close()

n=""

for itr in l :
    n = itr

# n = int(n)
print(n)

# temp = ""

# for i in range(n) :
#     temp = temp + 'X'

# print(temp)


# temper_data = temp + parity

# print(temper_data)







