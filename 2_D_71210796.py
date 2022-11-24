k = input('Masukkan nama pemain pertama: ')
j = input('Masukkan nama pemain kedua: ')
w = input('Masukkan nama pemain ketiga: ')

K1 = int(input('Masukkan jumlah kartu pemain pertama: '))
K2 = int(input('Masukkan jumlah kartu pemain kedua: '))
K3= int(input('Masukkan jumlah kartu pemain ketiga: '))

if K1 > 21 or K2 > 21 or K3 > 21:
    print('Jumlah kartu yang dimiliki melebihi batas')
else:
    if K1 > K2 and K1 > K3:
        print(K1,'menang dengan jumlah kartu sebanyak',K1)
    elif K2 > K1 and K2 > K3:
        print(K2,'menang dengan jumlah kartu sebanyak',K2)
    elif K3 > K1 and K3 > K2:
        print(K3,'menang dengan jumlah kartu sebanyak',K3)