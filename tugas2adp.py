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
hemat_1 = 25000
hemat_2 = 30000
reguler_A = 35000
reguler_B = 40000
reguler_C = 45000

#Menentukan pesanan dan harga
if paket_yang_dipesan == "Hemat 1" :
    p = ("Nasi telur dadar,es teh,takjil")
    total_harga = jumlah_paket_yang_dipesan*hemat_1
elif paket_yang_dipesan == "Hemat 2" :
    p = ("Nasi putih,Soto,es teh,takjil")
    total_harga = jumlah_paket_yang_dipesan*hemat_2
elif paket_yang_dipesan == "Reguler A" :
    p = ("Nasi putih,Ayam cabe hijau,eh teh,takjil")
    total_harga = jumlah_paket_yang_dipesan*reguler_A
elif paket_yang_dipesan == "Reguler B" :
    p = ("Nasi putih,Ayam cabe merah,es jeruk,takjil")
    total_harga = jumlah_paket_yang_dipesan*reguler_B
elif paket_yang_dipesan == "Reguler C" :
    p = ("Nasi putih,Pecel Ayam,lemon tea,takjil")
    total_harga = jumlah_paket_yang_dipesan*reguler_C


#menentukan pajak
pajak = total_harga*(10/100)

#menentukan biaya pengiriman
if total_harga<150000:
    biaya_pengiriman = 25000
else : #harga>=150000
    biaya_pengiriman = 0

#menentukan total harga
total_akhir = total_harga+pajak+biaya_pengiriman

#menampilkan hasil
print("                           'Struk Pemesanan'                               ")

print("Nama                                         :", nama)
print("No telepon                                   :", no_telepon)
print("Alamat Pemesanan                             :", alamat_pemesanan)
print("Paket yang dipesan                           :", paket_yang_dipesan)
print("Jumlah paket yang dipesan                    :", jumlah_paket_yang_dipesan)
print("Total harga                                  :", total_harga)
print("Pajak                                        :", pajak)
print("Biaya pengiriman                             :", biaya_pengiriman)
print("Total Akhir                                  :", total_akhir)


print("                           '-'Terimakasih'-'                               ")