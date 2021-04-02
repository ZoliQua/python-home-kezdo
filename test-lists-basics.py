
tombom = ['V', "C", "Ő", "O", "A", "K", "H"]
tombom.sort()
print(tombom)
print(tombom[2:2])

tomb2 = ['nem']

# utolso elem
print(tombom[-1])

# szeleteles (minusz első elem nélküli lista)
print(tombom[1:])

# multi dimenzios lista
tartomany = range(100)
print(list(tartomany))

for i in range(10):
    print("Szevasz", i)

fibo = [0,1]
[fibo.append(fibo[-2]+fibo[-1]) for i in range(50)]

