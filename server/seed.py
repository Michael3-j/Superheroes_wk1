from models import db, Hero, Power, HeroPower
from faker import Faker
from random import choice
from app import app  # Ensure the Flask app is imported and configured

fake = Faker()

def seed_database():
    with app.app_context():
        print("Seeding database...")
        
        # Clear existing data
        db.session.query(HeroPower).delete()
        db.session.query(Power).delete()
        db.session.query(Hero).delete()
        db.session.commit()
        
        # Create Powers
        powers = [
            Power(name="Super Strength", description=fake.text(max_nb_chars=50)),
            Power(name="Flight", description=fake.text(max_nb_chars=50)),
            Power(name="Invisibility", description=fake.text(max_nb_chars=50)),
            Power(name="Telepathy", description=fake.text(max_nb_chars=50))
        ]
        db.session.add_all(powers)
        db.session.commit()
        
        # Create Heroes
        heroes = [
            Hero(name=fake.name(), alter_ego=fake.name()),
            Hero(name=fake.name(), alter_ego=fake.name()),
            Hero(name=fake.name(), alter_ego=fake.name())
        ]
        db.session.add_all(heroes)
        db.session.commit()
        
        # Assign Powers to Heroes
        strengths = ["Strong", "Weak", "Average"]
        for hero in heroes:
            for power in powers:
                if choice([True, False]):  # Randomly assign powers
                    hero_power = HeroPower(
                        hero_id=hero.id,
                        power_id=power.id,
                        strength=choice(strengths)
                    )
                    db.session.add(hero_power)
        
        db.session.commit()
        print("Database seeding complete!")

if __name__ == "__main__":
    seed_database()
