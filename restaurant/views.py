from django.shortcuts import render



# Create your views here.
def index(request):
    return render(request, 'index.html', {})



# class menuview(APIView):
#     def post(self,request):
#         serializer = menuSerializer(data=request.data)

#         if serializer.is_valid():
#             serializer.save()
#             return Response({"status":"success" , "data":serializer.data})