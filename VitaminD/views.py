from django.shortcuts import render
from rdflib import Graph

g = Graph()
g.parse("./search/Vitamins.owl")


def strip(query_string):
    index = query_string.index('#') + 1
    c = query_string[index:]
    return c


def vitamin(request, result):
    ######## DIETARY SOURCE ########
    if result == 'Dietary_Source':
        qres = g.query(
            """
                prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#>
                prefix owl: <http://www.w3.org/2002/07/owl#>
                PREFIX doyin: <http://www.vitaminontology.com/vitamins/ontology/doyin#>
                PREFIX yetty: <http://www.vitaminontology.com/vitamins/ontology/doyin#>

                SELECT ?animal ?animallabel
                WHERE{ 
                         ?animal rdf:type doyin:Animal_Source_For_VitaminD.
                          ?animal rdfs:label ?animallabel.
                        }
                       """)
        animal = []
        for row in qres:
            animal.append({
                'animal': strip(row['animal']),
                'animallabel': row['animallabel']
            })

        query = g.query(
            """
                prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#>
                prefix owl: <http://www.w3.org/2002/07/owl#>
                PREFIX doyin: <http://www.vitaminontology.com/vitamins/ontology/doyin#> 
                PREFIX yetty: <http://www.vitaminontology.com/vitamins/ontology/doyin#>

                SELECT ?plant ?plantlabel
                WHERE{
                         ?plant rdf:type yetty:Plant_Source_For_VitaminD.
                         ?plant rdfs:label ?plantlabel.
                        }
                       """)

        plant = []
        for row in query:
            plant.append({
                'plant': strip(row['plant']),
                'plantlabel': row['plantlabel']

            })
        return render(request, 'vitD/vitfs.html', {'animal': animal, 'plant': plant})

    ########### EFFECT ###########
    elif result == 'Effect':
        qres = g.query(
            """
                prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#>
                prefix owl: <http://www.w3.org/2002/07/owl#>
                PREFIX doyin: <http://www.vitaminontology.com/vitamins/ontology/doyin#> 
                PREFIX yetty: <http://www.vitaminontology.com/vitamins/ontology/doyin#>

                SELECT ?deficiency ?deflabel
                WHERE{
                         ?deficiency rdf:type doyin:Deficiency_Of_VitaminD.
                         ?deficiency rdfs:label ?deflabel.
                        }
                       """)
        deficiency = []
        for row in qres:
            deficiency.append({
                'deficiency': strip(row['deficiency']),
                'deflabel': row['deflabel']
            })

        query = g.query(
            """
                prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#>
                prefix owl: <http://www.w3.org/2002/07/owl#>
                PREFIX doyin: <http://www.vitaminontology.com/vitamins/ontology/doyin#> 
                PREFIX yetty: <http://www.vitaminontology.com/vitamins/ontology/doyin#>

                SELECT ?toxicity ?toxlabel
                WHERE{
                         ?toxicity rdf:type yetty:Toxicity_Of_VitaminD.
                         ?toxicity rdfs:label ?toxlabel.
                        }
                       """)

        toxicity = []
        for row in query:
            toxicity.append({
                'toxicity': strip(row['toxicity']),
                'toxlabel': row['toxlabel'],
            })
        return render(request, 'vitD/viteffect.html', {'deficiency': deficiency, 'toxicity': toxicity})

    ######## SUPPLEMENT ########
    if result == 'Supplement':
        qres = g.query(
            """
                prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#>
                prefix owl: <http://www.w3.org/2002/07/owl#>
                PREFIX doyin: <http://www.vitaminontology.com/vitamins/ontology/doyin#> 
                PREFIX yetty: <http://www.vitaminontology.com/vitamins/ontology/doyin#>

                SELECT ?supplement ?supplabel
                WHERE{
                         ?supplement rdf:type doyin:Supplement_For_VitaminD.
                         ?supplement rdfs:label ?supplabel.
                        }
                       """)
        supplement = []
        for row in qres:
            supplement.append({
                'supplement': strip(row['supplement']),
                'supplabel': row['supplabel'],
            })
        return render(request, 'vitD/vitSupplement.html', {'supplement': supplement})


    ####### Solubility ########
    elif result == 'Solubility':
        qres = g.query(
            """
                prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#>
                prefix owl: <http://www.w3.org/2002/07/owl#>
                PREFIX doyin: <http://www.vitaminontology.com/vitamins/ontology/doyin#> 
                PREFIX yetty: <http://www.vitaminontology.com/vitamins/ontology/doyin#>

                SELECT ?solubility ?sollabel
                WHERE{
                         ?solubility rdf:type doyin:VitaminD_Solubility.
                         ?solubility rdfs:label ?sollabel.
                        }
                       """)
        solubility = []
        for row in qres:
            solubility.append({
                'solubility': strip(row['solubility']),
                'sollabel': row['sollabel'],
            })
        return render(request, 'vitD/vitsolubility.html', {'solubility': solubility})

    ######## RDA ########
    elif result == 'Recommended_Dietary_Allowance':
        ### Young ###
        qres = g.query(
            """
                prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#>
                prefix owl: <http://www.w3.org/2002/07/owl#>
                PREFIX doyin: <http://www.vitaminontology.com/vitamins/ontology/doyin#> 
                PREFIX yetty: <http://www.vitaminontology.com/vitamins/ontology/doyin#>

                SELECT ?young 
                WHERE{
                         ?young rdf:type doyin:VitaminD_RDA_Young_Children.
                        }
                       """)
        young = []
        for row in qres:
            young.append({
                'young': strip(row['young']),
            })

        ### YOUNGER ###
        query = g.query(
            """
                prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#>
                prefix owl: <http://www.w3.org/2002/07/owl#>
                PREFIX doyin: <http://www.vitaminontology.com/vitamins/ontology/doyin#> 
                PREFIX yetty: <http://www.vitaminontology.com/vitamins/ontology/doyin#>

                SELECT ?younger
                WHERE{
                         ?younger rdf:type yetty:VitaminD_RDA_Younger_Children.
                        }
                       """)
        younger = []
        for row in query:
            younger.append({
                'younger': strip(row['younger'])
            })

        ### YOUNGEST ###
        query1 = g.query(
            """
                prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#>
                prefix owl: <http://www.w3.org/2002/07/owl#>
                PREFIX doyin: <http://www.vitaminontology.com/vitamins/ontology/doyin#> 
                PREFIX yetty: <http://www.vitaminontology.com/vitamins/ontology/doyin#>

                SELECT ?youngest
                WHERE{
                         ?youngest rdf:type yetty:VitaminD_RDA_Youngest_Children.
                        }
                       """)
        youngest = []
        for row in query1:
            youngest.append({
                'youngest': strip(row['youngest'])
            })

        ### YOUNG I ###
        query2 = g.query(
            """
                prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#>
                prefix owl: <http://www.w3.org/2002/07/owl#>
                PREFIX doyin: <http://www.vitaminontology.com/vitamins/ontology/doyin#> 
                PREFIX yetty: <http://www.vitaminontology.com/vitamins/ontology/doyin#>

                SELECT ?yi
                WHERE{
                         ?yi rdf:type yetty:VitaminD_RDA_Young_Infant.
                        }
                       """)
        yi = []
        for row in query2:
            yi.append({
                'yi': strip(row['yi'])
            })

        ### YOUNGEST I ###
        query3 = g.query(
            """
                prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#>
                prefix owl: <http://www.w3.org/2002/07/owl#>
                PREFIX doyin: <http://www.vitaminontology.com/vitamins/ontology/doyin#> 
                PREFIX yetty: <http://www.vitaminontology.com/vitamins/ontology/doyin#>

                SELECT ?yri
                WHERE{
                         ?yri rdf:type yetty:VitaminD_RDA_Younger_Infant.
                        }
                       """)
        yri = []
        for row in query3:
            yri.append({
                'yri': strip(row['yri'])
            })

        ### LACTATING ADOL ###
        query4 = g.query(
            """
                prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#>
                prefix owl: <http://www.w3.org/2002/07/owl#>
                PREFIX doyin: <http://www.vitaminontology.com/vitamins/ontology/doyin#> 
                PREFIX yetty: <http://www.vitaminontology.com/vitamins/ontology/doyin#>

                SELECT ?ladol
                WHERE{
                         ?ladol rdf:type yetty:VitaminD_RDA_For_Lactating_Adolescent.
                        }
                       """)
        ladol = []
        for row in query4:
            ladol.append({
                'ladol': strip(row['ladol'])
            })

        ### Lactating Women ###
        query5 = g.query(
            """
                prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#>
                prefix owl: <http://www.w3.org/2002/07/owl#>
                PREFIX doyin: <http://www.vitaminontology.com/vitamins/ontology/doyin#> 
                PREFIX yetty: <http://www.vitaminontology.com/vitamins/ontology/doyin#>

                SELECT ?lwom
                WHERE{
                         ?lwom rdf:type yetty:VitaminD_RDA_For_Lactating_Women.
                        }
                       """)
        lwom = []
        for row in query5:
            lwom.append({
                'lwom': strip(row['lwom'])
            })

        ### MEN ###
        query6 = g.query(
            """
                prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#>
                prefix owl: <http://www.w3.org/2002/07/owl#>
                PREFIX doyin: <http://www.vitaminontology.com/vitamins/ontology/doyin#> 
                PREFIX yetty: <http://www.vitaminontology.com/vitamins/ontology/doyin#>

                SELECT ?men
                WHERE{
                         ?men rdf:type yetty:VitaminD_RDA_For_Men.
                        }
                       """)
        men = []
        for row in query6:
            men.append({
                'men': strip(row['men'])
            })

        ### Nom Pregnant Women ###
        query7 = g.query(
            """
                prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#>
                prefix owl: <http://www.w3.org/2002/07/owl#>
                PREFIX doyin: <http://www.vitaminontology.com/vitamins/ontology/doyin#> 
                PREFIX yetty: <http://www.vitaminontology.com/vitamins/ontology/doyin#>

                SELECT ?npw
                WHERE{
                         ?npw rdf:type yetty:VitaminD_RDA_For_Non_Pregnant_Women.
                        }
                       """)
        npw = []
        for row in query7:
            npw.append({
                'npw': strip(row['npw'])
            })

        ### Pregnant Adol ###
        query8 = g.query(
            """
                prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#>
                prefix owl: <http://www.w3.org/2002/07/owl#>
                PREFIX doyin: <http://www.vitaminontology.com/vitamins/ontology/doyin#> 
                PREFIX yetty: <http://www.vitaminontology.com/vitamins/ontology/doyin#>

                SELECT ?padol
                WHERE{
                         ?padol rdf:type yetty:VitaminD_RDA_For_Pregnant_Adolescent.
                        }
                       """)
        padol = []
        for row in query8:
            padol.append({
                'padol': strip(row['padol'])
            })

        ### Pregnant Women ###
        query9 = g.query(
            """
                prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#>
                prefix owl: <http://www.w3.org/2002/07/owl#>
                PREFIX doyin: <http://www.vitaminontology.com/vitamins/ontology/doyin#> 
                PREFIX yetty: <http://www.vitaminontology.com/vitamins/ontology/doyin#>

                SELECT ?pwom
                WHERE{
                         ?pwom rdf:type yetty:VitaminD_RDA_For_Pregnant_Women.
                        }
                       """)
        pwom = []
        for row in query9:
            pwom.append({
                'pwom': strip(row['pwom'])
            })
        return render(request, 'vitD/vitrda.html',
                      {'young': young, 'younger': younger, 'youngest': youngest, 'yi': yi, 'yri': yri, 'ladol': ladol,
                       'lwom': lwom, 'men': men, 'npw': npw, 'padol': padol, 'pwom': pwom})


    ######## TUI ########
    elif result == 'Tolerable_Upper_Intake':
        ### Young ###
        qres = g.query(
            """
                prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#>
                prefix owl: <http://www.w3.org/2002/07/owl#>
                PREFIX doyin: <http://www.vitaminontology.com/vitamins/ontology/doyin#> 
                PREFIX yetty: <http://www.vitaminontology.com/vitamins/ontology/doyin#>

                SELECT ?young 
                WHERE{
                         ?young rdf:type doyin:VitaminD_TUI_Young_Children.
                        }
                       """)
        young = []
        for row in qres:
            young.append({
                'young': strip(row['young']),
            })

        ### YOUNGER ###
        query = g.query(
            """
                prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#>
                prefix owl: <http://www.w3.org/2002/07/owl#>
                PREFIX doyin: <http://www.vitaminontology.com/vitamins/ontology/doyin#> 
                PREFIX yetty: <http://www.vitaminontology.com/vitamins/ontology/doyin#>

                SELECT ?younger
                WHERE{
                         ?younger rdf:type yetty:VitaminD_TUI_Younger_Children.
                        }
                       """)
        younger = []
        for row in query:
            younger.append({
                'younger': strip(row['younger'])
            })

        ### YOUNGEST ###
        query1 = g.query(
            """
                prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#>
                prefix owl: <http://www.w3.org/2002/07/owl#>
                PREFIX doyin: <http://www.vitaminontology.com/vitamins/ontology/doyin#> 
                PREFIX yetty: <http://www.vitaminontology.com/vitamins/ontology/doyin#>

                SELECT ?youngest
                WHERE{
                         ?youngest rdf:type yetty:VitaminD_RDA_Youngest_Children.
                        }
                       """)
        youngest = []
        for row in query1:
            youngest.append({
                'youngest': strip(row['youngest'])
            })

        ### YOUNG I ###
        query2 = g.query(
            """
                prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#>
                prefix owl: <http://www.w3.org/2002/07/owl#>
                PREFIX doyin: <http://www.vitaminontology.com/vitamins/ontology/doyin#> 
                PREFIX yetty: <http://www.vitaminontology.com/vitamins/ontology/doyin#>

                SELECT ?yi
                WHERE{
                         ?yi rdf:type yetty:VitaminD_TUI_Young_Infant.
                        }
                       """)
        yi = []
        for row in query2:
            yi.append({
                'yi': strip(row['yi'])
            })

        ### YOUNGEST I ###
        query3 = g.query(
            """
                prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#>
                prefix owl: <http://www.w3.org/2002/07/owl#>
                PREFIX doyin: <http://www.vitaminontology.com/vitamins/ontology/doyin#> 
                PREFIX yetty: <http://www.vitaminontology.com/vitamins/ontology/doyin#>

                SELECT ?yri
                WHERE{
                         ?yri rdf:type yetty:VitaminD_TUI_Younger_Infant.
                        }
                       """)
        yri = []
        for row in query3:
            yri.append({
                'yri': strip(row['yri'])
            })

        ### LACTATING ADOL ###
        query4 = g.query(
            """
                prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#>
                prefix owl: <http://www.w3.org/2002/07/owl#>
                PREFIX doyin: <http://www.vitaminontology.com/vitamins/ontology/doyin#> 
                PREFIX yetty: <http://www.vitaminontology.com/vitamins/ontology/doyin#>

                SELECT ?ladol
                WHERE{
                         ?ladol rdf:type yetty:VitaminD_TUI_For_Lactating_Adolescent.
                        }
                       """)
        ladol = []
        for row in query4:
            ladol.append({
                'ladol': strip(row['ladol'])
            })

        ### Lactating Women ###
        query5 = g.query(
            """
                prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#>
                prefix owl: <http://www.w3.org/2002/07/owl#>
                PREFIX doyin: <http://www.vitaminontology.com/vitamins/ontology/doyin#> 
                PREFIX yetty: <http://www.vitaminontology.com/vitamins/ontology/doyin#>

                SELECT ?lwom
                WHERE{
                         ?lwom rdf:type yetty:VitaminD_TUI_For_Lactating_Women.
                        }
                       """)
        lwom = []
        for row in query5:
            lwom.append({
                'lwom': strip(row['lwom'])
            })

        ### MEN ###
        query6 = g.query(
            """
                prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#>
                prefix owl: <http://www.w3.org/2002/07/owl#>
                PREFIX doyin: <http://www.vitaminontology.com/vitamins/ontology/doyin#> 
                PREFIX yetty: <http://www.vitaminontology.com/vitamins/ontology/doyin#>

                SELECT ?men
                WHERE{
                         ?men rdf:type yetty:VitaminD_TUI_For_Men.
                        }
                       """)
        men = []
        for row in query6:
            men.append({
                'men': strip(row['men'])
            })

        ### Nom Pregnant Women ###
        query7 = g.query(
            """
                prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#>
                prefix owl: <http://www.w3.org/2002/07/owl#>
                PREFIX doyin: <http://www.vitaminontology.com/vitamins/ontology/doyin#> 
                PREFIX yetty: <http://www.vitaminontology.com/vitamins/ontology/doyin#>

                SELECT ?npw
                WHERE{
                         ?npw rdf:type yetty:VitaminD_TUI_For_Non_Pregnant_Women.
                        }
                       """)
        npw = []
        for row in query7:
            npw.append({
                'npw': strip(row['npw'])
            })

        ### Pregnant Adol ###
        query8 = g.query(
            """
                prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#>
                prefix owl: <http://www.w3.org/2002/07/owl#>
                PREFIX doyin: <http://www.vitaminontology.com/vitamins/ontology/doyin#> 
                PREFIX yetty: <http://www.vitaminontology.com/vitamins/ontology/doyin#>

                SELECT ?padol
                WHERE{
                         ?padol rdf:type yetty:VitaminD_TUI_For_Pregnant_Adolescent.
                        }
                       """)
        padol = []
        for row in query8:
            padol.append({
                'padol': strip(row['padol'])
            })

        ### Pregnant Women ###
        query9 = g.query(
            """
                prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#>
                prefix owl: <http://www.w3.org/2002/07/owl#>
                PREFIX doyin: <http://www.vitaminontology.com/vitamins/ontology/doyin#> 
                PREFIX yetty: <http://www.vitaminontology.com/vitamins/ontology/doyin#>

                SELECT ?pwom
                WHERE{
                         ?pwom rdf:type yetty:VitaminD_TUI_For_Pregnant_Women.
                        }
                       """)
        pwom = []
        for row in query9:
            pwom.append({
                'pwom': strip(row['pwom'])
            })
        return render(request, 'vitD/vittui.html',
                      {'young': young, 'younger': younger, 'youngest': youngest, 'yi': yi, 'yri': yri, 'ladol': ladol,
                       'lwom': lwom, 'men': men, 'npw': npw, 'padol': padol, 'pwom': pwom})




