def domain_name(url: str) -> str:
    s = {"http://", "www.", "https://"}
    for i in s:
        if i in url:
            url = url.replace(i, "")
    return url[:url.find('.')]


if __name__ == "__main__":
    print(domain_name("http://google.com"))
