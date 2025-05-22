import streamlit as st
from streamlit_option_menu import option_menu
from streamlit_authenticator import Authenticate

# Nos données utilisateurs doivent respecter ce format
lesDonneesDesComptes = {
    'usernames': {
        'chat': {
            'name': 'chat',
            'password': 'chat',
            'email': 'chat@gmail.com',
            'failed_login_attemps': 0,  # Sera géré automatiquement
            'logged_in': False,          # Sera géré automatiquement
            'role': 'utilisateur'
        },
        'root': {
            'name': 'root',
            'password': 'rootMDP',
            'email': 'admin@gmail.com',
            'failed_login_attemps': 0,  # Sera géré automatiquement
            'logged_in': False,          # Sera géré automatiquement
            'role': 'administrateur'
        }
    }
}

authenticator = Authenticate(
    lesDonneesDesComptes,  # Les données des comptes
    "cookie name",         # Le nom du cookie, un str quelconque
    "cookie key",          # La clé du cookie, un str quelconque
    30,                    # Le nombre de jours avant que le cookie expire
)

# Utiliser la méthode login pour afficher le formulaire de connexion et vérifier 
# les informations d'identification de l'utilisateur
authenticator.login()


if st.session_state["authentication_status"]:
    
    # sidebar
    with st.sidebar:
       
        # bouton de déconnexion
        authenticator.logout("Déconnexion")
        selection = option_menu(
        menu_title="Bienvenue chat",  # Titre du menu
        options=["Accueil", "Les photos de mon chat"],  # Options du menu
        default_index=0  # Option sélectionnée par défaut
    )
    

    if selection == "Accueil":
        st.title("Bienvenu sur ma page")
        st.image("https://i.etsystatic.com/46682565/c/2048/1627/0/159/il/8e5e9f/5501111670/il_680x540.5501111670_5kwg.jpg")
    else :
        st.title("Bienvenu dans l'album de mon chat")
        # Création de 3 colonnes 
        col1, col2, col3 = st.columns(3)

        # Contenu de la première colonne : 
        with col1:
            st.video("https://imgur.com/a/bRQ8zop")

        # Contenu de la deuxième colonne :
        with col2:
            st.image("https://imgur.com/a/2TtrqRM")

        # Contenu de la troisième colonne : 
        with col3:
            st.video("https://imgur.com/a/HHCQeeY")

        
elif st.session_state["authentication_status"] is False:
    st.error("L'username ou le password est/sont incorrect")
elif st.session_state["authentication_status"] is None:
    st.warning('Les champs username et mot de passe doivent être remplie')

