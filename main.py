from typing import List


def domain_name(url: str) -> str:
    """метод domain_name, который вернет домен из url адреса"""
    s = {"http://", "www.", "https://"}
    for i in s:
        if i in url:
            url = url.replace(i, "")
    return url[:url.find('.')]


def int32_to_ip(int32: int) -> str:
    """int32_to_ip, который принимает на вход 32-битное целое число (integer) и возвращает строковое представление его в виде IPv4-адреса"""
    h = hex(int32)
    rt = str(h)[2:]
    if len(rt) < 8:
        rt = rt.zfill(8)
    ipV4 = []
    for i in range(0, len(rt), 2):
        s = rt[i] + rt[i + 1]
        ipV4.append(str(int(s, 16)))
    return '.'.join(ipV4)


def zeros(n: int) -> int:
    """метод zeros, который принимает на вход целое число (integer) и возвращает количество конечных нулей в факториале заданного числа"""
    result = 0
    while n > 0:
        n //= 5
        result += n
    return result


def bananas(s: str) -> set:
    """думаю, это гениальное решение)"""
    ret = get_list_of_words_banana(s, "banana")
    result = set()
    result.update(ret)
    # Your code here!
    return result


def get_list_of_words_banana(s: str, word: str) -> list:
    ret = []

    if word == '':
        ret.append(''.rjust(len(s), '-'))
        return ret

    for si in range(len(s)):
        if word[0] == s[si]:
            left_s = ''.rjust(si, '-') + s[si]
            if s[si + 1:] == '' and word[1:] == '':
                ret.append(left_s)
            else:
                right_s_list = get_list_of_words_banana(s[si + 1:], word[1:])
                for right_s in right_s_list:
                    ret.append(left_s + right_s)
    return ret


def count_find_num(primesL: list, limit: int) -> List[int]:  # primesL, limit
    count = 0
    max_n = 0
    for i in range(2, limit + 1):
        j = 2
        primfac = []
        while j * j <= i:
            while i % j == 0 and j in primesL:
                primfac.append(j)
                i = i / j
            j = j + 1
        if i > 1:
            primfac.append(int(i))
        d = primfac
        if set(primesL) == set(d):
            nu = 1
            for k in d:
                nu *= k
            max_n = nu
            count += 1
    return [count, max_n] if count != 0 else []


if __name__ == "__main__":
    primesL = [2, 3]
    limit = 200
    print(count_find_num(primesL, limit))
