import pytest as pytest

from server import Service


@pytest.mark.parametrize(
    'DNA_true',
    ['AAG', 'TTAAGG', 'TTAAG']
)
@pytest.mark.parametrize(
    'DNA_false',
    ['TTTA', 'ACACA']
)
def test_human_defining(DNA_true, DNA_false) -> None:
    """
        Tests that human health defined rightly
    """
    assert Service._check_health_impl(DNA_true)
    assert not Service._check_health_impl(DNA_false)


