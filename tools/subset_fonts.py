# Regenerate /fonts subsets: existing glyph set + all text in data.js/index.html
import sys
from fontTools.ttLib import TTFont
from fontTools.varLib import instancer
from fontTools import subset
SRC='/workspace/fontsrc/'
txt=open('data.js').read()+open('index.html').read()
for fam,w in [('NotoSansSC',400),('NotoSansSC',500),('NotoSansSC',700),('NotoSerifSC',700)]:
    out=f'fonts/{fam}-{w}.woff2'
    old=set(TTFont(out).getBestCmap())
    uni=old|{ord(c) for c in txt if ord(c)>=32}
    f=instancer.instantiateVariableFont(TTFont(SRC+fam+'.ttf'),{'wght':w})
    o=subset.Options();o.flavor='woff2';o.layout_features=['*']
    s=subset.Subsetter(o);s.populate(unicodes=uni);s.subset(f);f.flavor='woff2';f.save(out);print(out,len(uni))
