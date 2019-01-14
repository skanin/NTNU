cheeses = {
'cheddar':
('A235-4', 'A236-1', 'A236-2', 'A236-3', 'A236-5', 'C31-1', 'C31-2'),
'mozarella':
('Q456-9', 'Q456-8', 'A234-5', 'Q457-1', 'Q457-2'),
'gombost':
('ZLAFS55-4', 'ZLAFS55-9', 'GOMBOS-7', 'A236-4'),
'geitost':
('SPAZ-1', 'SPAZ-3', 'EMACS45-0'),
'port salut':
('B15-1', 'B15-2', 'B15-3', 'B15-4', 'B16-1', 'B16-2', 'B16-4'),
'camembert':
('A243-1', 'A234-2', 'A234-3', 'A234-4', 'A235-1', 'A235-2', 'A235-3'),
'ridder':
('GOMBOS-4', 'B16-3'),
}

print("Port Salut:", cheeses["port salut"])
infected_cheeses = []
hylleplasser = ["B15-1", "B15-2", "B15-3", "B15-4", "A234-1", "A234-2", "A234-3", "A234-4", "A234-5", "A235-1",
                "A235-2", "A235-3", "A325-4" "C31-1", "C31-2"]


for x in cheeses:
    for i in range(len(hylleplasser)):
        if hylleplasser[i] in cheeses[x]:
            if x in infected_cheeses:
                pass
            else:
                infected_cheeses.append(x)

print("Potentially infected cheeses:", infected_cheeses)

not_infected = []

for x in cheeses:
    if x not in infected_cheeses:
        not_infected.append(x)

for x in not_infected:
    liste = list(cheeses[x])
    for y in liste:
        print("('" + str(y) + "') '" + str(x) + "'")
