"""
Platform: StrataScratch 
Problem: Users Activity Per Month Day
Difficulty: Easy
Concepts: assign, groupby, agg, dt.month 
"""

result = (
    facebook_posts
    .assign(month=facebook_posts['post_date'].dt.month)
    .groupby('month', as_index=False)
    .agg(count_of_posts=('post_id','count'))
    
    )
