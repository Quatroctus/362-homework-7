from leapyear import leapyear


def test_non():
    assert leapyear(1999) == False
    assert leapyear(1998) == False
    assert leapyear(1997) == False


def test_leapyear100fail():
    assert leapyear(1900) == False
    assert leapyear(1800) == False
    assert leapyear(1700) == False


def test_leapyear400succeed():
    assert leapyear(2000) == True
    assert leapyear(1600) == True
    assert leapyear(1200) == True
