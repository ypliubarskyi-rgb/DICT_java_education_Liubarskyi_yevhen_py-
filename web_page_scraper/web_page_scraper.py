import requests
from bs4 import BeautifulSoup
import string
import os

def sanitize_filename(title: str) -> str:
    translator = str.maketrans("", "", string.punctuation)
    clean = title.strip().translate(translator)
    clean = clean.replace(" ", "_")
    return "_".join(clean.split())

url = input("Input the URL:\n> ").strip()


if "api.quotable.io" in url:
    try:
        response = requests.get(url)
        if response.status_code != 200:
            print("Invalid quote resource!")
        else:
            data = response.json()
            if "content" not in data or not data["content"]:
                print("Invalid quote resource!")
            else:
                print(data["content"])
    except Exception:
        print("Invalid quote resource!")


elif "imdb.com" in url:
    if "imdb.com/title" not in url:
        print("Invalid movie page!")
    else:
        headers = {"Accept-Language": "en-US,en;q=0.5"}
        response = requests.get(url, headers=headers)

        if response.status_code != 200:
            print("Invalid movie page!")
        else:
            soup = BeautifulSoup(response.text, "html.parser")
            title_tag = soup.find("title")
            desc_tag = soup.find("meta", {"name": "description"})

            if not title_tag or not desc_tag or not desc_tag.get("content"):
                print("Invalid movie page!")
            else:
                title = title_tag.text.strip().split(" - IMDb")[0].strip()
                if "⭐" in title:
                    title = title.split("⭐")[0].strip()
                description = desc_tag["content"].strip()
                print({"title": title, "description": description})


elif "nature.com" in url:
    num_pages = int(input("> ").strip())
    article_type_filter = input("> ").strip()

    headers = {"Accept-Language": "en-US,en;q=0.5"}
    BASE_URL = "https://www.nature.com/nature/articles?sort=PubDate&year=2022&page="

    for page_num in range(1, num_pages + 1):
        response = requests.get(BASE_URL + str(page_num), headers=headers)
        if response.status_code != 200:
            print(f"Page {page_num}: returned {response.status_code}!")
            continue

        soup = BeautifulSoup(response.content, "html.parser")
        dir_name = f"Page_{page_num}"
        os.makedirs(dir_name, exist_ok=True)

        for article in soup.find_all("article"):
            type_tag = article.find("span", {"data-test": "article.type"})
            if not type_tag or type_tag.text.strip() != article_type_filter:
                continue

            link_tag = article.find("a", {"data-track-action": "view article"})
            if not link_tag:
                continue

            article_url = "https://www.nature.com" + link_tag["href"]
            art_response = requests.get(article_url, headers=headers)
            if art_response.status_code != 200:
                continue

            art_soup = BeautifulSoup(art_response.content, "html.parser")
            title_tag = art_soup.find("h1")
            if not title_tag:
                continue

            body_div = art_soup.find("div", {"class": lambda c: c and "body" in c})
            if body_div:
                body_text = body_div.get_text(separator="\n").strip()
            else:
                body_text = "\n".join(p.get_text() for p in art_soup.find_all("p")).strip()

            if not body_text:
                continue

            filename = sanitize_filename(title_tag.text.strip()) + ".txt"
            filepath = os.path.join(dir_name, filename)
            with open(filepath, "wb") as f:
                f.write(body_text.encode("utf-8"))

    print("Saved all articles.")


else:
    response = requests.get(url)
    if response.status_code != 200:
        print(f"The URL returned {response.status_code}!")
    else:
        with open("source.html", "wb") as f:
            f.write(response.content)
        print("Content saved.")