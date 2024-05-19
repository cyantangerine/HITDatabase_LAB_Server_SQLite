import json
import traceback

from django.db import connection
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods

from database.models import *

ENABLE_DETAIL_FALSE = True


class CoverData:
    def __init__(self, source):
        if source:
            self.data = json.loads(source)
        else:
            raise Exception("SOURCE为空")

    def get(self, key: str, emptyable=False):
        val = self.data.get(key)
        if val is None and not emptyable:
            print("原始数据：", self.data)
            raise Exception("在JSON中读取" + key + "时出错")
        else:
            return val


def load_data(request):
    source = request.body.decode("utf-8")
    print("收到数据：", source)
    return CoverData(source)


def make_ret(info="OK", success=False, data=None):
    if not success and info == 'OK' and not ENABLE_DETAIL_FALSE: info = "服务器内部错误"
    result = {
        'status': success,
        'errMsg': info,
        'data': data
    }
    print(repr(data))
    result = json.dumps(result, ensure_ascii=False)
    return HttpResponse(result)


def query_all_dict(sql, params=None):
    '''
    查询所有结果返回字典类型数据
    :param sql:
    :param params:
    :return:
    '''
    with connection.cursor() as cursor:
        if params:
            cursor.execute(sql, params=params)
        else:
            cursor.execute(sql)
        if cursor.description is None: return None
        col_names = [desc[0] for desc in cursor.description]
        row = cursor.fetchall()
        rowList = []
        for list in row:
            tMap = dict(zip(col_names, list))
            rowList.append(tMap)
        return rowList


@require_http_methods(["POST"])
def init_client(request):
    try:
        data = {
            "Version": 1,
            "MinVersion": 1
        }
        return make_ret(success=True, data=data)
    except Exception as e:
        print(traceback.print_exc())
        return make_ret(repr(e))


@require_http_methods(["POST"])
def raw_sql_query(request):
    sql = ""
    try:
        source = load_data(request)
        sql = source.get("sql")
        data = query_all_dict(sql)
        return make_ret(success=True, data=data)
    except Exception as e:
        print(traceback.print_exc())
        return make_ret(repr(e), data=sql)

def cleardb(request):
    accounts.objects.all().delete()
    courses.objects.all().delete()
    departments.objects.all().delete()
    plan.objects.all().delete()
    rooms.objects.all().delete()
    # scores.objects.all().delete()
    students.objects.all().delete()
    teachers.objects.all().delete()
    return make_ret(success=True)
