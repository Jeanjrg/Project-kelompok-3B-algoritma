from PIL import Image

def convert_image_to_grayscale(input_path,output_path):
    """
    Mengonversi gambar berwarna menjadi gambar grayscale dan menyimpannya.

    Fungsi ini menerima jalur file gambar berwarna sebagai input, mengonversinya
    menjadi gambar grayscale, dan menyimpan gambar hasil di jalur yang ditentukan.

    Parameter:
    -----------
    input_path : str
        Jalur file gambar input yang akan diubah menjadi grayscale.
    output_path : str
        Jalur file tempat gambar grayscale akan disimpan.

    Catatan:
    - Jika terjadi kesalahan saat membuka gambar, fungsi akan menampilkan pesan kesalahan.
    - Setelah gambar berhasil diubah menjadi grayscale, gambar hasil akan disimpan dan ditampilkan.

    Returns:
    --------
    Tidak ada nilai yang dikembalikan secara eksplisit, tetapi gambar hasil akan disimpan 
    di jalur output yang ditentukan.
    """
    # Buka gambar
    try:
        image = Image.open(input_path)
    except Exception as e:
        print(f"Error opening image: {e}")
        return
    
    # Ubah gambar ke grayscale
    grayscale_image = image.convert('L')

    # Simpan gambar grayscale
    grayscale_image.save(output_path)
    print(f"Gambar grayscale telah disimpan di: {output_path}")

    # Menunjukkan hasil gambar
    grayscale_image.show()

# convert_image_to_grayscale(
#     "C:\\Users\jpael\OneDrive\Pictures\Ignition Teaser.png", # Buat backslash (\) menjadi double backslash (\\) agar path gambar dapat terbaca
#     "C:\\Users\jpael\OneDrive\Pictures\Ignition Teaser14.png" # Buat backslash (\) menjadi double backslash (\\) agar path gambar dapat terbaca
# )
