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
        assert number_to_words(-(10**2)) == "minus one hundred"
        assert number_to_words(-(10**3)) == "minus one thousand"
        assert number_to_words(-(10**6)) == "minus one million"
        assert number_to_words(-(10**9)) == "minus one billion"
        assert number_to_words(-(10**12)) == "minus one trillion"
        assert number_to_words(-(10**30)) == "minus one nonillion"
        assert number_to_words(-(10**33)) == "minus one decillion"

    def test_less_than_twenty(self):
        assert number_to_words(1) == "one"
        assert number_to_words(2) == "two"
        assert number_to_words(10) == "ten"
        assert number_to_words(18) == "eighteen"
        assert number_to_words(19) == "nineteen"

    def test_multiples_of_ten(self):
        assert number_to_words(20) == "twenty"
        assert number_to_words(30) == "thirty"
        assert number_to_words(40) == "forty"
        assert number_to_words(50) == "fifty"
        assert number_to_words(60) == "sixty"
        assert number_to_words(70) == "seventy"
        assert number_to_words(80) == "eighty"
        assert number_to_words(90) == "ninety"

    def test_less_than_hundred(self):
        assert number_to_words(21) == "twenty-one"
        assert number_to_words(32) == "thirty-two"
        assert number_to_words(43) == "forty-three"
        assert number_to_words(54) == "fifty-four"
        assert number_to_words(65) == "sixty-five"
        assert number_to_words(76) == "seventy-six"
        assert number_to_words(87) == "eighty-seven"
        assert number_to_words(98) == "ninety-eight"

    def test_less_than_thousand(self):
        assert number_to_words(100) == "one hundred"
        assert number_to_words(101) == "one hundred and one"
        assert number_to_words(110) == "one hundred and ten"
        assert number_to_words(115) == "one hundred and fifteen"
        assert number_to_words(120) == "one hundred and twenty"
        assert number_to_words(121) == "one hundred and twenty-one"

        assert number_to_words(700) == "seven hundred"
        assert number_to_words(778) == "seven hundred and seventy-eight"
        assert number_to_words(999) == "nine hundred and ninety-nine"

    def test_complex(self):
        assert number_to_words(87334) == "eighty-seven thousand three hundred and thirty-four"
        assert (
            number_to_words(54712671)
            == "fifty-four million seven hundred and twelve thousand six hundred and seventy-one"
        )
        assert (
            number_to_words(123456789)
            == "one hundred and twenty-three million four hundred and fifty-six thousand seven hundred and eighty-nine"
        )
        assert (
            number_to_words(999999999)
            == "nine hundred and ninety-nine million nine hundred and ninety-nine thousand nine hundred and ninety-nine"
        )
        assert number_to_words(1000000000) == "one billion"
        assert number_to_words(2000000000) == "two billion"
        assert number_to_words(3000000000) == "three billion"
