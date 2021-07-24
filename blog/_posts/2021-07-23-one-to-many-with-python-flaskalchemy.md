---
published: false
title: "[tutorial] Modeling Relationships with Flask-SQLAlchemy"
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

Building APIs often requires encoding business concepts and processes. Object-oriented programming makes this easy and effcient by allowing developers to build rich, encapsulated business models. However, APIs often require dealing with databases, some of them being scalar and relational in nature - such as MySQL or PostGres. And that's where an ORM comes in.

# What is an ORM?

An ORM is an Object Relational Mapper. The purpose of an ORM is to abstract away the underlying database and vendor-specific queries from the developer, hence speeding up development.

For this tutorial, we'll be using [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/) (an extension for Flask that adds support for SQLAlchemy ORM)

# Visualizing Relationships

While modelling a database, it is common to use an Entity Relationship Diagram, to visualize the different relationships between the tables.

Between entities, there can be three types of relationships,
- one-to-one: eg, person1<---partners--->person2 i.e in a monogamous partnership, one partner can have a single partner and vice-versa
- one-to-many: eg, person---purchases--->sales_order i.e a person can add many order, but each order will have a single purchaser
- many-to-one: eg,
- many-to-many: eg, book---author---person i.e a book may have multiple authors, and a person could have authored multiple books

# Modelling with Flask-SQLAlchemy

Let's take the Book-Author example and build different relationships between them,

## One-to-One

```python
class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ## uselist ensure one-to-one
    book = relationship("Book", uselist=False, backref="author")

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ## add author_id as a foreign key
    author_id = db.Column(db.Integer, ForeignKey('author.id'))
```


## One-to-Many

> Relationships are expressed with the relationship() function. However the foreign key has to be separately declared with the ForeignKey class:

> What does db.relationship() do? That function returns a new property that can do multiple things. In this case we told it to point to the Address class and load multiple of those. How does it know that this will return more than one address? Because SQLAlchemy guesses a useful default from your declaration. If you would want to have a one-to-one relationship you can pass uselist=False to relationship().

>So what do backref and lazy mean? backref is a simple way to also declare a new property on the Address class. You can then also use my_address.person to get to the person at that address.

> lazy defines when SQLAlchemy will load the data from the database:

```python
class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True)

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    author = relationship("Author", back_populates="books")
```

## Many-to-One

```python
class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    books = relationship("Book",
                    secondary=association_table,
                    backref="authors")

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
```


## Many-to-Many

Many to many is done by adding an association table between classes. The association table is denoted by the `secondary` argument.

> When using the relationship.backref parameter instead of relationship.back_populates, the backref will automatically use the same relationship.secondary argument for the reverse relationship

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

Difference between `back_ref` and `back_populates`