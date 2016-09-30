from os import path
import numpy as np
from wordcloud import WordCloud, STOPWORDS
from PIL import ImageDraw, Image

d = path.dirname(__file__)

def add_corners(im, rad):
    circle = Image.new('L', (rad * 2, rad * 2), 0)
    draw = ImageDraw.Draw(circle)
    draw.ellipse((0, 0, rad * 2, rad * 2), fill=255)
    alpha = Image.new('L', im.size, 255)
    w, h = im.size
    alpha.paste(circle.crop((0, 0, rad, rad)), (0, 0))
    alpha.paste(circle.crop((0, rad, rad, rad * 2)), (0, h - rad))
    alpha.paste(circle.crop((rad, 0, rad * 2, rad)), (w - rad, 0))
    alpha.paste(circle.crop((rad, rad, rad * 2, rad * 2)), (w - rad, h - rad))
    im.putalpha(alpha)
    return im

def get_wordcloud( file ):
    mymask = np.array(Image.open(path.join(d, "mask.png")))
    text = open(path.join(d, file)).read()
    wc = WordCloud(background_color="black", max_words=1500, mask=mymask,
                   stopwords=STOPWORDS.add("said"))
    wc.generate(text)
    wc.to_file("result.png")
    im = Image.open('result.png')
    im = add_corners(im, 350)
    im.save('result.png')

    print('wordcloud generated!')
