def curren_conv():
    while True:
        try:
            how = int(input("\nHow many dollars you wanna convert? <Enter in numbers, without $ symbol> :"))
            break
        except:
            print("You did something wrong\nTry again...\n")
            continue
    with open('c_names.txt','r+') as f:
        n = f.read()
    print("\n"+n)
    in_what = input("So what's your choice <1 to 7> :")
    #if-elif-else starts here :)
    if in_what=='1':
        print("\n"+str(how)+"$ is equal to "+str(how*3.75)+" Saudi Riyal\n")
    elif in_what=='2':
        print("\n"+str(how)+"$ is equal to "+str(how*23192)+" Vietnamese Dong\n")
    elif in_what=='3':
        print("\n"+str(how)+"$ is equal to "+str(how*250.40)+" Yemeni Riyal\n")
    elif in_what=='4':
        print("\n"+str(how)+"$ is equal to "+str(how*75.11)+" Indian Rupee\n")
    elif in_what=='5':
        print("\n"+str(how)+"$ is equal to "+str(how*0.88)+" Euro\n")
    elif in_what=='6':
        print("\n"+str(how)+"$ is equal to "+str(how*167.45)+" Pakistani Rupee\n")
    elif in_what=='7':
        print("\n"+str(how)+"$ is equal to "+str(how*3.67)+" UAE Dirham\n")
    else:
        print("\nYou choice didn't exist\n")


print("\n<<<--- Welcome to Currency Converter --->>>\n")
while True:
    curren_conv()
    again = input("<Press r to run again> | <Any other key to quit> :")
    if again=='r' or again=='R':
        continue
    else:
        print("Exiting....")
        break