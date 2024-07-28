import pandas as pd

def read_data(file_path):
    return pd.read_csv(file_path)

def compute_revenue_by_month(df):
    df['order_date'] = pd.to_datetime(df['order_date'])
    df['month'] = df['order_date'].dt.to_period('M')
    return df.groupby('month').apply(lambda x: (x['product_price'] * x['quantity']).sum())

def compute_revenue_by_product(df):
    return df.groupby('product_name').apply(lambda x: (x['product_price'] * x['quantity']).sum())

def compute_revenue_by_customer(df):
    return df.groupby('customer_id').apply(lambda x: (x['product_price'] * x['quantity']).sum())

def get_top_customers(customer_revenue, top_n=10):
    return customer_revenue.nlargest(top_n)

if __name__ == "__main__":
    df = read_data('orders.csv')
    monthly_revenue = compute_revenue_by_month(df)
    product_revenue = compute_revenue_by_product(df)
    customer_revenue = compute_revenue_by_customer(df)
    top_10_customers = get_top_customers(customer_revenue)

    print("Monthly Revenue:\n", monthly_revenue)
    print("\nProduct Revenue:\n", product_revenue)
    print("\nCustomer Revenue:\n", customer_revenue)
    print("\nTop 10 Customers:\n", top_10_customers)
