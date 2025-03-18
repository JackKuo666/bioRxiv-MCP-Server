import requests
from bs4 import BeautifulSoup
from urllib.parse import quote
from typing import List, Dict, Any

def fetch_article_content(url: str) -> Dict[str, Any]:
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        print("Error fetching page, status code:", response.status_code)
        return None

    page_content = response.text
    soup = BeautifulSoup(page_content, 'html.parser')
    
    # 提取标题
    title_tag = soup.find("h1", class_="highwire-cite-title")
    title = title_tag.get_text(strip=True) if title_tag else "N/A"
    
    # 提取摘要
    abstract_section = soup.find("div", class_="section abstract")
    abstract = abstract_section.get_text(separator="\n", strip=True) if abstract_section else "N/A"
    
    # 提取作者信息
    authors_tag = soup.find("span", class_="highwire-cite-authors")
    if not authors_tag:
        authors_tag = soup.find("div", class_="highwire-cite-authors")
    authors = authors_tag.get_text(strip=True) if authors_tag else "N/A"
    
    
    return {
        "title": title,
        "abstract": abstract,
        "authors": authors,
        "url": url
    }



def search_medrxiv(query: str, num_results: int = 10) -> List[Dict[str, Any]]:
    # 构造搜索 URL
    base_url = "https://www.medrxiv.org/search/"
    search_str = f"{query} numresults:{num_results} sort:relevance"
    url = base_url + quote(search_str)

    headers = {
        "User-Agent": "Mozilla/5.0"
    }
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        print("Error fetching page, status code:", response.status_code)
        return []

    soup = BeautifulSoup(response.text, 'html.parser')
    results = []
    
    # 根据页面结构查找搜索结果项
    for li in soup.find_all("li", class_="search-result"):
        # 提取标题和链接
        title_tag = li.find("a", class_="highwire-cite-linked-title")
        title = title_tag.get_text(strip=True) if title_tag else "N/A"
        link = title_tag["href"] if title_tag and "href" in title_tag.attrs else None
        if link and not link.startswith("http"):
            link = "https://www.medrxiv.org" + link

        # 提取 DOI 信息
        doi_tag = li.find("span", class_="highwire-cite-metadata-doi highwire-cite-metadata")
        doi = doi_tag.get_text(strip=True) if doi_tag else "N/A"

        # 提取作者信息
        authors_tag = li.find("span", class_="highwire-citation-authors")
        authors = authors_tag.get_text(strip=True) if authors_tag else "N/A"

        article = fetch_article_content(link)
        abstract = article["abstract"]

        results.append({
            "title": title,
            "abstract": abstract,
            "link": link,
            "authors": authors,
            "doi": doi
        })
    return results

if __name__ == "__main__":
    query = "COVID-19"
    articles = search_medrxiv(query, num_results=10)
    for article in articles:
        print("Title:", article["title"])
        print("Link:", article["link"])
        print("Authors:", article["authors"])
        print("Abstract:", article["abstract"])
        print("DOI:", article["doi"])
        print("-" * 50)

# Export the main function
__all__ = ['search_medrxiv']
