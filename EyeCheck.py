def tanya_gejala(daftar_pertanyaan):
    total = 0

    for p in daftar_pertanyaan:
        print("\n" + p)

        # Input frekuensi
        while True:
            frekuensi_input = input("  Frekuensi (0=tidak pernah, 1=kadang, 2=sering, ketik 'exit' untuk keluar): ")

            if frekuensi_input == "exit":
                print("Terima kasih! Program dihentikan👋🏻")
                return None

            if frekuensi_input.isdigit():
                frekuensi = int(frekuensi_input)
                if frekuensi in [0, 1, 2]:
                    break
                else:
                    print("⚠️ Inputan hanya boleh angka 0, 1, atau 2! ⚠️")
            else:
                print("⚠️ Harus berupa angka atau ketik 'exit' untuk keluar! ⚠️")

        if frekuensi == 0:
            continue

        # Input intensitas
        while True:
            intensitas_input = input("  Intensitas (1=ringan, 2=berat, ketik 'exit' untuk keluar): ")

            if intensitas_input == "exit":
                print("Terima kasih! Program dihentikan👋🏻")
                return None

            if intensitas_input.isdigit():
                intensitas = int(intensitas_input)
                if intensitas in [1, 2]:
                    break
                else:
                    print("⚠️ Masukkan hanya angka 1 atau 2! ⚠️")
            else:
                print("⚠️ Harus berupa angka atau ketik 'exit' untuk keluar! ⚠️")

        total += frekuensi * intensitas
        
    return total


def kategori_cvs(total):
    if total == 0:
        return "Tidak ada gejala CVS🌿"
    elif total <= 6:
        return "Tidak ada CVS🙌"
    elif total <= 13:
        return "CVS ringan😌"
    else:
        return "CVS sedang/berat🚨"


def saran_cvs(kategori):
    """Memberikan saran berdasarkan hasil kategori CVS"""
    if "Tidak ada" in kategori:
        return (
            "✅ Saran:\n"
            "- Pertahankan kebiasaan baik saat menggunakan komputer.\n"
            "- Pastikan pencahayaan ruangan cukup dan nyaman."
        )
        
    elif "CVS ringan" in kategori:
        return (
            "💡 Saran untuk CVS Ringan:\n"
            "- Kurangi waktu menatap layar secara terus-menerus.\n"
            "- Atur posisi duduk dan jarak pandang ke layar.\n"
            "- Perbanyak konsumsi air putih agar mata tidak kering."
        )
    else:
        return (
            "🚨 Saran untuk CVS Sedang/Berat:\n"
            "- Segera konsultasikan ke dokter mata jika kondisi tidak kunjung membaik.\n"
            "- Batasi waktu layar dan lakukan peregangan mata.\n"
            "- Perhatikan postur tubuh dan pencahayaan lingkungan kerja."
        )


def fitur_7():
    pertanyaan = [
        "1. Penglihatan kabur saat melihat jauh",
        "2. Penglihatan kabur saat melihat dekat",
        "3. Penglihatan ganda",
        "4. Mata terasa terbakar",
        "5. Mata terasa gatal",
        "6. Mata terasa berat",
        "7. Nyeri di sekitar mata",
        "8. Mata merah",
        "9. Mata berair",
        "10. Mata terasa kering",
        "11. Sakit kepala",
        "12. Sakit leher atau bahu",
        "13. Silau terhadap cahaya",
        "14. Sulit fokus",
        "15. Seperti ada benda asing di mata",
        "16. Rasa tidak nyaman di mata"
    ]

    print("=== KUESIONER COMPUTER VISION SYNDROME (CVS-Q) ===")
    print("Frekuensi: 0=Tidak Pernah | 1=Kadang-kadang | 2=Sering")
    print("Intensitas: 1=Ringan | 2=Berat")
    print("Ketik 'exit' kapan saja untuk keluar dari program.\n")

    nama = input("Masukkan nama Anda (atau ketik 'exit' untuk keluar): ")
    if nama == "exit":
        print("Terima kasih! Program dihentikan👋🏻")
        return

    total_skor = tanya_gejala(pertanyaan)
    if total_skor is None:
        return

    hasil = kategori_cvs(total_skor)
    saran = saran_cvs(hasil)

    print("\n=== HASIL PENILAIAN CVS ===")
    print("Nama:", nama)
    print("Total Skor:", total_skor)
    print("Kategori:", hasil)
    print("\n" + saran)
