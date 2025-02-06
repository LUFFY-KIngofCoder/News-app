from newsapi import NewsApiClient

print('What do you want to read:\n1)Everything\n2)Top-Headlines\n3)Sources')
news = int(input('>>>>>>'))

newsapi = NewsApiClient(api_key='33e40727a9634e19af5d10ab2597347c')

if news == 1:
    q = input("What type of news you want to read>>>>")
    SortBy = input('you want your news to be sort by: 1)relevancy\n2)popularity\n3)publishedAt') or 'publishedAt'
    sources = input('which source you want your news from. If more than one write with commas>>>>') or None
    domains = input('enter the domain you want to get the news from>>>>') or None
    excludeDomains = input('enter the domain you dont want want to get the news from>>>>') or None
    language = input("which language you want to read news in>>>>") or None

    Everything = newsapi.get_everything(q=q,
                                        sources=sources,
                                        sort_by=SortBy,
                                        domains=domains,
                                        exclude_domains=excludeDomains,
                                        language=language)

    print(f"Total Results = {Everything['totalResults']}")

    for i in Everything['aticles']:
        print(i)


elif news == 2:

    q = input("What type of news you want to read>>>>")
    sources = input('which source you want your news from. If more than one write with commas>>>>') or None
    if sources == None:
        country = input("whichs countries news you want to watch") or None
        category = input("Which category of new you want to read "
                         "\n1)business"
                         "\n2)entertainment"
                         "\n3)general"
                         "\n4)health"
                         "\n5)science"
                         "\n6)sports"
                         "\n7)technology")

    top_headlines = newsapi.get_top_headlines(q=q,
                                              sources=sources,
                                              category= category,
                                              country= country,
                                              )

    print(f"Total Results = {top_headlines['totalResults']}")

    for i in top_headlines['articles']:
        print(i)


elif news == 3:
    sources = newsapi.get_sources()
    for i in sources['sources']:
        print(i)
