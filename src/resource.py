import json

try:
    # ---- for website ---- #
    badges = open("src/badges.json", "r+")
except FileNotFoundError:
    # ---- for local run/test ---- #
    badges = open("badges.json", "r+")
badges = json.load(badges)
# ------- badges list ------- #
# ---- languages label ---- #
languages_list = ('apache-groovy', 'c', 'c#', 'c++', 'crystal', 'css3', 'clojure', 'dart', 'elixir', 'elm', 'erlang',
                  'fortran', 'go', 'graph-ql', 'haskell', 'html', 'java', 'javascript', 'julia', 'kotlin', 'latex',
                  'lua',
                  'markdown', 'nim', 'octave', 'php', 'perl', 'python', 'r', 'ruby', 'rust', 'scala', 'shell-script',
                  'solidity', 'swift', 'typescript', 'zig')
# ---- social media label ---- #
social_media_list = ('behance', 'codesandbox', 'codepen', 'codechef', 'codeforces', 'dev.to', 'discord', 'dribbble',
                     'facebook', 'gfg', 'hashnode', 'hackerrank', 'hackerearth', 'instagram', 'kaggel', 'leetcode',
                     'linkedin', 'medium', 'pinterest', 'quora', 'rss', 'reddit', 'stack-overflow', 'twitter',
                     'twitch', 'youtube')
# ---- hosting label ---- #
hosting_list = (
    'alibaba-cloud', 'aws', 'azure', 'cloudflare', 'codeberg', 'datadog', 'digitalocean', 'firebase', 'glitch',
    'google-cloud', 'heroku', 'netlify', 'oracle', 'openstack', 'ovh', 'scaleway', 'vercel')
# ---- frameworks label ---- #
frameworks_list = ('.net', 'adonisjs', 'anaconda', 'angular', 'angular.js', 'ant-Design', 'apache-kafka',
                   'apollo-graphql', 'aurelia', 'blazor', 'bootstrap', 'buefy', 'chakra', 'django', 'django-rest',
                   'electron.js', 'ember', 'expo', 'express.js', 'fastapi', 'fastify', 'flask', 'flutter', 'gatsby',
                   'green-sock', 'gulp', 'insomnia', 'jasmine', 'jquery', 'jwt', 'laravel', 'less', 'mui', 'meteorjs',
                   'npm', 'nestjs', 'nextjs', 'nodejs', 'nuxt', 'nx', 'opencv', 'opengl', 'p5js', 'pug', 'qt', 'quasar',
                   'ros', 'rabbitmq', 'rails', 'react', 'react-native', 'react-query', 'react-router', 'redux', 'rxdb',
                   'rxjs', 'saas', 'semantic-ui-react', 'socket.io', 'solidjs', 'spring', 'strapi', 'styled-components',
                   'stylus', 'svelte', 'symfony', 'tailwindcss', 'three.js', 'thymeleaf', 'typegraphql', 'vue.js',
                   'vuetify', 'webpack', 'windicss', 'xamarin', 'yarn')
# ---- servers label ---- #
servers_list = (
    'apache', 'apache-airflow', 'apache-ant', 'apache-flink', 'apache-maven', 'apache-tomcat', 'gunicorn', 'jenkins',
    'nginx')
# ---- designs label ---- #
designs_list = (
    'adobe', 'adobe-acrobat-reader', 'adobe-after-effects', 'adobe-audition', 'adobe-creative-cloud',
    'adobe-dreamweaver',
    'adobe-fonts', 'adobe-illustrator', 'adobe-indesign', 'adobe-lightroom', 'adobe-lightroom-classic',
    'adobe-photoshop',
    'Adobe-premiere-pro', 'adobe-xd', 'aseprite', 'affinity-designer', 'affinity-photo', 'blender', 'canva', 'dribbble',
    'figma', 'framer', 'gimp', 'inkscape', 'invision', 'krita', 'proto.io', 'sketch', 'storybook')
# ---- databases label ---- #
databases_list = (
    'amazon-dynamodb', 'cassandra', 'cockroach-labs', 'couchbase', 'firebase', 'influxdb', 'mariadb', 'musicbrainz',
    'microsoft-sql-server', 'mongodb', 'mysql', 'neo4j', 'postgres', 'realm', 'redis', 'singlestore', 'sqlite',
    'supabase')
# ---- ML/DL label ---- #
ml_dl_list = ('keras', 'numpy', 'pandas', 'plotly', 'pytorch', 'scikit-learn', 'scipy', 'tensorflow')
# ---- other label ---- #
other_list = (
    'alfred', 'ansible', 'aqua', 'arduino', 'babel', 'cmake', 'codecov', 'confluence', 'docker', 'eslint',
    'elasticsearch',
    'gradle', 'jira', 'kubernetes', 'notion', 'portfolio', 'postman', 'prezi', 'rancher', 'raspberrypi', 'swagger',
    'terraform', 'trello', 'vagrant')
# ---- support label ---- #
support_list = ('buy-me-a-coffee', 'patreon')
# ------- text values------- #
title_value = "Hi 👋, I'm "
subtitle_value = "A passionate data scientist from India."
preview_badge_link = "https://img.shields.io/badge/Instagram-%23E4405F.svg?style=for-the-badge&logo=Instagram&logoColor=white"
# ---------- work text values ---------- #
work_area_value = "- 🔭 I’m currently working on [project-name](https://github.com/) \n" \
                  "- 👯 I’m looking to collaborate on [project-name](https://github.com/) \n" \
                  "- 🤝 I’m looking for help with [project-name](https://github.com/) \n" \
                  "- 🌱 I’m currently learning  \n" \
                  "- 💬 Ask me about \n" \
                  "- 👨‍💻 All of my projects are available at [here](https://github.com/) \n" \
                  "- 📝 I regularly write articles on  [here](https://dev.to/) \n" \
                  "- 📫 How to reach me  **@gmail.com** \n" \
                  "- ⚡ Fun fact "
# ---- themes ---- #
github_stats_theme = ["default","solarized-light","dark", "radical", "merko", "gruvbox", "tokyonight", "onedark", "cobalt", "synthwave", "highcontrast", "dracula"]
badge_theme_list = ["For the badge", "Flat", "Flat Square", "Plastic"]
svg_banner_type = ["None", "Readme typing", "Svg banner", "Image banner"]
svg_banner_theme = ["origin",'textBox','glitch','luminance','typeWriter','rainbow']
