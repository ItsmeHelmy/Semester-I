# Di sini kita mengecek kombinasi username dan password
# Menggunakan percabangan if else

user = "admin"
paswd = "python"

username = input("Masukkan Username : ")
password = input("Masukkan Password : ")

if (password == paswd) and (username == user):
    print("Kombinasi username dan password BENAR")
else:
    print("Kombinasi username dan password SALAH")