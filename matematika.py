import sys
import os
import platform

# sistem clear
def cs():
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')

# matematika
def matematika():
    try:
        cs()
        
        # menu fitur
        print("""
        
# Pilih fitur (input example: 1)
        
#====#==============#
# no # Nama fitur   #
# 1  # Discount     #
# 2  # Perhitungan  #
# 3  # B. Datar     # 
# 4  # B. Ruang     # 
#====#==============#
""")
  
        # Start Code
  
        # discount sistem
        def discount():
            cs()
            price1 = float(input("harga barang : "))
            discount = float(input("harga discount : "))
            totatldiscount = discount / 100
  
            total = price1 - (price1 * totatldiscount)
            print(f"Total harga adalah {total}")
  
        # Perhitungan sistem
        def math():
            cs()
            print("""
        
# Pilih fitur (input example: 1)

#====#=============#
# no # Nama fitur  #
# 1  # Pertambahan #
# 2  # Pengurangan #
# 3  # Perkalian   #
# 4  # Pembagian   #
#====#=============#
            """)
    
            # System Pertambahan
            def pertambahan():
                x = float(input("Masukkan angka X : "))
                y = float(input("Masukkan angka Y : "))
                print(x + y)
            # System Pengurangan
            def pengurangan():
                x = float(input("Masukkan angka X : "))
                y = float(input("Masukkan angka Y : "))
                print(x - y)
            # System Perkalian
            def perkalian():
                x = float(input("Masukkan angka X : "))
                y = float(input("Masukkan angka Y : "))
                print(x * y)
            # System Pembagian
            def pembagian():
                x = float(input("Masukkan angka X : "))
                y = float(input("Masukkan angka Y : "))
                print(x / y)
      
            # pilih fitur Math
            fiturmath = float(input("Pilih fitur [0 = kembali] : "))
            if fiturmath == 0:
                matematika()
            elif fiturmath == 1:
                pertambahan()
            elif fiturmath == 2:
                pengurangan()
            elif fiturmath == 3:
                perkalian()
            elif fiturmath == 4:
                pembagian()
      
        # Bangun datar sistem
        def bdatar():
            cs()
            print("""
        
# mencari?

#====#=============#
# no # Nama fitur  #
# 1  # luas        #
# 2  # Keliling    #
#====#=============#
""")
    
            def luas():
                print("""
        
# mencari?
        
#====#=================#
# no # Nama fitur      #
# 1  # Persegi         #
# 2  # Persegi Panjang #
# 3  # Segitga         #
# 4  # Jajar Genjang   #
# 5  # Trapesium       #
# 6  # Layang Layang   #
# 7  # Lingkaran       #
# 8  # Segi Lima       #
# 9  # Segi Enam       #
#====#=================#
""")
                
                setengah = 0.5
      
                def persegi():
                    s = float(input("masukkan sisi : "))
                    print(f"Luas persegi adalah: {s*s}")
                    print("\n")
                    while True:
                        quest = input("kembali? y | n [n = exit] : ")
                        if quest.lower() == 'y':
                            luas()  # kembali ke menu luas
                        elif quest.lower() == 'n':
                            sys.exit(0)
                        
                def persegipanjang():
                    p = float(input("masukkan panjang : "))
                    l = float(input("masukkan lebar : "))
                    print(f"Luas persegi panjang adalah: {p*l}")
                    print("\n")
                    while True:
                        quest = input("kembali? y | n [n = exit] : ")
                        if quest.lower() == 'y':
                            luas()
                        elif quest.lower() == 'n':
                            sys.exit(0)

                def lingkaran():
                    phi = 3.14
                    r = float(input("masukkan jari jari : "))
                    print(f"Luas lingkaran adalah: {phi*r**2}")
                    print("\n")
                    while True:
                        quest = input("kembali? y | n [n = exit] : ")
                        if quest.lower() == 'y':
                            luas()
                        elif quest.lower() == 'n':
                            sys.exit(0)

                def segitiga():
                    a = float(input("masukkan alas : "))
                    t = float(input("masukkan tinggi : "))
                    print(setengah*a*t)
                    print("\n")
                    while True:
                        quest = input("kembali? y | n [n = exit] : ")
                        if quest.lower() == 'y':
                            luas()
                        elif quest.lower() == 'n':
                            sys.exit(0)

                def jajargenjang():
                    a = float(input("masukkan alas : "))
                    t = float(input("masukkan tinggi : "))
                    print(a*t)
                    print("\n")
                    while True:
                        quest = input("kembali? y | n [n = exit] : ")
                        if quest.lower() == 'y':
                            luas()
                        elif quest.lower() == 'n':
                            sys.exit(0)

                def trapesium():
                    a = float(input("masukkan sisi a : "))
                    b = float(input("masukkan sisi b : "))
                    t = float(input("masukkan tinggi : "))
                    print(setengah*(a+b)*t)
                    print("\n")
                    while True:
                        quest = input("kembali? y | n [n = exit] : ")
                        if quest.lower() == 'y':
                            luas()
                        elif quest.lower() == 'n':
                            sys.exit(0)

                def layang():
                    d1 = float(input("masukkan diagonal 1 : "))
                    d2 = float(input("masukkan diagonal 2 : "))
                    print(setengah*d1*d2)
                    print("\n")
                    while True:
                        quest = input("kembali? y | n [n = exit] : ")
                        if quest.lower() == 'y':
                            luas()
                        elif quest.lower() == 'n':
                            sys.exit(0)

                def segilima():
                    p = float(input("masukkan keliling : "))
                    a = float(input("masukkan apotema : "))
                    print(setengah*p*a)
                    print("\n")
                    while True:
                        quest = input("kembali? y | n [n = exit] : ")
                        if quest.lower() == 'y':
                            luas()
                        elif quest.lower() == 'n':
                            sys.exit(0)

                def segienam():
                    p = float(input("masukkan keliling : "))
                    a = float(input("masukkan apotema : "))
                    print(setengah*a*p)
                    print("\n")
                    while True:
                        quest = input("kembali? y | n [n = exit] : ")
                        if quest.lower() == 'y':
                            luas()
                        elif quest.lower() == 'n':
                            sys.exit(0)
                

                pluas = float(input("Masukkan pilihan menu [0 = kembali] : "))
      
                if pluas == 0:
                    bdatar()
                elif pluas == 1:
                    persegi()
                elif pluas == 2:
                    persegipanjang()
                elif pluas == 3:
                    lingkaran()
                elif pluas == 4:
                    segitiga()
                elif pluas == 5:
                    jajargenjang()
                elif pluas == 6:
                    trapesium()
                elif pluas == 7:
                    layang()
                elif pluas == 8:
                    segilima()
                elif pluas == 9:
                    segienam()
            
            fiturmath = float(input("Pilih fitur [0 = kembali] : "))
            if fiturmath == 0:
                matematika()
            elif fiturmath == 1:
                luas()
            elif fiturmath == 2:
                keliling()
            elif fiturmath == 3:
                matematika()
    
        # input fitur utama
        fitur = float(input("Pilih fitur [0 = kembali ke menu utama] : "))
        if fitur == 0:
            return
        elif fitur == 1:
            discount()
        elif fitur == 2:
            math()
        elif fitur == 3:
            bdatar()
        # elif fitur == 4:
        #   bruang()
    except KeyboardInterrupt:
        print("\nKembali ke menu utama...")
        return