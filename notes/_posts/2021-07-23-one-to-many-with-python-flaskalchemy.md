---
title: "How to model relationships with Flask-SQLAlchemy?"
description:
date: 2021-07-23
tags:
  - python
  - orm
  - flask
  - fullstack-engineering
layout: posts/default
published: false
---

<div class="column is-one-third">
    <aside class="menu">
        <p class="menu-label">
            Introduction
        </p>
        <ul class="menu-list">
            <li><a href='#what-is-an-orm'>What is an ORM?</a></li>
            <li><a href='#visualizing-relationships'>Visualizing Relationships</a></li>
        </ul>
         <p class="menu-label">
            Getting Started
        </p>
        <ul class="menu-list">
            <li><a href='#modelling'>Modeling with Flask SQLAlchemy</a></li>
            <li><a href='#one-to-one'>One to One</a></li>
            <li><a href='#one-to-many'>One to Many</a></li>
            <li><a href='#many-to-many'>Many to Many</a></li>
        </ul>
    </aside>
</div>
<div class="column">

<p>
Building APIs often requires encoding business concepts and processes. Object-oriented programming makes this easy and effcient by allowing developers to build rich, encapsulated business models. However, APIs often require dealing with databases, some of them being scalar and relational in nature - such as MySQL or Postgres. And that's where an ORM comes in.
</p>

<section class='section is-small'>

<h1>What is an ORM?</h1>
<a id='what-is-an-orm'></a>

<p>
An ORM is an Object Relational Mapper. The purpose of an ORM is to abstract away the underlying database and vendor-specific SQL queries, hence speeding up development.
</p>

<p>
For this tutorial, we'll be using [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/) (an extension for Flask that adds support for SQLAlchemy ORM)
</p>

</section>

<section class='section is-small'>

<h1>Visualizing Relationships</h1>
<a id='visualizing-relationships'></a>

<p>
While modelling a database, it is common to use an Entity Relationship Diagram, to visualize the different relationships between the tables.
</p>

<p>
Between entities, there can be different kinds of relationships,

- one-to-one: eg, person1<-partners->person2 i.e in a monogamous partnership, one partner can have a single partner and vice-versa
- one-to-many / many-to-one: eg, person-purchases->sales_order i.e a person can have many orders, but each order will have a single purchaser
- many-to-many: eg, book-author-person i.e a book may have multiple authors, and a person could have authored multiple books
</p>
</section>

<section class='section is-small'>
<h1>Modeling with Flask Alchemy</h1>
<a id='modeling'></a>

Let's take the Book-Author example and build different relationships between them,

<h2>One to One</h2>
<a id='one-to-one'></a>

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

<h2>One to Many / Many to One</h2>
<a id='one-to-many'></a>

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

<h2>Many to Many</h2>
<a id='many-to-many'></a>

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

</section>

<section class='section is-small'>

<h1>Key Highlights: Documention</h1>
<a id='higlights'></a>

[Documentation](https://flask-sqlalchemy.palletsprojects.com/en/2.x/models/#one-to-many-relationships)

Difference between the `relationship` function and specifying the `ForeignKey`

<quote>Relationships are expressed with the relationship() function. However the foreign key has to be separately declared with the ForeignKey class</quote>

What is the `relationship` function?

<quote> What does db.relationship() do? That function returns a new property that can do multiple things. In this case we told it to point to the Address class and load multiple of those. How does it know that this will return more than one address? Because SQLAlchemy guesses a useful default from your declaration. If you would want to have a one-to-one relationship you can pass uselist=False to relationship(). </quote>

What does `backref` mean?

<quote> backref is a simple way to also declare a new property on the Address class. You can then also use my_address.person to get to the person at that address. `back_populates` is unidirectional, whereas `backref` is bidirectional </quote>

What does `lazy` mean?

<quote>lazy defines when SQLAlchemy will load the data from the database:</quote>

</section>
</div>
