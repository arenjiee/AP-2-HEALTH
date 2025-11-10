from database_set import get_workouts, insert_progress, get_progress_history, get_target
    
def fitur_5():
    def input_progress():
        workouts = get_workouts()
        target_kalori, target_pro = get_target()

        if not workouts:
            print("⚠️ Belum ada daftar workout.")
            return
        while True:
            session = input("\nNama sesi progress (cth: 'Day 1', '01-01-2025'): ")
            status_list = []
            for _, nama_workout in workouts:
                workout_input = input(f"'{nama_workout}' udah kamu lakukan belum? (y/n): ").lower()
                status_workout = "✅" if workout_input == "y" else "❌"
                status_list.append((nama_workout, status_workout))
            
            if target_kalori > 0:
                kalori_input = int(input("Total kalori hari ini berapa? : "))
                if target_pro > 0:
                    protein_input = int(input("Total protein hari ini berapa? : "))
                else:
                    print("\n⚠️ Target protein belum diatur.")
                    protein_input = 0
            else:
                print("\n⚠️ Target kalori belum diatur.")
                kalori_input =0

            for nama, status in status_list:
                insert_progress(session, nama, kalori_input, protein_input, status)

            print("\n✅ Progress berhasil disimpan!\n")

    def lihat_history():
        print("\n=== HISTORY PROGRESS ===\n")

        data = get_progress_history()
        if not data:
            print("⚠️ Belum ada history ⚠️")
            return

        for session, workouts, kal, target_kal, pro, target_pro in data:
            print(f"Sesi: {session}")

            # Tampilkan workout (sudah berupa GROUP_CONCAT)
            workout_list = workouts.split("\n")
            for workout in workout_list:
                print(f"  - {workout}")

            # Status Kalori
            if target_kal > 0:
                kal_status = "✅" if kal >= target_kal else "❌"
                print(f"  Kalori : {kal}/{target_kal} {kal_status}")
            else:
                print(f"  Kalori : {kal}")

            # Status Protein
            if target_pro > 0:
                pro_status = "✅" if pro >= target_pro else "❌"
                print(f"  Protein: {pro}/{target_pro} {pro_status}")
            else:
                print(f"  Protein: {pro}")

            print("-" * 40)


    while True:
        print("\n=== MENU HEALTH PROGRESS ===")
        print("1. 🌿 Input Progress Harian")
        print("2. 🗂️ Lihat History Progress")
        print("3. 👋 Keluar")
        try:
            pilihan = int(input("👉 Pilih menu (1-3): "))
            if pilihan == 1:
                input_progress()
            elif pilihan == 2:
                lihat_history()
            elif pilihan == 3:
                print("✨ Program selesai. Good job hari ini!")
                break
            else:
                print("Wah, pilihan nggak valid...coba lagi! ⚠️\n")
        except ValueError:
            print("⚠️ INPUTAN HANYA BOLEH ANGKA ⚠️")
