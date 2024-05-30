from sqlalchemy import create_engine, ForeignKey, Integer, Float, String, DateTime, Column
from sqlalchemy.orm import relationship, declarative_base, mapped_column, Mapped

Base = declarative_base()

class Users(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    username: Mapped[str] = mapped_column(String, nullable=False, unique=True)  # Don't allow the same account on the same username
    password: Mapped[str] = mapped_column(String, nullable=False)
    email: Mapped[str] = mapped_column(String, unique=True, nullable=False)  # Don't allow the same account on the same email
    phone_number: Mapped[str] = mapped_column(String, nullable=False)

    # Relationships
    unpaid_given_depts = relationship("UnpaidGivenDept", back_populates="giver_user")
    paid_given_depts = relationship("PaidGivenDept", back_populates="giver_user")
    unpaid_taken_depts = relationship("UnpaidTakenDept", back_populates="taker_user")
    paid_taken_depts = relationship("PaidTakenDept", back_populates="taker_user")

class UnpaidGivenDept(Base):
    __tablename__ = "unpaid_given_dept"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    giver: Mapped[int] = mapped_column(Integer, ForeignKey("users.id"))
    taker: Mapped[str] = mapped_column(String, nullable=False)
    amount: Mapped[int] = mapped_column(Integer, nullable=False)
    given_time: Mapped[DateTime] = mapped_column(DateTime, nullable=False)
    deadline: Mapped[DateTime] = mapped_column(DateTime, nullable=False)
    taker_phone_number: Mapped[str] = mapped_column(String, nullable=False)

    # Relationship
    giver_user = relationship("Users", back_populates="unpaid_given_depts")

class PaidGivenDept(Base):
    __tablename__ = "paid_given_dept"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    giver: Mapped[int] = mapped_column(Integer, ForeignKey("users.id"))
    taker: Mapped[str] = mapped_column(String, nullable=False)
    amount: Mapped[int] = mapped_column(Integer, nullable=False)
    given_time: Mapped[DateTime] = mapped_column(DateTime, nullable=False)
    pay_date: Mapped[DateTime] = mapped_column(DateTime, nullable=False)
    taker_phone_number: Mapped[str] = mapped_column(String, nullable=False)

    # Relationship
    giver_user = relationship("Users", back_populates="paid_given_depts")

class UnpaidTakenDept(Base):
    __tablename__ = "unpaid_taken_dept"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    taker: Mapped[int] = mapped_column(Integer, ForeignKey("users.id"))
    giver: Mapped[str] = mapped_column(String, nullable=False)
    amount: Mapped[int] = mapped_column(Integer, nullable=False)
    taken_time: Mapped[DateTime] = mapped_column(DateTime, nullable=False)
    deadline: Mapped[DateTime] = mapped_column(DateTime, nullable=False)
    giver_phone_number: Mapped[str] = mapped_column(String, nullable=False)

    # Relationship
    taker_user = relationship("Users", back_populates="unpaid_taken_depts")

class PaidTakenDept(Base):
    __tablename__ = "paid_taken_dept"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    taker: Mapped[int] = mapped_column(Integer, ForeignKey("users.id"))
    giver: Mapped[str] = mapped_column(String, nullable=False)
    amount: Mapped[int] = mapped_column(Integer, nullable=False)
    given_time: Mapped[DateTime] = mapped_column(DateTime, nullable=False)
    pay_date: Mapped[DateTime] = mapped_column(DateTime, nullable=False)
    giver_phone_number: Mapped[str] = mapped_column(String, nullable=False)

    # Relationship
    taker_user = relationship("Users", back_populates="paid_taken_depts")

