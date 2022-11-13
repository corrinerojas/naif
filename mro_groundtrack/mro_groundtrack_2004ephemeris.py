import spiceypy as spice

spice.furnsh("mro.mk")
# Step is 300 seconds, or 5 min
step = 300

utc = ['2022-01-17T16:00:00','2022-01-18T00:00:00' ]

etStart = spice.str2et(utc[0])
etEnd = spice.str2et(utc[1])
etNow = etStart
print('# Time, Longitude, Latitude, Altitude, Phase Angle, Solar Incidence Angle, Emission Angle')
while etNow < etEnd:
    spoint = spice.subpnt('INTERCEPT/ELLIPSOID', 'MARS', etNow, 'IAU_MARS', 'NONE', 'MRO')
    illum = spice.illumg('ELLIPSOID', 'MARS', 'SUN', etNow, 'IAU_MARS', 'NONE', 'MRO', spoint[0])
    spstuff = spice.reclat(spoint[0])
    if spstuff[1] < 0:
        lon = 360 + (spstuff[1] * spice.dpr())
    else:
        lon = spstuff[1] * spice.dpr()
    lat = spstuff[2] * spice.dpr()
    str_curr = spice.et2utc(etNow, 'ISOC', 4, 26)
    print('%s %s %s %s %s %s %s' % (str_curr, lon, lat, spstuff[0], illum[2]*spice.dpr(), illum[3]*spice.dpr(), illum[4]*spice.dpr()))
    # Add the et_step as increment
    etNow += step
