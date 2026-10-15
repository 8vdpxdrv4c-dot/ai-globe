import json,numpy as np
from PIL import Image,ImageDraw,ImageFilter
Image.MAX_IMAGE_PIXELS=None
L=lambda f:json.load(open(f))['features']
land10=L('ne_10m_land.geojson');lakes10=[f for f in L('ne_10m_lakes.geojson') if (f['properties'].get('scalerank') or 0)<=8]
coast10=L('ne_10m_coastline.geojson');cb=L('chn_borders.geojson');dash=L('chn_dashline.geojson')  # PRC-standard, see make_borders_chn.py
adm1=L('chn_adm1_internal.geojson')
GR=Image.open('GRAY_HR_SR_OB.tif')
def rings(g):
    t=g['type'];c=g['coordinates']
    return {'Polygon':lambda:[c],'MultiPolygon':lambda:c,'LineString':lambda:[[c]],'MultiLineString':lambda:[[x] for x in c]}.get(t,lambda:[])()
def render(lon0,lon1,lat0,lat1,W,H,out,lw=1.0,q=85):
    S=2;WS,HS=W*S,H*S
    P=lambda x,y,s:((x-lon0)/(lon1-lon0)*W*s,(lat1-y)/(lat1-lat0)*H*s)
    def inb(r):
        xs=[p[0] for p in r];ys=[p[1] for p in r]
        return max(xs)>=lon0-1 and min(xs)<=lon1+1 and max(ys)>=lat0-1 and min(ys)<=lat1+1
    def fill(feats):
        m=Image.new('L',(W,H),0);d=ImageDraw.Draw(m)
        for f in feats:
            for poly in rings(f['geometry']):
                for i,r in enumerate(poly):
                    if len(r)>2 and inb(r): d.polygon([P(x,y,1) for x,y,*_ in r],fill=255 if i==0 else 0)
        return np.asarray(m,dtype=np.float32)/255
    def lines(feats,width):
        m=Image.new('L',(WS,HS),0);d=ImageDraw.Draw(m)
        for f in feats:
            for poly in rings(f['geometry']):
                for r in poly:
                    if len(r)<2 or not inb(r): continue
                    pts=[P(x,y,S) for x,y,*_ in r];seg=[pts[0]]
                    for a,b in zip(pts,pts[1:]):
                        if abs(a[0]-b[0])>WS/2:
                            if len(seg)>1:d.line(seg,fill=255,width=width,joint='curve')
                            seg=[b]
                        else: seg.append(b)
                    if len(seg)>1:d.line(seg,fill=255,width=width,joint='curve')
        return np.asarray(m.resize((W,H),Image.LANCZOS),dtype=np.float32)/255
    gw,gh=GR.size
    box=((lon0+180)/360*gw,(90-lat1)/180*gh,(lon1+180)/360*gw,(90-lat0)/180*gh)
    g=np.asarray(GR.resize((W,H),Image.LANCZOS,box=box),dtype=np.float32)/255
    land=fill(land10);land=np.asarray(Image.fromarray((land*255).astype('uint8')).filter(ImageFilter.GaussianBlur(.8)),dtype=np.float32)/255
    lake=fill(lakes10)
    gl=np.clip((g-0.55)*1.3+0.5,0,1)
    landc=np.stack([0.86+0.20*(gl-0.5)*2]*3,-1)*np.array([1.0,0.995,0.982])*(0.84+0.2*gl[...,None])
    ob=np.clip((g-0.35)/0.4,0,1)
    ocean=np.array([0.74,0.85,0.93])[None,None,:]*(0.93+0.09*ob[...,None])
    water=np.clip((1-land)+lake,0,1)[...,None]
    col=landc*(1-water)+ocean*water
    def ink(col,m,c,a): m=m[...,None]*a; return col*(1-m)+np.array(c)[None,None,:]*m
    w=lambda x:max(2,int(round(x*lw*S)))
    col=ink(col,lines(adm1,w(1.4)),[0.50,0.54,0.60],0.6)
    col=ink(col,lines(coast10,w(1.3)),[0.40,0.54,0.66],0.8)
    col=ink(col,lines(cb,w(2.2)),[0.42,0.42,0.48],0.85)
    col=ink(col,lines(dash,w(2.6)),[0.42,0.42,0.48],0.9)
    Image.fromarray((np.clip(col,0,1)*255).astype('uint8')).save(out,quality=q,optimize=True,progressive=True);print(out)
T='/workspace/ai-globe/textures/'
import sys
if 'world' in sys.argv: render(-180,180,-90,90,8192,4096,T+'map_8k.jpg',lw=1.0,q=84)
if 'us' in sys.argv: render(-126,-66,24,50,3600,1560*1,T+'patch_us.jpg',lw=1.0)
if 'cn' in sys.argv: render(73,135,18,54,3720,2160,T+'patch_cn.jpg',lw=1.0)
