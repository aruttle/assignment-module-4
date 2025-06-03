from app import db, create_app
from app.models import AccommodationType, Accommodation

app = create_app()

with app.app_context():
    db.drop_all()
    db.create_all()

    # Seed accommodation types
    types = ['Cabin', 'Yurt', 'Treehouse']
    accommodation_types = []
    for type_name in types:
        atype = AccommodationType(name=type_name)
        db.session.add(atype)
        accommodation_types.append(atype)
    
    db.session.commit()

    # Seed accommodations with reference to types
    accommodations = [
        {'name': 'Cozy Cabin #1', 'description': 'A warm, wooden cabin', 'price_per_night': 120.0, 'type_name': 'Cabin'},
        {'name': 'Forest Yurt', 'description': 'A spacious yurt in the forest', 'price_per_night': 150.0, 'type_name': 'Yurt'},
        {'name': 'Sky Treehouse', 'description': 'A treehouse with great views', 'price_per_night': 200.0, 'type_name': 'Treehouse'},
        {'name': 'Lakeside Cabin', 'description': 'Cabin by the lake', 'price_per_night': 130.0, 'type_name': 'Cabin'},
    ]

    for acc in accommodations:
        # find type id from seeded types
        atype = AccommodationType.query.filter_by(name=acc['type_name']).first()
        if atype:
            accommodation = Accommodation(
                name=acc['name'],
                description=acc['description'],
                price_per_night=acc['price_per_night'],
                type_id=atype.id
            )
            db.session.add(accommodation)

    db.session.commit()
    print("Database initialized and seeded with accommodation types and accommodations.")
