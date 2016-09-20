from os import path
from PIL import Image
import numpy as np
from wordcloud import WordCloud, STOPWORDS

d = path.dirname(__file__)

def get_wordcloud( file ):
    mymask = np.array(Image.open(path.join(d, "mask.png")))
    text = open(path.join(d, file)).read()
    wc = WordCloud(background_color="black", max_words=3000, mask=mymask,
                   stopwords=STOPWORDS.add("said"))
    wc.generate(text)
    filename = "result.png"
    wc.to_file(filename)
    print('wordcloud generated!')
