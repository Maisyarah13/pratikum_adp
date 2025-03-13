print("                           *SELAMAT DATANG*                               ")
print("                                  di                                      ")
print("                            'KAFE SADIRMA'                                ")
print("--------------------------------------------------------------------------")
print("                     PAKET HEMAT BERBUKA RAMADHAN                         ")
print("--------------------------------------------------------------------------")
print("PAKET                          ISI                                   HARGA")
print("Hemat 1             Nasi telur dadar,es teh,takjil                Rp.25000")
print("Hemat 2             Nasi putih,Soto,es teh,takjil                 RP.30000")
print("Reguler A           Nasi putih,Ayam cabe hijau,eh teh,takjil      RP.35000")
print("Reguler B           Nasi putih,Ayam cabe merah,es jeruk,takjil    Rp.40000")
print("Reguler C           Nasi putih,Pecel Ayam,lemon tea,takjil        RP.45000")
print("--------------------------------------------------------------------------")
print()


#Masukkan detail pemesanan
print("Pemesanan Anda")
nama = input("Nama                      : ")
no_telepon =int(input("No telepon                : "))
alamat_pemesanan = input("Alamat Pemesanan          : ")
paket_yang_dipesan = input("Paket yang dipesan        : ")
jumlah_paket_yang_dipesan = int(input("Jumlah paket yang dipesan : "))
print()

#Masukkan harga satuan
Hemat_1 = 25000
Hemat_2 = 30000
Reguler_A = 35000
Reguler_B = 40000
Reguler_C = 45000

#Menentukan pesanan dan harga
if paket_yang_dipesan == "Hemat 1" :
    p = ("Nasi telur dadar,es teh,takjil")
    Total_harga = jumlah_paket_yang_dipesan*Hemat_1
elif paket_yang_dipesan == "Hemat 2" :
    p = ("Nasi putih,Soto,es teh,takjil")
    Total_harga = jumlah_paket_yang_dipesan*Hemat_2
elif paket_yang_dipesan == "Reguler A" :
    p = ("Nasi putih,Ayam cabe hijau,eh teh,takjil")
    Total_harga = jumlah_paket_yang_dipesan*Reguler_A
elif paket_yang_dipesan == "Reguler B" :
    p = ("Nasi putih,Ayam cabe merah,es jeruk,takjil")
    Total_harga = jumlah_paket_yang_dipesan*Reguler_B
elif paket_yang_dipesan == "Reguler C" :
    p = ("Nasi putih,Pecel Ayam,lemon tea,takjil")
    Total_harga = jumlah_paket_yang_dipesan*Reguler_C


#menentukan pajak
pajak = Total_harga*(10/100)

#menentukan biaya pengiriman
if Total_harga<150000:
    Biaya_pengiriman = 25000
else : #harga>=150000
    Biaya_pengiriman = 0

#menentukan total harga
Total_Akhir = Total_harga+pajak+Biaya_pengiriman

#menampilkan hasil
print("                           'Struk Pemesanan'                               ")

print("Nama                                         :", nama)
print("No telepon                                   :", no_telepon)
print("Alamat Pemesanan                             :", alamat_pemesanan)
print("Paket yang dipesan                           :", paket_yang_dipesan)
print("Jumlah paket yang dipesan                    :", jumlah_paket_yang_dipesan)
print("Pajak                                        :", pajak)
print("Biaya pengiriman                             :", Biaya_pengiriman)
print("Total Akhir                                  :", Total_Akhir)


print("                           '-'Terimakasih'-'                               ")