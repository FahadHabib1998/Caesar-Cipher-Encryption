#Forming a dictionary where each alphabet/digit coressponds to the alphabet/digit according to ROT-13 and ROT-5  
def form():
    dic={}
    dic[" "]= " "
    for i in range(ord("A"),ord("Z")+1):
        newi = i
        shift = newi+13
        if shift > ord('Z'):
            shift=shift-26
            dic[chr(i)] = chr(shift)
        else:
            dic[chr(i)] = chr(shift)
    for i in range(ord("a"),ord("z")+1):
        newi = i
        shift = newi+13
        if shift > ord('z'):
            shift=shift-26
            dic[chr(i)] = chr(shift)
        else:
            dic[chr(i)] = chr(shift)
    for i in range(ord("0"),ord("9")+1):
        newi = i
        shift = newi+5
        if shift > ord('9'):
            shift=shift-10
            dic[chr(i)] = chr(shift)
        else:
            dic[chr(i)] = chr(shift)
    return(dic)


#Decoding and Encoding
def DeEn(word):
    dic=form()
    new=""
    for i in word:
        if i >="a" and i<="z" or i >="A" and i<="Z" or i >="0" and i<="9":
            new+=dic[i]
        else:
            dic[i]=i
            new+=dic[i]
    return new


run = True
while run:
    ch=input("\t Menu \t\n1.Decode a encryption text\n2.Encode a encryption text\n3.Exit\nEnter Choice: ")
    if ch == "1" or ch == "2":
        wor = input("Enter the phase:")
        print(DeEn(wor))
    elif ch == "3":
        run = False
    else:
        print("\nPlease Enter a Valid Option.\n")



            
                    
                
                
                
            
            
            
            
    

    
