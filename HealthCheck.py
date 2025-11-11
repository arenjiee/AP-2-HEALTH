def fitur_3():
    print("\n===== 🔍🔍 HealthCheck 🔍🔍 =====")
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