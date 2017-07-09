from nose.tools import assert_equal


def rev_word1(s):
    return " ".join(reversed(s.split()))


def rev_word2(s):
    return " ".join(s.split()[::-1])


def rev_word(s):
    words = []
    length = len(s)
    spaces = [' ']

    # Index Tracker
    i = 0

    while i < length:
        # se o elemento não esta na lista spaces
        if s[i] not in spaces:
            # rastreia até o fim da palavra
            word_start = i
            while i < length and s[i] not in spaces:
                # atualiza o 'i' ate o fim da palavra
                i += 1

            # adiciona a palavra a lista words
            words.append(s[word_start:i])

        i += 1

    return " ".join(map(str, words[::-1]))
    # return " ".join(reversed(words))


class ReversalTest(object):
    @staticmethod
    def test(sol):
        try:
            assert_equal(sol('          space before'), 'before space')
            assert_equal(sol('space after       '), 'after space')
            assert_equal(sol('     Hello John     how are you'), 'you are how John Hello')
            assert_equal(sol('1'), '1')
            print("Testes bem sucedidos")
        except AssertionError:
            print("Falha em um teste")


t = ReversalTest()
t.test(rev_word1)
t.test(rev_word2)
t.test(rev_word)
