"""
Platform: StrataScratch
Problem: Submission Types
Difficulty: Easy
Concepts: isin, groupby, nunique
"""

result = (
    loans[loans['type'].isin(['Refinance','InSchool'])]
    .groupby(['user_id'])['type']
    .nunique()
    .reset_index()
    .query('type==2')[['user_id']]
    )
