from sqlalchemy import create_engine,ForeignKey,Integer,Float,String,DateTime
from sqlalchemy.orm import relationship,declarative_base,mapped_column,Mapped

Base = declarative_base()

class User(Base):
    __tablename__ ="users"
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(nullable=False)
    password: Mapped[str] = mapped_column(nullable=False)
    email: Mapped[str] = mapped_column(nullable=False,unique=True)
    

class UnpaidDept(Base):
    id: Mapped[int]