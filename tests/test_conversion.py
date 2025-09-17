from wordifyer import number_to_words


class TestConversion:
    def test_simple(self):
        assert number_to_words(0) == "zero"
        assert number_to_words(10**2) == "one hundred"
        assert number_to_words(10**3) == "one thousand"
        assert number_to_words(10**6) == "one million"
        assert number_to_words(10**9) == "one billion"
        assert number_to_words(10**12) == "one trillion"
        assert number_to_words(10**30) == "one nonillion"
        assert number_to_words(10**33) == "one decillion"

    def test_negative(self):
        assert number_to_words(-0) == "zero"
        assert number_to_words(-(10**3)) == "minus one thousand"
        assert number_to_words(-(10**6)) == "minus one million"
        assert number_to_words(-(10**9)) == "minus one billion"
        assert number_to_words(-(10**12)) == "minus one trillion"
        assert number_to_words(-(10**30)) == "minus one nonillion"
        assert number_to_words(-(10**33)) == "minus one decillion"
