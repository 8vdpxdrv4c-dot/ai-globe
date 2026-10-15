# Build PRC-standard boundary layers from Natural Earth China point-of-view data.
# Run in /workspace/src. Inputs: ne_10m_admin_0_countries_chn.geojson, ne_10m_admin_1_states_provinces.geojson,
# ne_10m_admin_0_boundary_lines_maritime_indicator_chn.geojson
# Outputs: chn_borders.geojson (national land borders; Taiwan/HK/Macau merged into China, 藏南/阿克赛钦 inside China),
#          chn_adm1_internal.geojson (internal province/state lines, CHN incl. 台湾/香港/澳门 + USA),
#          chn_dashline.geojson (南海断续线 9 dashes from NE + 10th dash east of Taiwan)
import json
from shapely.geometry import shape,mapping,LineString,MultiLineString
from shapely.ops import unary_union
L=lambda f:json.load(open(f))['features']
CHN={'CHN','TWN','HKG','MAC'}
def dump(fn,geoms):
    json.dump({'type':'FeatureCollection','features':[{'type':'Feature','properties':{},'geometry':mapping(g)} for g in geoms if not g.is_empty]},open(fn,'w'))
def internal(polys):
    # lines shared by >=2 polygons = boundary of each minus the outer boundary of the union
    bnd=unary_union([p.boundary for p in polys])
    outer=unary_union(polys).boundary.buffer(0.02)
    return bnd.difference(outer)
cs={}
for f in L('ne_10m_admin_0_countries_chn.geojson'):
    a=f['properties']['ADM0_A3'];a='CHN' if a in CHN else a
    g=shape(f['geometry']).buffer(0)
    cs[a]=cs[a].union(g) if a in cs else g
print('countries',len(cs))
bnd=unary_union([g.boundary for g in cs.values()])
land=unary_union(list(cs.values())).boundary.buffer(0.02)
dump('chn_borders.geojson',[bnd.difference(land)])
ad=[f for f in L('ne_10m_admin_1_states_provinces.geojson')]
out=[]
for grp in (CHN,{'USA'}):
    ps=[shape(f['geometry']).buffer(0) for f in ad if f['properties']['adm0_a3'] in grp and not (grp is CHN and f['properties']['adm0_a3']=='TWN')]
    if grp is CHN: ps.append(unary_union([shape(f['geometry']).buffer(0) for f in ad if f['properties']['adm0_a3']=='TWN']))  # 台湾省 as one province
    out.append(internal(ps))
dump('chn_adm1_internal.geojson',out)
dash=[shape(f['geometry']) for f in L('ne_10m_admin_0_boundary_lines_maritime_indicator_chn.geojson')
      if 105<shape(f['geometry']).bounds[0]<126 and shape(f['geometry']).bounds[1]<24]
dash.append(LineString([(122.55,22.85),(122.75,24.15)]))  # 10th dash between Taiwan and Yonaguni
print('dashes',len(dash));dump('chn_dashline.geojson',dash)
