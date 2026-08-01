while(True):
    def hashidx(ascii_val,table):
        hash_idx=ascii_val%table
        print (hash_idx)
        return hash_idx
    key=input("Enter your name:")
    table=int(input("enter no of tables:"))
    ascii_val=sum(ord(i) for i in key)
    print(ascii_val)

    hashidx(ascii_val,table)


    def hash_idx(key,table):
        hash_idx=key%table
        print (hash_idx)
        return hash_idx
    key=int(input("Enter Roll no:"))
    table=int(input("enter no of tables:"))
    hash_idx(key,table)

    dec=input("Do you want to continue? (y/n): ")
    if dec== 'n' or dec== 'N':
        break
