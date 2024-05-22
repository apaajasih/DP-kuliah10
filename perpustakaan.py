# Buatlah aplikasi manajemen buku dengan menggunakan list dan dictionary, setiap buku terdiri dari (no_isbn, judul, pengarang, isihalaman, deskripsi, stok, booked).
# Lalu ada list mahasiswa (nama, nim, nomerhp, alamat)
# Lalu ada list peminjam (nim, no_isbn, tanggalpinjam, tanggal_kembali, status)


listbuku = [
    {
        "No_ISBN": "A1234",
        "Judul": "Petualangan Sherina",
        "Pengarang": "Adi",
        "Isi_Halaman": "123",
        "Deskripsi": "Petualangan",
        "Stok": 3,
        "Booked": 0,
    },
    {
        "No_ISBN": "B1234",
        "Judul": "Balada Kehidupan",
        "Pengarang": "Cici",
        "Isi_Halaman": "32",
        "Deskripsi": "Slice of Life",
        "Stok": 5,
        "Booked": 0,
    },
    {
        "No_ISBN": "C1234",
        "Judul": "Buddy's",
        "Pengarang": "Budi",
        "Isi_Halaman": "200",
        "Deskripsi": "Petualangan",
        "Stok": 7,
        "Booked": 0,
    }
]

def daftar_buku_tersedia():
    print("Daftar Buku Tersedia:")
    for buku in listbuku:
        if buku["Stok"] > 0:
            print(f"No ISBN: {buku['No_ISBN']}")
            print(f"Judul: {buku['Judul']}")
            print(f"Pengarang: {buku['Pengarang']}")
            print(f"Isi Halaman: {buku['Isi_Halaman']}")
            print(f"Deskripsi: {buku['Deskripsi']}")
            print(f"Stok: {buku['Stok']}")
            print(f"Booked: {buku['Booked']}")
            print()  # Baris kosong untuk memisahkan setiap buku

def pinjam_buku():
    judul = input("Masukkan Judul Buku: ")
    for buku in listbuku:
        if buku["Judul"].lower() == judul.lower() and buku["Stok"] > 0:
            buku["Stok"] -= 1
            buku["Booked"] += 1
            print("Buku berhasil dipinjam.")
            return
    print("Buku tidak tersedia atau stok habis.")

def main():
    while True:
        print("\nMenu:")
        print("1. Pinjam Buku")
        print("2. Tampilkan Daftar Buku Tersedia")
        print("0. Keluar")

        menu = input("Pilih Menu (1/2/0): ")

        if menu == "1":
            pinjam_buku()
        elif menu == "2":
            daftar_buku_tersedia()
        elif menu == "0":
            print("Terima kasih!")
            break
        else:
            print("Menu tidak valid. Silakan pilih menu yang sesuai.")


if __name__ == "__main__":
    main()
