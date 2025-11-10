# smartfat calculator: pengguna dapat menghitung kadar lemak dalam tubuh dalam bentuk persen (WHO/ACSM)

import re

# validasi inputan: gender, usia, berat badan, tinggi badan
def validasi_gender():
    while True:
        gender= input("Masukan jenis kelamin (L/P): ").strip().upper()
        if re.fullmatch(r"[LP]", gender):
            return gender
        else:
            print("⚠️ Inputan tidak valid! Masukkan 'L' untuk laki-laki atau 'P' untuk perempuan.\n")    

def validasi_usia():
    while True:
            usia = input("Masukkan usia anda (tahun): ")
            if re.fullmatch(r"[1-9]|[1-9][1-9]|[1-9][1-9][1-9]", usia):
                usia = int(usia)
                if usia > 99:
                    print ("⚠️ PERHITUNGAN HANYA SAMPAI USIA 99 TAHUN ⚠️\n")
                    continue
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

   