import pandas as pd

def compute_revenue_by_month(df):
    df['month'] = df['order_date'].dt.to_period('M')
    return df.groupby('month')['product_price', 'quantity'].apply(lambda x: (x['product_price'] * x['quantity']).sum()).reset_index(name='revenue').set_index('month')['revenue']

def compute_revenue_by_product(df):
    return df.groupby('product_name', group_keys=False).apply(lambda x: (x['product_price'] * x['quantity']).sum()).reset_index(name='revenue').set_index('product_name')['revenue']

def compute_revenue_by_customer(df):
    return df.groupby('customer_id', group_keys=False).apply(lambda x: (x['product_price'] * x['quantity']).sum()).reset_index(name='revenue').set_index('customer_id')['revenue']
