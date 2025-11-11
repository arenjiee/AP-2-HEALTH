def fitur_3():
    print("\n===== HealthCheck =====")
    print("Cek kesehatan berdasarkan kegiatan harianmu!!\n")

    while True:
        try:
            usia = int(input("Masukkan usia (tahun): "))
            if usia <= 0:
                print("⚠ Usia tidak valid! Masukkan angka lebih dari 0.\n")
                continue
            break
        except ValueError:
            print("⚠ Masukkan angka yang valid untuk usia.\n")

    while True:
        try:
            tidur = int(input("Masukkan durasi tidur (jam): "))
            if tidur <= 0:
                print("⚠ Durasi tidur tidak valid! Masukkan angka lebih dari 0.\n")
                continue
            break
        except ValueError:
            print("⚠ Masukkan angka yang valid untuk durasi tidur.\n")

    while True:
        try:
            air_float = input("Masukkan jumlah air yang diminum hari ini (liter): ").replace(",", ".")
            air = float(air_float)
            if air <= 0:
                print("⚠ Jumlah konsumsi air tidak valid! Masukkan angka lebih dari 0.\n")
                continue
            break
        except ValueError:
            print("⚠ Masukkan angka yang valid untuk jumlah konsumsi air.\n")

    while True:
        try:
            olahraga = int(input("Masukkan durasi olahraga hari ini (menit): "))
            if olahraga <= 0:
                print("⚠ Durasi olahraga tidak valid! Masukkan angka lebih dari 0.\n")
                continue
            break
        except ValueError:
            print("⚠ Masukkan angka yang valid untuk durasi olahraga.\n")

    print("\n=== Ringkasan Kegiatan Hari Ini ===")
    print(f"Usia kamu: {usia} tahun")
    print(f"Durasi tidur: {tidur} jam")
    print(f"Asupan air harian: {air} liter")
    print(f"Durasi olahraga: {olahraga} menit\n")

#perhitungan dan hasil kesehatan harian
#tidur
    if 1 <= usia <= 5:
        print("Untuk usia 1–5 tahun, kebutuhan tidur bisa berbeda tiap anak. Disarankan konsultasi ke dokter anak.")
    elif 6 <= usia <= 17:
        if tidur < 8:
            print("Kamu kurang tidur. Idealnya 8–10 jam per hari.")
        elif 8 <= tidur <= 10:
            print("Durasi tidur kamu sudah sesuai. Pertahankan!")
        else:
            print("Tidur kamu melebihi batas ideal.")
    elif 18 <= usia <= 59:
        if tidur < 7:
            print("Tidur kamu kurang. Idealnya 7–9 jam.")
        elif 7 <= tidur <= 9:
            print("Tidur kamu cukup sesuai anjuran.")
        else:
            print("Tidur kamu terlalu lama.")
    else:
        if tidur < 7:
            print("Kamu kurang tidur. Idealnya 7–8 jam.")
        elif 7 <= tidur <= 8:
            print("Tidur kamu cukup untuk lansia.")
        else:
            print("Tidur kamu terlalu lama untuk lansia.")

#air
    if 1 <= usia <= 5:
        print("Untuk anak usia 1–5 tahun, kebutuhan air berbeda tergantung berat badan dan aktivitas. Disarankan konsultasi ke dokter anak.")
    elif 6 <= usia <= 17:
        if air < 1.5:
            print("Kamu kurang minum. Idealnya 1.5–2.5 liter per hari.")
        elif 1.5 <= air <= 2.5:
            print("Asupan air kamu cukup.")
        else:
            print("Kamu minum terlalu banyak.")
    elif 18 <= usia <= 59:
        if air < 2:
            print("Kamu kurang minum. Idealnya 2–2.5 liter per hari.")
        elif 2 <= air <= 2.5:
            print("Asupan air kamu cukup.")
        else:
            print("Kamu minum berlebihan.")
    else:
        if air < 1.5:
            print("Kamu kurang minum. Idealnya 1.5–2 liter per hari.")
        elif 1.5 <= air <= 2:
            print("Asupan air kamu sudah cukup untuk lansia.")
        else:
            print("Kamu minum terlalu banyak.")

#olahraga
    if 1 <= usia <= 5:
        print("Untuk anak usia 1–5 tahun, aktivitas fisik sebaiknya berbentuk bermain aktif. Konsultasikan ke dokter anak untuk durasi yang tepat.")
    elif 6 <= usia <= 17:
        if olahraga < 60:
            print("Kamu kurang olahraga. Minimal 60 menit per hari untuk remaja.")
        elif 60 <= olahraga <= 90:
            print("Durasi olahraga kamu cukup untuk remaja.")
        elif 90 < olahraga <= 120:
            print("Olahraga kamu aktif dan masih dalam batas aman.")
        else:
            print("Durasi olahraga kamu berlebihan. Maksimal 120 menit per hari.")
    elif 18 <= usia <= 59:
        if olahraga < 30:
            print("Kamu kurang olahraga. Minimal 30 menit per hari diperlukan untuk dewasa.")
        elif 30 <= olahraga <= 60:
            print("Durasi olahraga kamu sudah sesuai anjuran WHO.")
        elif 60 < olahraga <= 120:
            print("Olahraga kamu cukup aktif, tetap jaga keseimbangan istirahat.")
        else:
            print("Olahraga kamu terlalu lama. Maksimal 120 menit per hari agar tubuh tidak kelelahan.")
    else:
        if olahraga < 30:
            print("Kamu kurang olahraga. Minimal 30 menit per hari disarankan.")
        elif 30 <= olahraga <= 60:
            print("Aktivitas fisik kamu sudah sesuai anjuran untuk lansia.")
        elif 60 < olahraga <= 90:
            print("Kamu cukup aktif. Tetap perhatikan kondisi tubuh.")
        else:
            print("Kamu olahraga terlalu lama. Batasi maksimal 90 menit per hari agar aman.")