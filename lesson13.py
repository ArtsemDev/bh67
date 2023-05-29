from datetime import datetime

from sqlalchemy import Column, INT, VARCHAR, TIMESTAMP, ForeignKey, TEXT, BOOLEAN, create_engine, DECIMAL
from sqlalchemy.orm import DeclarativeBase, declared_attr, sessionmaker
from sqlalchemy.exc import IntegrityError


class Base(DeclarativeBase):

    id = Column(INT, primary_key=True)

    engine = create_engine('postgresql://belhard:belhard@0.0.0.0:5432/belhard')
    session = sessionmaker(bind=engine)

    @declared_attr
    def __tablename__(cls):
        return ''.join(f'_{i.lower()}' if i.isupper() else i for i in cls.__name__).strip('_')


class Category(Base):
    name = Column(VARCHAR(64), unique=True, nullable=False, index=True)


class Post(Base):
    title = Column(VARCHAR(128), nullable=False)
    description = Column(TEXT, nullable=False)
    date_publish = Column(TIMESTAMP, default=datetime.now())
    category_id = Column(INT, ForeignKey('category.id', ondelete='CASCADE'), nullable=False)
    is_published = Column(BOOLEAN, default=False)

# with Category.session() as session:
#     categories = [
#         Category(name='Finance'),
#         Category(name='Sport'),
#     ]
#     session.add_all(categories)
#     try:
#         session.commit()
#     except IntegrityError:
#         pass
#     for category in categories:
#         session.refresh(category)
#
#     for category in categories:
#         print(category.id, category.name)

# with Category.session() as session:
#     category_1 = session.get(Category, 1)
#     print(category_1.id, category_1.name)
    # category_1.name = 'Politics'
    # session.add(category_1)
    # session.commit()
