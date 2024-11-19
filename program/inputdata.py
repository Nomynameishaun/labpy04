# Fungsi untuk menghitung nilai akhir
def hitung_nilai_akhir(tugas, uts, uas):
    return round((tugas * 0.3) + (uts * 0.3) + (uas * 0.4), 2)

# Inisialisasi list untuk menampung data mahasiswa
data_mahasiswa = []
no = 1

while True:
    print("Nama :", end=" ")
    nama = input()
    print("NIM :", end=" ")
    nim = input()
    print("Nilai Tugas :", end=" ")
    nilai_tugas = int(input())
    print("Nilai UTS :", end=" ")
    nilai_uts = int(input())
    print("Nilai UAS :", end=" ")
    nilai_uas = int(input())
    
    # Menghitung nilai akhir
    nilai_akhir = hitung_nilai_akhir(nilai_tugas, nilai_uts, nilai_uas)
    
    # Simpan data ke list
    data_mahasiswa.append([no, nama, nim, nilai_tugas, nilai_uts, nilai_uas, nilai_akhir])
    no += 1
    
    # Tambah lagi atau tidak?
    print("Tambah data(y/t)?", end=" ")
    lanjut = input().lower()
    if lanjut != 'y':
        break

# Tampilan ditampilkan dalam bentuk tabel
# Cetak header tabel
print("="*61)
print("| No | Nama      | NIM   | Tugas | UTS | UAS | Akhir |")
print("="*61)

# Cetak setiap data yang diinputkan
for data in data_mahasiswa:
    print(f"| {data[0]:<2} | {data[1]:<9} | {data[2]:<5} | {data[3]:<5} | {data[4]:<3} | {data[5]:<3} | {data[6]:<5} |")

print("="*61)
