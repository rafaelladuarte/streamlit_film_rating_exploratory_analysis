import numpy as np
import pandas as pd
import seaborn as sns
import streamlit as st
import matplotlib.pyplot as plt

class Tmbd():
    def __init__(self):
        path_tmbd = "tmbd_dataset_dashboard.csv"
        self.df_tmbd = pd.read_csv(path_tmbd)

    def plot_movie_genre_tmbd(self):
        rc = {'figure.figsize':(8,4.5),
          'axes.labelcolor': 'white',
          'text.color': '#0e1117',
          'font.size' : 10,
          'axes.labelsize': 12,
          'ytick.labelsize': 12}
        plt.rcParams.update(rc)
        df_tmbd_genre = self.df_tmbd["main_genre"].value_counts().to_frame().reset_index()
        df_tmbd_genre.rename(columns={"index":"main_genre","main_genre":"count"},inplace=True)
        df_tmbd_genre = df_tmbd_genre[:10]
        fig, ax = plt.subplots()
        ax = sns.barplot(
            x=df_tmbd_genre["main_genre"], 
            y=df_tmbd_genre["count"], 
            data=df_tmbd_genre,
            color="seagreen",
        )
        plt.xticks(rotation=45)
        ax.get_yaxis().set_visible(False)
        for retangulo in ax.patches:
            ax.text(retangulo.get_x() + retangulo.get_width() / 2,
                    retangulo.get_height() + 22,
                    '{:,}'.format(
                        int(retangulo.get_height())).replace(',','.'),
                        ha = 'center',
                        fontsize='medium'
                    )
        st.pyplot(fig)
        
    def plot_movie_decade_tmbd(self):
        rc = {'figure.figsize':(8,4.5),
          'axes.labelcolor': 'white',
          'text.color': '#0e1117',
          'font.size' : 10,
          'axes.labelsize': 12,
          'ytick.labelsize': 12}
        plt.rcParams.update(rc)
        year = self.df_tmbd["year"].dropna()
        decada = year.str.split(pat="",expand = True)
        decada["decada"] = decada[1] + decada[2] + decada[3] + '0'
        df_tmbd_year = pd.merge(year, decada["decada"], right_index= True, left_index= True)
        df_tmbd_year = df_tmbd_year.astype(str).astype(int)
        df_tmbd_year = df_tmbd_year[df_tmbd_year["year"] > 1970]
        df_tmbd_year = df_tmbd_year[df_tmbd_year["year"] < 2018]
        df_tmbd_year["year"].value_counts().to_frame().reset_index()
        df_tmbd_decada = df_tmbd_year["decada"].value_counts().to_frame().reset_index()
        df_tmbd_decada = df_tmbd_decada.rename(columns={"index":"decada","decada":"count"})
        fig, ax = plt.subplots()
        ax = sns.barplot(
            x=df_tmbd_decada["decada"], 
            y=df_tmbd_decada["count"], 
            data=df_tmbd_decada,
            color="seagreen"
        )
        st.pyplot(fig)

    def plot_movie_company_tmbd(self):
        pass

    def plot_movie_country_tmbd(self):
        pass

    def plot_movie_status_tmbd(self):
        pass