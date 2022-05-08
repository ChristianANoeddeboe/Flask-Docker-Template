# Database <!-- omit in toc -->

Author: Angercraft - 08/05/2022

<br/>

The database consists of a MySQL 8.0 database, setup with Docker compose.

The configuration for this can be seen in the docker-compose.prod.yml file, under `db`.

For the project, we're using Flask-SQLAlchemy (https://flask-sqlalchemy.palletsprojects.com/en/2.x/) which generates some of the boilerplate you usually would need to write yourself, to use it with Flask.

## Table of contents: <!-- omit in toc -->

1. [Initializing a database:](#initializing-a-database)
2. [Models:](#models)
3. [Making changes (Migrations)](#making-changes-migrations)
   1. [Applying changes (Upgrade database)](#applying-changes-upgrade-database)
   2. [Removing changes (Rollback database)](#removing-changes-rollback-database)
4. [FAQ In-depth:](#faq-in-depth)

---

<h2><center><b>PANIC FAQ</b></center></h2>

<center><h3><b>If you're in a hurry, read here!</b></h3></center>
<center>Please fill out with more questions/answer when new problems are found with solutions.</center>
<br/>

Q: I accidentially upgraded the database with a migration which deleted a table/column I did not mean to. Can I restore it along with the data?

A: No, migration files do not keep track of all the data in them. If you have a backup, you can recreate the data from that, but if not it is lost.

---

## Initializing a database:

I will not go through how to setup the code in the project, but in case the database is not even initialized, here is the command for initializing the database.

```
flask db init
```

This assumes you already have the logic in your code which calls `db.create_all()`. This project doesn't make use of it as the database already exists, so remember to include this in the code.

PLEASE CHECK THE DATABASE IS ACTUALLY EMPTY BEFORE YOU RUN `db.create_all()`. IT `WILL` DELETE EVERYTHING

All this should never be needed in this project, but if the database is lost for some insane reason and needs to be recreated, then here you go.

<br/>

## Models:

A model represents a table in the database. Below is the anatomy of a model.

```
#Enum used to force specific values to a column
class StatusEnum(enum.Enum):
    Init = 'Init'
    Good = 'Good'
    Bad = 'Bad'

#A model is always defined with a class, which extends the base Model class
class ExampleModel(db.Model):
    # The name of the table. This does not have to be the same as the model name
    __tablename__ = 'MODELS'

    # The columns in the table are created as seen below.
    # First column, which is also the private key of the table.
    id = db.Column(db.Integer(), primary_key=True, unique=True)
    # Every column will have a type defined, which will be used in the database.
    # These do not always follow the naming conventions of MySQL,
    # so make sure to check with the documentation before assigning a MySQL type to a column.
    name = db.Column(db.String(255), nullable=False)
    owner_id = db.Column(db.ForeignKey('COMPANIES.id'), nullable=False, index=True)
    author_id = db.Column(db.ForeignKey('USERS.id'), nullable=False, index=True)
    created = db.Column(db.DateTime(), nullable=False, server_default=func.now())
    version = db.Column(db.Integer(), nullable=False, server_default=db.text("'1'"))
    status = db.Column(db.Enum(StatusEnum), nullable=False, server_default="Init")
    model_file = db.Column(db.String(255), nullable=False)
    preview_image = db.Column(db.String(255))
    dim_x = db.Column(db.Float())
    dim_y = db.Column(db.Float())
    dim_z = db.Column(db.Float())
    volume = db.Column(db.Float())
    # Relationships are defined besides the foreign keys,
    # as this means the data from the relation will also be pulled when accessing this model/table entry.
    author = db.relationship('User')
    owner = db.relationship('Company')
```

<br/>

## Making changes (Migrations)

When the changes or new additions are made to the models, the database will not be updated to use these yet.

First we need to create a migration, which covers the changes required to add the new changes, but will also document the changes needed to rollback the structure of the database (though not data), in case something happens which requires a rollback.

Create new migration with

```
flask db migrate -m "Message"
```

When creating a migration, the new migration file will be placed in `{project folder}/migrations/versions/{id}_message.py` where the message is what you wrote after `-m` in the above command.

Please check this file thorougly, as it doesn't always detect what you actually want.

For example, renaming a model and table, will generate the migration where it deletes the old table, and creates a new. This means any data from the old table will not be transferred, but instead be lost.

### Applying changes (Upgrade database)

When the migration file is confirmed and you are sure you are ready the use the following command to apply the migration, which makes the changes to the database.

```
flask db upgrade
```

### Removing changes (Rollback database)

In case you wish to revert the database to an earlier state, you can use the following command.

Remember any data already in the columns or tables, which are removed, will be lost, and any columns or tables which are removed but then recreated with a rollback, will also be without data.

```
flask db downgrade
```

## FAQ In-depth:

Q: How to I rename a table, if the migration file will just destroy it?

A: Below is an example of renaming a table.

```
def upgrade():
    # Start by renaming the table
    op.rename_table("PARTS", "MODELS")
    # Then remove any constraints, mostly from foreign keys, as these should be reapplied.
    op.drop_constraint('part_author_id', 'MODELS', type_='foreignkey')
    # Good idea to drop their index as well.
    op.drop_index('ix_PARTS_author_id', table_name='MODELS')
    # Rename the columns pointing to the part_id, to instead point to model_id, as this makes more sense.
    op.alter_column('CONFIGURATIONS', 'part_id', new_column_name='model_id', existing_type=mysql.INTEGER(), nullable=False)
    # Recreate the foreign keys
    op.create_foreign_key('model_author_id', 'MODELS', 'USERS', ['author_id'], ['id'], ondelete='CASCADE')
    # Recreate the dropped index
    op.create_index(op.f('ix_MODELS_author_id'), 'MODELS', ['author_id'], unique=False)

def downgrade():
    # Downgrade will do almost the same as upgrade, but in the exact opposite way.
    # I'll include the code here, but will not comment on it.
    # ### commands auto generated by Alembic - please adjust! ###
    op.rename_table("MODELS", "PARTS")
    op.drop_constraint('model_author_id', 'PARTS', type_='foreignkey')
    op.alter_column('CONFIGURATIONS', 'model_id', new_column_name='part_id', existing_type=mysql.INTEGER(), nullable=False)
    op.create_foreign_key('part_author_id', 'PARTS', 'COMPANIES', ['owner_id'], ['id'], ondelete='CASCADE')
    op.create_index(op.f('ix_PARTS_author_id'), 'PARTS', ['author_id'], unique=False)
    op.drop_index('ix_MODELS_author_id', table_name='PARTS')
```
