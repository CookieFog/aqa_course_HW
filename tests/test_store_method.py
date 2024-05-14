import pytest


@pytest.mark.regression
def test_possibility_to_get_catalog(store):
    result = store.show_catalog()
    assert not result
    assert isinstance(result, list)


@pytest.mark.smoke
def test_possibility_to_show_catalog(store):
    result = store.show_catalog()
    assert result

