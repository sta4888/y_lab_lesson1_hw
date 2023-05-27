# --color=yes
import pytest

from main import domain_name, int32_to_ip, zeros


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
    assert zeros(0) == 0
