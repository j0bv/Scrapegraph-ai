# 🤖 AmazScraper

This repo is a Python open source library for making a faster scraping using AI and without any knowledge about the HTML code.

The tech stack is fully in Python and the main libraries used are pydantic, langchain and requests.

The use of this library allows to scrape and extract informations from websites in just few seconds instead of write ad-hoc code for each website.

This library can work passing as a parameter from the code the HTML to scrape or it can work passing the
link of the website that you want to extract informations.

# Setup

Follow the following steps:

1.  ```bash
    git clone https://github.com/VinciGit00/AmazScraper.git
    ```
2.  ```bash
    pip install -r requirements.txt
    ```
3.  Go to [https://openai.com](https://openai.com/) and login
4.  Now you can access to [https://platform.openai.com/docs/overview](https://platform.openai.com/docs/overview)
5.  Create a new API key and copy it
    ![Screenshot 2024-01-26 alle 17.10.10.png](doc/Screenshot_2024-01-26_alle_17.10.10.png)

![Screenshot 2024-01-26 alle 17.10.31.png](doc/Screenshot_2024-01-26_alle_17.10.31.png)

![Screenshot 2024-01-26 alle 17.10.52.png](doc/Screenshot_2024-01-26_alle_17.10.52.png)

![Screenshot 2024-01-26 alle 17.11.10.png](doc/Screenshot_2024-01-26_alle_17.11.10.png)

6. Open the .env file inside main and paste the API key

```config
API_KEY="your openai.com api key"
```

7. You are ready to go! 🚀

# Practical use

## Using AmazScraper as a library

```python
from AmazScraper.ClassGenerator import Generator

from AmazScraper.getter import get_function, scraper

values = [
    {
        "title": "title",
        "type": "str",
        "description": "Title of the items"
    }
]

if __name__ == "__main__":

    query_info = scraper("https://www.mockupworld.co", 4197)
    generator_instance = Generator(values)

    res = generator_instance.invocation(query_info)
```

### Case 2: Passing your own HTML code

```python
import sys
from AmazScraper.ClassGenerator import Generator

values = [
    {
        "title": "title",
        "type": "str",
        "description": "Title of the news"
    }
]

# Example using a HTML code
query_info = '''
        Given this code extract all the information in a json format about the news.
        <article class="c-card__wrapper aem_card_check_wrapper" data-cardindex="0">
            <div class="c-card__content">
                <h2 class="c-card__title">Booker show da 52 punti, chi ha più partite oltre quota 50</h2>
                <div class="c-card__label-wrapper c-label-wrapper">
                    <span class="c-label c-label--article-heading">LA CLASSIFICA</span>
                </div>
                <p class="c-card__abstract">Il n° 1 dei Suns ha dominato la sfida vinta a New Orleans segnando 52 punti. Si tratta della...</p>
                <div class="c-card__info">
                    <time class="c-card__date" datetime="20 gen - 07:54">20 gen - 07:54</time>
                    <span class="c-card__content-data">
                        <i class="icon icon--media-outline icon--gallery-outline icon--xxsmall icon--c-neutral">
                            <svg width="80" height="80" viewBox="0 0 80 80" xmlns="http://www.w3.org/2000/svg" class="icon__svg icon__svg--gallery-outline">
                                <path d="M26.174 32.174v31.975h44.588V32.174H26.174zm-3.08-9.238h50.747A6.159 6.159 0 0 1 80 29.095v38.134a6.159 6.159 0 0 1-6.159 6.158H23.095a6.159 6.159 0 0 1-6.159-6.158V29.095a6.159 6.159 0 0 1 6.159-6.159zM9.239 55.665a4.619 4.619 0 0 1-9.238 0V16.777C0 10.825 4.825 6 10.777 6H64.08a4.619 4.619 0 1 1 0 9.238H10.777c-.85 0-1.54.69-1.54 1.54v38.887z" fill="currentColor" fill-rule="evenodd"></path>
                            </svg>
                        </i>
                        28 foto
                    </span>
                </div>
            </div>
            <div class="c-card__img-wrapper">
                <figure class="o-aspect-ratio o-aspect-ratio--16-10 ">
                    <img crossorigin="anonymous" class="c-card__img j-lazyload" alt="Partite con 50+ punti: Booker in Top-20" data-srcset="..." sizes="..." loading="lazy" data-src="...">
                    <noscript>
                        <img crossorigin="anonymous" class="c-card__img" alt="Partite con 50+ punti: Booker in Top-20" srcset="..." sizes="..." src="...">
                    </noscript>
                </figure>
                <i class="icon icon--media icon--gallery icon--medium icon--c-primary">
                    <svg width="80" height="80" viewBox="0 0 80 80" xmlns="http://www.w3.org/2000/svg" class="icon__svg icon__svg--gallery">
                        <path d="M17.005 20.221h60.211c1.538 0 2.784 1.28 2.784 2.858v48.317c0 1.578-1.246 2.858-2.784 2.858H17.005c-1.537 0-2.784-1.28-2.784-2.858V23.079c0-1.578 1.247-2.858 2.784-2.858zM5.873 11.873V60.62a2.937 2.937 0 0 1-5.873 0V11.286A5.286 5.286 0 0 1 5.286 6h61.08a2.937 2.937 0 1 1 0 5.873H5.873z"></path>
                    </svg>
                </i>
            </div>
        </article>
    '''

if __name__ == "__main__":
    generator_instance = Generator(values)

    generator_instance.invocation(query_info)
```

Developed by

![logo-removebg-preview.png](doc/logo-removebg-preview.png)
