import pytest

from store.store_facade import StoreFacade


@pytest.fixture(name='store', autouse=True)
def store_facade_cls(request):
    print('Init store Facade in fixture')
    store = StoreFacade()
    yield store
    print('clean up Store Facade in fixture')
    del store.catalog.phones


















# @pytest.fixture(scope='package', autouse=True)
# def fix_package():
#     print('From package')
#     yield
#     print('From package, teardown')
#
#
# @pytest.fixture(scope='module', autouse=True)
# def fix_module():
#     print('From module')
#     yield
#     print('From module, teardown')
