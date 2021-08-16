import numpy as np

# Solar constant
Gsc = 1367.

# Pacific Grove
lat = np.deg2rad(36.62)
lon = -121.92

def irradiation(n, t):
    
    # Declination angle (delta)
    dec_ang = np.deg2rad(23.44 * np.sin(np.deg2rad(360 * (284+n) / 365.)))
    
    # Hour angle (omega)
    tz_lon = -120.
    B = (n - 1) * 360/365.
    E = 229.2 * (7.5e-5 + 1.868e-3 * np.cos(B) - 3.2077e-2 * np.sin(B) \
                 - 1.4615e-2 * np.cos(2*B) - 4.089e-2 * np.sin(2*B))
    tS = t[3] + (t[4]/60.) + (4 * (lon - tz_lon) + E) / 60.
    omega = np.deg2rad(15. * (tS - 12.))
    
    # Sun altitude
    #hs = np.arcsin(np.cos(lat)*np.cos(dec_ang)*np.cos(omega) \
    #               + np.sin(lat)*np.sin(dec_ang))
    
    # Solar azimuth
    #gamma = np.arcsin(np.cos(dec_ang)*np.sin(omega)/np.cos(hs))
    
    # Zenith angle
    thetaZ = np.arccos(np.cos(lat) * np.cos(dec_ang) * np.cos(omega) \
                       + np.sin(lat) * np.sin(dec_ang))
    
    # Irradiation incident TOA at theta = 0
    Gon = Gsc * (1. + 0.033 * np.cos(np.deg2rad(360*n/365.)))
    #Go = Gon * (np.cos(lat)*np.cos(dec_ang)*np.cos(omega) \
    #            + np.sin(lat)*np.sin(dec_ang))
    
    # Beam radiation
    r0, r1, rk, A = 0.97, 0.99, 1.02, 0.
    a0 = r0 * (0.4237 - 0.00821 * (6 - A)**2)
    a1 = r1 * (0.5055 + 0.00595 * (6.5 - A)**2)
    k  = rk * (0.2711 + 0.01858 * (2.5 - A)**2)
    Tb = a0 + a1 * np.e**(-k/np.cos(thetaZ))
    Gcb = Tb * Gon * (np.cos(lat)*np.cos(dec_ang)*np.cos(omega) \
                      + np.sin(lat)*np.sin(dec_ang))

    # Diffuse radiation
    Td = 0.271 - 0.294 * Tb
    Gcd = Td * Gon * (np.cos(lat)*np.cos(dec_ang)*np.cos(omega) \
                      + np.sin(lat)*np.sin(dec_ang))

    # Total radiation
    return Gcb + Gcd