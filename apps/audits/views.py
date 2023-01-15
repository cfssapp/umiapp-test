from django.shortcuts import render




from django.http import JsonResponse, HttpResponse
import json

# Create your views here.
api_urls = {
    "success": True,
    "data": 
        {
            "id": 1,
            "list": [
                {
                    "id": 2,
                    "user": {
                        "id": 1,
                        "email": "admin@admin.com",
                        "user_name": "admin",
                        "is_active": True,
                        "avatar": "https://antapi.pythonanywhere.com/media/upload_pics/287279348080d90deec11dfa24065fc0.jpg",
                        "status": "ok",
                        "currentAuthority": "admin",
                        "success": "true"
                    },
                    "product_id": "not set",
                    "product_name": "laptop",
                    "addcart_id": True
                }
            ],
            "cart_id": "not set",
            "customer": "admin"
        }
    ,
    "errorCode": 0
}


def apiOverview(request):

    # queryset = Cart.objects.get(pk=1)
    # serializer = CartSerializer(queryset)
    # jsonoutput = {
    #             "success": True,
    #             'data' : serializer.data,
    #             "errorCode": 0
    #         }

    jsonoutput = {
                "success": True,
                'data' : api_urls,
                "errorCode": 0
            }

    return HttpResponse(json.dumps(jsonoutput), content_type='application/json')