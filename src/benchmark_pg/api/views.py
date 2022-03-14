from sqlite3 import Cursor
from django.shortcuts import render
from django.http import JsonResponse

from django.contrib.auth.models import User
from django.db import connection
# Create your views here.
def test_benchmark_pg(request):
    query = 'SELECT "auth_user"."id", "auth_user"."password", \
            "auth_user"."last_login", "auth_user"."is_superuser", \
            "auth_user"."username", "auth_user"."first_name", \
            "auth_user"."last_name", "auth_user"."email", \
            "auth_user"."is_staff", "auth_user"."is_active", \
            "auth_user"."date_joined" FROM "auth_user"'
    cursor = connection.cursor()
    cursor.execute(query)
    return JsonResponse({"data": cursor.fetchone()})