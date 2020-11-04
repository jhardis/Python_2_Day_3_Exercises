def geo_concat3(city, country, population=None):
    
    """Returns city, country
    
    >>> geo_concat3("New York", "United States")
    'New York, United States'
    
    >>> geo_concat3("London", "England")
    'London, England'
    
    >>> geo_concat3("Paris", "France")
    'Paris, France'
    
    >>> geo_concat3("Anchorage", "United States", 288000)
    'Anchorage, United States - population 288,000'
    
    """
    
    if (population == None) :
        return f"{city}, {country}"
    else :
        return f"{city}, {country} - population {population:,}"

print (geo_concat3("New York", "United States"))
print (geo_concat3("London", "England"))
print (geo_concat3("Paris", "France"))
print (geo_concat3("Anchorage", "United States", 288000))
