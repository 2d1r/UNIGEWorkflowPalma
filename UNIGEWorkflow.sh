#!/bin/sh

unzip kba_ch_clean.zip

unzip One_WDPA.zip

ogr2ogr -dialect sqlite -sql "SELECT k.SitRecID, ST_INTERSECTION (k.geometry, w.geometry) AS new, SUM ( ST_AREA ( ST_TRANSFORM ( ST_INTERSECTION (k.geometry, w.geometry), 2056 ) ) ) AS area FROM kba_ch_clean k, One_WDPA w WHERE ST_INTERSECTS(k.geometry, w.geometry) GROUP BY k.SitRecID" intersection_out.shp input.vrt

ogr2ogr -dialect sqlite -sql "SELECT a.SitRecID, a.geometry, ST_AREA ( ST_TRANSFORM (a.geometry, 2056 ) ) AS area FROM kba_ch_clean a" area_out.shp kba_ch_clean.shp

python computeSDGIndicator.py >> output.txt


