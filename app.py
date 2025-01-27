import streamlit as st
from PIL import Image, ImageEnhance,ImageFilter
import io
st.set_page_config(page_icon="data:image/png;base64,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",
page_title="SnapIt")
st.markdown(
    """
    <style>
    .stApp{
    background-image:url("https://static.vecteezy.com/system/resources/previews/035/550/617/non_2x/ai-generated-spring-is-a-magic-season-beautifulrealistic-wallpaper-with-copy-space-for-text-free-photo.jpg");
    background-size:cover;

    }
    h1{
    color:purple;
    font-family:cambria;
    font-weight:lighter;
    padding-bottom:60px;}
    h3{
    color:grey;
    font-family:bookmanoldstyle;
    font-weight:lighter lighter lighter;
    padding-bottom:30px;
    }
    h4{
    font-weight:lighter;}
    </style>
    """,unsafe_allow_html=True
)
st.title("Add Unique Filters to your pictures")
st.markdown("<h3>Upload here to customise your images with filters and download!</h3>",unsafe_allow_html=True)
uploaded_image=st.file_uploader("Choose your image..!",type=["jpg","png","jpeg"])
if uploaded_image is None:
    st.markdown("<h4>Please upload image to apply Filters</h4>",unsafe_allow_html=True)
else:
    image=Image.open(uploaded_image)
    st.image(image,caption="Uploaded image",use_column_width=True)
    st.sidebar.title("Filters")
    filter_type=st.sidebar.selectbox("Select a Filter",["Original","Grayscale","Sepia","Blur","Contrast"])
    if filter_type=="Grayscale":
        filter_image=image.convert("L")
    elif filter_type=="Sepia":
        filter_image=image.convert("RGB").point(lambda p : p*0.7)
    elif filter_type=="Blur":
        filter_image=image.filter(ImageFilter.GaussianBlur(5))
    elif filter_type=="Contrast":
        filter_image=ImageEnhance.Contrast(image).enhance(2)
    else:
        filter_image=image
    st.image(filter_image,caption=" filtered image " ,use_column_width=True)
    download_button=st.sidebar.button("Download it!")
    if download_button:
        buff=io.BytesIO()
        filter_image.save(buff,format="PNG")
        b_img=buff.getvalue()
        st.download_button(label="Download" ,data=b_img,file_name="filteredimage.png",mime="image/png")
