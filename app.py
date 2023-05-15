import streamlit as st
import os
from streamlit_option_menu import option_menu
from pathlib import Path
import streamlit_authenticator as stauth
import yaml
from yaml.loader import SafeLoader
import pandas as pd

# https://github.com/jvcss/PyInstallerStreamlit


def main():
    with open(Path(__file__).parent /'header1.png', 'rb') as file:
        image_data = file.read()
    st.image(image_data)

    selected_language = "Russian"
    if selected_language == 'English':
        selected_language = st.sidebar.selectbox("Select Language", ["Russian", "English"])
    elif selected_language == 'Russian':
        selected_language = st.sidebar.selectbox("Выберите язык", ["Russian", "English"])

    # Display language-specific content
    if selected_language == 'English':
        st.write("Hello! Welcome to the Droughtmap data download app.")
            # Year range
        start_year = 2011
        end_year = 2022

        # Year selection
        selected_year = st.slider("Select Year", start_year, end_year)

        # Display the selected year
        st.write("Selected Year:", selected_year)


        # --- UI ---         
        # 2. horizontal menu w/o custom style
        selected = option_menu(
            menu_title=None,  # required
            options=["Bulletin",  "Data"],  # required
            icons=["bi bi-file-earmark-pdf", "bi bi-cloud-download"],  # optional
            menu_icon="cast",  # optional
            default_index=0,  # optional
            orientation="horizontal",
        )
    
    
    ############################################################################################################################################################################################################################################################################################################################################################

        # Specify the file path
        csv_file = Path(__file__).parent / 'rayon.csv'

        # Read the CSV file into a DataFrame
        all_admi = pd.read_csv(csv_file, encoding='utf-8')

        # Display the DataFrame
        print(all_admi)

        rayons = all_admi["rayon_en"].tolist()
        print(rayons)

############################################################################################################################################################################################################################################################################################################################################################
        if selected == "Bulletin":
            st.title(selected + " Download")
            countries = set(["Select a Country"]+all_admi["country_id"].tolist())
            countries.remove("Select a Country")
            countries = ["Select a Country"] + sorted(countries)
            Country = st.sidebar.selectbox("Select Country", countries)
            if Country != "Select a Country":
                oblasts = set(["Select an Oblast"]+all_admi[all_admi["country_id"] == Country]["oblast_en"].tolist())
                oblasts.remove("Select an Oblast")
                oblasts = ["Select an Oblast"] + sorted(oblasts)
                Oblast = st.sidebar.selectbox("Select Oblast", oblasts)
                if Oblast != "Select an Oblast":
                    rayons = set(["Select a Rayon"]+all_admi[(all_admi["country_id"] == Country) & (all_admi["oblast_en"] == Oblast)]["rayon_en"].tolist())
                    rayons.remove("Select a Rayon")
                    rayons = ["Select a Rayon"] + sorted(rayons)
                    Rayon = st.sidebar.selectbox("Select Rayon", rayons)
                    if Rayon == "Select a Rayon":
                        st.sidebar.button('Download Bulletin in Oblast ' +str(selected_year))
                    else:
                        st.sidebar.button('Download Bulletin in Rayon ' +str(selected_year))

            if Country != "Select a Country" and Oblast == "Select an Oblast":
                st.sidebar.button('Download Bulletin in Country ' +str(selected_year))
        
        ##############################################################################################################################################################################
        ##############################################################################################################################################################################
        if selected == "Data":
            st.title(selected + " Download")
            countries = set(["Select a Country"]+all_admi["country_id"].tolist())
            countries.remove("Select a Country")
            countries = ["Select a Country"] + sorted(countries)
            Country = st.sidebar.selectbox("Select Country", countries)
            if Country != "Select a Country":
                oblasts = set(["Select an Oblast"]+all_admi[all_admi["country_id"] == Country]["oblast_en"].tolist())
                oblasts.remove("Select an Oblast")
                oblasts = ["Select an Oblast"] + sorted(oblasts)
                Oblast = st.sidebar.selectbox("Select Oblast", oblasts)
                if Oblast != "Select an Oblast":
                    rayons = set(["Select a Rayon"]+all_admi[(all_admi["country_id"] == Country) & (all_admi["oblast_en"] == Oblast)]["rayon_en"].tolist())
                    rayons.remove("Select a Rayon")
                    rayons = ["Select a Rayon"] + sorted(rayons)
                    Rayon = st.sidebar.selectbox("Select Rayon", rayons)
                    if Rayon == "Select a Rayon":
                        st.sidebar.button('Download Data in Oblast'+str(selected_year))
                    else:
                        st.sidebar.button('Download Data in Rayon '+str(selected_year))

            if Country != "Select a Country" and Oblast == "Select an Oblast":
                st.sidebar.button('Download Data in Country '+ str(selected_year))

    # Add English-specific content or functionality
    elif selected_language == 'Russian':
        st.write("Здравствуйте! Добро пожаловать в приложение для загрузки данных карты засухи.")


        # Year range
        start_year = 2011
        end_year = 2022

        # Year selection
        selected_year = st.slider("Выберите год", start_year, end_year)

        # Display the selected year
        st.write("Выбранный год:", selected_year)


        # --- UI ---         
        # 2. horizontal menu w/o custom style
        selected = option_menu(
            menu_title=None,  # required
            options=["Бюллетень",  "Данные"],  # required
            icons=["bi bi-file-earmark-pdf", "bi bi-cloud-download"],  # optional
            menu_icon="cast",  # optional
            default_index=0,  # optional
            orientation="horizontal",
        )
    
    ############################################################################################################################################################################################################################################################################################################################################################

        # Specify the file path
        csv_file = Path(__file__).parent / 'rayon.csv'

        # Read the CSV file into a DataFrame
        all_admi = pd.read_csv(csv_file, encoding='utf-8')

        # Display the DataFrame
        print(all_admi)

        rayons = all_admi["rayon_ru"].tolist()
        print(rayons)

############################################################################################################################################################################################################################################################################################################################################################
        if selected == "Бюллетень":
            st.title(selected + " Скачать")
            countries = set(["Выберите страну"]+all_admi["country_id"].tolist())
            countries.remove("Выберите страну")
            countries = ["Выберите страну"] + sorted(countries)
            Country = st.sidebar.selectbox("Выберите страну", countries)
            if Country != "Выберите страну":
                oblasts = set(["Выберите область"]+all_admi[all_admi["country_id"] == Country]["oblast_ru"].tolist())
                oblasts.remove("Выберите область")
                oblasts = ["Выберите область"] + sorted(oblasts)
                Oblast = st.sidebar.selectbox("Выберите область", oblasts)
                if Oblast != "Выберите область":
                    rayons = set(["Выберите район"]+all_admi[(all_admi["country_id"] == Country) & (all_admi["oblast_ru"] == Oblast)]["rayon_ru"].tolist())
                    rayons.remove("Выберите район")
                    rayons = ["Выберите район"] + sorted(rayons)
                    Rayon = st.sidebar.selectbox("Выберите район", rayons)
                    if Rayon == "Выберите район":
                        st.sidebar.button('Скачать бюллетень в области ' +str(selected_year))
                    else:
                        st.sidebar.button('Скачать бюллетень по району ' +str(selected_year))

            if Country != "Выберите страну" and Oblast == "Выберите область":
                st.sidebar.button('Скачать бюллетень в стране ' +str(selected_year))
        
        ##############################################################################################################################################################################
        ##############################################################################################################################################################################
        if selected == "Данные":
            st.title(selected + " Скачать")
            countries = set(["Выберите страну"]+all_admi["country_id"].tolist())
            countries.remove("Выберите страну")
            countries = ["Выберите страну"] + sorted(countries)
            Country = st.sidebar.selectbox("Выберите страну", countries)
            if Country != "Выберите страну":
                oblasts = set(["Выберите область"]+all_admi[all_admi["country_id"] == Country]["oblast_ru"].tolist())
                oblasts.remove("Выберите область")
                oblasts = ["Выберите область"] + sorted(oblasts)
                Oblast = st.sidebar.selectbox("Выберите область", oblasts)
                if Oblast != "Выберите область":
                    rayons = set(["Выберите район"]+all_admi[(all_admi["country_id"] == Country) & (all_admi["oblast_ru"] == Oblast)]["rayon_ru"].tolist())
                    rayons.remove("Выберите район")
                    rayons = ["Выберите район"] + sorted(rayons)
                    Rayon = st.sidebar.selectbox("Выберите район", rayons)
                    if Rayon == "Выберите район":
                        st.sidebar.button('Скачать данные по области'+str(selected_year))
                    else:
                        st.sidebar.button('Скачать данные по району '+str(selected_year))

            if Country != "Выберите страну" and Oblast == "Выберите область":
                st.sidebar.button('Загрузить данные в стране '+ str(selected_year))

                
if __name__ == "__main__":
    main()




