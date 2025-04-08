# Test data for populating the octofit_db database

test_users = [
    {"email": "thundergod@mhigh.edu", "name": "Thor", "age": 30},
    {"email": "metalgeek@mhigh.edu", "name": "Tony Stark", "age": 35},
    {"email": "zerocool@mhigh.edu", "name": "Steve Rogers", "age": 32},
    {"email": "crashoverride@mhigh.edu", "name": "Natasha Romanoff", "age": 28},
    {"email": "sleeptoken@mhigh.edu", "name": "Bruce Banner", "age": 40},
]

test_teams = [
    {"name": "Avengers", "members": ["thundergod@mhigh.edu", "metalgeek@mhigh.edu", "zerocool@mhigh.edu", "crashoverride@mhigh.edu", "sleeptoken@mhigh.edu"]},
]

test_activities = [
    {"user": "thundergod@mhigh.edu", "type": "Cycling", "duration": 60, "date": "2025-04-08"},
    {"user": "metalgeek@mhigh.edu", "type": "Crossfit", "duration": 120, "date": "2025-04-07"},
    {"user": "zerocool@mhigh.edu", "type": "Running", "duration": 90, "date": "2025-04-06"},
    {"user": "crashoverride@mhigh.edu", "type": "Strength", "duration": 30, "date": "2025-04-05"},
    {"user": "sleeptoken@mhigh.edu", "type": "Swimming", "duration": 75, "date": "2025-04-04"},
]

test_leaderboard = [
    {"user": "thundergod@mhigh.edu", "score": 100},
    {"user": "metalgeek@mhigh.edu", "score": 90},
    {"user": "zerocool@mhigh.edu", "score": 95},
    {"user": "crashoverride@mhigh.edu", "score": 85},
    {"user": "sleeptoken@mhigh.edu", "score": 80},
]

test_workouts = [
    {"name": "Cycling Training", "description": "Training for a road cycling event", "duration": 60},
    {"name": "Crossfit", "description": "Training for a crossfit competition", "duration": 120},
    {"name": "Running Training", "description": "Training for a marathon", "duration": 90},
    {"name": "Strength Training", "description": "Training for strength", "duration": 30},
    {"name": "Swimming Training", "description": "Training for a swimming competition", "duration": 75},
]
