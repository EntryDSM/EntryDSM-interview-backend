from ysl.db import db


class Belong(db.Model):
    __tablename__ = 'BELOGN_TB'

    agency = db.Column(db.String(20), db.ForeignKey("AGENCY_TB.code"), primary_key=True)
    interviewer = db.Column(db.String(50), db.ForeignKey("INTERVIEWER_TB.email"), primary_key=True)
