import streamlit as st
import pickle
import pandas as pd

# Load saved files
df = pickle.load(open('df.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))


# Recommendation function
def recommend(song):
    song = song.lower().strip()

    matches = df[df['song'].str.lower().str.strip() == song]

    if matches.empty:
        return []

    idx = matches.index[0]

    distances = sorted(
        list(enumerate(similarity[idx])),
        reverse=True,
        key=lambda x: x[1]
    )

    recommended_songs = []

    for i in distances[1:6]:
        recommended_songs.append(df.iloc[i[0]].song)

    return recommended_songs


# Streamlit UI
st.title("🎵 Song Recommendation System")

selected_song = st.selectbox(
    "Choose a song",
    df['song'].values
)

if st.button("Recommend"):
    recommendations = recommend(selected_song)

    if recommendations:
        st.write("### Recommended Songs:")
        for song in recommendations:
            st.write(song)
    else:
        st.write("Song not found.")