import streamlit as st
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# extract all csv
# automatiser le chargement du df
df = [
        "anscombe", "attention", "brain_networks", "car_crashes", "diamonds",
        "dots", "exercise", "flights", "fmri", "gammas", "geyser",
        "iris", "mpg", "penguins", "planets", "tips", "titanic", "taxis"
    ]

# title it "Manipulation de données et création de graphiques"
st.header("Manipulation de données et création de graphiques")
# display "Quel dataset veux-tu utiliser"
# create a selectbox with datasets
df_selected = st.selectbox("Quel dataset veux-tu utiliser",df)
url = f"https://raw.githubusercontent.com/mwaskom/seaborn-data/master/{df_selected}.csv"
# load the selected df
df = pd.read_csv(url)
st.dataframe(df)
# liste of columns from selected df
columns = df.columns.tolist()
# display "Choisissez la colonne X"
# create a selectbox with the columns
X = st.selectbox("Choisissez la colonne X",columns)
# display "Choisissez la colonne Y"
# create a selectbox with the columns
Y = st.selectbox("Choisissez la colonne Y",columns)
# display "Quel graphique veux-tu utiliser ?"
# create a selectbox with :
    # scatter_chart
    # bar_chart
    # line_chart
chart = st.selectbox("Quel graphique veux-tu utiliser ?",["scatter_chart", "bar_chart", "line_chart"])
if chart == "scatter_chart":
    st.scatter_chart(df[[X, Y]])
elif chart == "bar_chart":
    st.bar_chart(df[[X, Y]])
else :
    st.line_chart(df[[X, Y]])
# create a checkbox and display "Afficher la matrice de corrélation"
matrix= st.checkbox("Afficher la matrice de corrélation")
# if checkbox checked: 
# display subtitle "Ma matrice de corrélation" and the correlation matrix of selected columns 
if matrix :
    st.subheader("Ma matrice de corrélation")
    corr = df[[X, Y]].corr()
    fig, ax = plt.subplots()
    sns.heatmap(corr, annot=True, cmap="copper", ax=ax)
    st.pyplot(fig)