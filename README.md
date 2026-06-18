from datetime import datetime
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker


Base = declarative_base()


class Zone(Base):
    __tablename__ = 'zones'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    risk_level = Column(String, nullable=False)
    fire_risk_score = Column(Integer, nullable=False)


if __name__ == "__main__":
    engine = create_engine('sqlite:///:memory:', echo=True)
    print("⏳ Starting up our mini testing environment...")
    Base.metadata.create_all(engine)
    print("✅ Success! Your database table structure was generated smoothly.")
    Session = sessionmaker(bind=engine)
    session = Session()
    test_zone = Zone(name="Hills & Foothills", risk_level="High", fire_risk_score=88)
    session.add(test_zone)
    session.commit()
    print(f"Created row entry inside database: {test_zone.name} with score {test_zone.fire_risk_score}!")
