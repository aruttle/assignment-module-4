from app import db  # Import the single shared db instance

class Guest(db.Model):
    __tablename__ = 'guests'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    phone = db.Column(db.String(20), nullable=True)

    bookings = db.relationship('Booking', backref='guest', lazy=True)

class Accommodation(db.Model):
    __tablename__ = 'accommodations'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=True)
    price_per_night = db.Column(db.Float, nullable=False)

    bookings = db.relationship('Booking', backref='accommodation', lazy=True)

class Booking(db.Model):
    __tablename__ = 'bookings'
    id = db.Column(db.Integer, primary_key=True)
    guest_id = db.Column(db.Integer, db.ForeignKey('guests.id'), nullable=False)
    accommodation_id = db.Column(db.Integer, db.ForeignKey('accommodations.id'), nullable=False)
    start_date = db.Column(db.Date, nullable=False)
    end_date = db.Column(db.Date, nullable=False)
