import streamlit as st

################ #################### ################ 
################ ### DATA IMPORT #### ################ 
################ #################### ################ 
from imbd import Imbd
from tmbd import Tmbd

imbd = Imbd()
tmbd = Tmbd()

################ #################### ################ 
################ ### PAGE CONFIG #### ################ 
################ #################### ################ 
st.set_page_config(
    page_title="Film ANalysis",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "# This is a header. This is an *extremely* cool app!"
    }
)


################ #################### ################ 
################ #####  SIDEBAR ##### ################ 
################ #################### ################ 

with st.sidebar:
    st.header('Streamlit App by [Rafaella Duarte](https://www.linkedin.com/in/rafaella-duarte-carvalho/)')
    st.subheader('Sobre as bases de dados utilizadas:')
    st.markdown('<div style="text-align: justify;"> <ul><li><b>IMDb:</b> conhecida como Internet Movie Database, é uma base de dados online de informação sobre cinema TV, música e games, hoje pertencente à Amazon.Nesta base há cerca de 100836 registros referente as votações dos filmes e 9742 registros na base referentes aos filmes.<li><b>TMDb:</b> conhecida como The Movie Database, é uma base de dados grátis e de código aberto,sobre filmes e seriados, criado por Travis Bell em 2008. Atualizado constantemente através do apoio da comunidade. Inicialmente, era apenas uma base de dados sobre filmes, mas em 2013 foi adicionada a seção de séries. Nesta base há cerca de 4803 registros referentes aos filmes e votações.</ul></div>',unsafe_allow_html=True)


################ #################### ################ 
################ ### INTRODUCTION ### ################ 
################ #################### ################ 

row0_spacer1, row0_1, row0_spacer2 = st.columns((.1, 2.3, .1))
with row0_1:
    st.title('Análise Exploratória - Classificação de Filmes')
row1_spacer1, row1_1, row1_spacer2 = st.columns((.1, 2.3, .1))
with row1_1:
    st.markdown('<div style="text-align: justify;">Prazer, meu nome é Rafaella Duarte sou graduanda em Ciências Econômicas, entusiasta em Big Data e apaixonada por processamento e infraestrutura de dados. Dessa forma, a fim de estudar a linguagem de programação python e suas principais bibliotecas utilizadas para analise de dados. Desenvolvi este projeto de análise exploratória utilizando duas base de dados sobre filmes.</div>',unsafe_allow_html=True)
    st.markdown('<div style="text-align: justify;">Você pode encontrar o código-fonte no <a href="https://github.com/rafaelladuarte/film_rating_exploratory_analysis"> Film Rating Exploratory Analysis GitHub Repository</a></div>',unsafe_allow_html=True)


################ ################ ################ 
################ ### ANALYSIS ### ################ 
################ ################ ################ 

################ IMBD
row4_spacer1, row4_1, row4_spacer2 = st.columns((.2, 7.1, .2))
with row4_1:
    st.subheader('IMBd')
row5_spacer1, row5_1, row5_spacer2, row5_2, row5_spacer3  = st.columns((.2, 2.3, .4, 4.4, .2))
with row5_1:
    st.markdown('<div style="text-align: justify;">Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum</div>',unsafe_allow_html=True)
    plot_movie_imbd = st.selectbox("Selecione", ('Genre IMBd','Decada IMBd')) 
with row5_2:
    if plot_movie_imbd == 'Genre IMBd':
        imbd.plot_movie_genre_imbd()
    elif plot_movie_imbd == 'Decada IMBd':
        imbd.plot_movie_genre_imbd()

################ TMBD

row6_spacer1, row6_1, row6_spacer2 = st.columns((.2, 7.1, .2))
with row6_1:
    st.subheader('TMBd')
row7_spacer1, row7_1, row7_spacer2, row7_2, row7_spacer3  = st.columns((.2, 2.3, .4, 4.4, .2))
with row7_1:
    st.markdown('<div style="text-align: justify;">Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum</div>',unsafe_allow_html=True)   
    plot_movie_tmbd = st.selectbox("Selecione", ('Genre TMBd','Decada TMBd')) 
with row7_2:
    if plot_movie_tmbd == 'Genre TMBd':
        tmbd.plot_movie_genre_tmbd()
    elif plot_movie_tmbd == 'Decada TMBd':
        tmbd.plot_movie_genre_tmbd()

