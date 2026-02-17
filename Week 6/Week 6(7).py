data = ['a5', 'a2', 'b1', 'b3', 'c2']
sorted_data = sorted(data, key=lambda x: (x[0], int(x[1:])))
print(sorted_data)


