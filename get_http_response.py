from urllib.request import urlopen
import ssl


def get(url):
    context = ssl._create_unverified_context()
    page = urlopen(url, context=context)
    try:
        html = page.read()
    except BaseException:
        print(url)
    return html
