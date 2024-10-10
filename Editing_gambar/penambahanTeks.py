from google.colab import files

# Unggah file font .ttf dari komputer
uploaded = files.upload()

# Setelah diunggah, gunakan path dari file yang diunggah
font_path = "/content/arial.ttf"
from PIL import Image, ImageDraw, ImageFont

def tambahkan_teks(input_path, output_path, teks, font_size, warna_font, posisi='center',nama_font=None):
    """
     Menambahkan teks pada gambar sesuai koordinat yang diberikan pengguna
     
     Args:
         input_path (str): Jalur gambar dari folder
         output_path (str): jalur gambar yang akan disimpan
         teks (str): Teks yang akan ditambahkan
         font_size: Ukuran font yang akan digunakan
         warna_font (str): Warna font yang akan digunakan
         posisi (str): Posisi penempatan teks pada gambar ('center','top-left','top-right','botttom-left','bottom-right')
         nama_font (str): Nama font yang akan digunakan ('arial.ttf','ALGER.TTF',calibri.ttf','cambriab.ttf','times.ttf')"""
    
    # Membuka file gambar
    gambar = Image.open(input_path)
    # Mengolah gambar
    draw = ImageDraw.Draw(gambar)

    # Mengolah font
    if nama_font is None:
        font = ImageFont.load_default(font_size)  # Menggunakan font default
    else:
        font = ImageFont.truetype(nama_font, font_size)  # Gunakan font yang diberikan

    # Menghitung ukuran teks
    # textbbox mengembalikan (x0, y0, x1, y1) yang merupakan kotak pembatas teks
    text_bbox = draw.textbbox((0, 0), teks, font=font) 
    teks_width = text_bbox[2] - text_bbox[0]
    teks_height = text_bbox[3] - text_bbox[1]

    # Menentukan posisi berdasarkan opsi
    if posisi == 'center':
        left = (gambar.width - teks_width) / 2
        top = (gambar.height - teks_height) / 2
    elif posisi == 'top-left':
        left = 10
        top = 10
    elif posisi == 'top-right':
        left = gambar.width - teks_width - 10
        top = 10
    elif posisi == 'bottom-left':
        left = 10
        top = gambar.height - teks_height - 10
    elif posisi == 'bottom-right':
        left = gambar.width - teks_width - 10
        top = gambar.height - teks_height - 10
    else:
        raise ValueError("Posisi tidak dikenal. Gunakan 'center', 'top-left', 'top-right', 'bottom-left', atau 'bottom-right'.")

    # Menempatkan teks
    draw.text((left, top), teks, fill=warna_font, font=font)
    gambar.save(output_path)  # Menyimpan hasil di output
    gambar.show()  # Menunjukkan hasil gambar yang telah ditambahkan teks

# help(tambahkan_teks)

# tambahkan_teks(
#     input_path="C:\\Users\\aisyah salsabila\Downloads\Jay Wallpaper.jpeg",
#     output_path="C:\\Users\\aisyah salsabila\Downloads\Jaii Wallpaper.jpeg",
#     teks="Halo Dunia",
#     font_size=100,
#     warna_font='red',
#     nama_font=None,
#     posisi='bottom-right'
# )
