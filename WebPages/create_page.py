from WebPages import *
from src.resource import *
import streamlit as st


class CreatePage:
    title = ''
    subtitle = ''
    work = ''
    theme = ''
    social_media = {}
    skills = []
    supports = {}
    github_username = ''
    stats_card = False
    trophy = False
    count_badge = False
    top_skills = False
    streak = False

    def create_page(self):
        # ---- text inputs ---- #
        st.text("Title")
        self.title = st.text_input(label="", value=title_value)
        st.text("Subtitle")
        self.subtitle = st.text_input(label="", value=subtitle_value)
        st.text("Work")
        self.work = st.text_area(label="", value=work_area_value, height=300)

        # ---- badge Theme selection ---- #
        st.text("Theme:")
        badge_theme = st.selectbox("", ["For the badge", "Flat", "Flat Square", "Plastic"])
        self.theme = badge_theme.lower().replace(" ", "-")
        # ---- based on theme: badge preview ---- #
        st.image(badge_them_link(preview_badge_link, self.theme))

        # ---- social media selection ---- #
        st.text("social")
        social_media_input = st.multiselect("", options=social_media_list)
        self.social_media = {}
        for i in social_media_input:
            st.text(f"{i} profile link")
            self.social_media[i] = st.text_input(label=i)

        # ---- skills selection ---- #
        st.text("Skills")
        st.text("LANGUAGES")
        languages_input = st.multiselect("", options=languages_list)
        st.text("FRAMEWORKS, PLATFORMS & LIBRARIES")
        frameworks_input = st.multiselect("", options=frameworks_list)
        st.text("SERVERS")
        servers_input = st.multiselect("", options=servers_list)
        st.text("DATABASES")
        databases_input = st.multiselect("", options=databases_list)
        st.text("DESIGN")
        design_input = st.multiselect("", options=designs_list)
        st.text("ML/DL")
        ml_dl_input = st.multiselect("", options=ml_dl_list)
        st.text("OTHER")
        other_input = st.multiselect("", options=other_list)

        # ---- Add-ons selection ---- #
        st.text("Github User Name")
        self.github_username = st.text_input('')
        st.text("Add-ons")
        self.stats_card = st.checkbox(label="display github profile stats card")
        self.trophy = st.checkbox(label="display github trophy")
        self.streak = st.checkbox(label="display github streak stats")
        self.count_badge = st.checkbox(label="display visitors count badge")
        self.top_skills = st.checkbox(label="display top skills")

        # ---- Support selection ---- #
        support_inputs = st.multiselect("", options=support_list)
        for i in support_inputs:
            st.text(f"{i.replace('-', ' ').capitalize()} profile link")
            self.supports[i] = st.text_input(label=i)

        # ---- all list to one list ----- #
        self.skills = languages_input + frameworks_input + servers_input + databases_input + design_input + ml_dl_input + other_input
