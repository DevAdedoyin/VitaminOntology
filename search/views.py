from django.shortcuts import render
from rdflib import Graph

g = Graph()
g.parse("./search/Vitamins.owl")


def Classes(request, vitamins):
    qres = g.query(
        """
            prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#>
            prefix owl: <http://www.w3.org/2002/07/owl#>
            PREFIX doyin: <http://www.vitaminontology.com/vitamins/ontology/doyin#> 
            
            SELECT DISTINCT ?detail ?label
                WHERE{ 
                    ?detail rdfs:subClassOf doyin:Vitamin_Details;
                             rdfs:label ?label.
                } order by ?label """)
    result = []
    for row in qres:
        result.append({
            'detail': strip(row['detail']),
            'label': row['label'],
        })
    return render(request, 'search/list.html', {'result': result, 'vitamins': vitamins})


def strip(query_string):
    index = query_string.index('#') + 1
    c = query_string[index : ]
    return c


def Vitamins(request):
    qres = g.query(
    """
        prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        prefix owl: <http://www.w3.org/2002/07/owl#>
        PREFIX doyin: <http://www.vitaminontology.com/vitamins/ontology/doyin#> 

        SELECT ?vitamin ?b
        WHERE{
                ?vitamin rdfs:subClassOf doyin:Vitamin;
                         rdfs:label ?b.
                }order by ?b""")
    result = []
    for row in qres:
        result.append({
            'class': strip(row['vitamin']),
            'label': row['b'],
        })
    return render(request, 'search/index.html', {'result': result})

