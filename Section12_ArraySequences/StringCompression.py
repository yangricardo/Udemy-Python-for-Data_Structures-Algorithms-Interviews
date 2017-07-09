from nose.tools import assert_equal


def string_compress(s):

    if s == '':
        return ''

    length = len(s)
    i = 0
    sc = ""

    while i < length:
        aux = s[i]
        sc.join(aux)
        c = 1
        print(s[i])
        i += 1

        while i < length and s[i] == aux:
            c += 1
            print(s[i])
            i += 1
        sc.join(str(c))

    print(sc)
    return sc


class StringCompressTest(object):

    @staticmethod
    def test(sol):
        try:
            #assert_equal(sol(''), '')
            assert_equal(sol('AABBCC'), 'A2B2C2')
            assert_equal(sol('AAABCCDDDDD'), 'A3B1C2D5')
            print("Testes bem sucedidos")
        except AssertionError:
            print("Teste falhou")


t = StringCompressTest
t.test(string_compress)
