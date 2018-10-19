from PIL import Image, ImageDraw, ImageFont

base_dir = 'BannerGenerator/'
export_dir = base_dir + 'export/'
src_dir = base_dir + 'src/'
font_path = '/usr/share/fonts/TTF/RobotoCondensed-Bold.ttf'
cjk_font_path = '/usr/share/fonts/noto-cjk/NotoSansCJK-DemiLight.ttc'

def gen_num(text):
    img = Image.open(src_dir + '-num.png')
    num_box = (95, 150, 155, 195)
    num_area = draw_num(text)
    img.paste(num_area, num_box)
    img.save(export_dir + text + '-num.png')

def draw_num(text):
    num_area = Image.new('RGB', (60, 45), color='white');
    fnt = ImageFont.truetype(font_path, 38);
    d = ImageDraw.Draw(num_area)
    d.text((0, 0), text, font=fnt, fill=(61, 167, 66))
    return num_area

def gen_date(text):
    img = Image.open(src_dir + '-date.png')
    date_box = (180, 30, 250, 70)
    time_box = (315, 35, 465, 65)
    date_area, time_area = draw_date(text)
    img.paste(date_area, date_box)
    img.paste(time_area, time_box)
    img.save(export_dir + text[0] + text[1] + '-date.png')

def draw_date(text):
    date_area = Image.new('RGB', (70, 40), color='white');
    time_area = Image.new('RGB', (150, 30), color='white');
    date_fnt = ImageFont.truetype(font_path, 28);
    time_fnt = ImageFont.truetype(cjk_font_path, 20);
    date_d = ImageDraw.Draw(date_area)
    time_d = ImageDraw.Draw(time_area)
    date_d.text((0, 0), text[0], font=date_fnt, fill=(61, 167, 66))
    time_d.text((0, 0), text[1], font=time_fnt, fill=(88, 88, 88))

    return date_area, time_area

if __name__ == "__main__":
    gen_num('123')
    gen_date(['10.13', '晚上 18:30 入场'])
