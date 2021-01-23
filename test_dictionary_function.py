day_data = ['October 15', 'October 14', 'October 16', 'October 14', 'October 14', 'October 14']
cal_data = [1, 54, 2, 8, 6, 7]
dictionary = {}
for count in range(len(day_data)):
    if day_data[count] in dictionary:
        dictionary[day_data[count]] += cal_data[count]
    else:
        dictionary[day_data[count]] = cal_data[count]

print(list(dictionary.values()))

