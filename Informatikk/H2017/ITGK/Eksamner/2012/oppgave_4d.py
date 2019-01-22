def create_db(temp, rain, humidity, wind):
    weather = {}
    for i in range(1, len(temp)+1):
        weather[i] = [temp[i-1], rain[i-1], humidity[i-1], wind[i-1]]

    return weather


temp = [1, 5, 3]
rain = [0, 30, 120]
humidity = [30, 50, 65]
wind = [3, 5, 7]

print(create_db(temp, rain, humidity, wind))
