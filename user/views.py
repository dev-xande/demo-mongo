from rest_framework.views import APIView, Response
from .models import User
from bson.objectid import ObjectId

class UserView(APIView):
    def post(self, request):
        User.create(request.data)
        # del request.data['_id']
        request.data.update({"_id": str(request.data["_id"])})
        
        
        return Response(request.data, 201)

    def get(self, _):
        res = list(User.find())

        return Response({"data": res}, 200)


class UserDetailView(APIView):
    def patch(self, request, id):
        res = User.update(ObjectId(id), request.data)

        return Response(res, 200)

    def delete(self, _, id):
        User.delete(ObjectId(id))

        return Response(status=204)
