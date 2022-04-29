from flask_sqlalchemy import SQLAlchemy
from settings import *
import json

db = SQLAlchemy(app)

class Demand(db.Model):
    __tablename__ = 'demands'
    id = db.Column(db.Integer, primary_key=True)
    company_name = db.Column(db.String(80), nullable=False)
    applicant_names = db.Column(db.String(80), nullable=False)
    phone_number = db.Column(db.String(80), nullable=False)
    company_email = db.Column(db.String(80), unique=True, nullable=False)
    solution_type = db.Column(db.String(80), nullable=False)
    reffered_by = db.Column(db.String(80), nullable=True)
    additional_comments = db.Column(db.String(80), nullable=True)

    
    def json(self):
        return {
            'id': self.id,
            'company_name': self.company_name,
            'applicant_names': self.applicant_names,
            'phone_number': self.phone_number,
            'company_email': self.company_email,
            'solution_type': self.solution_type,
            'reffered_by': self.reffered_by,
            'additional_comments': self.additional_comments
        }
    
    def add_demand(company_name, applicant_names, phone_number, company_email, solution_type, reffered_by, additional_comments):
        demand = Demand(company_name=company_name, applicant_names=applicant_names, phone_number=phone_number, company_email=company_email, solution_type=solution_type, reffered_by=reffered_by, additional_comments=additional_comments)
        db.session.add(demand)
        db.session.commit()

    def get_all_demands():
        return [Demand.json(demand) for demand in Demand.query.all()]

    def get_demand(id):
        return [Demand.json(Demand.query.filter_by(id=id).first())]

    def update_demand(id, company_name, applicant_names, phone_number, company_email, solution_type, reffered_by, additional_comments):
        demand = Demand.query.filter_by(id=id).first()
        demand.company_name = company_name
        demand.applicant_names = applicant_names
        demand.phone_number = phone_number
        demand.company_email = company_email
        demand.solution_type = solution_type
        demand.reffered_by = reffered_by
        demand.additional_comments = additional_comments
        db.session.commit()

    def delete_demand(id):
        demand = Demand.query.filter_by(id=id).first()
        db.session.delete(demand)
        db.session.commit()