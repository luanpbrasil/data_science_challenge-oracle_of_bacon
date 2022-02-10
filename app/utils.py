import streamlit as st
import pandas as pd
import queue

sampled_data_filepath = 'data/sampled_cast_and_movies_data.csv'
graph_filepath = 'data/graph.csv'
movies_filepath = 'data/movies_data.csv'
cast_filepath = 'data/cast_data.csv'


@st.cache(allow_output_mutation=True, suppress_st_warning=True)
def get_data(
    sampled_data_filepath=sampled_data_filepath,
    graph_filepath=graph_filepath,
    movies_filepath=movies_filepath,
    cast_filepath=cast_filepath,
):
    sampled_cast_movies_df = pd.read_csv(sampled_data_filepath)

    graph = pd.read_csv(graph_filepath, sep=',').drop('Unnamed: 0', axis=1)
    graph = [graph.iloc[i].dropna().astype(int).to_list() for i in graph.index]

    movies_df = pd.read_csv(movies_filepath)
    cast_df = pd.read_csv(cast_filepath)

    return sampled_cast_movies_df, graph, movies_df, cast_df


@st.cache(allow_output_mutation=True, suppress_st_warning=True)
def build_graph(sampled_cast_movies_df):
    person_nodes = {}
    for i, value in enumerate(
        sampled_cast_movies_df['person_id'].sort_values().unique()
    ):
        person_nodes[i] = value

    movie_edges = {}
    for i, value in enumerate(
        sampled_cast_movies_df['movie_id'].sort_values().unique()
    ):
        movie_edges[i] = value

    return person_nodes, movie_edges


def minEdgeBFS(edges, u, v, n):

    # visited[n] for keeping track
    # of visited node in BFS
    visited = [0] * n

    # Initialize distances as 0
    distance = [0] * n

    # queue to do BFS.
    Q = queue.Queue()
    distance[u] = 0

    Q.put(u)
    visited[u] = True
    while not Q.empty():
        x = Q.get()

        for i in range(len(edges[x])):
            if visited[edges[x][i]]:
                continue

            # update distance for i
            distance[edges[x][i]] = distance[x] + 1
            Q.put(edges[x][i])
            visited[edges[x][i]] = 1
    return distance[v]
