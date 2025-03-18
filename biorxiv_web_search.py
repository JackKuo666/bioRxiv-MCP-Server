import requests
from bs4 import BeautifulSoup
from urllib.parse import quote

def generate_biorxiv_search_url(term=None, title=None, author1=None, author2=None, abstract_title=None, 
                                text_abstract_title=None, journal_code="biorxiv", section=None,
                                start_date=None, end_date=None, num_results=10, sort="relevance-rank"):
    """根据用户输入的字段生成 bioRxiv 搜索 URL"""

    base_url = "https://www.biorxiv.org/search/"
    query_parts = []
    if term:
        query_parts.append(f"{quote(term)}")
    if title:
        query_parts.append(f"title%3A{quote(title)} title_flags%3Amatch-all")
    if author1:
        query_parts.append(f"author1%3A{quote(author1)}")
    if author2:
        query_parts.append(f"author2%3A{quote(author2)}")
    if abstract_title:
        query_parts.append(f"abstract_title%3A{quote(abstract_title)} abstract_title_flags%3Amatch-all")
    if text_abstract_title:
        query_parts.append(f"text_abstract_title%3A{quote(text_abstract_title)} text_abstract_title_flags%3Amatch-all")
    if journal_code:
        query_parts.append(f"jcode%3A{quote(journal_code)}")
    if section:
        query_parts.append(f"toc_section%3A{quote(section)}")
    if start_date and end_date:
        query_parts.append(f"limit_from%3A{start_date} limit_to%3A{end_date}")
    
    query_parts.append(f"numresults%3A{num_results}")
    query_parts.append(f"sort%3A{quote(sort)} format_result%3Astandard")

    return base_url + "%20".join(query_parts)

def scrape_biorxiv_results(search_url):
    """从 bioRxiv 搜索结果页面解析文章信息，包括 DOI"""
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'
    }
    response = requests.get(search_url, headers=headers)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        articles = soup.find_all('li', class_='search-result')

        results = []
        for article in articles:
            title_tag = article.find('span', class_='highwire-cite-title')
            title = title_tag.text.strip() if title_tag else "No title"

            authors_tag = article.find('span', class_='highwire-citation-authors')
            authors = authors_tag.text.strip() if authors_tag else "No authors"

            abstract_tag = article.find('div', class_='highwire-cite-snippet')
            abstract = abstract_tag.text.strip() if abstract_tag else "No abstract"

            link_tag = article.find('a', class_='highwire-cite-linked-title')
            link = "https://www.biorxiv.org" + link_tag['href'] if link_tag else "No link"

            doi_tag = article.find('span', class_='highwire-cite-metadata-doi')
            doi_link = doi_tag.text.strip().replace("doi:", "").strip() if doi_tag else "No DOI"

            metadata = {}
            result = {
                "Title": title,
                "Authors": authors,
                "DOI_link": doi_link,
                "Link": link
            }
            if doi_link != "No DOI":
                metadata = doi_get_biorxiv_metadata(doi_link.replace("https://doi.org/", ""))
                if metadata:
                    result.update(metadata)

            results.append(result)
        
        return results
    else:
        print(f"Error: Unable to fetch data (status code: {response.status_code})")
        return None

def doi_get_biorxiv_metadata(doi, server="biorxiv"):
    """使用 bioRxiv API 通过 DOI 获取文章的详细元数据"""
    url = f"https://api.biorxiv.org/details/{server}/{doi}/na/json"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'
    }
    
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        data = response.json()
        if 'collection' in data and len(data['collection']) > 0:
            article = data['collection'][0]
            return {
                "DOI": article.get("doi", "No DOI"),
                "Title": article.get("title", "No title"),
                "Authors": article.get("authors", "No authors"),
                "Corresponding Author": article.get("author_corresponding", "No corresponding author"),
                "Corresponding Institution": article.get("author_corresponding_institution", "No institution"),
                "Date": article.get("date", "No date"),
                "Version": article.get("version", "No version"),
                "Category": article.get("category", "No category"),
                "JATS XML Path": article.get("jats xml path", "No XML path"),
                "Abstract": article.get("abstract", "No abstract")
            }
        else:
            print("No data found for DOI:", doi)
            return None
    else:
        print(f"Error: Unable to fetch metadata (status code: {response.status_code})")
        return None

def search_key_words(key_words, num_results=10):
    # 生成搜索 URL
    search_url = generate_biorxiv_search_url(term=key_words, num_results=num_results)

    print("Generated URL:", search_url)

    # 获取并解析搜索结果
    articles = scrape_biorxiv_results(search_url)

    return articles


def search_advanced(term, title, author1, author2, abstract_title, text_abstract_title, section, start_date, end_date, num_results):
    # 生成搜索 URL
    search_url = generate_biorxiv_search_url(term, title=title, author1=author1, author2=author2, 
                                            abstract_title=abstract_title, 
                                            text_abstract_title=text_abstract_title,
                                            section=section, start_date=start_date, 
                                            end_date=end_date, num_results=num_results)

    print("Generated URL:", search_url)

    # 获取并解析搜索结果
    articles = scrape_biorxiv_results(search_url)

    return articles



if __name__ == "__main__":
    # 1. search_key_words 
    key_words = "COVID-19"
    articles = search_key_words(key_words, num_results=5)
    print(articles)

    # 2. search_advanced
    # 示例：用户输入搜索参数
    term = "CRISPR"
    title = "CRISPR"
    author1 = "Doudna"
    author2 = None
    abstract_title = "genome"
    text_abstract_title = None
    section = "New Results"
    start_date = "2025-02-27"
    end_date = "2025-03-18"
    num_results = 5
    articles = search_advanced(term, title, author1, author2, abstract_title, text_abstract_title, section, start_date, end_date, num_results)
    print(articles)

    # 3. doi get biorxiv metadata
    doi = "10.1101/2024.06.25.600517"
    metadata = doi_get_biorxiv_metadata(doi)
    print(metadata)
