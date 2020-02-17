
def test_even():
    nums = []
    for i in range(0, 21):
        nums.append(i)
    not_even_nums = []
    even_nums = []
    for i in nums:
        if i % 2 != 0 or i == 0:
            not_even_nums.append(i)
        elif  i % 2 == 0 or i == 0:
            even_nums.append(i)

    assert not_even_nums == [0, 1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
    assert even_nums == [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
