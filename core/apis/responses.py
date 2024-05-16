from flask import Response, jsonify, make_response


class APIResponse(Response):
    @classmethod
    def respond(cls, data,status=200):
        if(status==200):
            return make_response(jsonify(data=data))
        else :
            return make_response(jsonify(data=data),status)
