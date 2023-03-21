from PIL import ImageFont, Image, ImageDraw
from io import BytesIO
import ddddocr
from fontTools.ttLib import TTFont


def font_to_img(_code, filename):
    """将字体画成图片"""
    img_size = 1024
    img = Image.new("1", (img_size, img_size), 255)
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype(filename, int(img_size * 0.7))
    txt = chr(_code)
    x, y = draw.textsize(txt, font=font)
    draw.text(((img_size - x) // 2, (img_size - y) // 2), txt, font=font, fill=0)
    return img


def identify_word(_ttf_path):
    """识别ttf字体结果"""
    font = TTFont(_ttf_path)
    ocr = ddddocr.DdddOcr()
    dict_data1 = {}
    dict_data2 = {}
    for cmap_code, glyph_name in font.getBestCmap().items():
        bytes_io = BytesIO()
        pil = font_to_img(cmap_code, _ttf_path)
        pil.save(bytes_io, format="PNG")
        word = ocr.classification(bytes_io.getvalue())  # 识别字体
        dict_data1[glyph_name] = word
        dict_data2[str(cmap_code)] = word
        # print(cmap_code, glyph_name, word)
        # with open(f"./img/{cmap_code}_{glyph_name}.png", "wb") as f:
        #     f.write(bytes_io.getvalue())
    # 将打印出来的字典数据直接粘贴到一个新的文件中，使用"替换' ——CmapCode2word.json和GlyphName2word.json文件生成的方式
    print(dict_data1)
    print(dict_data2)


if __name__ == "__main__":
    identify_word("sarasa-shuffle.ttf")
