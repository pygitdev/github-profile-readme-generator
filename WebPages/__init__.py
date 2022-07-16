import base64

import streamlit as st
from src.resource import *


def badge_them_link_generator(url, theme):
    """
    it is change the badge_theme of badge based on user input
    """
    try:
        return url.replace("for-the-badge", theme)
    except KeyError or NameError:
        return url.replace("{}", theme)


def connect_with_me_generator(social_media: dict, theme):
    """
    it created the social media section markdown
    """
    if len(social_media) != 0:
        output = """### Connect with me \n"""
        for badge in social_media:
            profile_link = social_media[badge]
            badge = badge_them_link_generator(badges[badge], theme)
            output += f"[{badge}]({profile_link}) \n"

        return f"{output}\n"
    return ''


def tech_stack_generator(skills: list, theme):
    """
    it created the tech stack section in markdown
    """
    if len(skills) != 0:
        output = """### Languages and tools \n"""
        for badge in skills:
            badge = badge_them_link_generator(badges[badge], theme)
            output += f"{badge} \n"
        return f"{output} \n"
    return ''


def add_ons_generator(x: classmethod, trophy_count=True):
    """
    it creates a add-ons.
    in add-ons there are two sections.
    section (1): trophy,count badge
    section (2): GitHub stats
    it generated based on parameter trophy_count
    warning: the code maybe changed in future
    """
    github_username = x.github_username.lower()
    github_theme = x.github_theme
    badge_theme = x.badge_theme
    markdown = ''
    if len(github_username) != 0:
        if trophy_count:
            if x.trophy:
                trophs = f'\n<p align="center"> <img src="https://github-profile-trophy.vercel.app/?username={github_username}&theme={github_theme}" alt="trophs"/> </p> \n'
                markdown += trophs
            if x.count_badge:
                count_badge = f'<p align="left"> <img src="https://komarev.com/ghpvc/?username={github_username}&label=Profile%20views&color=0e75b6&style={badge_theme}" alt="count badge" /> </p> \n'
                markdown += count_badge
            return markdown
        else:
            markdown += "### My Github Stats \n"
            html_markdown = ""
            if x.stats_card:
                stats = f'\n <img src="https://github-readme-stats.vercel.app/api?username={github_username}&theme={github_theme}&show_icons=true&locale=en" />\n'
                html_markdown += stats
            if x.top_skills:
                most_skills = f'<img src="https://github-readme-stats.vercel.app/api/top-langs?username={github_username}&theme={github_theme}&show_icons=true&locale=en&layout=compact"/> \n'
                html_markdown += most_skills
            if x.streak:
                streak = f'<img src="https://github-readme-streak-stats.herokuapp.com/?user={github_username}&theme={github_theme}" />\n'
                html_markdown += streak
            markdown += f"""<p align="center">{html_markdown}</p>"""
            return markdown
    return markdown


def support_generator(supports: dict, theme):
    """
    it created the support stack section markdown
    """
    if len(supports) != 0:
        output = """### Support: \n"""
        for badge in supports:
            profile_link = supports[badge]
            badge = badge_them_link_generator(badges[badge], theme)
            output += f"[{badge}]({profile_link}) \n"
        return f"{output} \n"
    return ''


def download_readme(code):
    """
    it converts the plain markdown string to file and download
    """
    btn = st.button("Generate README")
    if btn:
        st.download_button(label="Download Readme", data=code, mime='text/markdown', file_name="README.md")
        st.code(code, language="markdown")


def svg_banner_generator(type: str, text: str, width: int = 800, height: int = 400):
    text = text.replace(' ', '%20')
    banner = """<p align="center">\n<img src="https://svg-banners.vercel.app/api?type={}&text1={}&width={}&height={}" alt='svg banner' width=100%/> \n</p>\n""".format(
        type, text,
        width, height)
    return banner


def img_banner_generator(url: str, width: int = 800, height: int = 400):
    banner = """<p align="center">\n<img src="{}" alt='svg banner' width={} height={}/> \n</p>\n""".format(url, width,
                                                                                                           height)
    return banner


def readme_typo_banner(color: str, text: str, font: str, font_size: str, duration: str):
    color = color.replace("#","")
    banner = f"https://readme-typing-svg.herokuapp.com/?size={font_size}&font={font}&duration={duration}&color={color}&size=32&center=true&vCenter=true&width=800&height=50&lines={text}"
    markdown = f'<img src="{banner}" width="100%">'
    return markdown


def meme_quote_generator(x: classmethod):
    markdown = ""
    if x.quote:
        markdown += '### Random quote \n\n <img src="https://github-readme-quotes.herokuapp.com/quote?theme=dark"> \n\n'
    if x.meme:
        markdown += '### Random Meme \n\n<img src="https://random-memer.herokuapp.com/" width="100%"> \n'
    return markdown
