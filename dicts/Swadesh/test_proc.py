#coding: utf-8

from proc import proc
from Slavic.Russian import dictionary as ru
from wtypes import dictionary as tp
from itertools import product

tp_w = {}
for i, w in sorted(ru.iteritems()):
    t = tp.get(i)
    if not t:
        continue
    tp_w.setdefault(t, []).append(w)
r_tp = {
    't': 't',
    'l': 'l',
    's': 's',
    'w': 'w',
    'a': 's',
    'o': 's',
    'h': 'h',
    'i': 'i',
    'q': 's',
    'd': 'd',
    'p': 'p'
}
tp_w['t']=['вчера', 'вечером', 'в десять вечера']
tp_w['l']=['дома', 'в Москве', 'на столе']
tp_w['w']=['громко', 'как дятел']
tp_w['h']=['из лесу', 'из-за дома']
tp_w['i']=['поганою метлой', 'зубами']
tp_w['d']=['домой', 'в Швецию']

for v, vt in sorted(proc.iteritems()):
    vt = vt.split("|", 1)[0] # Пока не учитываем ограничения
    l = list(filter(lambda c: tp_w.get(r_tp.get(c)), vt))
    vpos = l.index("s") + 1
    l.insert(vpos, "v")
    for comb in product(
        *(
            tp_w.get(r_tp.get(c))
            for c in vt
            if tp_w.get(r_tp.get(c))
        )
    ):
        comb = list(comb)
        comb.insert(vpos, ru[v])
        print " ".join(
            w + "/" + c
            for w, c in zip(comb, l)
        )
