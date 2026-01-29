import pandas as pd

# 1. Load the fresh Excel sheet
source_file = "Translation_Master_Sheet.xlsx"
output_file = "Translation_Master_Filled.xlsx"

print("Loading Excel file...")
try:
    df = pd.read_excel(source_file).fillna("")
except FileNotFoundError:
    print(f"Error: Could not find '{source_file}'.")
    exit()

# 2. THE MASTER DICTIONARY (English -> Malay)
# Combined from Batch 1 & Batch 2
translation_memory = {
    # --- COMMON BUTTONS & LABELS ---
    "Email": "E-mel",
    "Password": "Kata Laluan",
    "Login": "Log Masuk",
    "Sign In": "Log Masuk",
    "Sign Out": "Log Keluar",
    "Sign Up": "Daftar",
    "Register": "Daftar",
    "Logout": "Log Keluar",
    "Submit": "Hantar",
    "Save": "Simpan",
    "Cancel": "Batal",
    "Edit": "Sunting",
    "Delete": "Padam",
    "View": "Lihat",
    "Add": "Tambah",
    "Update": "Kemaskini",
    "Back": "Kembali",
    "Next": "Seterusnya",
    "Close": "Tutup",
    "Yes": "Ya",
    "No": "Tidak",
    "Confirm": "Sahkan",
    "OK": "OK",
    "Search": "Cari",
    "Filter": "Tapis",
    "Reset": "Tetap Semula",
    "Active": "Aktif",
    "Inactive": "Tidak Aktif",
    "Pending": "Menunggu",
    "Approved": "Diluluskan",
    "Rejected": "Ditolak",
    "Draft": "Draf",
    "Created": "Dicipta",
    "Completed": "Selesai",
    "Closed": "Ditutup",
    "Removed": "Dibuang",
    "Available": "Tersedia",
    "Cancelled": "Dibatalkan",
    "All": "Semua",
    "List": "Senarai",
    "Detail": "Perincian",
    "New": "Baru",
    
    # --- FORM LABELS ---
    "Full Name": "Nama Penuh",
    "First Name": "Nama Pertama",
    "Last Name": "Nama Akhir",
    "Old Password": "Kata Laluan Lama",
    "New Password": "Kata Laluan Baru",
    "Password Confirmation": "Pengesahan Kata Laluan",
    "OTP": "OTP",
    "Remember Me": "Ingat Saya",
    "Forgot Password?": "Lupa Kata Laluan?",
    "Forgot Password": "Lupa Kata Laluan",
    "Reset Password": "Tetap Semula Kata Laluan",
    "Set Password": "Tetapkan Kata Laluan",
    "Change Password": "Tukar Kata Laluan",
    "Username": "Nama Pengguna",
    "Mobile Number": "Nombor Telefon",
    "Roles": "Peranan",
    "Email Address": "Alamat E-mel",
    "Name": "Nama",
    "Timezone": "Zon Masa",
    "Dealer Role": "Peranan Pengedar",
    "Branch Role": "Peranan Cawangan",
    
    # --- BUTTONS & ACTIONS ---
    "Approve": "Luluskan",
    "Reject": "Tolak",
    "Back to Sign In": "Kembali ke Log Masuk",
    "Confirm OTP": "Sahkan OTP",
    "Contact Us": "Hubungi Kami",
    "Continue": "Teruskan",
    "Create": "Cipta",
    "Download File": "Muat Turun Fail",
    "Export CSV/Excel": "Eksport CSV/Excel",
    "Import CSV/Excel": "Import CSV/Excel",
    "More Info": "Maklumat Lanjut",
    "Need Help?": "Perlu Bantuan?",
    "Profile": "Profil",
    "Registration": "Pendaftaran",
    "Resend OTP": "Hantar Semula OTP",
    "Upload File": "Muat Naik Fail",
    "Yes, Confirm": "Ya, Sahkan",
    "No, Go Back": "Tidak, Kembali",
    "About Us": "Tentang Kami",
    "Terms & Conditions": "Terma & Syarat",
    "Privacy Policy": "Dasar Privasi",
    "Click here": "Klik di sini",
    "Drop the files here...": "Letakkan fail di sini...",
    
    # --- MONTHS ---
    "January": "Januari", "February": "Februari", "March": "Mac",
    "April": "April", "May": "Mei", "June": "Jun",
    "July": "Julai", "August": "Ogos", "September": "September",
    "October": "Oktober", "November": "November", "December": "Disember",
    
    # --- MENU ITEMS ---
    "Admins": "Pentadbir",
    "Clients": "Pelanggan",
    "Dashboard - Malaysia": "Papan Pemuka - Malaysia",
    "Maintenance": "Penyelenggaraan",
    "Reports": "Laporan",
    "Settings": "Tetapan",
    "Tickets": "Tiket",
    "Select Start Date - End Date": "Pilih Tarikh Mula - Tarikh Tamat",

    # --- ERRORS & ALERTS (COMPLEX) ---
    "Invalid email format.": "Format e-mel tidak sah.",
    "Invalid file": "Fail tidak sah",
    "Invalid phone number format.": "Format nombor telefon tidak sah.",
    "Minimum phone number 9 - 10 digits (eg 08XXXXXXXX)": "Nombor telefon minimum 9 - 10 digit (cth 08XXXXXXXX)",
    "The new password must differ from the old password.": "Kata laluan baru mesti berbeza daripada kata laluan lama.",
    "New password and Password Confirmation do not match.": "Kata laluan baru dan Pengesahan Kata Laluan tidak sepadan.",
    "Please recheck all required fields.": "Sila semak semula semua ruangan yang diperlukan.",
    "An OTP has been sent to your email.": "OTP telah dihantar ke e-mel anda.",
    "Your password must follow these rules": "Kata laluan anda mesti mengikut peraturan ini",
    "Please setup your password within the next 5 minutes.": "Sila tetapkan kata laluan anda dalam masa 5 minit.",
    "Must be 8-16 characters": "Mesti 8-16 aksara",
    "At least 1 lowercase character": "Sekurang-kurangnya 1 huruf kecil",
    "At least 1 special character !@#$": "Sekurang-kurangnya 1 aksara khas !@#$",
    "At least 1 uppercase character": "Sekurang-kurangnya 1 huruf besar",
    "At least 1 digit": "Sekurang-kurangnya 1 digit",
    "This action cannot be undone.": "Tindakan ini tidak boleh dibuat asal.",
    "Alert!": "Amaran!",
    "No Permission": "Tiada Kebenaran",
    
    # --- VARIABLES (KEEP CURLY BRACES) ---
    "Add {{new_text}}": "Tambah {{new_text}}",
    "New {{new_text}}": "Baru {{new_text}}",
    "Add {{text}}": "Tambah {{text}}",
    "Yes, {{status}}": "Ya, {{status}}",
    "Successfully {{success_text}}": "Berjaya {{success_text}}",
    "Are you sure you want to {{status}}?": "Adakah anda pasti mahu {{status}}?",
    "Are you sure you want to sign out?": "Adakah anda pasti mahu log keluar?",
    "Are you sure you want to remove file: {{fileName}}?": "Adakah anda pasti mahu membuang fail: {{fileName}}?",
    "{{label}} cancelled successfully.": "{{label}} berjaya dibatalkan.",
    "{{label}} has been created successfully.": "{{label}} telah berjaya dicipta.",
    "Successfully {{message}}": "Berjaya {{message}}",
    "The webpage will redirect to {{webpage}} page in {{seconds}} seconds.": "Laman web akan dialihkan ke halaman {{webpage}} dalam {{seconds}} saat.",
    "Please upload up to 1 file ({{type}}, max 5MB) for each upload field.": "Sila muat naik sehingga 1 fail ({{type}}, maks 5MB) untuk setiap medan.",
    "{{label}} must not be less than {{minimum}}.": "{{label}} tidak boleh kurang daripada {{minimum}}.",
    "{{label}} must not be more than {{maximum}}.": "{{label}} tidak boleh lebih daripada {{maximum}}.",
    "The OTP ({{ref_code}}) has expired.": "OTP ({{ref_code}}) telah tamat tempoh.",
    "Time limit exceeded. Each attempt cannot take longer than 5 minutes. Please try again.": "Had masa tamat. Setiap percubaan tidak boleh melebihi 5 minit. Sila cuba lagi.",
    "Please attach a maximum of {{maxFiles}} photos.": "Sila lampirkan maksimum {{maxFiles}} foto.",
    "Supports only {{type}} files.": "Hanya menyokong fail jenis {{type}}.",
    " to upload or drop file here": " untuk memuat naik atau letak fail di sini"
}

print("Translating...")

def get_translation(english_text):
    # THE TRIM COMMAND: Removes invisible spaces
    clean_text = str(english_text).strip()
    
    if clean_text in translation_memory:
        return translation_memory[clean_text]
    else:
        # If we can't find it, verify if it's just a number or symbol
        return ""

# Apply translation
df['Bahasa_Melayu'] = df['English_Source'].apply(get_translation)

# Save
df.to_excel(output_file, index=False)
print(f"Done! Created '{output_file}' with translations filled in.")