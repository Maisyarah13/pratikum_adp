nomor_mahasiswa=[]
nama_mahasiswa=[]
nilai_mahasiswa =[]
x = True
while x :
    print("=== MENU MANAJEMEN NILAI MAHASISWA ===")
    print(" 1. Tambah data")
    print(" 2. Hapus data")
    print(" 3. Tampilkan data")
    print(" 4. Keluar")
    print()
    pilihan =int(input("Inputkan pilihan : "))
    print()
    if pilihan == 1 :
        print("*Tambahkan data mahasiswa*")
        print("--------------------------")
        no = int(input("Nomor mahasiswa : "))
        nama = (input("Nama mahasiswa  : "))
        nilai = float(input("Nilai mahasiswa : "))

        nomor_mahasiswa.append(no)
        nama_mahasiswa.append(nama)
        nilai_mahasiswa.append(nilai)
        print("---------------------------")
        print("*Data berhasil ditambahkan*")
        print()
    elif pilihan == 2:
        print("*Hapus data mahasiswa*")
        print("----------------------")
        no_hapus = int(input("Masukkan nomor mahasiswa yang akan dihapus: "))
        ditemukan = False
        for i in range(len(nomor_mahasiswa)):
            if nomor_mahasiswa[i] == no_hapus:
                del nomor_mahasiswa[i]
                del nama_mahasiswa[i]
                del nilai_mahasiswa[i]
                ditemukan = True
                print("*Data berhasil dihapus*\n")
                break
        if ditemukan == False:
            print("*Data tidak ditemukan*\n")

    elif pilihan == 3 : 
        print("                   Data mahasiswa                   ")
        print("----------------------------------------------------")
        print(f"|{'No Mahasiswa':<15} | {'Nama Mahasiswa':>15} | {'Nilai Mahasiswa':<15}|")
        print("----------------------------------------------------")
        if len(nomor_mahasiswa) == 0:
            print("Belum ada data.\n")
        else:
            gabungan = []
            for i in range(len(nomor_mahasiswa)):
                gabungan.append((nomor_mahasiswa[i], nama_mahasiswa[i], nilai_mahasiswa[i]))
            n = len(gabungan)
            batas = n
            while batas > 1 :
                for i in range(batas -1) :
                    if gabungan[i][2] < gabungan[i+1][2]:
                        temp = gabungan[i]
                        gabungan[i] = gabungan[i+1]
                        gabungan[i+1] = temp
                batas -=1
            for data in gabungan:
                print(f"|{data[0]:<15} | {data[1]:<15} | {data[2]:<15}|")
            print()
    elif pilihan == 4 :
        print("Terima kasih telah menggunakan program ini")
        print("------------------------------------------")
        x = False
    else :
        print("Pilihan tidak valid , silahkan coba lagi")

                
       

