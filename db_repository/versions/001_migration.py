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
)

=======
>>>>>>> e23ef868c1dc12df73fec87ef01c2e9b9fb62e81

def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
<<<<<<< HEAD
    post_meta.tables['user'].create()
=======
>>>>>>> e23ef868c1dc12df73fec87ef01c2e9b9fb62e81


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
<<<<<<< HEAD
    post_meta.tables['user'].drop()
=======
>>>>>>> e23ef868c1dc12df73fec87ef01c2e9b9fb62e81
