#!/usr/bin/env python3

from random import choice as rc
from faker import Faker
from app import app
from models import db, Message

fake = Faker()

# Generate a list of fake usernames
usernames = [fake.first_name() for i in range(4)]
if "Duane" not in usernames:
    usernames.append("Duane")

def make_messages():
    print("Seeding messages...")

    # Delete all existing messages
    Message.query.delete()
    
    # Generate new messages
    messages = []
    for i in range(20):
        message = Message(
            body=fake.sentence(),
            username=rc(usernames),
        )
        messages.append(message)

    # Add new messages to the database
    db.session.add_all(messages)
    db.session.commit()

    print("Seeding completed!")

if __name__ == '__main__':
    with app.app_context():
        make_messages()

