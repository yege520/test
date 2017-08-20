from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
<<<<<<< HEAD
user = Table('user', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('nickname', String(length=64)),
    Column('email', String(length=120)),
    Column('role', SmallInteger, default=ColumnDefault(0)),
    Column('about_me', String(length=140)),
    Column('last_seen', DateTime),
=======
post = Table('post', pre_meta,
    Column('id', INTEGER, primary_key=True, nullable=False),
    Column('body', VARCHAR(length=140)),
    Column('timestamp', DATETIME),
    Column('user_id', INTEGER),
)

user = Table('user', pre_meta,
    Column('id', INTEGER, primary_key=True, nullable=False),
    Column('nickname', VARCHAR(length=64)),
    Column('email', VARCHAR(length=120)),
>>>>>>> e23ef868c1dc12df73fec87ef01c2e9b9fb62e81
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
<<<<<<< HEAD
    post_meta.tables['user'].columns['about_me'].create()
    post_meta.tables['user'].columns['last_seen'].create()
=======
    pre_meta.tables['post'].drop()
    pre_meta.tables['user'].drop()
>>>>>>> e23ef868c1dc12df73fec87ef01c2e9b9fb62e81


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
<<<<<<< HEAD
    post_meta.tables['user'].columns['about_me'].drop()
    post_meta.tables['user'].columns['last_seen'].drop()
=======
    pre_meta.tables['post'].create()
    pre_meta.tables['user'].create()
>>>>>>> e23ef868c1dc12df73fec87ef01c2e9b9fb62e81
