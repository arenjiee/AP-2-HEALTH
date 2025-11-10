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

   