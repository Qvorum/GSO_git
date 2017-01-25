#Hákon Haraldsson
#GSÖ2
#25.1.2017
texti = input("Hvað viltu að skráin heiti? ")
y = open(texti +".txt","w+")
y.write("Gert af Hákoni Haraldssyni")       #Skrifar texta
y.close()                                   #Lokar skránni
