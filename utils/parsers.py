from typing import List, Dict
from bs4 import BeautifulSoup
from models.site import SiteURL


def parse_iostip(text: str):
    soup = BeautifulSoup(text, features="html.parser")
    items = soup.find_all("div", class_="site-list-item")
    tip_list: List[dict] = []

    for item in items:
        a = item.find("a", class_="site-list-item-title")
        title = a.get_text()
        link = a.get("href")
        summary = item.find("a", class_="site-list-item-des").get_text()
        tip: Dict[str, str] = {"title": title, "summary": summary, "url": "https://awesome-tips.github.io/" + link}
        tip_list.append(tip)

    return tip_list


def meituan_page(page: int = 1):
    if page > 1:
        return '{}page/{}.html'.format(SiteURL.MEITUAN.value, page)
    else:
        return SiteURL.MEITUAN.value


def parse_meituan(text: str):
    soup = BeautifulSoup(text, features="html.parser")
    items = soup.find_all("div", class_="row post-container-wrapper")
    blog_list: List[dict] = []

    for item in items:
        posts = item.find_all("div", class_="post-container")
        for post in posts:
            title = post.find("h2").get_text()
            link = post.find("h2").find("a").get("href")
            summary = post.find("div", class_="post-content post-expect").get_text()
            tip: Dict[str, str] = {"title": title, "summary": summary, "url": link}
            blog_list.append(tip)

    return blog_list


def parse_swifttips(text: str):
    soup = BeautifulSoup(text, features="html.parser")
    items = soup.find_all("article", class_="tips")
    tip_list: List[dict] = []

    for item in items:
        article = item.find("h1")
        a = article.find("a")
        title = a.get_text()
        link = a.get("href")
        summary = item.find("div", class_="metadata").get_text()
        tip: Dict[str, str] = {"title": title, "summary": summary, "url": link}
        tip_list.append(tip)

    return tip_list
