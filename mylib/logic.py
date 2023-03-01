import wikipedia


def wiki(name="War Godess", length=1):
    """This is wikipidea fetcher"""

    my_wiki = wikipedia.summary(name, length)
    return my_wiki

def search_wiki(name):
    """Search wiki for the names we want"""

    results = wikipedia.search(name)
    return results