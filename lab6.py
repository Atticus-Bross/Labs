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
    #dictionaries require special handling
    if type(seq)==dict:
        seq=seq.values()
    #exclusions needs to use list methods
    exclusions:list=list(seq)
    for value_outer in seq:
        # the identity not the order of elements matters
        # all the remaining combinations with value_outer in them will be tried in the next inner loop
        exclusions.remove(value_outer)
        for value_inner in exclusions:
            return_values=return_values+(f(value_outer,value_inner),)
    return return_values
def temp_variances(county_index:int)->tuple[Number,...]:
    """temp_variances(county_index) Gives the temperature differences between every possible set of months

    county_index: the index where the county is located"""
    pass