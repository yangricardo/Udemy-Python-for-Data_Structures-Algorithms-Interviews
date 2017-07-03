from nose.tools import assert_equal


def pair_sum(arr, k):
    # imprime os pares cuja soma formam 'k' e retorna a quantidade de pares

    if len(arr) < 2:
        return

    # Sets for tracking, rastreio de elementos vistos no conjunto
    seen = set()
    output = set()

    for num in arr:
        target = k - num
        if target not in seen:
            seen.add(num)
        else:
            output.add(((min(num, target)), max(num, target)))

    print('\n'.join(map(str, list(output))))
    return len(output)


class TestPair(object):
    def test(self, sol):
        try:
            assert_equal(sol([1, 9, 2, 8, 3, 7, 4, 6, 7, 7, 12, 14, 11, 13, -1], 10), 5)
            assert_equal(sol([1, 2, 3, 1, 3], 3), 1)
            assert_equal(sol([1, 3, 2, 2], 4), 2)
            print('Testes bem sucedidos')
        except AssertionError:
            print('Algum teste falhou')


t = TestPair()
t.test(pair_sum)
