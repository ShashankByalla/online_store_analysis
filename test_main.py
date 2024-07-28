import pytest
import pandas as pd
from main import read_data, compute_revenue_by_month, compute_revenue_by_product, get_top_customers, compute_revenue_by_customer

@pytest.fixture
def sample_data():
    data = {
        'order_id': [1, 2, 3],
        'customer_id': [101, 102, 101],
        'order_date': ['2024-01-01', '2024-01-15', '2024-02-01'],
        'product_id': [1001, 1002, 1001],
        'product_name': ['Product A', 'Product B', 'Product A'],
        'product_price': [10.0, 20.0, 10.0],
        'quantity': [1, 2, 3]
    }
    return pd.DataFrame(data)

def test_read_data():
    df = read_data('orders.csv')
    assert not df.empty

def test_compute_revenue_by_month(sample_data):
    revenue_by_month = compute_revenue_by_month(sample_data)
    assert not revenue_by_month.empty
    assert revenue_by_month.iloc[0]['total_revenue'] == 30.0

def test_compute_revenue_by_product(sample_data):
    revenue_by_product = compute_revenue_by_product(sample_data)
    assert not revenue_by_product.empty
    assert revenue_by_product.iloc[0]['total_revenue'] == 40.0

def test_compute_revenue_by_customer(sample_data):
    revenue_by_customer = compute_revenue_by_customer(sample_data)
    assert not revenue_by_customer.empty
    assert revenue_by_customer.iloc[0]['total_revenue'] == 40.0

def test_get_top_customers(sample_data):
    top_customers = get_top_customers(sample_data)
    assert len(top_customers) == 2
