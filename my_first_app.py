import streamlit as st
import pandas as pd

# lien du dataset à utiliser dans cette appli
url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/taxis.csv"
# Avec pandas lis le fichier csv du lien et affecte à df
df = pd.read_csv(url)

# créer une liste des arrondissements
arrondissements = df['pickup_borough'].unique().tolist()

# associe les photos à une variable
manhattan_photo = "https://res.cloudinary.com/dtljonz0f/image/upload/c_auto,ar_16:9,g_auto/f_auto/q_auto/v1/gc-v1/new-york/bedford-shutterstock_1715292730?_a=BAVAZGE70"
bronx_photo = "https://photo620x400.mnstatic.com/fdd552b53deea69a647a6ffcca9ed153/bronx-.jpg"
brooklyn_photo = "https://trvlr.fr/wp-content/uploads/2020/08/brooklyn-bridge-conseils-village-trvlr-voyage-que-voir-que-faire-7-jours.jpg"
queens_photo = "https://www.new-york-city-travel-tips.com/wordpress/wp-content/uploads/2015/04/Queens-BPVNY-NYCTT-MPVNY-23-600x400.jpg"
nan_photo = "https://us.123rf.com/450wm/janifest/janifest1607/janifest160700377/59949477-panneau-de-signalisation-de-new-york-city-one-way-avec-feu-de-circulation-pi%C3%A9tonne-dans-la-rue-sous-.jpg"

# Titre de mon site
st.header("Bienvenue sur le site web de PAULINE")

# selectbox
arrondissement_select = st.selectbox("Indiquez votre arrondissement de récupération",
                                          arrondissements) 

if arrondissement_select == "Brooklyn":
    st.write(f"Tu as choisi: {arrondissement_select}")
    st.image(brooklyn_photo,width=700)
elif arrondissement_select == "Bronx":
    st.write(f"Tu as choisi: {arrondissement_select}")
    st.image(bronx_photo,width=700)
elif arrondissement_select == "Queens":
    st.write(f"Tu as choisi: {arrondissement_select}")
    st.image(queens_photo,width=700)
elif arrondissement_select == "Manhattan":
    st.write(f"Tu as choisi: {arrondissement_select}")
    st.image(manhattan_photo,width=700)
else:
    st.write(f"Tu as choisi: {arrondissement_select}")
    st.image(nan_photo,width=700)

