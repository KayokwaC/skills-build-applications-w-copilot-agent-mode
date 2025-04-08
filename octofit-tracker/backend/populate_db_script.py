#!/usr/bin/env python3
"""
Script to populate the MongoDB database with test data for the octofit_tracker app.
This script directly uses pymongo to interact with the database rather than Django's ORM.
"""

import sys
from pymongo import MongoClient
import datetime
from bson import ObjectId

# Import test data from the test_data.py file
sys.path.append('/workspaces/skills-build-applications-w-copilot-agent-mode/octofit-tracker/backend')
from octofit_tracker.test_data import test_users, test_teams, test_activities, test_leaderboard, test_workouts

def connect_to_mongodb():
    """Connect to MongoDB and return the database object."""
    client = MongoClient('localhost', 27017)
    db = client['octofit_db']
    return db

def drop_collections(db):
    """Drop existing collections to start with a clean database."""
    collections = ['users', 'teams', 'activity', 'leaderboard', 'workouts']
    for collection in collections:
        if collection in db.list_collection_names():
            db[collection].drop()
            print(f"Dropped {collection} collection")

def populate_users(db):
    """Populate the users collection."""
    users_collection = db['users']
    for user in test_users:
        user['_id'] = ObjectId()  # Add an ObjectId for each user
        users_collection.insert_one(user)
    print(f"Inserted {len(test_users)} users")
    
    # Create a unique index on email
    users_collection.create_index("email", unique=True)
    print("Created unique index on email field")

def populate_teams(db):
    """Populate the teams collection."""
    teams_collection = db['teams']
    users_collection = db['users']
    
    for team_data in test_teams:
        # Find ObjectIds for team members based on their emails
        member_emails = team_data['members']
        member_ids = []
        for email in member_emails:
            user = users_collection.find_one({"email": email})
            if user:
                member_ids.append(user['_id'])
        
        # Create team document with member IDs
        team = {
            '_id': ObjectId(),
            'name': team_data['name'],
            'members': member_ids
        }
        teams_collection.insert_one(team)
    print(f"Inserted {len(test_teams)} teams")

def populate_activities(db):
    """Populate the activities collection."""
    activities_collection = db['activity']
    users_collection = db['users']
    
    for activity_data in test_activities:
        # Find user by email
        user = users_collection.find_one({"email": activity_data['user']})
        if user:
            # Create activity document
            activity = {
                '_id': ObjectId(),
                'user_id': user['_id'],
                'type': activity_data['type'],
                'duration': activity_data['duration'],
                'date': datetime.datetime.strptime(activity_data['date'], '%Y-%m-%d').date()
            }
            activities_collection.insert_one(activity)
    print(f"Inserted {len(test_activities)} activities")

def populate_leaderboard(db):
    """Populate the leaderboard collection."""
    leaderboard_collection = db['leaderboard']
    users_collection = db['users']
    
    for leaderboard_data in test_leaderboard:
        # Find user by email
        user = users_collection.find_one({"email": leaderboard_data['user']})
        if user:
            # Create leaderboard entry
            entry = {
                '_id': ObjectId(),
                'user_id': user['_id'],
                'score': leaderboard_data['score']
            }
            leaderboard_collection.insert_one(entry)
    print(f"Inserted {len(test_leaderboard)} leaderboard entries")

def populate_workouts(db):
    """Populate the workouts collection."""
    workouts_collection = db['workouts']
    
    for workout_data in test_workouts:
        # Create workout document
        workout = {
            '_id': ObjectId(),
            'name': workout_data['name'],
            'description': workout_data['description'],
            'duration': workout_data['duration']
        }
        workouts_collection.insert_one(workout)
    print(f"Inserted {len(test_workouts)} workouts")

def verify_data(db):
    """Verify the data was inserted correctly."""
    collections = ['users', 'teams', 'activity', 'leaderboard', 'workouts']
    for collection in collections:
        count = db[collection].count_documents({})
        print(f"Collection '{collection}' contains {count} documents")

def main():
    """Main function to execute the database population."""
    print("Connecting to MongoDB...")
    db = connect_to_mongodb()
    
    print("Dropping existing collections...")
    drop_collections(db)
    
    print("Populating collections...")
    populate_users(db)
    populate_teams(db)
    populate_activities(db)
    populate_leaderboard(db)
    populate_workouts(db)
    
    print("\nVerifying data...")
    verify_data(db)
    
    print("\nDatabase population completed successfully!")

if __name__ == "__main__":
    main()
