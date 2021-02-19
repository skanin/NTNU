def balance(book):
    book = book.split('\n')
    all_values_string = []
    all_values_float = []
    balances = []
    original_value = format(float("".join([c for c in book[0] if c.isdigit() or c == "."])), ".2f")
    items = []
    i = 0
    temp_balance = float(original_value)

    for elem in book:
        temp = []
        if elem != "" and elem != book[0]:
            temp = elem.split()
            all_values_string.append("".join([c for c in temp[2] if c.isdigit() or c == "."]))
            items.append("".join([c for c in temp[0] if c.isdigit()]))
            items[i] += " " + "".join([c for c in temp[1] if c.isalpha()])
            i += 1

    for elem in all_values_string:
        all_values_float.append(float(elem))
        balances.append('{0:.2f}'.format(float(temp_balance - float(elem))))
        temp_balance -= float(elem)

    total = sum(all_values_float)
    average = sum(all_values_float)/len(all_values_float)

    return_str = "Original Balance: " + original_value
    for i in range(len(items)):
        return_str += "\r\n" + items[i] + " " + '{0:.2f}'.format(all_values_float[i]) + " Balance " + balances[i]

    return_str += "\r\nTotal expense  " + '{0:.2f}'.format(float(total)) + "\r\nAverage expense  " + '{0:.2f}'.format(float(average))

    return return_str

b2="""1233.00
125 Hardware;! 24.8?;
123 Flowers 93.5
127 Meat 120.90
120 Picture 34.00
124 Gasoline 11.00
123 Photos;! 71.4?;
122 Picture 93.5
132 Tyres;! 19.00,?;
129 Stamps 13.6
129 Fruits{} 17.6
129 Market;! 128.00?;
121 Gasoline;! 13.6?;"""

b2sol = """Original Balance: 1233.00\r
125 Hardware 24.80 Balance 1208.20\r
123 Flowers 93.50 Balance 1114.70\r
127 Meat 120.90 Balance 993.80\r
120 Picture 34.00 Balance 959.80\r
124 Gasoline 11.00 Balance 948.80\r
123 Photos 71.40 Balance 877.40\r
122 Picture 93.50 Balance 783.90\r
132 Tyres 19.00 Balance 764.90\r
129 Stamps 13.60 Balance 751.30\r
129 Fruits 17.60 Balance 733.70\r
129 Market 128.00 Balance 605.70\r
121 Gasoline 13.60 Balance 592.10\r
Total expense  640.90\r
Average expense  53.41"""

print(balance(b2))
print("-----------------------------------------")
print(b2sol)
print()
print(balance(b2) == b2sol)