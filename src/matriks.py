import numpy as np

print ("TUGAS BESAR ALJABAR GEOMETRI")
print ("Kelompok 6\n")

def input_matriks():
    print("Masukkan nilai matriks:")
    a11 = float(input("Masukkan a11: "))
    a12 = float(input("Masukkan a12: "))
    a21 = float(input("Masukkan a21: "))
    a22 = float(input("Masukkan a22: "))
    return np.array([[a11, a12], [a21, a22]])

def input_matriks_3x3():
    print("Masukkan nilai matriks:")
    a11 = float(input("Masukkan a11: "))
    a12 = float(input("Masukkan a12: "))
    a13 = float(input("Masukkan a13: "))
    a21 = float(input("Masukkan a21: "))
    a22 = float(input("Masukkan a22: "))
    a23 = float(input("Masukkan a23: "))
    a31 = float(input("Masukkan a31: "))
    a32 = float(input("Masukkan a32: "))
    a33 = float(input("Masukkan a33: "))
    return np.array([[a11, a12, a13], [a21, a22, a23], [a31, a32, a33]])

def input_vektor():
    print("Masukkan nilai vektor:")
    b1 = float(input("Masukkan b1: "))
    b2 = float(input("Masukkan b2: "))
    return np.array([b1, b2])

while True:
    print("【••••••••••MENU••••••••••】")
    print("1. Penjumlahan dan Pengurangan Matriks")
    print("2. Matriks Transpose")
    print("3. Matriks Balikan (Invers)")
    print("4. Determinan")
    print("5. Sistem Persamaan Linier")
    print("6. Keluar")
    print("【••••••••••••••••••••••••】")
    
    pilihan_menu = int(input("Masukkan pilihan menu (1-6): "))
    
    if pilihan_menu == 1:
        print("\n1. Penjumlahan matriks")
        print("2. Pengurangan matriks")
        operasi = int(input("Masukkan pilihan operasi (1-2): "))
        
        matriks_a = input_matriks()
        matriks_b = input_matriks()
        
        if operasi == 1:
            print("\nHasil penjumlahan matriks:")
            print(matriks_a + matriks_b)
        elif operasi == 2:
            print("\nHasil pengurangan matriks:")
            print(matriks_a - matriks_b)
        else:
            print("\nPilihan operasi tidak valid.")
            
    elif pilihan_menu == 2:
        print("\n1. Matriks 2x2")
        print("2. Matriks 3x3")
        ukuran = int(input("Masukkan pilihan ukuran matriks (1-2): "))
        
        if ukuran == 1:
            matriks = input_matriks()
            print("\nHasil transpose matriks:")
            print(np.transpose(matriks))
        elif ukuran == 2:
            matriks = input_matriks_3x3()
            print("\nHasil transpose matriks:")
            print(np.transpose(matriks))
        else:
            print("\nPilihan ukuran matriks tidak valid.")
    
    elif pilihan_menu == 3:
        matriks = input_matriks()
        if matriks.shape == (2, 2):
            print("\nHasil invers matriks:")
            print(np.linalg.inv(matriks))
        else:
            print("\nMatriks tidak berukuran 2x2.")
    
    elif pilihan_menu == 4:
        print("\n1. Matriks 2x2")
        print("2. Matriks 3x3")
        ukuran = int(input("Masukkan pilihan ukuran matriks (1-2): "))
        
        if ukuran == 1:
            matriks = input_matriks()
            if matriks.shape == (2, 2):
                print("\nDeterminan matriks:")
                print(np.linalg.det(matriks))
            else:
                print("\nMatriks tidak berukuran 2x2.")
        elif ukuran == 2:
            matriks = input_matriks_3x3()
            if matriks.shape == (3, 3):
                print("\nDeterminan matriks:")
                print(np.linalg.det(matriks))
            else:
                print("\nMatriks tidak berukuran 3x3.")
        else:
            print("\nPilihan ukuran matriks tidak valid.")
    
    elif pilihan_menu == 5:
        print("\nMasukkan nilai matriks A dan vektor b untuk SPL:")
        matriks_a = input_matriks()
        vektor_b = input_vektor()
        
        if matriks_a.shape == (2, 2) and vektor_b.shape == (2,):
            print("\nSolusi SPL:")
            print(np.linalg.solve(matriks_a, vektor_b))
        else:
            print("\nMatriks A harus berukuran 2x2 dan vektor b berukuran 2x1.")
    
    elif pilihan_menu == 6:
        print("\nTerima kasih telah menggunakan program ini.")
        break
    else:
        print("\nPilihan tidak valid. Silakan pilih angka antara 1 hingga 6.")
