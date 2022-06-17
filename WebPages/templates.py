from WebPages import *
import streamlit as st


def template_one(x):
    title = x.title
    subtitle = x.subtitle
    work = x.work
    theme = x.theme
    social_media = x.social_media
    skills = x.skills
    supports = x.supports
    # ---- all sections added to markdown ---- #
    markdown = """"""
    # ---- top section (1) ---- #
    markdown += f'<h1 align="center"> {title} </h1>'
    markdown += f'<h3 align="center">{subtitle}</h3>'
    markdown += f"{add_ons(x)}\n\n"
    markdown += f"{work}\n"
    # ---- middle section (2) ---- #
    SocialMedia = connect_with_me(social_media, theme)
    Skills = tech_stack(skills, theme)
    Supports = support(supports, theme)
    markdown += f"{SocialMedia}"
    markdown += f"{Skills}"
    # ---- bottom section (3) ---- #
    markdown += f"{add_ons(x, False)}\n\n"
    markdown += f"{Supports}"
    st.markdown(markdown, unsafe_allow_html=True)
    return markdown
