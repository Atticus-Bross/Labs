from json import load
from lab4 import average
Number=int|float
Sequence=str|list|tuple|dict
#indexable sequences that can contain numbers
NumList=list|tuple
with open('datasets/counties.json', 'r') as jsonfile:
    data = load(jsonfile)
def fetch(seq:Sequence,*indexes:object)->tuple:
    """fetch(seq, *indexes) retrieves specific elements from a sequence

    seq: the sequence to be retrieved from
    *indexes: the indexes or keys of the items to be retrieved"""
    return_tuple:tuple=()
    for index in indexes:
        return_tuple=return_tuple+(seq[index],)
    return return_tuple
def variance(numbers:NumList)->Number:
    """variance(numbers) Finds the variance of a list of numbers

    numbers: the list of numbers"""
    avg:Number=average(numbers)
    #the iterable map returns does not work well with other functions
    difs:list=list(map(lambda x:(avg-x)**2,numbers))
    return average(difs)
def query_county(county:dict,f,directory:object,*keys:object)->object:
    """query_county(county, f, directory, *keys) Gets information from a county

    county: the county to be queried
    f: the function to be preformed on the data
    directory: the key of the sub dictionary, if None then the function looks in the whole county
    *keys: the keys in the sub dictionary to be used"""
    if directory is None:
        county_data:tuple=fetch(county,*keys)
    else:
        county_data:tuple=fetch(county[directory],*keys)
    return f(county_data)
def temp_variance(county:dict)->Number:
    """temp_variance(county) Finds the temperature variance for a county

    county: the county for which the variance is to be found"""
    temps:tuple=fetch(county['noaa'],'temp-jan','temp-apr','temp-jul','temp-oct')
    return variance(temps)
def growth(county:dict)->Number:
    """growth(county) Finds how much a county has grown in population from the start to the end of the data

    county: the county for which the growth is to be found"""
    pops:tuple=fetch(county['population'],'2010','2019')
    return pops[1]-pops[0]
def deadlyness(county:dict)->Number:
    """deadlyness(county) Finds the deadlyness of a county

    county: the county for which the deadlyness is to be found"""
    pass
def header(text:str,level:int, file)->None:
    """header(text, level, file) Adds a header to a markdown file

    text: the text of the header
    level: 1-6, 1 is the largest
    file: the markdown file"""
    file.write('\n'+'#'*level+' '+text+'\n')