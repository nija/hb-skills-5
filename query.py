"""
This file is the place to write solutions for the
skills assignment called skills-sqlalchemy. Remember to
consult the exercise directions for more complete
explanations of the assignment.

All classes from model.py are being imported for you
here, so feel free to refer to classes without the
[model.]User prefix.
"""

from model import *

init_app()

# -------------------------------------------------------------------
# Part 2: Write queries


def get_brand_id_8():
    '''
    Get the brand with the **id** of 8.
    Use SQLAlchemy's .get(), not .filter() nor .filter_by().
    '''
    return Brand.query.get(8)


def get_all_model_name_brand_name():
    '''
    Get all models with the **name** Corvette and the **brand_name** 
    Chevrolet.
    '''
    return Model.query.filter_by(name='Corvette').all()


def get_all_models_1960_older():
    '''
    Get all models that are older than 1960.
    '''
    return Model.query.filter(Model.year>1960).all()


def get_brands_after_1920():
    '''
    Get all brands that were founded after 1920.
    '''
    return Brand.query.filter(Brand.founded > 1920).all()


def get_models_begining_with_Cor():
    '''
    Get all models with names that begin with "Cor".
    '''
    return Model.query.filter(Model.name.like('Cor%')).all()


def get_all_live_brands_after_1903():
    '''
    Get all brands that were founded in 1903 and that are not yet 
    discontinued.
    '''
    return Brand.query.filter(Brand.founded == 1903, Brand.discontinued.is_(None)).all()


def get_all_dead_brands_or_before_1950():
    '''
    Get all brands that are either 1) discontinued (at any time) or 
    2) founded before 1950.
    '''
    return Brand.query.filter((Brand.founded == 1903) | (Brand.discontinued.isnot(None))).all()


def get_all_models_not_Chevrolet():
    '''
    Get any model whose brand_name is not Chevrolet.
    '''
    return Model.query.filter(~ (Model.brand_name == 'Chevrolet')).all()


# Fill in the following functions. 
# 1. Fill in get_model_info so that it takes a year as input, and prints each
#    model's name, brand_name and brand headquarters for each car model from
#    that year.
# 2. Fill in get_brands_summary so that it takes nothing as input and prints
#    each brand name, and all of that brand's models. (Feel free to format with
#    newlines (\n) and/or tabs (\t) to create helpful and readable output.)
# To open an interactive terminal in order to test queries: python -i model.py

def get_model_info(year):
    '''
    Takes in a year, and prints out each model, brand_name, and
    brand headquarters for that year using only ONE database query.
    '''
    return db.session.query(Model.name, Model.brand_name, Brand.headquarters).join(Brand).filter(Model.year == year)


def get_brands_summary():
    '''
    Prints out each brand name, and each model name for that
    brand using only ONE database query.
    '''
    return Model.query.options(db.joinedload('brand')).order_by(Model.brand_name, Model.name).all()


# -------------------------------------------------------------------
# Part 2.5: Discussion Questions (Include your answers as comments.)

# 1. What is the returned value and datatype of 
#    ``Brand.query.filter_by(name='Ford')``?
'''
The returned value (what gets executed when the query is called) is:
SELECT brands.brand_id AS brands_brand_id, brands.name AS brands_name, brands.founded AS brands_founded, brands.headquarters AS brands_headquarters, brands.discontinued AS brands_discontinued
FROM brands
WHERE brands.name = :name_1

The datatype is <class 'flask_sqlalchemy.BaseQuery'>, which is a query object.
'''

# 2. In your own words, what is an association table, and what *type* of
#    relationship does an association table manage?
'''
An association table is a table which references the primary keys in two or more
tables. An association table manages many-to-many relationships.
'''
# -------------------------------------------------------------------
# Part 3
# Please compose the following python functions and add them to query.py.

# 1. Design a function in python that takes in any string as parameter, and
# returns a list of objects that are brands whose name contains or is equal
# to the input string.
# 2. Design a function that takes in a start year and end year (two integers),
# and returns a list of objects that are models with years that fall between
# the start year (inclusive) and end year (exclusive).

def search_brands_by_name(mystr):
    '''
    Design a function in python that takes in any string as parameter, and
    returns a list of objects that are brands whose name contains or is equal
    to the input string.
    '''
    return Brand.query.filter(Brand.name.like('%' + mystr + '%'))


def get_models_between(start_year, end_year):
    '''
    Design a function that takes in a start year and end year (two integers),
    and returns a list of objects that are models with years that fall between
    the start year (inclusive) and end year (exclusive).
    '''
    return Model.query.filter(Model.year >= start_year, Model.year < end_year).all()

