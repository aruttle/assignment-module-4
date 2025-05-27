from flask import Blueprint, render_template
from app.models import Booking

bp = Blueprint('booking', __name__)

@bp.route('/')
def home():
    bookings = Booking.query.all()
    return render_template('base.html', bookings=bookings)
