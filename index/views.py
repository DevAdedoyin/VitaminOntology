from django.shortcuts import render
from rdflib import Graph

g = Graph()
g.parse("./search/Vitamins.owl")


def home(request):
    return render(request, 'home/index.html')


def search(request):
    userValue = request.GET.get('s')
    userstr = str(userValue).lower()
    query = g.query(
        """
            PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
            PREFIX owl: <http://www.w3.org/2002/07/owl#>
            PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
            PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
            prefix d: <http://www.vitaminontology.com/vitamins/ontology/doyin#>

            SELECT DISTINCT ?value ?c ?deflabel ?e ?vitlabel
            WHERE { ?a d:effect ?value.
            ?a rdf:type ?c.
            ?c rdfs:subClassOf ?d.
            ?c rdfs:label ?deflabel.
            ?d rdfs:subClassOf ?e.
            ?e rdfs:label ?vitlabel.
            ?e rdfs:subClassOf ?f. 
                      }
 """)
    result = []
    for row in query:
        result.append({
            'symptom': row['value'],
            'c': strip(row['c']),
            'deflabel': row['deflabel'],
            'e': strip(row['e']),
            'vitlabel': row['vitlabel']
        })
    '''for symptom in result[0]:
         symp == symptom.lower()
        if symp == userstr:
            return render(request, 'home/result.html', {'result': result})
        else:
            continue'''
    return render(request, 'home/result.html', {'result': result, 'userstr': userstr})


def strip(query_string):
    index = query_string.index('#') + 1
    c = query_string[index:]
    return c

