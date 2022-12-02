
def encrypt(file_name,user):
    import os
    from reedsolo import RSCodec
    from pathlib import Path

    str1=""
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
    os.mkdir(user+'_encoded')
    os.chdir(user+'_encoded')
    fle=file_name+"_encode.bin"
    f = open(fle, "wb")

    f.write(parity_block)

    f.close()

    size = str(size_of_file)
    fli1=file_name+"_original_len.txt"
    
    f=open(fli1, "w")
    f.write(size)
    print('File is Encoded successfully')

def recover(file_name,user):
    import os
    from reedsolo import RSCodec
    from pathlib import Path
    # from encode import size_of_file
    os.chdir('./media/'+user+'_encoded')             #making and changing directories as per user
    fli = file_name+".txt"   
    fle=+file_name+"_encode.bin"

    f = open(fle, 'rb')

    parity=f.read()

    f.close()
    fle_s =file_name+"_original_len.txt"
    f = open(fle_s, 'r')
    size = f.read()
    os.chdir('../media')                #making and changing directories as per user
    os.mkdir(user+'recovered_file')            #making and changing directories as per user
    os.chdir(user+'recovered_file')            #making and changing directories as per user

    size_of_file = int(size)

    f.close()
    # print(parity)

    temp=""

    for i in range(size_of_file) :
        temp = temp + 'X'

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

    fli=file_name+".txt"
    f = open(fli, "w")
    f.write(data)

    print('File is decoded successfully')

    # print(data)
