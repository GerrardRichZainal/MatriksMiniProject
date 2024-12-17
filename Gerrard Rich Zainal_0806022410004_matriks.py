# Fungsi untuk input matriks
def input_matriks(n, m):
    print(f"Masukkan elemen matriks berukuran {n}x{m}:")
    matriks = []
    for i in range(n):
        row = list(map(int, input(f"Baris {i+1}: ").split()))
        while len(row) != m:
            print("Jumlah elemen tidak sesuai! Coba lagi.")
            row = list(map(int, input(f"Baris {i+1}: ").split()))
        matriks.append(row)
    return matriks

# Fungsi menampilkan matriks
def tampilkan_matriks(matriks):
    for row in matriks:
        print(" ".join(map(str, row)))

# Penjumlahan matriks
def tambah_matriks(A, B):
    return [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

# Pengurangan matriks
def kurang_matriks(A, B):
    return [[A[i][j] - B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

# Perkalian matriks
def kali_matriks(A, B):
    result = [[0] * len(B[0]) for _ in range(len(A))]
    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                result[i][j] += A[i][k] * B[k][j]
    return result

# Menghitung determinan matriks (metode rekursif)
def determinan_matriks(mat):
    n = len(mat)
    if n == 1:
        return mat[0][0]
    if n == 2:
        return mat[0][0]*mat[1][1] - mat[0][1]*mat[1][0]
    det = 0
    for c in range(n):
        minor = [[mat[i][j] for j in range(n) if j != c] for i in range(1, n)]
        det += ((-1)**c) * mat[0][c] * determinan_matriks(minor)
    return det

# Menghitung invers matriks
def invers_matriks(mat):
    n = len(mat)
    det = determinan_matriks(mat)
    if det == 0:
        print("Matriks ini tidak memiliki invers (determinan 0).")
        return None
    cofaktor = [[((-1)**(i+j)) * determinan_matriks([[mat[x][y] for y in range(n) if y != j] 
                                                     for x in range(n) if x != i]) 
                 for j in range(n)] for i in range(n)]
    adjoint = [[cofaktor[j][i] for j in range(n)] for i in range(n)]
    invers = [[adjoint[i][j] / det for j in range(n)] for i in range(n)]
    return invers

def menu():
    while True:
        print("\nPilih Operasi Matriks:")
        print("1. Penjumlahan Matriks")
        print("2. Pengurangan Matriks")
        print("3. Perkalian Matriks")
        print("4. Determinan Matriks")
        print("5. Inverse Matriks")
        print("0. Keluar")
        
        pilihan = input("Masukkan pilihan Anda: ")
        
        if pilihan == '1':  # Penjumlahan Matriks
            n, m = map(int, input("Masukkan ukuran matriks (n m): ").split())
            A = input_matriks(n, m)
            B = input_matriks(n, m)
            print("Hasil Penjumlahan:")
            tampilkan_matriks(tambah_matriks(A, B))
        
        elif pilihan == '2':  # Pengurangan Matriks
            n, m = map(int, input("Masukkan ukuran matriks (n m): ").split())
            A = input_matriks(n, m)
            B = input_matriks(n, m)
            print("Hasil Pengurangan:")
            tampilkan_matriks(kurang_matriks(A, B))
        
        elif pilihan == '3':  # Perkalian Matriks
            n, m = map(int, input("Masukkan ukuran matriks A (n m): ").split())
            A = input_matriks(n, m)
            p, q = map(int, input("Masukkan ukuran matriks B (p q): ").split())
            if m != p:
                print("Jumlah kolom A harus sama dengan jumlah baris B!")
            else:
                B = input_matriks(p, q)
                print("Hasil Perkalian:")
                tampilkan_matriks(kali_matriks(A, B))
        
        elif pilihan == '4':  # Determinan Matriks
            n = int(input("Masukkan ukuran matriks persegi (n): "))
            if n > 4 or n < 1:
                print("Ukuran matriks harus antara 1x1 hingga 4x4.")
            else:
                A = input_matriks(n, n)
                print(f"Determinan Matriks: {determinan_matriks(A)}")
        
        elif pilihan == '5':  # Inverse Matriks
            n = int(input("Masukkan ukuran matriks persegi (n): "))
            if n > 4 or n < 1:
                print("Ukuran matriks harus antara 1x1 hingga 4x4.")
            else:
                A = input_matriks(n, n)
                invers = invers_matriks(A)
                if invers:
                    print("Invers Matriks:")
                    tampilkan_matriks(invers)
        
        elif pilihan == '0':  # Keluar
            print("Terima kasih!")
            break
        else:
            print("Pilihan tidak valid. Coba lagi.")

# Eksekusi program
menu()