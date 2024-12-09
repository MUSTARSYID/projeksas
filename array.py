class Contact:
    def _init_(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

    def _str_(self):
        return f"Nama: {self.name}\nTelepon: {self.phone}\nEmail: {self.email}"

class ContactManager:
    def _init_(self):
        self.contacts = []  # Menyimpan daftar kontak

    def add_contact(self, contact):
        self.contacts.append(contact)

    def remove_contact(self, name):
        for contact in self.contacts:
            if contact.name == name:
                self.contacts.remove(contact)
                print(f"Kontak {name} berhasil dihapus.")
                return
        print(f"Kontak dengan nama {name} tidak ditemukan.")

    def show_all_contacts(self):
        if not self.contacts:
            print("Tidak ada kontak yang disimpan.")
        else:
            for contact in self.contacts:
                print(contact)
                print("-" * 30)  # Pemisah antara kontak

def main():
    manager = ContactManager()  # Membuat objek ContactManager

    while True:
        print("\n=== Sistem Manajemen Kontak ===")
        print("1. Tambah Kontak")
        print("2. Hapus Kontak")
        print("3. Tampilkan Semua Kontak")
        print("4. Keluar")
        
        choice = input("Pilih menu (1/2/3/4): ")
        
        if choice == '1':
            name = input("Masukkan nama: ")
            phone = input("Masukkan nomor telepon: ")
            email = input("Masukkan email: ")
            
            contact = Contact(name, phone, email)
            manager.add_contact(contact)
            print("Kontak berhasil ditambahkan.")
        
        elif choice == '2':
            name = input("Masukkan nama kontak yang ingin dihapus: ")
            manager.remove_contact(name)
        
        elif choice == '3':
            print("\nDaftar Kontak:")
            manager.show_all_contacts()
        
        elif choice == '4':
            print("Keluar dari program.")
            break
        
        else:
            print("Pilihan tidak valid, coba lagi.")

        if __name__ == "_main_":
            main()