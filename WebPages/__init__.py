import base64

import streamlit as st
from src.resource import *


def badge_them_link(url, theme):
    """
    it is change the theme of badge based on user input
    """
    try:
        return url.replace("for-the-badge", theme)
    except KeyError or NameError:
        return url.replace("{}", theme)


def connect_with_me(social_media: dict, theme):
    """
    it created the social media section markdown
    """
    if len(social_media) != 0:
        output = """### Connect with me \n"""
        for badge in social_media:
            profile_link = social_media[badge]
            badge = badge_them_link(badges[badge], theme)
            output += f"[{badge}]({profile_link}) "

        return f"{output}\n"
    return ''


def tech_stack(skills: list, theme):
    """
    it created the tech stack section in markdown
    """
    if len(skills) != 0:
        output = """### Languages and tools \n"""
        for badge in skills:
            badge = badge_them_link(badges[badge], theme)
            output += f"{badge} "
        return output
    return ''


def add_ons(x: classmethod, trophy_count=True):
    """
    it creates a add-ons.
    in add-ons there are two sections.
    section (1): trophy,count badge
    section (2): GitHub stats
    it generated based on parameter trophy_count
    warning: the code maybe changed in future
    """
    github_username = x.github_username.lower()
    markdown = ''
    if trophy_count:
        if x.trophy:
            trophs = '<p align="left"> <img src="https://github-profile-trophy.vercel.app/?username={}" alt="{}" /> </p>'
            markdown += f"{trophs.replace('{}', github_username)} \n"
        if x.count_badge:
            count_badge = '<p align="left"> <img src="https://komarev.com/ghpvc/?username={}&label=Profile%20views&color=0e75b6&style=flat" alt="{}" /> </p>'
            markdown += f"{count_badge.replace('{}', github_username)}\n"
    else:
        if x.stats_card:
            stats = '<p>&nbsp;<img align="center" src="https://github-readme-stats.vercel.app/api?username={}&show_icons=true&locale=en" alt="{}" /></p>'
            markdown += stats.replace('{}', github_username)
        if x.top_skills:
            most_skills = '<p><img align="left" src="https://github-readme-stats.vercel.app/api/top-langs?username={}&show_icons=true&locale=en&layout=compact" alt="{}" /></p>'
            markdown += most_skills.replace('{}', github_username)
        if x.streak:
            streak = '<p><img align="right" src="https://github-readme-streak-stats.herokuapp.com/?user={}&" alt="{}" /></p>'
            markdown += streak.replace('{}', github_username)
    return markdown


def support(supports: dict, theme):
    """
    it created the support stack section markdown
    """
    if len(supports) != 0:
        output = """### Support: \n"""
        for badge in supports:
            profile_link = supports[badge]
            badge = badge_them_link(badges[badge], theme)
            output += f"[{badge}]({profile_link}) "
        return output
    return ''


def download_readme(code):
    """
    :param code:
    :return: it converts the plain markdown string to file and download
    """
    st.download_button(label="Download Readme", data=code, mime='text/markdown', file_name="README.md")
