#!/bin/env python

import sys
import imp
import json

def dicts(base=''):
    print base + 'dicts.py'
    d = imp.load_source('', base + 'dicts.py')
    return json.dumps(d.dicts)

def get_dict(lang, wtypes=None, wtype=None, base=''):
    d = imp.load_source('dict_dst', base + lang)
    print base + lang
    if wtype and wtypes:
        out = {}
        print base + 'types.py'
        t = imp.load_source('dict_typ', base + wtypes)
        for i in d.dictionary.keys():
            if t.dictionary[i] == wtype:
                out[i] = d.dictionary[i]
        d.dictionary = out

    return json.dumps(d.dictionary)

def translate(word, src, dst, base=''):
    src = imp.load_source('dict_src', base + src)

    if type(dst) == type(""):
        dst = [dst]

    out = None

    for d in dst:
        try:
            d = imp.load_source('dict_dst', base + d)
            out = d.dictionary[word]            
        except KeyError:
            continue
        if out:
            break

    if out == None:
        out = src.dictionary[word]

    return json.dumps({"word": word,
                       "src": src.dictionary[word],
                       "dst": out})

if __name__ == "__main__":
    base = 'dicts/'
    #print dicts(base)
    #print get_dict(sys.argv[1], sys.argv[2], sys.argv[3], base)
    print translate(int(sys.argv[1]), sys.argv[2], sys.argv[3:], base)
