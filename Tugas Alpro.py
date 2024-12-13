N = int(input("Masukkan nilai N: "))
jumlah_genap = 0

for i in range(1, N + 1):
    if i % 2 == 0:
        jumlah_genap += 1

print("Jumlah bilangan genap dari 1 sampai", N, "adalah", jumlah_genap)

harga_barang = [50000, 30000, 80000]
total_belanja = 0
diskon = 0

for harga in harga_barang:
    total_belanja += harga

if total_belanja > 100000:
    diskon = total_belanja * 0.1
    total_belanja -= diskon

print("Total belanja:", total_belanja)
print("Diskon:", diskon)
