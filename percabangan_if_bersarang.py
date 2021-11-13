# Di sini kita mengecek bilangan yang dimasukan
# apakah lebih besar atau lebih kecil
# Menggunakan percabangan if bersarang

x = 23
y = 20

if x == y:
    print(x, "mempunyai nilai yang sama dengan", y)
else: 
    if x > y:
        print(x, "lebih besar dari", y)
    else:
        print(x, "lebih kecil dari", y)