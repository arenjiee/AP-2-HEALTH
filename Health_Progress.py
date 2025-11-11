from database_set import get_progress_history, get_target, get_workouts, insert_progress, get_session
import re
    
def fitur_5():
    def input_progress():
        workouts = get_workouts()

        existing_sessions = [s[0].capitalize() for s in get_session()]
        target_kalori, target_pro = get_target()

        while True:
            session = input("\nNama sesi progress (cth: 'Day 1', '01-01-2025'): ").strip().capitalize()
            if re.match(r"^(Day\s+[1-9]|Day\s+[1-9][0-9]|Day\s+[1-9][0-9][0-9]|\d{2}-\d{2}-\d{4})$", session):
                if session.capitalize() in existing_sessions:
                    print(f"Session {session} sudah ada sebelumnya!!")
                    continue
                else:
                    break
            elif re.match(r"^(Day\s+-[1-9]|Day\s+-[1-9][0-9]|Day\s+-[1-9][0-9][0-9]|\d{2}-\d{2}-\d{4})$", session):
                print("❌ Sesi tidak boleh dimulai dari 'Day -X'. Mulai dari 'Day 1', ya!")
                continue
            elif re.match(r"^(Day\s+[0])$", session):
                print("❌ Sesi tidak boleh dimulai dari 'Day 0'. Mulai dari 'Day 1', ya!")
                continue
            else:
                print("❌ Format salah! Gunakan 'Day X' atau 'DD/MM/YYYY'. Coba lagi.")
                continue
        status_list = []
        if not workouts:
            print ("⚠️ Belum ada daftar workout.")
            status_list.append(("Tidak ada workout", "❌"))
        else:
            for _, nama_workout in workouts:
                while True:
                    workout_input = input(f"'{nama_workout}' udah kamu lakukan belum? (y/n): ").lower()
                    if re.match(r"^(y|yes|n|no)$", workout_input):
                        if workout_input == "y" or "yes":
                            status_workout = "✅"  
                            break
                        else:
                            status_workout = "❌"
                            break
                    else:
                        print("⚠️ Inputan hanya  boleh 'y'/'yes' atau 'n'/'no' ⚠️")
                        continue
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
            if not workout_list:
                print ("⚠️ Belum ada daftar workout.")
            else:
                for workout in workout_list:
                    print(f"  - {workout}")

            # Status Kalori
            if kal == target_kal:
                print(f"  Kalori : {kal}/{target_kal} ✅")
            elif kal > target_kal or kal < target_kal :
                print(f"  Kalori : {kal}/{target_kal} ❌")
                print(f"  Capaian Kalori tidak sesuai target!")
            else:
                print(f"  Kalori : {kal}")

            # Status Protein
            if pro == target_pro:
                print(f"  Protein: {pro}/{target_pro} ✅")
            elif pro > target_pro or pro < target_pro:
                print(f"  Kalori : {pro}/{target_pro} ❌")
                print(f"  Capaian Protein tidak sesuai target!")
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