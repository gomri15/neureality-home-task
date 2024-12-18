
import pytest

from src.neu_reality import NeuReality

@pytest.mark.parametrize("input_string, expected_output", [
    ("The quick brown fox", "fox brown quick The"),
    ("", ""),
    ("Hello, World! 123", "123 World! Hello,"),
    ("""this is a very long string that should be reversed quickly and without issues as soon as possible""",
     """possible as soon as issues without and quickly reversed be should that string long very a is this""")
])
def test_reverse_endpoint(neureality: NeuReality, input_string: str, expected_output: str):
    """Test the /reverse endpoint."""
    response = neureality.string_handler_api_client.reverse(input_string)
    assert response["result"] == expected_output


def test_restore_endpoint(neureality: NeuReality):
    """Test the /restore endpoint."""
    neureality.string_handler_api_client.reverse("The quick brown fox")
    response = neureality.string_handler_api_client.restore()
    assert response["result"] == "fox brown quick The"
