def domain_name(url: str) -> str:
    s = {"http://", "www.", "https://"}
    for i in s:
        if i in url:
            url = url.replace(i, "")
    return url[:url.find('.')]


def int32_to_ip(int32):
    h = hex(int32)
    rt = str(h)[2:]
    if len(rt) < 8:
        rt = rt.zfill(8)
    ipV4 = []
    for i in range(0, len(rt), 2):
        s = rt[i] + rt[i+1]
        ipV4.append(str(int(s, 16)))
    return '.'.join(ipV4)


if __name__ == "__main__":
    # print(domain_name("http://google.com"))
    print(int32_to_ip(0))
