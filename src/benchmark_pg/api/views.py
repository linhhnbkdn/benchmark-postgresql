import time

from django.http import JsonResponse

from django.db import connection

from celery import shared_task

# Create your views here.
@shared_task
def test_benchmark_pg_mul():
    start_time = time.process_time()
    query = 'SELECT "auth_user"."id", "auth_user"."password", \
            "auth_user"."last_login", "auth_user"."is_superuser", \
            "auth_user"."username", "auth_user"."first_name", \
            "auth_user"."last_name", "auth_user"."email", \
            "auth_user"."is_staff", "auth_user"."is_active", \
            "auth_user"."date_joined" FROM "auth_user"'
    cursor = connection.cursor()
    cursor.execute(query)
    timming_process = time.process_time() - start_time
    return {"timming_process": timming_process}

def test_benchmark_pg(request, num_of_req):
    tasks = []
    start_time = time.process_time()
    for i in range(0, int(num_of_req)):
        _task = test_benchmark_pg_mul.delay()
        tasks.append(_task)
    result = []
    for task in tasks:
        result.append(task.get()['timming_process'])
    timming_process = time.process_time() - start_time
    return JsonResponse({"min": min(result),
                         "max": max(result),
                         "mean": sum(result) / len(result),
                         "total": timming_process,
                         'num_of_req': num_of_req})
