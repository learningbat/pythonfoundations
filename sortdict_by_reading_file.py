import json
import collections
import sys

#read the json file and return a dic object
def json_file_to_dict(json_file):
    with open('data.json') as jsf:
        return json.loads(jsf.read())
#get the value for the key indexes         
def get_indexes(dict,indexkey):
    if indexkey in dict:
        return dict[indexkey]
    return -1
#sort the indexes dictinary
def sort_dict(dict):
    return sorted(dict.items(),key=lambda pair: int(pair[0]))
#sort the original dict using indexes dictionary
def sort_using_index(dict,index):
    out_dict=collections.OrderedDict()
    for pair in index:
        if pair[1] in dict:
            out_dict[pair[1]]=dict[pair[1]]
    return out_dict
#conver back the dict objec to json
def from_dict_json(dict):
    dict=json.dumps(dict)
    out_json=json.loads(dict)
    return out_json
#prettyfy the json output
def print_json_prettyfy(out_json):
    print(json.dumps(out_json,indent=4))
#main fucntion to call other methods
def main():
    file_name=input("Enter the file name :")
    dict=json_file_to_dict(file_name)
    idx_dict=get_indexes(dict,'indexes')
    if idx_dict==-1:
        sys.exit(-1)
    srt_idx=sort_dict(idx_dict)
    out_dict=sort_using_index(dict,srt_idx)
    out_json=from_dict_json(out_dict)
    print_json_prettyfy(out_json)
#invoking the main
if __name__ == "__main__":
    main()
    
