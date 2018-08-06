from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from utils import logger
import traceback as tb
from rest_api.models import Token, Request
from ip_collector.models import ProxyPool
import random


class NewsVoteAPI(APIView):
    """
    Get Proxy
    """
    permission_classes = (AllowAny,)
    http_method_names = ['get']

    def get(self, request, *args, **kwargs):
        try:
            token = Token.objects.get(token=request.GET['token'], is_available=True)
            ip_obj = random.choice(ProxyPool.objects.all())
            Request.objects.get_or_create(token=token, proxy=ip_obj)
            r = {
                'ip': ip_obj.ip,
                'port': ip_obj.port,
                'type': ip_obj.type
            }
        except Token.DoesNotExist:
            return Response('Invalid Token', status=status.HTTP_400_BAD_REQUEST)
        except:
            logger.error(tb.format_exc())
            return Response('Invalid parameters', status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(r, status=status.HTTP_200_OK)