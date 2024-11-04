import requests
from bs4 import BeautifulSoup


print('Type "en" if you want to translate from French into English, or "fr" if you want to translate from English into French:')
language = input()


print("Type the word you want to translate:")
word = input()


print(f'You chose "{language}" as a language to translate "{word}".')


if language == "en":
    url = f"https://context.reverso.net/translation/french-english/{word}"
elif language == "fr":
    url = f"https://context.reverso.net/translation/english-french/{word}"
else:
    print("Invalid language selection.")
    exit()


headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
    "Connection": "keep-alive",
    "Referer": "https://context.reverso.net/",
}

response = requests.get(url, headers=headers)


if response.status_code == 200:
    print("200 OK")
else:
    print("Error:", response.status_code)
    exit()


soup = BeautifulSoup(response.content, "html.parser")


translations = [elem.get_text(strip=True) for elem in soup.select('.translation')[:5]]
examples = [elem.get_text(" ", strip=True) for elem in soup.select('.example')[:5]]

print("Translations")
print(translations)
print(examples)