from datetime import datetime

import pytest

from wordifyer import validate


class TestValidation:
    def test_integer(self):
        validate(0)
        validate(12345)
        validate(-654987)
        assert 12345 == validate("12345")

    def test_fractions_not_allowed(self):
        with pytest.raises(TypeError):
            validate(10.5)

        with pytest.raises(TypeError):
            validate(-10.5)

    def test_large(self):
        validate(10**36 - 1)
        validate(-(10**36) + 1)
        with pytest.raises(ValueError):
            validate(10**36)
        with pytest.raises(ValueError):
            validate(-(10**36))

    def test_wrong_type(self):
        with pytest.raises(TypeError):
            validate("string")

        with pytest.raises(TypeError):
            validate(datetime.now())

        with pytest.raises(TypeError):
            validate([])

        with pytest.raises(TypeError):
            validate({})
