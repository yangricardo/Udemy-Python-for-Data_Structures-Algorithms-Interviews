from nose.tools import assert_equal


def large_cont_sum(arr):
    if len(arr) == 0:
        return 0

    max_sum = current_sum = arr[0]

    for num in arr[1:]:
        #começa a partir do segundo elemento
        print(str(current_sum)+' : '+str(num))
        current_sum = max(current_sum + num, num)
        print(str(current_sum)+' : '+str(max_sum))
        max_sum = max(current_sum, max_sum)

    print('[max_sum]:'+str(max_sum))
    return max_sum


class LargeContTest(object):
    @staticmethod
    def test(sol):
        try:
            assert_equal(sol([1, 2, -1, 3, 4, -1]), 9)
            assert_equal(sol([1, 2, -1, 3, 4, 10, 10, -10, -1]), 29)
            assert_equal(sol([-1, 1]), 1)
            print("Testes bem sucedidos")
        except AssertionError:
            print("Teste falhou")


t = LargeContTest()
t.test(large_cont_sum)
