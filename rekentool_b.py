import math

def berekeningen(lengte_bouwplaats,breedte_bouwplaats,lengte_tegel,breedte_tegel,snijverlies):
    m2_bouwplaats = lengte_bouwplaats * breedte_bouwplaats
    m2_tegels = lengte_tegel * breedte_tegel
    m2_tegels = m2_tegels / 10000
    aantal_tegels = math.ceil(m2_bouwplaats / m2_tegels)
    extra_tegels = math.ceil(aantal_tegels / 100 * snijverlies)
    totaal = aantal_tegels + extra_tegels
    return m2_bouwplaats,m2_tegels,aantal_tegels,extra_tegels,totaal

# m2_bouwplaats,m2_tegels,aantal_tegels,extra_tegels,totaal = berekeningen(5.8,3.2,30,60,15)
# print(m2_bouwplaats)
# print(m2_tegels)
# print(aantal_tegels)
# print(extra_tegels)
# print(totaal)

