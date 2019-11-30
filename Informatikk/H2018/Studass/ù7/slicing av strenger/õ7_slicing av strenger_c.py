
#Kodesnutt 1
#streng = "I Want Cake"
#streng[7:] = "Cupcake"   #streng er ikke en list fra før.
#print(streng)

streng = "I Want Cake"
strengList = streng.split()
strengList.pop()
strengList.append('Cupcake')
streng = ' '.join(strengList)
print(streng)



#Kodesnutt 2   #rett
streng = "I Want Cake"
streng = streng[-4:100:]
print(streng)



#Kodesnutt 3
#streng = "I Want Cake"
#streng = streng[]   #streng er ikke en liste
#print(streng)

streng = "I Want Cake"
strengList = streng.split()
print(strengList)
