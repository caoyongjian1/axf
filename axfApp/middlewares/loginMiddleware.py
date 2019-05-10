# -*- coding:utf-8 -*-

from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import redirect
from django.core.cache import cache
from axfApp.models import Customer
from django.http import JsonResponse

class LoginMiddleware(MiddlewareMixin):
    # 对process_request方法，先注册的中间件会先执行
    # 在视图执行之前调用，注意：该方法可以返回None或者response对象，如果返回response对象，则视图函数就不会再执行了，可以进行一些拦截操作
    def process_request(self, request):
        if request.path in ["/cart/", "/showAddress/", "/changeCart/"]:
            fromPath = request.GET.get("from")
            #验证是否登录
            ctoken = request.COOKIES.get("token")
            if not ctoken:
                if request.is_ajax():
                    return JsonResponse({"error": 1, "data": "/login/?from=%s"%fromPath})
                return redirect("/login/?from=%s" % fromPath)
            phone = request.session.get("phone")
            if not phone:
                if request.is_ajax():
                    return JsonResponse({"error": 1, "data": "/login/?from=%s"%fromPath})
                return redirect("/login/?from=%s" % fromPath)
            # 缓存中获取token
            stoken = cache.get(phone)
            if not stoken:
                # 去mysql中获取
                stoken = Customer.objects.get(phone=phone).token
                # 同步到redis缓存中
                cache.set(phone, stoken)
            #验证token
            if ctoken != stoken:
                if request.is_ajax():
                    return JsonResponse({"error": 1, "data": "/login/?from=%s"%fromPath})
                return redirect("/login/?from=%s"%fromPath)
        request.phone = request.session.get("phone")
        return None




