from PIL import Image, ImageDraw, ImageFont

base_dir = 'BannerGenerator/'
export_dir = base_dir + 'export/'
src_dir = base_dir + 'src/'
font_path = '/usr/share/fonts/TTF/RobotoCondensed-Bold.ttf'

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
    date_box = (200, 30, 250, 70)
    date_area = draw_date(text)
    img.paste(date_area, date_box)
    img.save(export_dir + text + '-date.png')

def draw_date(text):
    date_area = Image.new('RGB', (50, 40), color='white');
    fnt = ImageFont.truetype(font_path, 28);
    d = ImageDraw.Draw(date_area)
    d.text((0, 0), text, font=fnt, fill=(61, 167, 66))
    return date_area

if __name__ == "__main__":
    gen_num('121')
    gen_date('9.15')
