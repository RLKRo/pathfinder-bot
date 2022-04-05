import requests
import tokens


def link(message: str) -> str:
    url = "https://google-search3.p.rapidapi.com/api/v1/search/q=site%3Ad20pfsrd.com%20" + message.replace(' ', '%20')

    headers = {
        "X-User-Agent": "desktop",
        "X-Proxy-Location": "EU",
        "X-RapidAPI-Host": "google-search3.p.rapidapi.com",
        "X-RapidAPI-Key": tokens.google_token
    }

    response = requests.request("GET", url, headers=headers).json()["results"][0]

    return f'[{response["title"]}]({response["link"]})\n{response["description"]}'

