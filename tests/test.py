# --color=yes
import pytest

from main import domain_name, int32_to_ip, zeros, bananas, count_find_num


@pytest.mark.parametrize(
    'input, expected', [("http://google.com", "google"),
                        ("http://google.co.jp", "google"),
                        ("www.xakep.ru", "xakep"),
                        ("https://youtube.com", "youtube")
                        ]
)
def test_domain_name(input, expected):
    assert domain_name(input) == expected


@pytest.mark.parametrize(
    'input, expected', [(2154959208, "128.114.17.104"),
                        (0, "0.0.0.0"),
                        (2149583361, "128.32.10.1")
                        ]
)
def test_int32_to_ip(input, expected):
    assert int32_to_ip(input) == expected


@pytest.mark.parametrize(
    'input, expected', [(0, 0),
                        (6, 1),
                        (30, 7)
                        ]
)
def test_zeros(input, expected):
    assert zeros(input) == expected


@pytest.mark.parametrize(
    "input, expected", [
        ("banann", set()),
        ("banana", {"banana"}),
        ("bbananana", {"b-an--ana", "-banana--", "-b--anana", "b-a--nana", "-banan--a",
                       "b-ana--na", "b---anana", "-bana--na", "-ba--nana", "b-anan--a",
                       "-ban--ana", "b-anana--"}),
        ("bananaaa", {"banan-a-", "banana--", "banan--a"}),
        ("bananana", {"ban--ana", "ba--nana", "bana--na", "b--anana", "banana--", "banan--a"}),
    ]
)
def test_bananas(input, expected):
    assert bananas(input) == expected


@pytest.mark.parametrize(
    "primesL, limit, expected", [
        ([2, 3], 200, [13, 192]),
        ([2, 5], 200, [8, 200]),
        ([2, 3, 5], 500, [12, 480]),
        ([2, 3, 5], 1000, [19, 960]),
        ([2, 3, 47], 200, []),
    ]
)
def test_count_find_num(primesL, limit, expected):
    assert count_find_num(primesL, limit) == expected
