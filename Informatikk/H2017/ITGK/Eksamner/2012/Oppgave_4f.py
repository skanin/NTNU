def strange_weather(temp, rain):
    x = None
    y = None

    for i in range(len(temp)-1):
        if temp[i] < 0:
            if temp[i] < temp[i+1] and rain[i] < rain[i+1]:
                x = i
                if temp[i] > temp[i+1] and rain[i] > rain[i+1]:
                    y = i
                    return x, y
    return 0, 0

temp=[1,3, 4,-5,-6,-7,-8,-9,3,0]
rain=[0,20,30,0,10,30,50,0,5,2]

(start, stop) = strange_weather(temp, rain)

print("Start: " + str(start))
print("Stop: ", str(stop))
