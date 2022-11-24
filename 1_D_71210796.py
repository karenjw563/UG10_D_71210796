print("\(^o^ Selamat datang di Kalkulator Sederhana (^o^)/")
print("Ketik 1 untuk menghitung penjumlahan.")
print("Ketik 2 untuk menghitung pengurangan.")
print("Ketik 3 untuk menghitung perkalian.")
print("Ketik 4 untuk menghitung pembagian.")
print("Ketik 5 untuk menghitung sisa hasil bagi(modulus).")
print("Ketik 6 untuk menghitung pemangkatan")
    
pilihan = input("Masukkan pilihan Anda: ")

a = int(input("Masukkan bilangan pertama: "))
b = int(input("Masukkan bilangan kedua: "))

if pilihan == "1":
    print("Hasil dari", a, "dijumlahkan dengan", b, "adalah", a+b)
elif pilihan == "2":
    print("Hasil dari", a, "dikurangkan dengan", b, "adalah", a-b)
elif pilihan == "3":
    print("Hasil dari", a, "dikalikan dengan", b, "adalah", a*b)
elif pilihan == "4":
    print("Hasil dari", a, "dibagi dengan", b, "adalah", a/b)
elif pilihan == "5":
    print("Hasil dari", a, "dimodulus dengan", b, "adalah", a%b)
elif pilihan == "6":
    print("Hasil dari", a, "dipangkatkan dengan", b, "adalah", a**b)
else:
    print("Invalid Input")