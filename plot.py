import matplotlib.pyplot as plt

data = []

with open("data.txt", "r") as f:
    f.readline()
    for x in f.readlines():
        spis = list(map(float, x.split()))
        data.append(spis[0])

print(77.47699)
print(77.47699/len(data))
print( len(data)/82 )

plt.plot(data, ".")
plt.show()

f.close()

