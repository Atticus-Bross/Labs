from json import load, loads
Number=int|float
Sequence=str|list|tuple|dict
with open('datasets/counties.json', 'r') as file:
    data = load(file)
def seq_comb(seq:Sequence, f)->tuple:
    """seq_comb(seq, f) Evaluates a function on every unique combination of two elements in seq

    seq: the sequence the operation is to be preformed on
    f: a function that takes two parameters"""
    return_values:tuple=()
    #exclusions needs to use list methods
    exclusions:list=list(seq)
    for index_outer, value_outer in enumerate(seq):
        for index_inner, value_inner in enumerate(exclusions):
            return_values=return_values+(f(value_outer,value_inner),)
        #the identity not the order of elements matters
        #all the combinations with value_outer in them have been tried
        exclusions.remove(value_outer)
    return return_values
def temp_variances(county_index:int)->tuple[Number,...]:
    """temp_variances(county_index) Gives the temperature differences between every possible set of months

    county_index: the index where the county is located"""
    pass
print(data[0]['noaa']['temp-jan'])