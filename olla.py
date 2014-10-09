#!/bin/env python

import sys
import imp
import json

def dicts(base=''):
    print base + 'dicts.py'
    d = imp.load_source('', base + 'dicts.py')
    return json.dumps(d.dicts)

def get_dict(lang, base=''):
    d = imp.load_source('dict_dst', base + lang)
    return json.dumps(d.dictionary)

def translate(src, dst, word, base=''):
    src = imp.load_source('dict_src', base + src)
    dst = imp.load_source('dict_dst', base + dst)

    return json.dumps({"word": word,
                       "src": src.dictionary[word],
                       "dst": dst.dictionary[word]})

if __name__ == "__main__":
    base = 'dicts/'
    #print dicts(base)
    #print get_dict(sys.argv[1],base)
    print translate(sys.argv[1], sys.argv[2], int(sys.argv[3]),base)
