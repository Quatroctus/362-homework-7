from leapyear import leapyear


def test_non():
    assert leapyear(1999) == False
    assert leapyear(1998) == False
    assert leapyear(1997) == False

