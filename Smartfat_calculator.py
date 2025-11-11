# smartfat calculator: pengguna dapat menghitung kadar lemak dalam tubuh dalam bentuk persen (WHO/ACSM)

import re

# validasi inputan: gender, usia, berat badan, tinggi badan
def validasi_gender():
    while True:
        gender = input("Masukkan jenis kelamin (L/P atau Laki-laki/Perempuan): ").strip().lower()
        if gender in ["l", "laki", "laki-laki", "laki laki"]:
            return "L"
        elif gender in ["p", "perempuan"]:
            return "P"
        else:
            print("⚠️ Masukkan hanya 'L' untuk laki-laki atau 'P' untuk perempuan ⚠️\n")

def validasi_usia():
    while True:
            usia = input("Masukkan usia anda (tahun): ")
            if re.fullmatch(r"\d+", usia):
                usia = int(usia)
                if usia > 99:
                    print ("⚠️ PERHITUNGAN HANYA SAMPAI USIA 99 TAHUN ⚠️\n")
                else:
                    return usia
            else:
                print ("⚠️ INPUTAN HARUS ANGKA DAN POSITIF ⚠️\n")
    
def validasi_bb():
    while True:
        bb = input("Masukkan berat badan anda (Kg): ")
        if re.fullmatch(r"\d+(\.\d+)?", bb) and float(bb) > 0:
                return float(bb)
        else:
           print ("⚠️ INPUTAN HANYA BOLEH ANGKA DAN POSITIF ⚠️\n")

def validasi_tb():
    while True:
        tb = input("Masukkan tinggi badan anda (Cm): ")
        if re.fullmatch(r"\d+(\.\d+)?", tb) and float(tb) > 0:
                    return float(tb)
        else:
            print ("⚠️ INPUTAN HANYA BOLEH ANGKA DAN POSITIF ⚠️\n")
    
def smartfat_calcu():
    print("\n=== SmartFat Calculator ===")
    print("Selamat Datang👋🤩🎉")
    print("Masukkan data diri Anda untuk menghitung persentase lemak tubuh\n")

    jenis_kelamin = validasi_gender()
    umur = validasi_usia()
    berat = validasi_bb()
    tinggi = validasi_tb()

    tinggi_m = tinggi / 100
    bmi = berat / tinggi_m**2
    jk = 1 if jenis_kelamin == "L" else 0

    bodyfat = (1.20 * bmi) + (0.23 * umur) - (10.8 * jk) - 5.4

    if jenis_kelamin == "L":
        ok = "Laki laki"
        if umur < 6:
            kategori = "Tidak dapat dipastikan"

        elif  6 <= umur <= 12:
            if bodyfat < 11:
                kategori = "Essential Fat (Sangat rendah)"
            elif bodyfat < 19:
                kategori = "Sehat"
            elif bodyfat < 25:
                kategori = "Kelebihan berat badan"
            else:
                kategori = "Obesitas"
        elif  13 <= umur <= 17:
            if bodyfat < 9:
                kategori = "Essential Fat (Sangat rendah)"
            elif bodyfat < 17:
                kategori = "Sehat"
            elif bodyfat < 23:
                kategori = "Kelebihan berat badan"
            else:
                kategori = "Obesitas"
        elif 18 <= umur <= 39:
            if bodyfat < 6:
                kategori = "Essential Fat (Sangat rendah)"
            elif bodyfat < 18:
                kategori = "Bugar (Fitness)"
            elif bodyfat < 25:
                kategori = "Sehat"
            else: 
                kategori = "Obesitas"
        elif 40 <= umur <= 59:
            if bodyfat < 11:
                kategori = "Essential Fat (Sangat rendah)"
            elif bodyfat < 18:
                kategori = "Bugar (Fitness)"
            elif bodyfat < 27:
                kategori = "Sehat"
            else: 
                kategori = "Obesitas"
        else:
            if umur >= 60:
                if bodyfat < 13:
                    kategori = "Essential Fat (Sangat rendah)"
                elif bodyfat < 21:
                    kategori = "Bugar (Fitness)"
                elif bodyfat < 28:
                    kategori = "Sehat"
                else: 
                    kategori = "Obesitas"
        
    else: 
        ok = "Perempuan"
        if umur < 6:
            kategori = "Tidak dapat dipastikan"
        elif  6 <= umur <= 12:
            if bodyfat < 15:
                kategori = "Essential Fat (Sangat rendah)"
            elif bodyfat < 25:
                kategori = "Sehat"
            elif bodyfat < 30:
                kategori = "Kelebihan berat badan"
            else:
                kategori = "Obesitas"
        elif  13 <= umur <= 17:
            if bodyfat < 16:
                kategori = "Essential Fat (Sangat rendah)"
            elif bodyfat < 28:
                kategori = "Sehat"
            elif bodyfat < 33:
                kategori = "Kelebihan berat badan"
            else:
                kategori = "Obesitas"
        elif 18 <= umur <= 39:
            if bodyfat < 18:
                kategori = "Essential Fat (Sangat rendah)"
            elif bodyfat < 28:
                kategori = "Bugar (Fitness)"
            elif bodyfat < 37:
                kategori = "Sehat"
            else: 
                kategori = "Obesitas"
        elif 40 <= umur <= 59:
            if bodyfat < 18:
                kategori = "Essential Fat (Sangat rendah)"
            elif bodyfat < 30:
                kategori = "Bugar (Fitness)"
            elif bodyfat < 40:
                kategori = "Sehat"
            else: 
                kategori = "Obesitas"
        elif umur >= 60:
            if bodyfat < 14:
                kategori = "Essential Fat (Sangat rendah)"
            elif bodyfat < 22:
                kategori = "Bugar (Fitness)"
            elif bodyfat < 28:
                kategori = "Sehat"
            else: 
                kategori = "Obesitas"

    print("\n=== Hasil SmartFat Calculator ===")
    print(f"Jenis Kelamin : {ok}")
    print(f"Usia          : {umur} tahun")
    print(f"Berat Badan   : {berat:.1f} kg")
    print(f"Tinggi Badan  : {tinggi:.1f} cm")
    print(f"BMI           : {bmi:.2f}")
    print(f"Body Fat (%)  : {bodyfat:.1f}%")
    print(f"Kategori      : {kategori}")

    if "Essential Fat (Sangat rendah)" in kategori:
        print("Silakan konsultasi kesehatan Anda ke dokter! 😔")
    elif "Obesitas" in kategori:
        print("Kurangi asupan kalori dan rutin berolahraga 🏃🏃\nSemangat 🤩😊")
    elif "Tidak dapat dipastikan" in kategori:
            print("Silakan konsultasikan kepada dokter anak untuk mengetahui lebih lanjut 👶👧")
    else:
        if "Bugar (Fitness)" in kategori or "Sehat" in kategori:
            print("Pertahankan pola hidup sehat dan seimbang 💪💪")

def fitur_2():
    while True:
        smartfat_calcu()
        while True:
            lagi = input("\nIngin menghitung lagi? (y/n): ").lower()
            if lagi == "y":
                break
            elif lagi == "n":
                print("\nTerima kasih telah menggunakan SmartFat Calculator 🤩 ")
                print("Tetap jaga kesehatan dan semangat! 👋")
                return
            else:
                print("\n⚠️ Input tidak valid! Masukkan hanya 'y' untuk ya atau 'n' untuk tidak ⚠️\n")