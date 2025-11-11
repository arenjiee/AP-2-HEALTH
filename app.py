import BMI, Smartfat_calculator, HealthCheck, Set_Health_Mission, Health_Progress, How_Are_You_Today, EyeCheck
import show

def main():
    show.greeting()
    while True:
        show.menu()
        try:     
            pilihan = int(input("Pilih Menu (1-8): "))

            if pilihan == 1:
                BMI.fitur_1()

            elif pilihan == 2:
                Smartfat_calculator.fitur_2()

            elif pilihan == 3:
                HealthCheck.fitur_3()
            
            elif pilihan == 4:
                Set_Health_Mission.fitur_4()
            
            elif pilihan == 5:
                Health_Progress.fitur_5()
            
            elif pilihan == 6:
                How_Are_You_Today.fitur_6()
            
            elif pilihan == 7:
                EyeCheck.fitur_7()
                
            elif pilihan == 8:
                print("\nPROGRAM BERHENTI")
                exit()
            else:
                print("Pilihan tidak ada di menu")

        except ValueError:
            print("\n ⚠️ INPUTAN HANYA BOLEH ANGKA ⚠️\n")
            

if __name__ == "__main__":
    main()