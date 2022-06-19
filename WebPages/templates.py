from WebPages import *
import streamlit as st


class Templates:
    def __init__(self, x):
        self.title = x.title
        self.subtitle = x.subtitle
        self.work = x.work
        self.badge_theme = x.badge_theme
        self.social_media = x.social_media
        self.skills = x.skills
        self.supports = x.supports
        self.banner_type = x.banner_type
        self.banner_height = x.banner_height
        self.banner_width = x.banner_width
        self.banner_theme = x.banner_theme
        self.image_banner = x.image_banner
        self.x = x

    def template_one(self):
        # ---- all sections added to markdown ---- #
        markdown = """"""
        # ---- top section (1) ---- #
        if self.banner_type == "Svg banner":
            markdown += svg_banner_generator(type=self.banner_theme,
                                             text=self.title,
                                             width=self.banner_width,
                                             height=self.banner_height)
        elif self.banner_type == "Image banner":
            markdown += img_banner_generator(self.image_banner)
        if self.banner_type in ["None", "Image banner"]:
            markdown += f'<h1 align="center"> {self.title} </h1>\n'
        markdown += f'<h3 align="center">{self.subtitle}</h3>'
        markdown += f"{add_ons_generator(self.x)}\n\n"
        markdown += f"{self.work}\n\n"
        # ---- middle section (2) ---- #
        SocialMedia = connect_with_me_generator(self.social_media, self.badge_theme)
        Skills = tech_stack_generator(self.skills, self.badge_theme)
        Supports = support_generator(self.supports, self.badge_theme)
        markdown += f"{SocialMedia}"
        markdown += f"{Skills}"
        # ---- bottom section (3) ---- #
        markdown += f"{add_ons_generator(self.x, False)}\n\n"
        markdown += f"{Supports}"
        st.markdown(markdown, unsafe_allow_html=True)
        return markdown


