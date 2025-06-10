filename = "data_keuangan.txt"
data = []

open(filename, "a").close()
f = open(filename, "r")
for line in f:
    parts = line.strip().split("|")
    if len(parts) == 4:
        data.append({"tanggal": parts[0], "keterangan": parts[1], "jumlah": int(parts[2]), "tipe": parts[3]})
f.close()

while True:
    print("1. Tambah\n2. Hapus\n3. Tampil\n4. Keluar")
    pilih = input("Pilih: ")
    if pilih == "1":
        t = input("Tanggal: ")
        k = input("Keterangan: ")
        j = input("Jumlah: ")
        tipe = input("Tipe: ")
        data.append({"tanggal": t, "keterangan": k, "jumlah": int(j), "tipe": tipe})
        f = open(filename, "w")
        for d in data:
            f.write(f"{d['tanggal']}|{d['keterangan']}|{d['jumlah']}|{d['tipe']}\n")
        f.close()
    elif pilih == "2":
        if len(data) == 0:
            print("Data kosong")
            continue
        for i in range(len(data)):
            d = data[i]
            print(f"{i+1}. {d['tanggal']} {d['keterangan']} Rp{d['jumlah']} {d['tipe']}")
        h = input("Hapus nomor: ")
        data.pop(int(h)-1)
        f = open(filename, "w")
        for d in data:
            f.write(f"{d['tanggal']}|{d['keterangan']}|{d['jumlah']}|{d['tipe']}\n")
        f.close()
    elif pilih == "3":
        if len(data) == 0:
            print("Data kosong")
        else:
            for i in range(len(data)):
                d = data[i]
                print(f"{d['tanggal']} {d['keterangan']} Rp{d['jumlah']} {d['tipe']}")
    elif pilih == "4":
        print("Terimakasih telah menggunakan program ini")
        break