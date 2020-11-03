import re


d={
'&arrow;':'<MarkersSymbolizer placement="line" marker-type="arrow" spacing="150" allow-overlap="true" max-error="0.3" stroke-width="0.5" stroke="white" fill="#8c7d4a" transform="scale(0.7 0.6)"/>',
'&mapid;':'1',
'&bigroadcolor;':'#f0d06e',
'&tunnelcolor;':'#FFE895',
'&downcolor;':'#bea3a3',
'&maxscale_zoom0;':'<MaxScaleDenominator>250000000000</MaxScaleDenominator>',
'&maxscale_zoom1;':'<MaxScaleDenominator>500000000</MaxScaleDenominator>',
'&minscale_zoom1;':'<MinScaleDenominator>200000000</MinScaleDenominator>',
'&maxscale_zoom2;':'<MaxScaleDenominator>200000000</MaxScaleDenominator>',
'&minscale_zoom2;':'<MinScaleDenominator>100000000</MinScaleDenominator>',
'&maxscale_zoom3;':'<MaxScaleDenominator>100000000</MaxScaleDenominator>',
'&minscale_zoom3;':'<MinScaleDenominator>50000000</MinScaleDenominator>',
'&maxscale_zoom4;':'<MaxScaleDenominator>50000000</MaxScaleDenominator>',
'&minscale_zoom4;':'<MinScaleDenominator>25000000</MinScaleDenominator>',
'&maxscale_zoom5;':'<MaxScaleDenominator>25000000</MaxScaleDenominator>',
'&minscale_zoom5;':'<MinScaleDenominator>12500000</MinScaleDenominator>',
'&maxscale_zoom6;':'<MaxScaleDenominator>12500000</MaxScaleDenominator>',
'&minscale_zoom6;':'<MinScaleDenominator>6500000</MinScaleDenominator>',
'&maxscale_zoom7;':'<MaxScaleDenominator>6500000</MaxScaleDenominator>',
'&minscale_zoom7;':'<MinScaleDenominator>3000000</MinScaleDenominator>',
'&maxscale_zoom8;':'<MaxScaleDenominator>3000000</MaxScaleDenominator>',
'&minscale_zoom8;':'<MinScaleDenominator>1500000</MinScaleDenominator>',
'&maxscale_zoom9;':'<MaxScaleDenominator>1500000</MaxScaleDenominator>',
'&minscale_zoom9;':'<MinScaleDenominator>750000</MinScaleDenominator>',
'&maxscale_zoom10;':'<MaxScaleDenominator>750000</MaxScaleDenominator>',
'&minscale_zoom10;':'<MinScaleDenominator>400000</MinScaleDenominator>',
'&maxscale_zoom11;':'<MaxScaleDenominator>400000</MaxScaleDenominator>',
'&minscale_zoom11;':'<MinScaleDenominator>200000</MinScaleDenominator>',
'&maxscale_zoom12;':'<MaxScaleDenominator>200000</MaxScaleDenominator>',
'&minscale_zoom12;':'<MinScaleDenominator>100000</MinScaleDenominator>',
'&maxscale_zoom13;':'<MaxScaleDenominator>100000</MaxScaleDenominator>',
'&minscale_zoom13;':'<MinScaleDenominator>50000</MinScaleDenominator>',
'&maxscale_zoom14;':'<MaxScaleDenominator>50000</MaxScaleDenominator>',
'&minscale_zoom14;':'<MinScaleDenominator>25000</MinScaleDenominator>',
'&maxscale_zoom15;':'<MaxScaleDenominator>25000</MaxScaleDenominator>',
'&minscale_zoom15;':'<MinScaleDenominator>12500</MinScaleDenominator>',
'&maxscale_zoom16;':'<MaxScaleDenominator>12500</MaxScaleDenominator>',
'&minscale_zoom16;':'<MinScaleDenominator>5000</MinScaleDenominator>',
'&maxscale_zoom17;':'<MaxScaleDenominator>5000</MaxScaleDenominator>',
'&minscale_zoom17;':'<MinScaleDenominator>2500</MinScaleDenominator>',
'&maxscale_zoom18;':'<MaxScaleDenominator>2500</MaxScaleDenominator>',
'&minscale_zoom18;':'',
'/storage/www/moscowmap/moscowmap.ru/htdocs/leaflet/':'',
"&datasource;":"""<Parameter name='type'>postgis</Parameter>
<Parameter name='password'>qaz</Parameter>
<Parameter name='host'>pg</Parameter>
<Parameter name='port'>5432</Parameter>
<Parameter name='user'>postgres</Parameter>
<Parameter name='dbname'>template_postgis</Parameter>"""}


with open('tstyle.xml', 'r') as in_file:
	s = in_file.read()

pattern = re.compile('|'.join(d.keys()))
result = pattern.sub(lambda x: d[x.group()], s)

with open('ready_style.xml', 'w') as out_file:
	out_file.write(result)
