import numpy as np
import pandas as pd
import seaborn as sns
import streamlit as st
import matplotlib.pyplot as plt

class Imbd():
    def __init__(self):
        path_imbd = "imbd_dataset_dashboard.csv"
        self.df_imbd = pd.read_csv(path_imbd)

    def plot_movie_genre_imbd(self):
        rc = {'figure.figsize':(8,4.5),
          'axes.labelcolor': 'white',
          'text.color': '#0e1117',
          'font.size' : 10,
          'axes.labelsize': 12,
          'ytick.labelsize': 12}
        plt.rcParams.update(rc)
        df_imbd_genre = self.df_imbd["main_genre"].value_counts().to_frame().reset_index()
        df_imbd_genre.rename(columns = {"index":"main_genre","main_genre":"count"}, inplace = True)
        df_imbd_genre = df_imbd_genre[:10]
        fig, ax = plt.subplots()
        ax = sns.barplot(
            x=df_imbd_genre["main_genre"], 
            y=df_imbd_genre["count"], 
            data=df_imbd_genre,
            color="salmon",
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

    def plot_movie_decade_imbd(self):
        pass

    def plot_movie_rating_imbd(self):
        pass
