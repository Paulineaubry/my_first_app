Create apps with Streamlit

# my_first_app
From this dataset:
https://raw.githubusercontent.com/mwaskom/seaborn-data/master/taxis.csv

- title it “Bienvenue sur le site web de PAULINE”.
- display “Indiquez votre arrondissement de récupération”.
- create a selectbox with the boroughs
- display “Tu as choisi:” and the selected district
- display an image corresponding to the selected arrondissement

# manipulate graphics
From this link : https://github.com/mwaskom/seaborn-data

- extract all csv
- title it "Manipulation de données et création de graphiques"
- display "Quel dataset veux-tu utiliser"
- create a selectbox with datasets
- display "Choisissez la colonne X"
- create a selectbox with the columns
- display "Choisissez la colonne Y"
- create a selectbox with the columns
- display "Quel graphique veux-tu utiliser ?"
- create a selectbox with :
    - scatter_chart
    - bar_chart
    - line_chart
- create a checkbox and display "Afficher la matrice de corrélation"
- if checkbox checked: display the correlation matrix of selected columns

# Streamlit advanced
- Create a navigation menu
- Organize the display of an application
- Create a login page
- Put an application online

# app_st_adv
- The application must include an authentication page giving access to the home page and the photo album of the cat (or any other animal of your choice).
- The cat images are arranged so as to have 3 on the same line.
- Account data will come from a csv file read with pandas in the streamlit application. This csv file will contain the following columns:
    - name,
    - password,
    - email,
    - failed_login_attemps,
    - logged_in and role
- The menu should be placed in the sidebar. This bar will also include : Logout and a welcome message such as Welcome username.
- Finally, you'll need to deploy your application on the Streamlit cloud.




