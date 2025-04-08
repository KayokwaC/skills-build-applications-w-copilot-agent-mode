import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from django.core.management.base import BaseCommand
from octofit_tracker.test_data import test_users, test_teams, test_activities, test_leaderboard, test_workouts
from django.conf import settings
from pymongo import MongoClient

class Command(BaseCommand):
    help = 'Populate the database with test data for users, teams, activities, leaderboard, and workouts'

    def handle(self, *args, **kwargs):
        # Connect to MongoDB
        client = MongoClient(settings.DATABASES['default']['HOST'], settings.DATABASES['default']['PORT'])
        db = client[settings.DATABASES['default']['NAME']]

        # Drop existing collections
        db.users.drop()
        db.teams.drop()
        db.activity.drop()
        db.leaderboard.drop()
        db.workouts.drop()

        # Populate users
        for user in test_users:
            db.users.insert_one(user)

        # Populate teams
        for team in test_teams:
            members = [db.users.find_one({"username": member})["_id"] for member in team["members"]]
            team["members"] = members
            db.teams.insert_one(team)

        # Populate activities
        for activity in test_activities:
            user_id = db.users.find_one({"username": activity["user"]})["_id"]
            activity["user"] = user_id
            db.activity.insert_one(activity)

        # Populate leaderboard
        for entry in test_leaderboard:
            user_id = db.users.find_one({"username": entry["user"]})["_id"]
            entry["user"] = user_id
            db.leaderboard.insert_one(entry)

        # Populate workouts
        for workout in test_workouts:
            db.workouts.insert_one(workout)

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with test data.'))
