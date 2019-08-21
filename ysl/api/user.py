from flask import Blueprint, request, Response
from flask_restful import Resource, Api

from ysl.db.agency import Agency

bp_agency = Blueprint("agency", __name__, url_prefix="/api/agency")
api_agency = Api(bp_agency)


class AgencyCode(Resource):
    def get(self):
        agency_code = request.args.get('code')

        agency = Agency.query.filter_by(code=agency_code).first()

        if agency:
            return Response({"agency_name": agency.name,
                             "agency_explanation": agency.explanation}, 200)
        else:
            return Resource({
                "msg": "unseen agency"
            })


api_agency.add_resource(Agency, "/check")
