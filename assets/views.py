from django.shortcuts import render,HttpResponse
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
import json
from assets import models
from assets import asset_handler



@csrf_exempt    #忽略csrf cookie
def report(request):
    if request.method == "POST":
        asset_data = request.POST.get('asset_data')
        data = json.loads(asset_data)
        if not data:
            return HttpResponse('数据接收为空')
        if not issubclass(dict,type(data)):
            return HttpResponse("数据必须为字典格式")
        #是否携带关键的sn好
        sn = data.get('sn',None)
        if sn:
            asset_obj = models.Asset.objects.filter(sn=sn)
            if asset_obj:
                pass
                return HttpResponse("资产数据更新")
            else:
                obj = asset_handler.NewAsset(request,data)
                response = obj.add_to_new_assets_zone()
                return HttpResponse(response)
        else:
            return HttpResponse("没有资产SN号,请检查数据")



        return HttpResponse('服务器获取到数据!')
    return HttpResponse("200")