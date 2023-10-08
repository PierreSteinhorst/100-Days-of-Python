# {
#   Key:  [List],
#   Key2: {Dict},
# }
#

# nesting
capitals = {
    "France": "Paris",
    "Germany": "Berlin",
}

# nesting a List in Dictionary
# nesting a dictionary in a dictionary

travel_log = {
    "France": {"cities_visited": ["Paris", "Lille", "Djion"], "total_visits": 12},
    "Germany": {"cities_visited": ["Hamburg", "Berlin", "Rostock"], "total_visits": 5},
}

# [{
#   Key:  [List],
#   Key2: {Dict},
# },
# {  Key: Value,
#   Key2: Value
# }]

# nesting a dictionary in a list

travel_log2 = [
    {
        "county": "France",
        "cities_visited": ["Paris", "Lille", "Djion"],
        "total_visits": 12
    },
    {
        "country": "Germany",
        "cities_visited": ["Hamburg", "Berlin", "Rostock"],
        "total_visits": 5
    }
]
print(travel_log2[1]["cities_visited"][0])