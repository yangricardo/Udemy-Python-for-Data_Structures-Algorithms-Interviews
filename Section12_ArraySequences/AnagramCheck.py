from nose.tools import assert_equal


def anagram1(s1, s2):
    # remove espaços e coloca caracteres em caixa baixa
    s1 = s1.replace(' ', '').lower()
    s2 = s2.replace(' ', '').lower()

    # sorted retorna uma lista dos elementos de s1
    return sorted(s1) == sorted(s2)


def anagram2(s1, s2):
    # remove espaços e coloca caracteres em caixa baixa
    s1 = s1.replace(' ', '').lower()
    s2 = s2.replace(' ', '').lower()

    # compara tamanho das strings, se diferente, retorna falso
    if len(s1) != len(s2):
        return False

    # count é um dicionário utilizado para contar a existencia dos caractere
    count = {}

    for letter in s1:
        # para cada letra, verifico se ja esta em count
        if letter in count:
            # se existir, adiciono 1
            count[letter] += 1
        else:
            # ou adiciono a existencia da letra ao dicionario
            count[letter] = 1

    for letter in s2:
        # para cada letra, verifico se ja esta em count
        if letter in count:
            # se existir, subtraio 1
            count[letter] -= 1
        else:
            # ou adiciono a existencia da letra ao dicionario
            count[letter] = 1

    # verifica se os valores do dicionario são todos 0
    for k in count:
        if count[k] != 0:
            return False

    return True


class AnagramTest(object):
    @staticmethod
    def test(msg, sol):
        try:
            assert_equal(sol('go go go ', 'gggooo'), True)
            assert_equal(sol('abc', 'cba'), True)
            assert_equal(sol('hi man', 'hi       man'), True)
            assert_equal(sol('123', '2 1'), False)
            assert_equal(sol("Rato Trai America", 'Rita Rota Iracema'), True)
            print(msg + "All Test Cases Passed")
        except AssertionError:
            print("Um ou mais testes falharam")


t = AnagramTest()
t.test("Anagram Check Type 1: ", anagram1)
t.test("Anagram Check Type 2: ", anagram2)
