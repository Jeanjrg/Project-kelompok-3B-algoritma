from PIL import Image     

def ukuran_gambar(Input_path,Output_path,left,top,right,bottom):
    """Fungsi untuk memotong gambar sesuai dengan koordinat yang ditentukan oleh pengguna.

    Fungsi ini menerima jalur gambar input, jalur gambar output, dan koordinat
    batas potongan (kiri, atas, kanan, bawah) untuk memotong gambar dalam bentuk persegi panjang.

    Parameters:
    Input_path (str): Jalur lengkap file gambar yang ingin dipotong. Pastikan format jalur sudah benar.
                      Contoh: r'C:\\Users\\nama\\Pictures\\image.png'
    Output_path (str): Jalur lengkap tempat menyimpan gambar hasil potongan. Pastikan format jalur sudah benar.
                       Contoh: r'C:\\Users\\nama\\Pictures\\image_cropped.png'
    left (int): Koordinat batas kiri gambar yang ingin dipotong (nilai piksel).
    top (int): Koordinat batas atas gambar yang ingin dipotong (nilai piksel).
    right (int): Koordinat batas kanan gambar yang ingin dipotong (nilai piksel).
    bottom (int): Koordinat batas bawah gambar yang ingin dipotong (nilai piksel).

    Returns:
    str: Pesan sukses atau pesan kesalahan jika terjadi masalah.

    Contoh penggunaan:
    ukuran_gambar(
        r'C:\\Users\\nama\\Pictures\\image.png',    # Jalur gambar input
        r'C:\\Users\\nama\\Pictures\\image_cropped.png',  # Jalur gambar output
        0, 0, 2000, 2000  # Koordinat kiri, atas, kanan, bawah
    )
    """
    try:
        image = Image.open(Input_path) # Membuka file gambar
        cropped_image = image.crop((left, top, right, bottom)) # Memotong gambar sesuai koordinat kiri atas dan kanan bawah sehingga terbentuk segii empat
        cropped_image.save(Output_path) # Menyimpan hasil di jalur output
        cropped_image.show() # Menunjukkan hasil gambar yang telah dipotong
        return f"Gambar berhasil dipotong dan disimpan di {Output_path}" # Akhir dari program
    except Exception as e:
        return f"Terjadi kesalahan: {e}"

# ukuran_gambar(
#               "C:\\Users\jpael\OneDrive\Pictures\Ignition Teaser.png", # Buat backslash (\) menjadi double backslash (\\) agar path gambar dapat terbaca
#               "C:\\Users\jpael\OneDrive\Pictures\Ignition Teaser14.png", # Buat backslash (\) menjadi double backslash (\\) agar path gambar dapat terbaca
#               0,0,2000,2000 # parameter untuk batasan pemotongan gambar
# )


