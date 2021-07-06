from datetime import datetime

import pytz
from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsOwnerOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        return bool(
            request.user.is_authenticated
        )

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True

        return bool(
            obj.id == request.user.id
        )


def str_to_bool(s):
    if s in [1, True, 'TRUE', 'True', 'true', '1']:
        return True
    return False


def get_or_none(classmodel, **kwargs):
    try:
        return classmodel.objects.get(**kwargs)
    except classmodel.MultipleObjectsReturned as e:
        print(e)
    except classmodel.DoesNotExist:
        return None


def str_to_int(str_list):
    if len(str_list) > 0:
        return list(map(lambda x: int(x), str_list))
    return []


def date_to_timezone(date):
    if date:
        return pytz.utc.localize(datetime.strptime(date, '%Y-%m-%d'))
    return None
