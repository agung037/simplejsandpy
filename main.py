from tabulate import tabulate

# Soal 1
x = input("masukan nama kota: ")
for i in range(len(x)): print(x[i:])

# Soal 2
n = int(input("masukan ketinggian: "))
for i in range(n, 0, -1): print("*"*i)

# Soal 3
result = []
for i in range(10,101,10): result.append([i, i*1.8+32, i*0.8])
print(tabulate(result, headers=["°C", "°F", "°R"]))