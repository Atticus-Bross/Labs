from json import load, loads
from lab4 import *
Number=int|float
Sequence=str|list|tuple|dict
with open('datasets/counties.json', 'r') as jsonfile:
    data = load(jsonfile)
def seq_comb(seq:Sequence, f)->tuple:
    """seq_comb(seq, f) Evaluates a function on every unique combination of two elements in seq

    seq: the sequence the operation is to be preformed on
    f: a function that takes two parameters"""
    if len(seq)<2:
        raise ValueError('seq should be at least two length')
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
def fetch(seq:Sequence,*indexes)->tuple:
    """fetch(seq, *indexes) retrieves specific elements from a sequence

    seq: the sequence to be retrieved from
    *indexes: the indexes or keys of the items to be retrieved"""
    return_tuple:tuple=()
    for index in indexes:
        return_tuple=return_tuple+(seq[index],)
    return return_tuple
def temp_variance(county_index:int)->Number:
    """temp_variance(county_index) Gives the average temperature variance of a county over a year

    county_index: the index where the county is located in counties.json"""
    temps:tuple =fetch(data[county_index]['noaa'],'temp-jan','temp-apr','temp-jul','temp-oct')
    temps_variance:tuple=seq_comb(temps,lambda x,y:abs(x-y))
    return average(temps_variance)
def header(text:str,level:int, file)->None:
    """header(text, level, file) Adds a header to a markdown file

    text: the text of the header
    level: 1-6, 1 is the largest
    file: the markdown file"""
    file.write('\n'+'#'*level+' '+text+'\n')