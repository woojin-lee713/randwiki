import requests

def get_random_wikipedia_page():
    random_url = "https://en.wikipedia.org/api/rest_v1/page/random/summary"
    response = requests.get(random_url)

    if response.status_code == 200:
        print("URL of the random Wikipedia page:", response.url)
        return response.text
    else:
        return "Failed to retrieve a random Wikipedia page"

if __name__=="__main__":
    page_content = get_random_wikipedia_page()
    print(page_content)
