#a
r = 5
print("Vi har en sirkel med radius" + str(r))
omkrets = 2 * 3.14 * r
print("Omkretsen er", omkrets)
areal = 3.14 * r**2
print("Arealet er", areal)
h = 8
volum = areal * h
print("Sylinder med høyde", h, ": Volumet er", volum)


#b
r = 5
print("Vi har en sirkel med radius " + str(r))
omkrets = 2 * 3.14 * r
print("Omkretsen er", format(omkrets, '.2f'))
areal = 3.14 * r**2
print("Arealet er", format(areal, '.2f'))
h = 8
volum = areal * h
print("Sylinder med høyde", h, ": Volumet er", format(volum, '.2f'))
