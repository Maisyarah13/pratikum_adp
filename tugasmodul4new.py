print("Selamat datang di sistem reservasi tiket konser")
m = 17
n = 5 
total_kursi = m * n

print("\nTampilan Layout Kursi")
for i in range(1, total_kursi+1):
    print(i, end=" ")
    if i % n == 0:
        print()  
        i = i + 1

print("\nHarga Tiket:")
print("VVIP    Rp 1.000.000")
print("VIP     Rp   800.000")
print("Reguler Rp   600.000")
print("Ekonomi Rp   300.000")

jumlah_pesanan=int(input("\nMasukkan jumlah tiket yang ingin dipesan : "))

pesanan_vvip = 0
pesanan_vip = 0
pesanan_reguler = 0
pesanan_ekonomi = 0
kosong = ","
for i in range(1, jumlah_pesanan + 1):
    print(f"\nPemesanan ke-{i}")
    nama = input("Masukkan nama Anda                       : ")
    no_kursi = int(input("Masukkan nomor kursi yang ingin dipesan  : "))
    if 1<=no_kursi<=10:
        kategori = "VVIP"
        harga_tiket = 1000000
        pesanan_vvip += 1
    elif 11<=no_kursi<=25:
        kategori = "VIP"
        harga_tiket = 800000
        pesanan_vip += 1
    elif 26<=no_kursi<=75:
        kategori = "Reguler"
        harga_tiket = 600000
        pesanan_reguler += 1
    elif 76 <= no_kursi <= 85 :
        kategori = "Ekonomi"
        harga_tiket = 300000
        pesanan_ekonomi += 1
    else : 
        kategori = "Kursi Tidak Tersedia"
        harga_tiket = 0
        print("Kursi Tidak Tersedia")

    password = input("Buat password untuk akses konser         : ")
    kosong = kosong + str(no_kursi) + ","
    print("\n=== Struk Pemesanan Tiket ===")
    print("Nama       :",nama)
    print("Nomor Kursi:",no_kursi)
    print("Kategori   :",kategori)
    print("Harga      :Rp",harga_tiket)
    print("Password   :",password)
    print("--------------------------------")

print("\nSisa kursi per kategori")
sisa_vvip = 10 - pesanan_vvip
sisa_vip = 15 - pesanan_vip
sisa_reguler = 50 - pesanan_reguler
sisa_ekonomi = 10 - pesanan_ekonomi

print("VVIP    : ",sisa_vvip)
print("VIP     : ",sisa_vip)
print("Reguler : ",sisa_reguler)
print("Ekonomi : ",sisa_ekonomi)

print("\nLayout Kursi Setelah Pemesanan:")
for j in range(1, 86):
    if f",{j},"  in kosong :
        print("0", end=" ")
    else:
        print(j, end=" ")
    if j % n == 0 :
        print()
    