class TestStore:

    def test_possibility_to_get_catalog(self, store):
        result = store.show_catalog()
        assert not result
        assert isinstance(result, list)

    def test_possibility_to_add_phone_to_catalog(self, store):
        result = store.add_phone_to_catalog('Iphone', '1000$')
        assert result

    def test_possibility_to_remove_phone_from_catalog(self, store):
        self.result = store.remove_phone_from_catalog('Iphone')
        assert self.result
