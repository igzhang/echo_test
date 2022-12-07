import datetime
import uvicorn
from starlette.applications import Starlette
from starlette.responses import PlainTextResponse
from starlette.routing import Route


request_record_database = []


async def api(request):
    record = {
        "datetime": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "method": request.method,
        "headers": request.headers.items(),
        "query": request.query_params.items(),
        "client": {
            "host": request.client.host,
            "port": request.client.port
        },
        "cookies": dict(request.cookies.items())
    }

    content_type  = request.headers.get("content-type")
    if content_type == "application/json":
        record["body"] = await request.json()
    elif "form-data" in content_type:
        form_data = await request.form()
        record["body"] = dict(form_data.items())
    else:
        record["body"] = await request.body()
    print(record)
    return PlainTextResponse('success')


app = Starlette(routes=[
    Route('/api', api, methods=['GET', 'POST', 'PUT', 'DELETE', 'PATCH', 'OPTIONS', 'HEAD']),
])


if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8080)
