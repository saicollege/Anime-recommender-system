import streamlit as st
import pickle
import pandas as pd

def recommend(partial):
    l = []
    st.write("Search results:")
    found = False
    for index,row in anime.iterrows():
        if partial.lower() in row['name'].lower():
            st.write(row['name'],row['rating'])
            found = True

    if not found:
        st.write("No matching anime found.")

anime_list = pickle.load(open('anime_dict.pkl','rb'))
anime = pd.DataFrame(anime_list)
st.sidebar.markdown(
    "ARS"
)
st.markdown(
        f"""
            <style>
                [data-testid="stSidebar"] {{
                    background-image: url(https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS0C_QmY1GNqC6fvuEVt2PFZV8u7QST8hauGIpUYYljQ4SvMzpALj9rIcw&usqp=CAU);
                    background-repeat: no-repeat;
                    padding-top: 10px;
                    position: center;
                    background-position: 5px 5px;
                }}
            </style>
            """,
        unsafe_allow_html=True,
    )
st.markdown("# Home")
st.title("Anime Recommendation System")

selected_anime = st.selectbox(
    'Get your animes here !',
    anime['name'].values
)

if st.button('Recommend'):
    recommend(selected_anime)
images = ['img.png','img_7.png','img_1.png','img_7.png','img_2.png']
st.image(images)
images1 = ['img_3.png','img_7.png','img_4.png','img_7.png','img_5.png']
st.image(images1)
images2 = ['img_6.png','img_7.png','img_8.png','img_7.png','img_9.png']
st.image(images2)

