from os import path
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

d = path.dirname(__file__)
data_file = "word_data.txt"
# image_file = "batman.jpeg"
image_file = "batman.jpeg"
# font_file = "Inconsolata for Powerline.otf"
# font_file = "Monofur for Powerline.ttf"
font_file = "Go Mono Bold for Powerline.ttf"
logo_file = "logo.jpg"

print("Reading data file ...")
text = open(path.join(d, data_file)).read()

print("Getting colors from image ...")
alice_coloring = np.array(Image.open(path.join(d, image_file)))

print("Generating text with WordCloud ... ")
wc = WordCloud(
    background_color="white",
    max_words=500000,
    mask=alice_coloring,
    max_font_size=60,
    random_state=102,
    scale=8,
    font_path=path.join(d, font_file)
).generate(text)

print("Loading Text ...")
wc.generate_from_text(text)

# change text colors
print("Generating colors for text ...")
img_colors = ImageColorGenerator(alice_coloring)

# text color to background color
wc.recolor(color_func=img_colors)

# plot wordcloud image
plt.imshow(wc, interpolation="bilinear")

# remove x, y axises
plt.axis("off")
plt.show()


save_logo = input("\n=============\nSave: yes/no\n")

if save_logo.lower() in ["yes", "y"]:
    logo_file = str(input("Logo name(no extension): \n")) + ".jpg"
    d = path.dirname(__file__)
    logo_path = path.join(d, logo_file)
    wc.to_file(logo_path)
    print("Logo saved in ./{}".format(logo_path))
else:
    print("Logo discarded.")





