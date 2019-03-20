import collections

def sort_json_on_index(dct):
    '''
    I/P : Json object with one of the key being indexes and corresponding value is a dictionay
            contains the key,val pairs. Where the value is a key in the json object
    O/P : Sorted key,val pair of the json object except indexes where the order depends on the
            key of the indexes dictionary corresponding to the key of the json object
    Example : I/P: {"k2":"val3","k1":"val1","k3":"val3","indexes":{"0":"k3","1":"k2","2":"k1"}}  
              O/P: {"k3":"val3","k2":"val2","k1":"val1"}
    '''
    #unordered dictionay to capture the output in the order of insertion
    out_dict=collections.OrderedDict()
    #get the indexes from the json/dict
    idx_unsrtd=dct['indexes']
    #sort the indexes dict based on the int(key)
    idx_srtd=sorted(idx_unsrtd.items(),key=lambda pair: int(pair[0]))

    for pair in idx_srtd:
        if pair[1] in dct:
            out_dict[pair[1]]=dct[pair[1]]
    
    return out_dict
def print_dct_in_json(dct):
    '''
    Beautify the unordered dictionay according to expected output
    '''
    print("{")
    for pair in dct.items():
        print('"{}":"{}",'.format(pair[0],pair[1]))
    print("}")

dct={
    "k4":"val4",
    "k1":"val1",
    "k9":"val9",
    "k8":"val8",
    "k5":"val5",
    "k7":"val7",
    "k6":"dummy",
    "k2":"val2",
    "k3":"val3",
    "k10":"any val",
    "indexes":{
        "1":"k5",
        "7":"k8",
        "2":"k1",
        "8":"k3",
        "6":"k4",
        "0":"k2",
        "3":"k9",
        "4":"k6",
        "5":"k7",
        "9":"k10"
    }
}

print_dct_in_json(sort_json_on_index(dct))
