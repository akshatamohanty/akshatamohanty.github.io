---
title: "Modeling Relationships with Flask-SQLAlchemy"
summary:
date:  2021-07-23
image:
credits:
tags:
 - python
 - orm
 - flask
 - SQLAlchemy
---

Building APIs often requires encoding business concepts and processes. Object-oriented programming makes this easy and effcient by allowing developers to build rich, encapsulated business models. However, APIs often require dealing with databases, some of them being scalar and relational in nature - such as MySQL or Postgres. And that's where an ORM comes in.

# What is an ORM?

An ORM is an Object Relational Mapper. The purpose of an ORM is to abstract away the underlying database and vendor-specific SQL queries, hence speeding up development.

For this tutorial, we'll be using [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/) (an extension for Flask that adds support for SQLAlchemy ORM)

# Visualizing Relationships

While modelling a database, it is common to use an Entity Relationship Diagram, to visualize the different relationships between the tables.

Between entities, there can be different kinds of relationships,
- one-to-one: eg, person1<-partners->person2 i.e in a monogamous partnership, one partner can have a single partner and vice-versa
- one-to-many / many-to-one: eg, person-purchases->sales_order i.e a person can have many orders, but each order will have a single purchaser
- many-to-many: eg, book-author-person i.e a book may have multiple authors, and a person could have authored multiple books

# Modelling with Flask-SQLAlchemy

Let's take the Book-Author example and build different relationships between them,

### One-to-One

```python
class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    book = relationship("Book", back_populates="author", useList=False)

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ## add author_id as a foreign key
    author_id = db.Column(db.Integer, ForeignKey('author.id'))
```

In `Book`, there's only one thing required,

- defining the `ForeignKey`

Properties in `book`,
- id
- author_id
- author (back populated)

In `Author`, there are 3 things happening,

- `relationship` function returns a function that can load `book` instances for the property
- `useList=False` ensures that only a single `Book` instance is expected and loaded, hence conslidating the one-to-one relationship
- `back_populates='author'` back populates `book.author` in the `Book` instance

Properties in `author`,
- id
- book
## One-to-Many // Many-to-One

The above one-to-one mapping can be easily converted to a one-to-many relationship by removing the `useList=False`

```python
class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    books = relationship("Book", back_populates="author")

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ## add author_id as a foreign key
    author_id = db.Column(db.Integer, ForeignKey('author.id'))
```

In `Book`, there's only one thing required,

- defining the `ForeignKey`

Properties in `book`,
- id
- author_id
- author (back populated)


In `Author`, there are 3 things happening,

- `relationship` function returns a function that can load `book` instances for the property
- removing `useList=True` allows for loading multiple book instances, hence conslidating the many-to-one relationship
- `back_populates='author'` back populates `book.author` in the `Book` instances

Properties in `author`,
- id
- books (an array)

## Many-to-many
Many to many is done by adding an association table between classes. The association table is denoted by the `secondary` argument.
The `backref` parameter automatically uses the same relationship.secondary argument for the reverse relationship.


```python
association_table = Table('association', Base.metadata,
    Column('author', ForeignKey('author.id'), primary_key=True),
    Column('book', ForeignKey('book.id'), primary_key=True)
)

class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    books = relationship("Book",
                    secondary=association_table,
                    backref="authors")

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
```

Properites in `author`,
- id
- books

Properties in `book`
- id
- authors (backpopulated)

## Some Key Points from the documentation

[Documentation](https://flask-sqlalchemy.palletsprojects.com/en/2.x/models/#one-to-many-relationships)

Difference between the `relationship` function and specifying the `ForeignKey`
> Relationships are expressed with the relationship() function. However the foreign key has to be separately declared with the ForeignKey class

What is the `relationship` function?
> What does db.relationship() do? That function returns a new property that can do multiple things. In this case we told it to point to the Address class and load multiple of those. How does it know that this will return more than one address? Because SQLAlchemy guesses a useful default from your declaration. If you would want to have a one-to-one relationship you can pass uselist=False to relationship().

What does `backref` mean?
> backref is a simple way to also declare a new property on the Address class. You can then also use my_address.person to get to the person at that address. `back_populates` is unidirectional, whereas `backref` is bidirectional

What does `lazy` mean?
> lazy defines when SQLAlchemy will load the data from the database:
