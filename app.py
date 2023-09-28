import streamlit as st
import pickle
import pandas as pd
from workout import fetch_poster

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    film_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x:x[1])[1:6]
    #print("Film List: ",film_list)
    recommended = []
    recommended_posters = []
    for i in film_list:
        movie_id = i[0]
        #print("movie_id: ",movie_id,"movie_title: ",movies.iloc[i[0]].title)
        recommended.append(movies.iloc[i[0]].title)
        recommended_posters.append(fetch_poster(movies.iloc[i[0]].mov_ser_id))
    return recommended, recommended_posters

#api key
movies_list = pickle.load(open('movies_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_list)

similarity = pickle.load(open('similarity.pkl', 'rb'))


st.title(":red[Arun] Arunisto :male-technologist:")
st.title("Movie Recommendation System :clapper:")

selected_movie_name = st.selectbox(
   label='',
   options=movies['title'].values,
    index=None,
   placeholder="Select or type movie to find similar recommendation",
)

if st.button('Search Movies'):
    names, posters = recommend(selected_movie_name)
    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.text(names[0])
        st.image(posters[0])

    with col2:
        st.text(names[1])
        st.image(posters[1])

    with col3:
        st.text(names[2])
        st.image(posters[2])

    with col4:
        st.text(names[3])
        st.image(posters[3])

    with col5:
        st.text(names[4])
        st.image(posters[4])
else:
    st.title("Over Kaggle's Dataset of :red[20,000] data")
