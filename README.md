"# Project-kelompok-3B-algoritma" 
pip install .
# cara pakai menggunakan link github di Google collab (!pip install git+https://github.com/Jeanjrg/Project-kelompok-3B-algoritma.git)
# cara pakai menggunakan link pypi di google collab (pip install Project-kelompok-3B-algoritma
, import Editing_gambar *)

Library editing gambar merujuk pada fitur dalam platform seperti WordPress yang memungkinkan pengguna untuk mengupload dan menyimpan file gambar. Di dalam library ini, pengguna dapat melakukan beberapa manipulasi dasar pada gambar yang diunggah, seperti pemotongan dan penyesuaian sederhana.

# fitur kecerahan
Brightness feature adalah paket Python yang digunakan untuk menyesuaikan kecerahan gambar. Paket ini memudahkan pengguna dalam mengubah kecerahan gambar sesuai kebutuhan.

## Fitur
- Menyesuaikan kecerahan gambar
- Mendukung berbagai format gambar

## cara penggunaan
- image_path (str): Jalur gambar dari folder.
- output_path (str): Jalur gambar yang akan disimpan.
- level (float): Tingkat kecerahan yang diinginkan (angka antara 0.0 dan 2.0)



## fitur hitam putih
Digunakan untuk mengubah gambar berwarna menjadi gambar grayscale (hitam-putih). 

## Fitur
- Menyesuaikan warna hitam putih pada gambar
- Mendukung berbagai format gambar

## cara penggunaan 
- input_image_path (str): Jalur gambar dari folder.
- output_image_path (str): Jalur gambar yang akan disimpan.

## fitur pencerminan
Digunakan untuk membalik (flip) gambar secara horizontal atau vertikal. 

## Fitur
- Membalik gambar
- Mendukung berbagai format gambar

## cara penggunaan 
 image_path(str):
        Lokasi file gambar yang akan dibalik. Pastikan menggunakan double backslashes (\\)
        
    output_path(str):
        Lokasi file tempat gambar yang akan disimpan. Pastikan menggunakan double backslashes (\\)

    direction(str):
         Arah pemantulan gambar dapat berupa:
            -'horizontal': untuk membalik gambar secara horizontal
            -'vertikal': untuk membalik gambar secara vertikal.

## fitur pemotongan gambar
Digunakan untuk memotong (crop) gambar. 

## Fitur
- Memotong gambar
- Mendukung berbagai format gambar

## cara penggunaan
- input_path (str): jalur gambar dari folder
- out_path (str): jalur gambar yang akan disimpan
- left,top: koordinat parameter pemotongan gambar bagian kiri atas
- right,bottom: koordinat parameter pemotongan gambar bagian kanan bawah"""


## fitur penambahan teks
Digunakan untuk menambahkan teks ke dalam gambar. 

## Fitur
- Menambah teks
- Mendukung berbagai format gambar

## cara penggunaan
        input_path (str): Jalur gambar dari folder
        output_path (str): jalur gambar yang akan disimpan
        teks (str): Teks yang akan ditambahkan
        font_size: Ukuran font yang akan digunakan
        warna_font: Warna font yang akan digunakan
        posisi: Posisi teks yang akan ditambahkan"""

## fitur rotasi gambar
Digunakan untuk memutar gambar pada sudut tertentu. 

## Fitur
- Memutar gambar
- Mendukung berbagai format gambar

## cara penggunaan
    input_path (str): Jalur gambar dari folder.
    output_path (str): Jalur gambar yang akan disimpan.
    angle (float): Sudut rotasi dalam derajat.
