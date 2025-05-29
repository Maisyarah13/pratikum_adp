def proses_data_praktikan():
    n = int(input("Masukkan jumlah praktikan: "))
    data = []

    for i in range(n):
        print(f"\nPraktikan ke-{i+1}")
        nama = input("Nama           : ")
        nim = input("NIM            : ")
        pretest = float(input("Nilai Pretest  : "))
        postest = float(input("Nilai Postest  : "))
        tugas = float(input("Nilai Tugas    : "))
        bonus = float(input("Nilai Bonus    : "))
        data.append([nama, nim, pretest, postest, tugas, bonus])
    
    for x in data:
        nilai_akhir = 0.25 * x[2] + 0.25 * x[3] + 0.5 * x[4] + x[5]
        x.append(nilai_akhir)
    
    n = len(data)
    for i in range(n):
        for j in range(0, n - i - 1):
            if data[j][6] < data[j + 1][6]:  
                data[j], data[j + 1] = data[j + 1], data[j]
    
    for i in range(len(data)):
        data[i].append(i + 1)
   
    print("-" * 54)
    print(f"{'Nama':<14} | {'NIM':<8}  | {'Nilai Akhir'} | {'Peringkat'} |")
    print("-" * 54)
    for d in data:
        print(f"{d[0]:<15}| {d[1]:<10}| {d[6]:<12.2f}| {d[7]}         |")
    
    total_akhir = 0
    for d in data:
        total_akhir += d[6]
    rata_akhir = total_akhir / len(data)

    print("-" * 54)
    print(f"{'Rata-rata Akhir':<26} |   {rata_akhir:<21.2f} |")
    print("-" * 54)
    
proses_data_praktikan()

