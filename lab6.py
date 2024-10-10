from json import load
from lab4 import average
Number=int|float
Sequence=str|list|tuple|dict
#sequences that can contain numbers
NumList=list|tuple|dict
with open('datasets/counties.json', 'r') as jsonfile:
    data = load(jsonfile)
def fetch(seq:Sequence,*indexes)->tuple:
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
    #handle dictionaries
    if type(numbers)==dict:
        numbers=list(numbers.values())
    avg:Number=average(numbers)
    #the iterable map returns does not work well with other functions
    difs:list=list(map(lambda x:(avg-x)**2,numbers))
    return average(difs)
def replace(start_list:list,original,replacement)->list:
    """replace(start_list, original, replacement) Replaces a value in a list with another value wherever it occurs

    start_list: the list the operation is to be preformed on
    original: the original value
    replacement: the value to replace the original with"""
    occurrences:int=start_list.count(original)
    #the nature of for loops handles cases where original is not in start_list automatically
    #in this case the list remains unchanged
    for i in range(occurrences):
        index:int=start_list.index(original)
        start_list.insert(index,replacement)
        start_list.remove(original)
def query_county(county:dict,f,directory,*keys):
    """query_county(county, f, directory, *keys, if_none) Gets information from a county

    county: the county to be queried
    f: the function to be preformed on the data
    directory: the key of the sub dictionary, if None then the function looks in the whole county
    *keys: the keys in the sub dictionary to be used"""
    if directory is None:
        county_data:tuple|list=fetch(county,*keys)
    else:
        county_data:tuple|list=fetch(county[directory],*keys)
    county_data=list(county_data)
    #None in this database means zero
    replace(county_data,None,0)
    return f(county_data)
def temp_variance(county:dict)->Number:
    """temp_variance(county) Finds the temperature variance for a county

    county: the county for which the variance is to be found"""
    return query_county(county,variance,'noaa','temp-jan','temp-apr','temp-jul','temp-oct')
def growth(county:dict)->Number:
    """growth(county) Finds how much a county has grown in population from the start to the end of the data

    county: the county for which the growth is to be found"""
    return query_county(county,lambda x:x[1]-x[0],'population','2010','2019')
def deadlyness(county:dict)->Number:
    """deadlyness(county) Finds the deadlyness of a county

    county: the county for which the deadlyness is to be found"""
    return query_county(county,sum,'deaths','suicides','homicides','vehicle')
def education(county:dict)->Number:
    """education(county) Finds the education of a county

    county: the county for which the education is to be found"""
    return query_county(county,lambda x:x[0],'edu','bachelors+')
def portion_female(county:dict)->Number:
    """portion_female(county) Finds the portion of a county that is female

    county: the county for which the female portion is to be found"""
    return query_county(county,lambda x:x[1]/(x[0]+x[1]),None,'male','female')
def oldness(county:dict)->Number:
    """oldness(county) Finds the portion of a county that is over 65

    county: the county for which the oldness is to be found"""
    return query_county(county,sum,'age','65-69','70-74','75-79','80-84','85+')
def youngness(county:dict)->Number:
    """youngness(county) Finds the portion of a county that is under 20

    county: the county for which the youngness is to be found"""
    return query_county(county,sum,'age','0-4','5-9','10-14','15-19')
def age_variance(county:dict)->Number:
    """age_variance(county) Finds the age variation for a county

    county: the county for which the age variation is to be found"""
    return query_county(county,lambda x:variance(*x),None,'age')
def employees(industries:dict[str:dict[str:Number,...],...])->tuple[Number,...]:
    """employees(industries) Returns a list of the employees in the given industries

    industries: the industries to be evaluated"""
    industries=list(industries.values())
    return_tuple:tuple=()
    for industry in industries:
        return_tuple=return_tuple+(industry['employees'],)
    return return_tuple
def raw_employment(raw_data:tuple[dict[str:Number,...],dict[str:dict[str:Number,...],...]])->Number:
    """raw_employment(raw_data) A function to be passed to a query_county function

    raw_data: generated by query_county, directory: None, *keys: 'population', 'industry'"""
    #raw_data[0] == population, raw_data[1] == industry
    employee_num=sum(employees(raw_data[1]))
    return employee_num/raw_data[0]['2019']
def employment(county:dict)->Number:
    """employment(county) Finds the employment rate for a county

    county: the county for which the employment is to be found"""
    return query_county(county,raw_employment,None,'population','industry')
def capitalize(string:str)->str:
    """capitalize(string) Capitalizes the words of a string

    string: the string to be capitalized"""
    letter_equivalents: dict = {'a': 'A', 'b': 'B', 'c': 'C', 'd': 'D', 'e': 'E', 'f': 'F', 'g': 'G', 'h': 'H',\
        'i': 'I', 'j': 'J', 'k': 'K', 'l': 'L', 'm': 'M', 'n': 'N', 'o': 'O', 'p': 'P', 'q': 'Q', 'r': 'R', 's': 'S'\
        , 't': 'T','u': 'U', 'v': 'V', 'w': 'W', 'x': 'X', 'y': 'Y', 'z': 'Z'}
    cap_next:bool=True
    return_string:str=''
    for character in string:
        if cap_next and character in letter_equivalents.keys():
            return_string=return_string+letter_equivalents[character]
        else:
            return_string=return_string+character
        if character==' ':
            cap_next=True
        else:
            cap_next=False
    return  return_string
def full_name(county:dict)->str:
    """full_name(county) Gives the full name of a county

    county: the county for which the name is to be given"""
    return capitalize(county['name'])+', '+county['state']
def criteria_winner(f,reverse:bool)->tuple[str,...]:
    """criteria_winner(f, mode) Finds the winning county(s) for a given criteria

    f: the criteria function
    reverse: True or False, True sorts from greatest to least and False sorts from least to greatest"""
    sort:list=sorted(data,key=f,reverse=reverse)
    first:dict=sort[0]
    counties:tuple=()
    for county in sort:
        if county==first:
            counties=counties+(full_name(county),)
        else:
            break
    return counties
def text_list(*items:str)->str:
    """text_list(*items) Gives a grammatically correct list

    *items: the items in the list"""
    if len(items)<1:
        raise ValueError('there must be at least one item')
    elif len(items)==1:
        return items[0]
    elif len(items)==2:
        return items[0]+' and '+items[1]
    else:
        return_string:str=''
        for index, item in enumerate(items):
            #not the last item
            if index!=len(items)-1:
                return_string=return_string+item+', '
            else:
                return_string=return_string+'and '+item
        return return_string
def header(text:str,level:int)->str:
    """header(text, level, file) Gives header text for a markdown file

    text: the text of the header
    level: 1-6, 1 is the largest"""
    return '#'*level+' '+text
def write_lines(file,*lines:str)->None:
    """write_lines(file, *lines) Writes lines to a markdown file, handling good practices automatically

    file: the markdown file
    *lines: the lines to be written"""
    to_write:str=''
    last_line:str=''
    for line in lines:
        #check for headers
        if line[0]=='#':
            if last_line=='plain':
                to_write=to_write+'\n'*2+line+'\n'*2
            elif last_line=='header':
                to_write=to_write+line+'\n'*2
            elif last_line=='':
                to_write=to_write+'\n'+line+'\n'*2
            last_line = 'header'
        #check for normal text
        else:
            if last_line=='header' or last_line=='':
                to_write=to_write+line
            elif last_line=='plain':
                to_write=to_write+'<br>'+line
            last_line='plain'
    file.write(to_write)