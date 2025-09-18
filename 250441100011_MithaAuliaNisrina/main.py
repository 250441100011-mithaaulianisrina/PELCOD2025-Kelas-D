#soal ke-1
nama = "Mitha Aulia Nisrina"
umur = "19tahun"
tinggi = "148cm"
angka_favorit = "5"

print(f"{nama}, {umur}, {tinggi }, {angka_favorit}")

#soal ke-2
pensil = 4
buku = 2

harga_pensil = 2000
harga_buku = 5000

total_pensil = pensil * harga_pensil
total_buku = buku * harga_buku
total = total_pensil + total_buku

print(f"total harga {pensil} pensil = Rp{total_pensil}")
print(f"total harga {buku} buku = Rp{total_buku}")
print(f"total yang harus dibayar Rp{total}")

#soal ke-3
angka_favorit = 5

if angka_favorit % 2 == 0:
    print(angka_favorit, "adalah angka genap")
else:
    print(angka_favorit, "adalah angka ganjil")