"""Models and database functions for Ratings project."""

from flask_sqlalchemy import SQLAlchemy

# Here's where we create the idea of our database. We're getting this through
# the Flask-SQLAlchemy library. On db, we can find the `session`
# object, where we do most of our interactions (like committing, etc.)

db = SQLAlchemy()


##############################################################################
# Part 1: Compose ORM
# Using SQLAlchemy, fill in the columns for the classes already defined in
# model.py. The column names and datatypes should be the same as those in the
# cars database. (Since you already have tables, there is no need to run the
# command db.create_all() at any point during this assignment.)

# Be sure to include a relationship between the two tables, using a foreign keys
# between the two tables.

# Helper commands

# To open the database: psql cars
# To see a list of the tables: \dt (must be inside psql)
# To inspect the schema for each table: \d TABLENAME (must be inside psql)
# Hint

# You will know if you have the right answer if you can run the interactive
# python terminal in model.py and the only output you see is:
# Connected to DB



class Model(db.Model):
    """Car model.
    NOTE: I renamed the primary key column in the database because naming a
    field id is like asking for the clowns to eat me in my sleep"""

    __tablename__ = "models"
    # Let's rename this poorly named business
    model_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    year = db.Column(db.Integer, nullable=False)
    brand_name = db.Column(db.String(50), db.ForeignKey('brands.name'))
    name = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return "<Model model_id={} year={} brand_name={} name={}>".format(
                   self.model_id, self.year, self.brand_name, self.name)



class Brand(db.Model):
    """Car brand.
    NOTE: I renamed the primary key column in the database because naming a
    field id is like asking for the clowns to eat me in my sleep"""

    __tablename__ = "brands"
    brand_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False)
    founded = db.Column(db.Integer)
    headquarters = db.Column(db.String(50))
    discontinued = db.Column(db.Integer)

    # Define relationship to Model and backreference
    models = db.relationship("Model", backref="brand")

    def __repr__(self):
        return "<Brand brand_id={} name={} founded={} headquarters={} discontinued={}>".format(
                    self.brand_id, self.name, self.founded, self.headquarters, self.discontinued)

# Tests for relationship bridges - copying and pasting here for my reference later
'''
brands = Brand.query.all()
a_brand = brands[5]
print a_brand.models[0].year

models = Model.query.all()
a_model = models[5]
print a_model.brand.headquarters
'''

# End Part 1


##############################################################################
# Helper functions

def init_app():
    # So that we can use Flask-SQLAlchemy, we'll make a Flask app
    from flask import Flask
    app = Flask(__name__)

    connect_to_db(app)
    print "Connected to DB."


def connect_to_db(app):
    """Connect the database to our Flask app."""

    # Configure to use our database
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres:///cars'
    app.config['SQLALCHEMY_ECHO'] = True
    db.app = app
    db.init_app(app)


if __name__ == "__main__":
    # As a convenience, if we run this module interactively, it will leave
    # you in a state of being able to work with the database directly.

    # So that we can use Flask-SQLAlchemy, we'll make a Flask app
    from flask import Flask

    app = Flask(__name__)

    connect_to_db(app)
    print "Connected to DB."
