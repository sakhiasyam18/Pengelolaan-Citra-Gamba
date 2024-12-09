from PIL import Image, ImageFilter

def lighten_image(image, factor=1.5):
    return image.point(lambda p: min(255, int(p * factor)))

def darken_image(image, factor=0.5):
    return image.point(lambda p: int(p * factor))

def process_image(image_path):
    try:
        # Membuka gambar asli
        gambar_asli = Image.open(image_path)

        # Memastikan gambar dalam orientasi potret
        if gambar_asli.width > gambar_asli.height:
            gambar_asli = gambar_asli.rotate(90, expand=True)

        # Mengubah ukuran gambar (misalnya, menjadi setengah dari ukuran asli)
        gambar_asli = gambar_asli.resize((gambar_asli.width // 2, gambar_asli.height // 2))

        # Menerapkan filter dan menyimpan hasilnya
        filters = {
            "Gambar_Blur.jpg": gambar_asli.filter(ImageFilter.BLUR),
            "Gambar_Sharpen.jpg": gambar_asli.filter(ImageFilter.SHARPEN),
            "Gambar_Emboss.jpg": gambar_asli.filter(ImageFilter.EMBOSS),
            "Gambar_Edge_Detection.jpg": gambar_asli.filter(ImageFilter.FIND_EDGES),
            "Gambar_Lighten.jpg": lighten_image(gambar_asli),
            "Gambar_Darken.jpg": darken_image(gambar_asli)
        }

        for filename, img in filters.items():
            img.save(filename, quality=95)  # Menyimpan dengan kualitas 95
            img.show()

    except FileNotFoundError:
        print(f"File gambar '{image_path}' tidak ditemukan.")
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")

# Panggil fungsi dengan path gambar yang sesuai
process_image("DSC00257.PNG")