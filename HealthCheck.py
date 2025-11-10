def healthcheck():
    print("\n=== HealthCheck ===")
    print("Cek kesehatan berdasarkan kegiatan harianmu!!\n")

    usia = int(input("Masukkan usia (tahun): "))
    tidur = int(input("Masukkan durasi tidur (jam): "))
    air = float(input("Masukkan jumlah air yang diminum hari ini (liter): "))
    olahraga = int(input("Masukkan durasi olahraga hari ini (menit): "))

    print("\nData kamu telah dicatat!")
healthcheck()