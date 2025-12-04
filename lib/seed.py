#!/usr/bin/env python3

from faker import Faker
import random
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Game

fake = Faker()

if __name__ == '__main__':
    
    engine = create_engine('sqlite:///seed_db.db')
    Session = sessionmaker(bind=engine)
    session = Session()

    session.query(Game).delete()
    session.commit()

    botw = Game(title="Breath of the Wild", platform="Switch", genre="Adventure", price=60)
    ffvii = Game(title="Final Fantasy VII", platform="Playstation", genre="RPG", price=30)
    mk8 = Game(title="Mario Kart 8", platform="Switch", genre="Racing", price=50)
    smb = Game(title="Super Mario Bros", platform="NES", genre="Platformer", price=20)
    halo = Game(title="Halo", platform="Xbox", genre="Shooter", price=40)

platforms = ["Switch", "Xbox", "Playstation", "PC"]
genres = ["RPG", "Shooter", "Adventure", "Puzzle", "Strategy", "Racing"]

games = []

for _ in range(50):
    game = Game(
        title=fake.sentence(nb_words=3),
        platform=random.choice(platforms),
        genre=random.choice(genres),
        price=random.randint(10, 70)
    )
    games.append(game)

session.bulk_save_objects(games)
session.commit()