from PIL import Image, ImageEnhance
import os

def adjust_brightness(image_path,output_path,level=1):
    """
    Mengubah kecerahan gambar berdasarkan level yang ditentukan dan menyimpan hasilnya.

    Fungsi ini menerima jalur file gambar, jalur keluaran untuk gambar hasil, 
    dan level kecerahan yang diinginkan. Kecerahan gambar akan diatur 
    berdasarkan level yang ditentukan, dengan pilihan level sebagai berikut:
    
    - 'sangat gelap': 0.2
    - 'gelap': 0.5
    - 'normal': 1.0 (default)
    - 'cerah': 1.5
    - 'sangat cerah': 2.0
    
    Jika level yang diberikan tidak dikenali, fungsi akan menggunakan nilai 
    kecerahan default (1.0 - normal).

    Parameter:
    -----------
    image_path : str
        Jalur file gambar input yang akan diubah kecerahannya.
    output_path : str
        Jalur file tempat gambar hasil akan disimpan.
    level : str
        Level kecerahan yang diinginkan (misalnya 'gelap', 'cerah', dll.).

    Catatan:
    - Fungsi ini akan menampilkan pesan kesalahan jika file gambar tidak ditemukan.
    - Gambar hasil akan disimpan dan ditampilkan setelah kecerahan diubah.

    Returns:
    --------
    Tidak ada nilai yang dikembalikan secara eksplisit, tetapi gambar hasil 
    akan disimpan di jalur output yang ditentukan.
    """
    # Faktor kecerahan berdasarkan level yang ditentukan
    brightness_factors = {
        'sangat gelap': 0.2,
        'gelap': 0.5,
        'normal': 1.0,
        'cerah': 1.5,
        'sangat cerah': 2.0
    }
    
    # Mendapatkan faktor kecerahan dari level yang diberikan
    factor = brightness_factors.get(level.lower(), 1.0)  # Default ke 'normal' jika level tidak valid

    # Cek apakah file gambar ada
    if not os.path.isfile(image_path):
        print(f"File gambar tidak ditemukan: {image_path}")
        return

    image = Image.open(image_path) # Membuka file gambar
    enhancer = ImageEnhance.Brightness(image) # Menggunakan fungsi pencerahan dari pillow
    brightened_image = enhancer.enhance(factor) #  Menentukan skala kecerahan gambar
    brightened_image.save(output_path) # Menyimpan hasil di jalur output
    brightened_image.show(output_path) # Menunjukkan hasil pencerahan gambar

# adjust_brightness(
#     "C:\\Users\jpael\OneDrive\Pictures\Ignition Teaser.png", # Buat backslash (\) menjadi double backslash (\\) agar path gambar dapat terbaca
#     "C:\\Users\jpael\OneDrive\Pictures\Ignition Teaser14.png", # Buat backslash (\) menjadi double backslash (\\) agar path gambar dapat terbaca
#     "sangat gelap" # Pilihan level yang tersedia: sangat gelap, gelap, normal, cerah, sangat cerah
# )
