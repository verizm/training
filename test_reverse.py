def test_reverse():
    list = [1, 2, 3]
    new_list = list[::-1] # инвертирование через индексы
    list_1 = sorted(list, reverse=True)# через sorte
    assert new_list == [3, 2, 1]
    assert list_1 == [3, 2, 1]

