def test_reverse():
    list = [1, 2, 3]
    new_list = list[::-1] # �������������� ����� �������
    list_1 = sorted(list, reverse=True)# ����� sorte
    assert new_list == [3, 2, 1]
    assert list_1 == [3, 2, 1]

