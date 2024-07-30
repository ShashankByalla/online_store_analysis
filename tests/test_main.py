import sys
import os
import pytest
import pandas as pd

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from main import read_data, compute_revenue_by_month, compute_revenue_by_product, compute_revenue_by_customer, get_top_customers

@pytest.fixture
def sample_data():
    data = {
        'order_id': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        'customer_id': [101, 102, 101, 103, 104, 101, 102, 105, 106, 107],
        'order_date': pd.to_datetime([
            '2024-01-01', '2024-01-15', '2024-02-01', '2024-02-10',
            '2024-03-05', '2024-03-15', '2024-04-20', '2024-04-25',
            '2024-05-01', '2024-05-15'
        ]),
        'product_id': [1001, 1002, 1001, 1003, 1004, 1001, 1002, 1005, 1006, 1007],
        'product_name': [
            'Product A', 'Product B', 'Product A', 'Product C',
            'Product D', 'Product A', 'Product B', 'Product E',
            'Product F', 'Product G'
        ],
        'product_price': [10.0, 20.0, 10.0, 15.0, 25.0, 10.0, 20.0, 30.0, 35.0, 40.0],
        'quantity': [1, 2, 3, 1, 4, 2, 1, 5, 1, 2]
    }
    return pd.DataFrame(data)

def test_compute_revenue_by_month(sample_data):
    monthly_revenue = compute_revenue_by_month(sample_data)
    assert not monthly_revenue.empty, "Monthly revenue calculation failed."

def test_compute_revenue_by_product(sample_data):
    product_revenue = compute_revenue_by_product(sample_data)
    assert not product_revenue.empty, "Product revenue calculation failed."

def test_compute_revenue_by_customer(sample_data):
    customer_revenue = compute_revenue_by_customer(sample_data)
    assert not customer_revenue.empty, "Customer revenue calculation failed."

def test_get_top_customers(sample_data):
    customer_revenue = compute_revenue_by_customer(sample_data)
    top_10_customers = get_top_customers(customer_revenue)
    assert len(top_10_customers) <= 10, "Top 10 customers calculation failed."
