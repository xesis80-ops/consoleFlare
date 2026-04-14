def hamming(a,b):
    if len(a) != len(b):
        print("Strings should be of same lenght")
        return
    count=0
    for i in range(len(a)):
        if a[i] != b[i]:
            count+=1
    print (f"The hamming distance between both strings is {count}")
    
str1=input("Enter string 1:")
str2=input("Enter string 2:")
hamming(str1,str2)