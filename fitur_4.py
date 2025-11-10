import database_set

# Menu program
def fitur_4():

    def set_target():
        while True:
            print("\n=== SET TARGET HARIAN ===")
            print("1. Workout")
            print("2. Kalori")
            print("3. Protein")
            print("4. Exit")

            pilihan = int(input("Pilih Target yang di set (1/2/3): "))
            
            if pilihan == 1:
                workout = (input("Masukkan target : "))
                database_set.insert_target_workout(workout)
            elif pilihan == 2:
                kalori = int(input("Masukkan target kalori harian (kcal): "))
                database_set.insert_target_kalori(kalori)
            elif pilihan == 3:
                protein = int(input("Masukkan target protein harian (gram): "))
                database_set.insert_target_protein(protein)
            elif pilihan == 4:
                break



        print("\n✅ Target baru berhasil disimpan (data lama diganti).\n")

    def hapus_workout():
        workouts = database_set.get_workouts()

        if not workouts:
            print("\n❌ Tidak ada workout yang bisa dihapus.\n")
            return

        print("\n=== HAPUS WORKOUT ===")
        for i, w in enumerate(workouts, 1):
            print(f"{i}. {w[1]}")   # Tampilkan tanpa ID

        try:
            nomor = int(input("\nMasukkan nomor workout yang ingin dihapus: "))

            # Validasi rentang nomor
            if nomor < 1 or nomor > len(workouts):
                print("❌ Nomor tidak valid.\n")
                return

            # Ambil ID dari workout berdasarkan index
            workout_id = workouts[nomor - 1][0]

            database_set.delete_workout_by_id(workout_id)
            print("✅ Workout berhasil dihapus!\n")

        except ValueError:
            print("❌ Input harus berupa angka.\n")


    def lihat_target():
        print("\n=== TARGET SAAT INI ===")
        target = database_set.get_target()

        if target is None:
            print("❌ Belum ada target kalori/protein.")
            return

        kalori, protein = target
        workouts = database_set.get_workouts()

        print("\n-- Workout yang Ditargetkan --")
        if workouts:
            for i, w in enumerate(workouts, 1):
                print(f"{i}. {w[1]}")  # tanpa ID
        else:
            print("Belum ada workout ditambahkan.")

        print(f"\nKalori  : {kalori} kkal")
        print(f"Protein : {protein} gram\n")
        
    while True:
        print("\n=== MENU ===\n")
        print("1. Set Target Harian")
        print("2. Lihat Target Tersimpan")
        print("3. Hapus workout")
        print("4. Keluar")

        pilihan = input("Pilih menu (1-3): ")

        if pilihan == "1":
            set_target()
        elif pilihan == "2":
            lihat_target()
        elif pilihan == "3":
            hapus_workout()
        elif pilihan == "4":
            print("Program selesai.")
            break
        else:
            print("Pilihan tidak valid, coba lagi.\n")