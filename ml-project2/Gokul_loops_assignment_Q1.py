temperatures = [28, 32, 35, 29, 31, 27, 30]
highest = temperatures[0]
lowest = temperatures[0]
    if temp > highest:
        highest = temp
    if temp < lowest:
        lowest = temp
print("Highest Temperature:", highest, "°C")
print("Lowest Temperature:", lowest, "°C")
