import requests
from bs4 import BeautifulSoup

urls = [f'https://github.com/LinusWillmont?page=1&tab=repositories',
f'https://github.com/LinusWillmont?page=2&tab=repositories',
f'https://github.com/LinusWillmont?page=3&tab=repositories']

repos = []

for url in urls: 

    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    repo_links = soup.find_all('a', itemprop='name codeRepository')

    for link in repo_links:
        repo_name = link.get_text(strip=True)
        repo_url = f'https://github.com/LinusWillmont/{repo_name}'
        repos.append(repo_url)

for repo in repos:
    print(repo)

with open('repos.txt', 'w') as f:
    for repo in repos:
        f.write(f'{repo}\n')

print("Repository URLs have been written to repos.txt")
