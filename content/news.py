import bs4
from urllib.request import Request, urlopen


def bbc():
    website = 'https://bbc.co.uk/'
    req = Request("https://bbc.co.uk/news")
    req.add_header('User-agent','Mozilla/5.0 (Windows; U; Windows NT 5.1; de; rv:1.9.1.5) Gecko/20091102 Firefox/3.5.5')
    response = urlopen(req)
    soup = bs4.BeautifulSoup(response.read(), "html.parser")
    title = []
    desc = []
    href = []
    for i in soup.find_all("h3", class_="title-link__title"):
        title.append(i.text)

    for i in soup.find_all("p", class_="buzzard__summary"):
        desc.append(i.text)

    for i in soup.find_all("a", class_="title-link", href=True):
        href.append('`'+website+i['href'][1:]+'`')

    return ('Current Headline on BBC.co.uk: `' +title[0] + '`\n' +desc[0] + '\n' +'Read more at: `' + href[0]+'`')




def cnn():
    website = 'http://edition.cnn.com/'
    req = Request("http://edition.cnn.com/")
    req.add_header('User-agent','Mozilla/5.0 (Windows; U; Windows NT 5.1; de; rv:1.9.1.5) Gecko/20091102 Firefox/3.5.5')
    response = urlopen(req)
    soup = bs4.BeautifulSoup(response.read(), "html.parser")
    href = []
    productDivs = soup.findAll('h3', attrs={'class': 'cd__headline'})
    for div in productDivs:
        href.append(div.find('a')['href'])

    # Gets current 'top story' from CNN.
    top_story_url = website+href[0][1:]

    newreq = Request(top_story_url)
    newreq.add_header('User-agent','Mozilla/5.0 (Windows; U; Windows NT 5.1; de; rv:1.9.1.5) Gecko/20091102 Firefox/3.5.5')
    newresponse = urlopen(newreq)
    newsoup = bs4.BeautifulSoup(newresponse.read(), "html.parser")
    title = []
    desc = []

    for i in newsoup.find_all("h1", class_="pg-headline"):
        title.append(i.text)

    for i in newsoup.find_all("p", class_="zn-body__paragraph"):
        desc.append(i.text)

    return ( 'Current Headline on CNN.com: `'+title[0]+'`\n'+desc[0].replace(' (CNN)','')+'\n'+'Read more at: `'+top_story_url+'`')
