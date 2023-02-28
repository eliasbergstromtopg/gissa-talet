import random

print("\n /gissa talet\ \n")

print("gissa på ett tal och vinn en anka! Du har 3 försök. \n")

slumptal = random.randint(1,10)

#print(slumptal)

vinst = False

i=1 #antal gånger man får frågan, används i loopen

while i< 4:
    gissatalet = input("skriv in ett tal: ")
    #print("gissatalet=" + gissatalet)
    #print("slumptalet=" + str(slumtal))
    i = i + 1

if slumptal == int (gissatalet):
    print("grattis du vann en anka!")
    vinst = True
    break

if vinst==False
    print("tyvärr, du vann ingen anka denna gång!")