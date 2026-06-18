from datetime import datetime
from flask import Flask, render_template_string
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

# ==========================================
# 1. DATABASE SETUP (Your Original Core Code)
# ==========================================
Base = declarative_base()

class Zone(Base):
    __tablename__ = 'zones'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    risk_level = Column(String, nullable=False)
    fire_risk_score = Column(Integer, nullable=False)

# We use a file 'wildfire.db' instead of ':memory:' so the website can read it
engine = create_engine('sqlite:///wildfire.db', echo=True)
print("⏳ Starting up our mini testing environment...")
Base.metadata.create_all(engine)
print("✅ Success! Your database table structure was generated smoothly.")

Session = sessionmaker(bind=engine)
session = Session()

# Only add the test zone if it doesn't exist yet to avoid duplicate rows
if not session.query(Zone).filter_by(name="Hills & Foothills").first():
    test_zone = Zone(name="Hills & Foothills", risk_level="High", fire_risk_score=88)
    session.add(test_zone)
    session.commit()
    print(f"Created row entry inside database: {test_zone.name} with score {test_zone.fire_risk_score}!")
session.close()

# ==========================================
# 2. WEB SERVER SETUP (The Visible Website)
# ==========================================
app = Flask(__name__)

@app.route('/')
def home_page():
    # Fetch the zone data from the database to display it
    db_session = Session()
    zone_data = db_session.query(Zone).filter_by(name="Hills & Foothills").first()
    db_session.close()
    
    # Visual look of the website
    html_layout = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Wildfire Risk Dashboard</title>
        <style>
            body {{ font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background-color: #f7f9fc; color: #333; margin: 0; padding: 40px; display: flex; justify-content: center; }}
            .card {{ background: white; padding: 30px; border-radius: 12px; box-shadow: 0 4px 15px rgba(0,0,0,0.05); text-align: center; max-width: 400px; width: 100%; border-top: 5px solid #ff4d4d; }}
            h1 {{ color: #d9383a; margin-bottom: 5px; font-size: 24px; }}
            .date {{ color: #888; font-size: 12px; margin-bottom: 25px; }}
            .info-group {{ margin: 15px 0; text-align: left; background: #fdfdfd; padding: 10px 15px; border-left: 3px solid #ff9900; }}
            .label {{ font-size: 12px; text-transform: uppercase; color: #777; font-weight: bold; }}
            .value {{ font-size: 18px; color: #222; margin-top: 2px; }}
            .score-badge {{ background: #fff5f5; color: #e53e3e; font-size: 32px; font-weight: bold; padding: 15px; border-radius: 8px; margin-top: 20px; border: 1px dashed #feb2b2; }}
        </style>
    </head>
    <body>
        <div class="card">
            <h1>🔥 Wildfire Risk Dashboard</h1>
            <div class="date">System Live Status</div>
            
            <div class="info-group">
                <div class="label">Region / Zone Name</div>
                <div class="value">{zone_data.name}</div>
            </div>
            
            <div class="info-group" style="border-left-color: #e53e3e;">
                <div class="label">Threat Level</div>
                <div class="value">{zone_data.risk_level} Risk</div>
            </div>
            
            <div class="score-badge">
                {zone_data.fire_risk_score} <span style="font-size: 16px; color: #777;">/ 100</span>
            </div>
        </div>
    </body>
    </html>
    """
    return render_template_string(html_layout)

if __name__ == "__main__":
    # Start the web server
    app.run(debug=True)
