import pytest
from tut2.app.sample import validate_age

# def test_validate_age():
#     validate_age(10)
     
# def test_validate_age_():
#     with pytest.raises(ValueError) as exc_info:
#         validate_age(-1)
#     print(str(exc_info.value))


# def test_validate_age_invalid_age():
#     with pytest.raises(ValueError) as exc_info :
#         validate_age(-1)
#     assert str(exc_info.value) == "Age Can not be less than 0"  


def test_validate_age_invalid_age():
    with pytest.raises(ValueError, match="Age cannot be less than 0"):
        validate_age(-1)