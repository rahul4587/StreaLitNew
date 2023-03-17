import easyocr as ocr  #OCR
import streamlit as st  #Web App
from PIL import Image #Image Processing
import numpy as np #Image Processing

#title
st.title("Let the Image Speak! 🗣️ ")

#subtitle
st.markdown("### Created using OCR and StreamLit")

st.markdown("")

#image uploader
image = st.file_uploader(label = "Upload your image here ⬇️ ",type=['png','jpg','jpeg'])

st.markdown("")


@st.cache
def load_model(): 
    reader = ocr.Reader(['en'],model_storage_directory='.')
    return reader 

reader = load_model() #load model

if image is not None:

    input_image = Image.open(image) #read image
    st.image(input_image) #display image
    st.markdown("")

    with st.spinner("🤖 AI is at Work, Hang Alive... "):
        

        result = reader.readtext(np.array(input_image))

        result_text = [] #empty list for results


        for text in result:
            result_text.append(text[1])

        st.write(result_text)
    #st.success("Here you go!")
    st.balloons()
else:
    st.write("Upload an Image")

st.caption("Made with ❤️ by @Rahul_Pal")





