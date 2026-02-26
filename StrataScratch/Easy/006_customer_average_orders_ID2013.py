"""
Platform: SS
Problem: Customer Average Orders
Difficulty: Easy
Concepts: nunique, mean
"""


import pandas as pd

result = pd.DataFrame({
    "users_count" : [postmates_orders['customer_id'].nunique()],
    "avg" : [postmates_orders['amount'].mean()]
})
