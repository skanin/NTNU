'''
a) tall_1, tall_2 og resultat kalles variabler.
b) Den ene feilen er at tall_2 må ha int(input()), ellers vet ikke python at et
    tall blir skrevet inn. En får da en error fordi det går ikke å heltallsdividere
    int på string. Retter man opp denne feilen, vil man få feilmelding når brukeren
    skriver inn en string.
    I tillegg vil en input av tallet 0 alltid gi en feilmelding, da det er matematisk
    ukorrekt å dele på 0.
c) Med koden som er nå, vil det skrives ut a:6 og b:3.
    Setter man a = 3 og b = 3 vil man få a:3 og b:6, da b<a = false og
    not b&a = 0 som gir true
'''
