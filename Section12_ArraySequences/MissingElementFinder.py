from nose.tools import assert_equal
import collections


def finder(arr1, arr2):
    # Solução em O(NLogN)

    # ordena arrays
    arr1.sort()
    arr2.sort()

    # zip: gera um array de tuplas formadas pelos i-esimos elementos

    for num1, num2 in zip(arr1, arr2):
        if num1 != num2:
            print('[FINDER1]: ' + str(num1) + ' é o elemento perdido')
            return num1

    return arr1[-1]


def finder2(arr1, arr2):
    # Solução em O(N)

    # importa um dicionario default de inteiros
    d = collections.defaultdict(int)

    # gero um dicionario a partir do segundo array
    for num in arr2:
        d[num] += 1

    for num in arr1:
        # caso o num seja zero no dicionario, esse é o numero procurado
        # caso contrario, subtrai a existencia do numero
        if d[num] is 0:
            print('[FINDER2]: ' + str(num) + ' é o elemento perdido')
            return num
        else:
            d[num] -= 1


def finder3(arr1, arr2):
    result = 0
    # opera XOR para cada elemento da união dos arrays
    for num in (arr1 + arr2):
        result ^= num
        print('[FINDER3-result] ' + str(result))

    print('[FINDER3]: ' + str(result) + ' é o elemento perdido')
    return result


class TestFinder(object):
    def test(self, sol):
        try:
            assert_equal(sol([5, 5, 7, 7], [5, 7, 7]), 5)
            assert_equal(sol([5, 5, 7, 7], [5, 7, 7]), 5)
            assert_equal(sol([9, 8, 7, 6, 5, 4, 3, 2, 1], [9, 8, 7, 5, 4, 3, 2, 1]), 6)
            print('Testes bem sucedidos')
        except AssertionError:
            print('Algum teste falhou')


t = TestFinder()
t.test(finder)
t.test(finder2)
t.test(finder3)
