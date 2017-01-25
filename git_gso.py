#Hákon Haraldsson
#GSÖ2
#25.1.2017
texti = input("Hvað viltu að skráin heiti? ")
texti = texti + ".txt"
y = open(texti,"w+")
y.write("Gert af Hákoni Haraldssyni\n")       #Skrifar texta
y.close()                                   #Lokar skránni
y=open(texti,"a")
innihald = input("Hvað viltu að skráin inniheldur? ")
for i in range(0,3):
    y.write(innihald+"\n")
y.close()
