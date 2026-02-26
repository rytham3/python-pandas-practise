"""
Platform: StrataScratch
Problem: Number of Comments Per User in 30 days before 2020-02-10
Difficulty: Easy
Concepts: to_datetime, timedelta, loc, groupby, sum
"""


import pandas as pd

# Define date window
end_date = pd.to_datetime('2020-02-10')
start_date = end_date - pd.Timedelta(days=30)

result = (
    fb_comments_count
    .loc[
        (fb_comments_count['created_at'] >= start_date) &
        (fb_comments_count['created_at'] <= end_date)
        ]
    .groupby(['user_id'],as_index=False)['number_of_comments']
    .sum()
    )
