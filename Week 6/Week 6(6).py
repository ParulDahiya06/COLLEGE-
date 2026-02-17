data = []

for i in range(5):
    data.append(lambda a, i=i*2: i * a)

for j in range(5):
    print(data[j](10))