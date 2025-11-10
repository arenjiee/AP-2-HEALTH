def tanya_gejala(daftar_pertanyaan):
    total = 0

    for p in daftar_pertanyaan:
        print("\n" + p)

        # Input frekuensi
        while True:
            frek_input = input("  Frekuensi (0=tidak pernah, 1=kadang, 2=sering, ketik 'exit' untuk keluar): ")

            # Jika pengguna ingin keluar
            if frek_input == "exit":
                print("Terima kasih! Program dihentikan.")
                return None

            # Pastikan input angka valid
            if frek_input.isdigit():
                frek = int(frek_input)
                if frek in [0, 1, 2]:
                    break
                else:
                    print("Masukkan hanya angka 0, 1, atau 2!")
            else:
                print("Harus berupa angka atau ketik 'exit' untuk keluar!")

        # Jika frekuensi = 0 → lanjut ke pertanyaan berikutnya
        if frek == 0:
            continue

        # Input intensitas
        while True:
            inten_input = input("  Intensitas (1=ringan, 2=berat, ketik 'exit' untuk keluar): ")

            if inten_input == "exit":
                print("Terima kasih! Program dihentikan.")
                return None

            if inten_input.isdigit():
                inten = int(inten_input)
                if inten in [1, 2]:
                    break
                else:
                    print("Masukkan hanya angka 1 atau 2!")
            else:
                print("Harus berupa angka atau ketik 'exit' untuk keluar!")

        # Hitung skor pertanyaan ini
        skor = frek * inten
        total += skor
        
    return total