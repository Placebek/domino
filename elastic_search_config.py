from elasticsearch import AsyncElasticsearch
from fastapi.responses import JSONResponse


es = AsyncElasticsearch(
    hosts=["http://localhost:9200"],
    verify_certs=False
)

def search_houses(request):
    query = request.GET.get('query', '')
    if query:
        response = es.search(index="houses", body={
            "query": {
                "wildcard": {
                    "name": {
                        "value": f"{query}*"
                    }
                }
            }
        })
        return JSONResponse(response['hits']['hits'], safe=False)
    return JSONResponse({'error': 'No query provided'}, status=400)