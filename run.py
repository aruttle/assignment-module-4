from app import create_app, db
from app.models import Project

app = create_app()

def seed_data():
    if Project.query.count() == 0:
        sample_projects = [
            Project(name="Project A", description="Description for Project A"),
            Project(name="Project B", description="Description for Project B"),
            Project(name="Project C", description="Description for Project C"),
        ]
        db.session.add_all(sample_projects)
        db.session.commit()
        print("Sample projects added!")
    else:
        print("Sample projects already exist.")

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        seed_data()
    app.run(debug=True)
