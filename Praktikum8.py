class DaftarNilaiMahasiswa:
    def __init__(self):
        self.data_mahasiswa = []
    
    def tambah(self, nama, nilai):
        """Menambah data mahasiswa ke dalam daftar."""
        self.data_mahasiswa.append({"nama": nama, "nilai": nilai})
        print(f"Data mahasiswa '{nama}' berhasil ditambahkan.")
    
    def tampilkan(self):
        """Menampilkan semua data mahasiswa."""
        if not self.data_mahasiswa:
            print("Tidak ada data mahasiswa.")
        else:
            print("\nDaftar Nilai Mahasiswa:")
            for i, mahasiswa in enumerate(self.data_mahasiswa, 1):
                print(f"{i}. Nama: {mahasiswa['nama']}, Nilai: {mahasiswa['nilai']}")
    
    def hapus(self, nama):
        """Menghapus data mahasiswa berdasarkan nama."""
        for mahasiswa in self.data_mahasiswa:
            if mahasiswa["nama"] == nama:
                self.data_mahasiswa.remove(mahasiswa)
                print(f"Data mahasiswa '{nama}' berhasil dihapus.")
                return
        print(f"Data mahasiswa dengan nama '{nama}' tidak ditemukan.")
    
    def ubah(self, nama, nilai_baru):
        """Mengubah nilai mahasiswa berdasarkan nama."""
        for mahasiswa in self.data_mahasiswa:
            if mahasiswa["nama"] == nama:
                mahasiswa["nilai"] = nilai_baru
                print(f"Data mahasiswa '{nama}' berhasil diubah.")
                return
        print(f"Data mahasiswa dengan nama '{nama}' tidak ditemukan.")

# Contoh penggunaan
daftar = DaftarNilaiMahasiswa()

# Menambahkan data
daftar.tambah("Safitri", 85)
daftar.tambah("Diva", 90)

# Menampilkan data
daftar.tampilkan()

# Mengubah data
daftar.ubah("Safitri", 95)

# Menampilkan data setelah perubahan
daftar.tampilkan()

# Menghapus data
daftar.hapus("Diva")

# Menampilkan data setelah penghapusan
daftar.tampilkan()