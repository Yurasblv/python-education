"""Module testing Shop and Product functionalities"""
import pytest
from tests.to_test import Product, Shop


@pytest.fixture
def fix_prod():
    """Creates example of product obj"""
    return Product('Samsung Bassbooster 3', 499.50)


def test_init(fix_prod):
    """Tests initialization"""
    assert fix_prod.title == 'Samsung Bassbooster 3'
    assert fix_prod.price != 500


@pytest.mark.parametrize('quantity', [1, 2, 3, 4, 5, 6, 7, 8, 9, 10.0])
def test_add(fix_prod, quantity):
    """Tests adding for values"""
    fix_prod.add_quantity(5)
    assert fix_prod.quantity == 6
    fix_prod.add_quantity(0.5)
    assert type(fix_prod.quantity) == float
    fix_prod.add_quantity(quantity)
    assert fix_prod.quantity != [1, 2, 3, 4, 5, 6, 7, 8, 9, 10.0]


def test_change_price(fix_prod):
    """Tests process of adding price"""
    assert fix_prod.change_price(659.00) != fix_prod.price
    assert fix_prod.change_price(600) != float


def test_substract(fix_prod):
    """Tests taking the quantity"""
    fix_prod.add_quantity(10)
    fix_prod.subtract_quantity(2)
    assert fix_prod.quantity == 9


@pytest.fixture
def fix_shop(fix_prod):
    """Creates shop obj with default params"""
    return Shop(fix_prod)


def test_product(fix_shop):
    """Testing the init of base Shop obj """
    assert fix_shop.products[0].title == 'Samsung Bassbooster 3'


@pytest.mark.parametrize('shop', [Product('Hyper X Mouse', 34.99)])
def test_add_product(fix_shop, shop):
    """Tests adding new item to the shop"""
    shop_ = Shop(shop)
    assert shop_.products == [shop]
    fix_shop.add_product(shop)
    assert len(fix_shop.products) == 2
    assert fix_shop.products[1] == shop

def test_idx(fix_shop,fix_prod):
    """Tests personal id for item in Shop bill"""
    assert fix_shop._get_product_index('Samsung Bassbooster 3') == 0
    shop_ = Shop()
    shop_.add_product(Product('Hyper X Mouse', 34.99))
    assert shop_._get_product_index('Hyper X Mouse') == 0
    shop_.add_product(fix_prod)
    assert shop_._get_product_index('Samsung Bassbooster 3') == 1
