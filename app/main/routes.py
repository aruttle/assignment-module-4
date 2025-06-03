from flask import render_template, request, redirect, url_for, flash
from datetime import datetime
from app.main import main
from app import db
from app.models import Guest, Accommodation, Booking, AccommodationType

@main.route('/')
def home():
    return render_template('home.html')

@main.route('/about')
def about():
    return render_template('about.html')

@main.route('/accommodations')
def accommodations():
    accommodations = Accommodation.query.all()
    return render_template('accommodations.html', accommodations=accommodations)

@main.route('/book', methods=['GET', 'POST'])
def book():
    accommodation_types = AccommodationType.query.all()
    accommodation_objects = Accommodation.query.all()

    accommodations = [
        {
            "id": acc.id,
            "name": acc.name,
            "type_id": acc.type_id
        }
        for acc in accommodation_objects
    ]

    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        accommodation_id = request.form.get('accommodation')
        start_date_str = request.form.get('start_date')
        end_date_str = request.form.get('end_date')

        if not all([name, email, accommodation_id, start_date_str, end_date_str]):
            flash('Please fill in all required fields.', 'danger')
            return redirect(url_for('main.book'))

        try:
            start_date = datetime.strptime(start_date_str, '%Y-%m-%d').date()
            end_date = datetime.strptime(end_date_str, '%Y-%m-%d').date()
        except ValueError:
            flash('Invalid date format.', 'danger')
            return redirect(url_for('main.book'))

        if start_date >= end_date:
            flash('End date must be after start date.', 'danger')
            return redirect(url_for('main.book'))

        # Check for overlapping bookings for selected accommodation
        existing_bookings = Booking.query.filter_by(accommodation_id=accommodation_id).all()
        for booking in existing_bookings:
            if not (end_date <= booking.start_date or start_date >= booking.end_date):
                flash('Selected accommodation is not available for those dates.', 'danger')
                return redirect(url_for('main.book'))

        # Save guest and booking
        guest = Guest.query.filter_by(email=email).first()
        if not guest:
            guest = Guest(name=name, email=email, phone=phone)
            db.session.add(guest)
            db.session.commit()

        booking = Booking(
            guest_id=guest.id,
            accommodation_id=accommodation_id,
            start_date=start_date,
            end_date=end_date
        )
        db.session.add(booking)
        db.session.commit()

        flash('Booking successful! Thank you.', 'success')
        return redirect(url_for('main.home'))

    # For GET request – build date ranges to disable in Flatpickr
    all_bookings = Booking.query.all()
    booked_ranges = [
        {
            "accommodation_id": b.accommodation_id,
            "start": b.start_date.strftime('%Y-%m-%d'),
            "end": b.end_date.strftime('%Y-%m-%d')
        }
        for b in all_bookings
    ]

    return render_template(
        'book.html',
        accommodation_types=accommodation_types,
        accommodations=accommodations,
        booked_ranges=booked_ranges
    )


