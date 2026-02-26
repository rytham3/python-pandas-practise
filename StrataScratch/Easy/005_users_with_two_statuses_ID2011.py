"""
Platform: SS 
Problem: Users With Two Statuses
Difficulty: Easy
Concepts: isin, groupby, nunique, reset_index, query
"""

result = (
    twitch_sessions[twitch_sessions['session_type'].isin(['viewer','streamer'])]
    .groupby('user_id')['session_type']
    .nunique()
    .reset_index(name='type_count')
    .query('type_count == 2')[['user_id']]
    )
