"""
Platform: SS 
Problem: April & May Sign Up's
Difficulty: Easy
Concepts: dt.month, isin, drop_duplicates
"""


result = (
    transactions[transactions['transaction_start_date'].dt.month.isin([4,5])]
        [['signup_id']]
        .drop_duplicates()
    
    )
