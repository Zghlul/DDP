#Nomer 1
print("Nomer 1")
def celcius(c):
    return (c * 9/5) + 32

print(celcius(0))    
print(celcius(100)) 

#Nomer 2
print("Nomer 2")
def genap(angka):
    return angka % 2 == 0

print(genap(4)) 
print(genap(7))

#Nomer 3
print("Nomer 3")
def nilai(n):
    if n >= 70:
        return "lulus"
    else:
        return "gagal"

print(nilai(80))  
print(nilai(60))  

#Nomer 4
print("Nomer 4")
def bilangan(n):
    for i in range(1, n):
        if i % 2 != 0:
            print(i, end=",")
            
bilangan(20) 

