from fluentstream.pystream import Stream


def test_filter():
    assert Stream([1, 2, 3, 4]).filter(lambda x: x < 3).list() == [3, 4]


def test_map():
    assert Stream([1, 2, 3, 4]).filter(lambda x: x < 3).map(lambda x: str(x * 9)).list() == ['27', '36']


def test_order_by():
    assert Stream([3, 1, 2]).order_by(lambda x: x).list() == [1, 2, 3]


def test_find_first():
    assert Stream(['x', 1, 9, 'z']).find_first(lambda x: x == 9) == 9


def test_find_any():
    assert Stream([1, 2, 3]).find_any(lambda x: x == 2) == 2
    assert not Stream([1, 2, 3]).find_any(lambda x: x == 4)


def test_flatten():
    assert Stream([[1, 2], [3, 4]]).flatten().list() == [1, 2, 3, 4]


def test_dict():
    assert Stream([1, 2]).dict(lambda x: str(x)) == {'1': 1, '2': 2}


def test_min_max():
    assert Stream([1, 2, 3]).max() == 3
    assert Stream([1, 2, 3]).min() == 1


def test_for_each():
    assert Stream([1, 3, 4]).for_each(lambda x: x * 2).list() == [2, 6, 8]


def test_all_match():
    assert Stream([1, 2, 3]).all_match(lambda x: x > 0)
    assert not Stream([0, 2, 3]).all_match(lambda x: x > 0)


def test_any_match():
    assert Stream([1, 2, 3]).any_match(lambda x: x == 1)
    assert not Stream([1, 2, 3]).any_match(lambda x: x == 4)


def test_none_match():
    assert Stream([1, 2, 3]).none_match(lambda x: x < 0)
    assert not Stream([-1, 2, 3]).none_match(lambda x: x < 0)


def test_take():
    assert Stream([1, 2, 3]).take(0, 1, 2).list() == [1, 2]
    assert Stream([1, 2, 3, 4, 5, 6, 7]).take(0, 2, 6).list() == [1, 3, 5]
    assert Stream([1, 2, 3, 4]).take(0, 2, 6).list() == [1, 3]


def test_limit():
    assert Stream([1, 2, 3, 4, 5]).limit(3).list() == [1, 2, 3]
    assert Stream([1, 2, 3, 4, 5]).limit(9).list() == [1, 2, 3, 4, 5]


def test_skip():
    assert Stream([1, 2, 3, 4, 5, 6, 7]).skip(5).list() == [6, 7]