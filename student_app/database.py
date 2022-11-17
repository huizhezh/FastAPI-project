from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
SQLALCHEMY_DATABASE_URL = "sqlite:///./student_app.db"
# SQLALCHEMY_DATABASE_URL = "mysql://self_service:cmbjxccwtn@localhost/rd2pro"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

# if 0:   # for SQL lite
#     SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"
#     # SQLALCHEMY_DATABASE_URL = "mysql://self_service:cmbjxccwtn@localhost/rd2pro"
#
#     engine = create_engine(
#         SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
#     )
#
# if 1:   # for MySQL
#     SQLALCHEMY_DATABASE_URL = "mysql://self_service:cmbjxccwtn@localhost/rd2pro"
#     engine = create_engine(
#         SQLALCHEMY_DATABASE_URL
#     )

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()