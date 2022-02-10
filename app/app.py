import streamlit as st
from PIL import Image

from utils import get_data, build_graph, minEdgeBFS

st.set_page_config(page_title="T10 Challenge", layout='wide', page_icon="🥓")

st.header("🥓 The Oracle of Bacon")
st.subheader("Find out how many movies your favourite artist is from Kevin Bacon")

kevin_bacon_id = 102
bacon_img = Image.open('pics/Kevin_Bacon-removebg-preview.png')
st.image(bacon_img)

sampled_cast_movies_df, graph, movies_df, cast_df = get_data()
options = (
    cast_df[cast_df['id'].isin(sampled_cast_movies_df['person_id'].unique())]['name']
    .sort_values()
    .values
)
person_nodes, movie_edges = build_graph(sampled_cast_movies_df)

result_col_1, middle_col, result_col_2 = st.columns(3)

selected_name = st.selectbox('Choose yout artist', options)

selected_id = cast_df[cast_df['name'] == selected_name].values[0][0]

selected_id_graph_node = list(person_nodes.keys())[
    list(person_nodes.values()).index(selected_id)
]
kevin_bacon_id_graph_node = list(person_nodes.keys())[
    list(person_nodes.values()).index(kevin_bacon_id)
]

n = len(graph)
result = minEdgeBFS(graph, selected_id_graph_node, kevin_bacon_id_graph_node, n)

st.success(f"{selected_name} is {result} movies away from Kevin Bacon.")
