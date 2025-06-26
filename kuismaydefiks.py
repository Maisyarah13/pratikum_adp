import os
import time
import msvcrt
from termcolor import cprint

def clear():
    os.system('cls' )

def efek_ketik(teks, kecepatan=0.07):
    for huruf in teks:
        print(huruf, end='', flush=True)
        time.sleep(kecepatan)
    print()

def countdown_timer(detik):
    for i in range(detik, 0, -1):
        clear()
        print("\n" * 3)
        cprint(f"{' ' * 10}⏳ {i} ...", "yellow", attrs=["bold"])
        time.sleep(1)
    clear()

soal_jawaban = [
    ["🐰 Usia bayi kelinci sekarang 154 hari. Ia lahir... minggu yang lalu.", ["22", "23", "21", "24"], "22"],
    ["📦 Panjang sisi kubus = 30 cm. Volume kubus (cm³)?", ["36.000", "27.000", "48.000", "56.000"], "27.000"],
    ["🔢 Jika 5x = 25, maka x = ?", ["5", "4", "3", "2"], "5"],
    ["🧠 f(x) = 2x² - 3x + 1. f(3) = ?", ["10", "11", "12", "13"], "10"],
    ["📝 Akar-akar persamaan x² - 5x + 6 = 0 adalah...", ["2 dan 3", "3 dan -2", "3 dan 4", "2 dan 4"], "2 dan 3"]
]
def tampilkan_soal(index, soal):
    cprint(f"\n📚 Soal {index + 1}: {soal[0]}", "cyan")

def tampilkan_pilihan(soal):
    label = ['A', 'B', 'C', 'D']
    for i in range(len(soal[1])):
        print(f" {label[i]}. {soal[1][i]}")

def ambil_input_timeout(timeout=7):
    print("\n✍️  Jawaban Anda (A/B/C/D atau Q untuk keluar): ", end='')
    start = time.time()
    input_str = ''
    while True:
        if msvcrt.kbhit():
            char = msvcrt.getwch()
            if char in ['\r', '\n']:
                break
            print(char, end='', flush=True)
            input_str += char
            if len(input_str) >= 1:
                break 
        if time.time() - start > timeout:
            print("\n⏰ Waktu habis!")
            return ""
    return input_str.upper()

def simpan_skor(nama, skor):
    with open("skor.txt", "a") as file:
        file.write(f"{nama}|{skor}\n")

def sudah_pernah_main(nama):
    if not os.path.exists("skor.txt"):
        return False
    with open("skor.txt", "r") as file:
        for line in file:
            if line.startswith(nama + "|"):
                return True
    return False

def tampilkan_peringkat():
    if not os.path.exists("skor.txt"):
        cprint("📭 Belum ada data skor yang tersimpan.", "red")
        return

    with open("skor.txt", "r") as file:
        lines = file.readlines()

    data = []
    for i in range(len(lines)):
        parts = lines[i].strip().split("|")
        if len(parts) == 2 and parts[1].isdigit():
            data.append((parts[0], int(parts[1])))

    data.sort(key=lambda x: x[1], reverse=True)

    print("\n🏆===== Peringkat Pemain =====🏆")
    print(f"{'No.':<4}{'Nama':<20}{'Skor':<5}")
    for i in range(len(data)):
        print(f"{i+1:<4}{data[i][0]:<20}{data[i][1]:<5}")
    print("================================\n")

def reset_peringkat():
    with open("skor.txt", "w") as file:
        file.write("")
    cprint("🧹 Data peringkat telah direset!", "yellow")

def mulai_kuis():
    skor = 0
    label = ['A', 'B', 'C', 'D']
    for i in range(len(soal_jawaban)):
        soal = soal_jawaban[i]

        tampilkan_soal(i, soal)
        time.sleep(5)
        clear()
        
        tampilkan_pilihan(soal)
        
        jawaban = ambil_input_timeout(7)

        if jawaban == "":
            jawaban_terpilih = "timeout"
        elif jawaban == "Q":
            cprint("🚪 Kuis dihentikan oleh pengguna.", "yellow")
            exit()
        elif jawaban in label:
            index_jawaban = label.index(jawaban)
            jawaban_terpilih = soal[1][index_jawaban]
        else:
            jawaban_terpilih = "tidak valid"

        benar = soal[2]
        print("\n🔎 Jawaban Anda:", end=" ")
        if jawaban_terpilih == benar:
            cprint(f"{jawaban_terpilih} ✅ Benar!", "green")
            skor += 1
        elif jawaban_terpilih == "timeout":
            cprint("⏰ Waktu habis ✘", "red")
            cprint(f"✔ Jawaban benar: {benar}", "green")
        elif jawaban_terpilih == "tidak valid":
            cprint("❗ Jawaban tidak valid ✘", "red")
            cprint(f"✔ Jawaban benar: {benar}", "green")
        else:
            cprint(f"{jawaban_terpilih} ❌ Salah", "red")
            cprint(f"✔ Jawaban benar: {benar}", "green")

        time.sleep(2)
        clear()
    return skor

def main():
    clear()
    efek_ketik("🎮 Selamat datang di MyDee Quiziz 🎉", kecepatan=0.06)
    time.sleep(0.5)

    cprint("\n📜 PERATURAN:", "yellow", attrs=["bold"])
    print("1️⃣  Anda hanya punya 5 detik untuk melihat soal.")
    print("2️⃣  Lalu Anda hanya punya 7 detik untuk mengetik jawaban.")
    print("3️⃣  Tekan A/B/C/D atau Q untuk keluar .")
    print("4️⃣  Gunakan nama yang belum pernah dipakai, jika ingin main lagi reset nama anda\n")
    print (input("✅ Tekan ENTER jika Anda sudah siap..."))

    nama = ""
    while True:
        nama = input("📝 Masukkan nama Anda: ").strip()
        if nama == "":
            continue
        if sudah_pernah_main(nama):
            cprint("🛑 Nama ini sudah pernah bermain. Masukkan nama yang berbeda.", "red")
        else:
            break

    clear()
    cprint("🚦 Bersiap ya! Kuis akan dimulai dalam...", "yellow")
    time.sleep(1.5)
    countdown_timer(5)

    skor_akhir = mulai_kuis()
    cprint(f"\n📊 Skor Akhir: {skor_akhir} dari {len(soal_jawaban)}", "cyan", attrs=["bold"])
    simpan_skor(nama, skor_akhir)
    tampilkan_peringkat()

    print("🧭 Apa yang ingin Anda lakukan selanjutnya?")
    print("1️⃣  Ulangi kuis")
    print("2️⃣  Reset peringkat")
    print("3️⃣  Keluar")

    pilihan = input("🔢 Masukkan pilihan (1/2/3): ")
    if pilihan == "1":
        clear()
        main()
    elif pilihan == "2":
        reset_peringkat()
        time.sleep(2)
        clear()
        main()
    else:
        cprint("\n👋 Terima kasih telah bermain! Sampai jumpa! ✨", "yellow", attrs=["bold"])

main()

