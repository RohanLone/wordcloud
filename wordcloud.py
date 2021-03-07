import streamlit as st
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
from wordcloud import WordCloud,ImageColorGenerator,STOPWORDS

st.set_option('deprecation.showPyplotGlobalUse', False)
def cloud_generator(image,text, max_words,max_font,random):

  fontp='Mermaid Swash Caps.ttf'
  stop_words=set(STOPWORDS)
  stop_words.update(['no','not','nor','asked', 'made', 'half', 'much',
    'certainly', 'might', 'came','us', 'one', 'will', 'said', 'now', 'well', 'man', 'may',
    'little', 'say', 'must', 'way', 'long', 'yet', 'mean',
    'put', 'seem'])
  wc = WordCloud(stopwords=stop_words, font_path=fontp, 
               background_color="Black", max_words=max_words,
               max_font_size=max_font,mask=image, random_state=random).generate(text)
  image_colors = ImageColorGenerator(image)

  plt.figure(figsize=(100,100))
  fig, axes = plt.subplots(1,2, gridspec_kw={'width_ratios': [3, 2]})
  axes[0].imshow(wc, interpolation="bilinear")
    # recolor wordcloud and show
    # we could also give color_func=image_colors directly in the constructor
   # axes[1].imshow(wc.recolor(color_func=image_colors), interpolation="bilinear")
  axes[1].imshow(image, cmap=plt.cm.gray, interpolation="bilinear")
  for ax in axes:
    ax.set_axis_off()
    
  st.pyplot()


def main():
  st.title('Word Cloud')
  st.write('[By Rohan Lone](https://www.linkedin.com/in/rohanlone/)')
  max_words = st.sidebar.slider('Maximum Words', 200, 2000, 500)
  max_font = st.sidebar.slider('Maximum font size',60,256,100)
  random = st.sidebar.slider("Random State", 30, 100, 42 )
  image = st.file_uploader("Please upload an image file", type=["jpg", "png"])
  text = st.text_area("Paste text here....")
  if image and text is not None:
    if st.button('PLOT WORD CLOUD'):
      image=np.asarray(Image.open(image))
      st.write('WordCloud vs Original Image')
      st.write(cloud_generator(image,text, max_words,max_font,random))


if __name__=="__main__":
    main()