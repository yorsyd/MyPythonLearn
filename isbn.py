while(True):
    print("\n","-"*5, "ISBN", "-"*5)
    print("1. Generate Nomor Uji ISBN")
    print("2. Validasi Nomor Uji ISBN")
    print("0. exit")
    pilih1 = int(input("1/2/0 : "))

    next = True

    if pilih1 == 1:
        next = False
        while(True):
            print("\n","-"*5, "Generate Nomor Uji ISBN", "-"*5)
            print("1. ISBN 10 Digit")
            print("2. ISBN 13 Digit")
            print("0. Back")
            pilih = int(input("1/2/0 : "))
            
            cek = True
            temp = 0
            i = 1
            if pilih == 1:
                cek = False
                while(i<10):
                    print("Karakter ke-", i, ": ")
                    karakter = int(input())
                    temp = karakter*(i) + temp
                    i=i+1
                
                karakterUji = temp % 11
                print("Karakter Uji: ", karakterUji)

            if pilih == 2:
                cek = False
                while(i<13):
                    print("Karakter ke-", i, ": ")
                    karakter = int(input())
                    if(i%2 == 0):
                        temp = karakter*3 + temp
                    if(i%2 == 1):
                        temp = karakter*1 + temp
                    i=i+1
                
                karakterUji = 10 - temp % 10
                print("Karakter Uji: ", karakterUji)

            if pilih == 0:
                break
            
            if (cek):
                print("Pilih 1 atau 2 saja!")

            lagi = input("Lagi? (y/n)")
            if lagi == 'n' or lagi == 'N':
                print("\nTerimakasih >_<")
                exit()

    if pilih1 == 2:
        next = False
        while(True):
            print("\n","-"*5, "Validasi Nomor Uji ISBN", "-"*5)
            print("1. ISBN 10 Digit")
            print("2. ISBN 13 Digit")
            print("0. Back")
            pilih = int(input("1/2/0 : "))
            
            cek = True
            temp = 0
            i = 1
            if pilih == 1:
                print("Masukkan Nomor Uji dari ISBN 10 Digit: ")
                nomorUji = int(input())

                cek = False
                while(i<10):
                    print("Karakter ke-", i, ": ")
                    karakter = int(input())
                    temp = karakter*(i) + temp
                    i=i+1
                
                karakterUji = temp % 11
                if nomorUji == karakterUji:
                    print("Nomor Uji ", nomorUji, "Valid!")
                else:
                    print("Nomor Uji ", nomorUji, "Tidak Valid!\nNomor Uji yang Valid adalah ", karakterUji)

            if pilih == 2:
                print("Masukkan Nomor Uji dari ISBN 13 Digit: ")
                nomorUji = int(input())

                cek = False
                while(i<13):
                    print("Karakter ke-", i, ": ")
                    karakter = int(input())
                    if(i%2 == 0):
                        temp = karakter*3 + temp
                    if(i%2 == 1):
                        temp = karakter*1 + temp
                    i=i+1
                
                karakterUji = 10 - temp % 10
                if nomorUji == karakterUji:
                    print("Nomor Uji ", nomorUji, "Valid!")
                else:
                    print("Nomor Uji ", nomorUji, "Tidak Valid!\nNomor Uji yang Valid adalah ", karakterUji)
                
            if pilih == 0:
                break
            
            if (cek):
                print("Pilih 1 atau 2 saja!")

            lagi = input("Lagi? (y/n)")
            if lagi == 'n' or lagi == 'N':
                print("\nTerimakasih >_<")
                exit()

    if pilih1 == 0:
        print("\nTerimakasih >_<")
        exit()

    if (next):
        print("Pilih 1 atau 2 saja!")

        lagi = input("Lagi? (y/n)")
        if lagi == 'n' or lagi == 'N':
            exit()     