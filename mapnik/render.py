#!/usr/bin/env python3

import mapnik

mapfile = 'ready_style.xml'
map_output = 'mymap.png'
ll=(55.8851814,37.6125984)

merc = mapnik.Projection('+proj=merc +a=6378137 +b=6378137 +lat_ts=0.0 +lon_0=0.0 +x_0=0.0 +y_0=0 +k=1.0 +units=m +nadgrids=@null +no_defs +over')
longlat = mapnik.Projection('+proj=longlat +ellps=WGS84 +datum=WGS84 +no_defs')

m = mapnik.Map(800,600)
mapnik.load_map(m, mapfile)
#bbox=mapnik.Box2d(37.1,55.45,38,56.05)
#bbox=mapnik.Box2d(37.6020,55.7107,37.6087,55.7137365)
bbox=mapnik.Box2d(ll[1]-0.0033,ll[0]-0.00151825,ll[1]+0.0033,ll[0]+0.00151825)
transform = mapnik.ProjTransform(longlat,merc)
merc_bbox = transform.forward(bbox)

m.aspect_fix_mode = mapnik.aspect_fix_mode.GROW_BBOX

m.zoom_to_box(merc_bbox)
print("Scale = " , m.scale())
print(mapnik.mapnik_version())
mapnik.render_to_file(m, map_output)