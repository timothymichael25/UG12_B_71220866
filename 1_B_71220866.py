print("SELAMAT DATANG DI PROGRAM PEMBUATAN PIRAMIDA BERLUBANG")
b = int(input("Masukan Angka: "))
print(' '*(b-2),"*")
for c in range ((b-2),0,-1):
    print(' '*(c-1),"**")
print ("**"*b)

