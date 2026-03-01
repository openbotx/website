import os

from modules import time

# general
root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
build_dir = os.path.join(root_dir, "build")
template_dir = os.path.join(root_dir, "templates")

title = "OpenBotX"
rtl = False
base_url = "https://openbotx.ai"

page_description = (
    "OpenBotX is an open-source platform for orchestrating AI agents"
    " — manage, coordinate, and monitor multiple intelligent agents"
    " with security, visibility, and control."
)
page_keywords = (
    "openbotx, ai agents, ai orchestration, open source, automation,"
    " multi-agent platform, artificial intelligence, agent management"
)
page_author = "Paulo Coutinho"
page_language = "en"

page_og_locale = "en_US"
page_og_type = "website"
page_og_site_name = title
page_og_image = f"{base_url}/assets/images/logo-og.png"
page_og_image_width = "1024"
page_og_image_height = "1024"

page_twitter_card = "summary_large_image"
page_twitter_site = "@openbotx"

page_apple_mobile_web_app_title = title
page_application_name = title

version_js_file = time.current_time()
version_css_file = time.current_time()
