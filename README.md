# labpy04
# Program Input Data list Sederhana
Program sederhana ini ditulis dalam Python untuk pengguna memasukkan data, menghitung nilai akhir berdasarkan bobot nilai tugas, UTS, dan UAS, lalu menampilkan data tersebut dalam format tabel yang rapih.
```ruby
def hitung_nilai_akhir(tugas, uts, uas):
    return round((tugas * 0.3) + (uts * 0.3) + (uas * 0.4), 2)

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
    
    nilai_akhir = hitung_nilai_akhir(nilai_tugas, nilai_uts, nilai_uas)
    
    data_mahasiswa.append([no, nama, nim, nilai_tugas, nilai_uts, nilai_uas, nilai_akhir])
    no += 1
    
    print("Tambah data(y/t)?", end=" ")
    lanjut = input().lower()
    if lanjut != 'y':
        break

print("="*61)
print("| No | Nama      | NIM   | Tugas | UTS | UAS | Akhir |")
print("="*61)

for data in data_mahasiswa:
    print(f"| {data[0]:<2} | {data[1]:<9} | {data[2]:<5} | {data[3]:<5} | {data[4]:<3} | {data[5]:<3} | {data[6]:<5} |")

print("="*61)
```
# Flowchart
![flow](</gambar/Flowchart.png>)

## Penjelasan Struktur Kode Program
### 1. Fungsi Hitung Nilai Akhir
```ruby
def hitung_nilai_akhir(tugas, uts, uas):
    return round((tugas * 0.3) + (uts * 0.3) + (uas * 0.4), 2)
```
Fungsi ini menerima tiga parameter: tugas, uts, dan uas.
Menghitung nilai akhir berdasarkan bobot:
* Tugas: 30%
* UTS: 30%
* UAS: 40%
Menggunakan fungsi round() untuk membatasi hasil ke dua desimal.

### 2. Inisialisasi Variabel
```ruby
data_mahasiswa = []
no = 1
```
data_mahasiswa adalah list kosong untuk menyimpan semua data mahasiswa.
no adalah nomor urut mahasiswa, dimulai dari 1.

### 3. Loop Input Data
```ruby
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
```
Bagian ini meminta input dari pengguna berupa:
* nama
* nim
* nilai_tugas
* nilai_uts
* nilai_uas

### 4. Hitung Nilai Akhir dan Simpan ke List
```ruby
nilai_akhir = hitung_nilai_akhir(nilai_tugas, nilai_uts, nilai_uas)
data_mahasiswa.append([no, nama, nim, nilai_tugas, nilai_uts, nilai_uas, nilai_akhir])
no += 1
```
Nilai Akhir dihitung menggunakan fungsi hitung_nilai_akhir.
Data disimpan dalam format list:
```ruby
[No, Nama, NIM, Nilai Tugas, Nilai UTS, Nilai UAS, Nilai Akhir]
```
Nomor urut no bertambah 1 untuk setiap inputan baru.

### 5. Konfirmasi Untuk Menambah Data
```ruby
print("Tambah data(y/t)?", end=" ")
lanjut = input().lower()
if lanjut != 'y':
    break
```
Program meminta pengguna untuk menambah data baru:
* Ketik y untuk melanjutkan.
* Ketik t untuk berhenti.

### 6. Cetak Header Tabel
```ruby
print("="*61)
print("| No | Nama      | NIM   | Tugas | UTS | UAS | Akhir |")
print("="*61)
```
Menampilkan header tabel dengan format rapi menggunakan padding.

### 7. Cetak Data
```ruby
for data in data_mahasiswa:
    print(f"| {data[0]:<2} | {data[1]:<9} | {data[2]:<5} | {data[3]:<5} | {data[4]:<3} | {data[5]:<3} | {data[6]:<5} |")
```
Loop melalui semua data mahasiswa dan menampilkannya dalam tabel dengan format rapi:
:<n> memastikan teks rata kiri dengan panjang n.

### 8. Cetak Footer Tabel
```ruby
print("="*61)
```

## Contoh input/Output
### Input
```ruby
Nama : rasya
NIM : 321241045
Nilai Tugas : 95 
Nilai UTS : 100
Nilai UAS : 100
Tambah data(y/t)? y
Nama : Andi
NIM : 321414123
Nilai Tugas : 80
Nilai UTS : 80
Nilai UAS : 90
Tambah data(y/t)? t
```
### Output
```ruby
=============================================================
| No | Nama      | NIM   | Tugas | UTS | UAS | Akhir |
=============================================================
| 1  | rasya     | 321241045 | 95    | 100 | 100 | 98.5  |
| 2  | Andi      | 321414123 | 80    | 80  | 90  | 84.0  |
=============================================================
```
