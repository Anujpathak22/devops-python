import wikipedia


def wiki(name="War Godess", length=1):
    """This is wikipidea fetcher"""

    my_wiki = wikipedia.summary(name, length)
    return my_wiki
