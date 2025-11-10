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