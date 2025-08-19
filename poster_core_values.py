from PIL import Image, ImageDraw, ImageFont

# Kanvas A3 300 DPI: 3508 x 4961 px
img = Image.new("RGB", (3508, 4961), color=(237, 242, 252))
draw = ImageDraw.Draw(img)

# Font default (bisa diganti TTF jika ingin)
font_title = ImageFont.load_default()
font_sub = ImageFont.load_default()

# Judul
header_text = "🌟 Core Values SMK Bina Cipta 🌟"
w, h = draw.textsize(header_text, font=font_title)
draw.text(((3508 - w) / 2, 150), header_text, fill=(25, 25, 112), font=font_title)

# Isi core values
values = [
    ("Religius & Berakhlak Mulia", "Berlandaskan iman, takwa, doa, dan akhlak mulia."),
    ("Integritas", "Menjunjung tinggi kejujuran, disiplin, dan tanggung jawab."),
    ("Keunggulan (Excellence)", "Memberikan yang terbaik dalam prestasi akademik & keterampilan."),
    ("Kepedulian & Empati", "Peduli terhadap sesama, khususnya yatim dhuafa."),
    ("Kolaborasi & Kekeluargaan", "Kerja sama harmonis antar guru, siswa, orang tua, dan mitra industri."),
    ("Inovasi & Pembelajaran", "Terbuka terhadap perubahan, berani berinovasi, terus berkembang."),
]

start_y = 400
for title, desc in values:
    draw.text((300, start_y), f"• {title}", fill=(48, 25, 52), font=font_title)
    draw.text((350, start_y + 50), f"{desc}", fill=(60, 60, 60), font=font_sub)
    start_y += 200

# Footer
footer_text = '"Membangun Generasi Unggul, Religius, dan Peduli Sesama"'
w, h = draw.textsize(footer_text, font=font_title)
draw.text(((3508 - w) / 2, 4600), footer_text, fill=(90, 90, 90), font=font_title)

# Simpan JPG
img.save("core_values_smk_bina_cipta_A3.jpg", "JPEG")
