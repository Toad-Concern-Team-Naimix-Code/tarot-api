from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class MajorArcana(Base):
    __tablename__ = "major_arcana"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    description = Column(Text, nullable=False)
    relationship_interpretation = Column(Text, nullable=False)
    career_interpretation = Column(Text, nullable=False)

class TarotHRInsights(Base):
    __tablename__ = "tarot_hr_insights"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    description = Column(Text, nullable=False)
    workplace_relationship_interpretation = Column(Text, nullable=False)
    career_interpretation = Column(Text, nullable=False)
