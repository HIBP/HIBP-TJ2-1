'''
Define main parameters of TJ-II HIBP-1 geometry
'''
import numpy as np
import hibplib as hb


# %%
def define_geometry(config):
    '''

    Parameters
    ----------
    config : str
        tj2 magnetic cofiguration, e.g. '100_44_64'

    Returns
    -------
    geom : Geometry
        Geometry object with a proper configuration.

    '''

    geom = hb.Geometry()

    # plasma parameters
    geom.R = 1.5  # major radius of the torus [m]
    geom.r_plasma = 0.4  # plasma minor radius [m]
    geom.elon = 1.  # plasma elongation

    # PRIMARY beamline geometry
    # alpha and beta angles of the PRIMARY beamline [deg]
    dalpha = -1.2  #0.0
    dbeta = 11.0  # 13.5  # 0.0
    alpha_prim = 75.2 + dalpha
    beta_prim = -22. + dbeta
    gamma_prim = 0.
    prim_angles = {'r0': np.array([alpha_prim, beta_prim, gamma_prim]),
                   'A1': np.array([alpha_prim, beta_prim, gamma_prim]),
                   'B1': np.array([alpha_prim, beta_prim, gamma_prim]),
                   'B2': np.array([alpha_prim, beta_prim, gamma_prim]),
                   'A2': np.array([alpha_prim, beta_prim, gamma_prim])}
    geom.angles_dict.update(prim_angles)

    # coordinates of the injection port [m]
    xport_in = 1.34817
    yport_in = 0.8658
    zport_in = 0.
    geom.r_dict['port_in'] = np.array([xport_in, yport_in, zport_in])

    # distance from the injection port to the Alpha2 plates
    dist_A2 = 0.2305  # [m]
    # distance from Alpha2 plates to the Beta2 plates
    dist_B2 = 0.19  # [m]
    # distance from Beta2 plates to the Beta1 plates
    dist_B1 = 0.39
    # distance from Beta1 plates to the Alpha1 plates
    dist_A1 = 0.18
    # distance from Alpha1 plates to the initial point of the traj [m]
    dist_r0 = 0.2

    # coordinates of the center of the ALPHA2 plates
    geom.add_coords('A2', 'port_in', dist_A2, geom.angles_dict['A2'])
    # coordinates of the center of the BETA2 plates
    geom.add_coords('B2', 'A2', dist_B2, geom.angles_dict['B2'])
    # coordinates of the center of the BETA2 plates
    geom.add_coords('B1', 'B2', dist_B1, geom.angles_dict['B1'])
    # coordinates of the center of the BETA2 plates
    geom.add_coords('A1', 'B1', dist_A1, geom.angles_dict['A1'])
    # coordinates of the initial point of the trajectory [m]
    geom.add_coords('r0', 'A1', dist_r0, geom.angles_dict['r0'])

    # AIM position (BEFORE the Secondary beamline) [m]
    # coordinates of the output port
    xport_out = 2.3786
    yport_out = -0.38
    zport_out = -0.03677 + 0.02
    geom.r_dict['port_out'] = np.array([xport_out, yport_out, zport_out])

    # SECONDARY beamline geometry
    # alpha and beta angles of the SECONDARY beamline [deg]
    alpha_sec = 0.
    beta_sec = 13.15
    gamma_sec = 0.
    sec_angles = {'aim': np.array([alpha_sec, beta_sec, gamma_sec]),
                  'A3': np.array([alpha_sec, beta_sec, gamma_sec]),
                  'B3': np.array([alpha_sec, beta_sec, gamma_sec]),
                  'an': np.array([alpha_sec, beta_sec, gamma_sec])}
    geom.angles_dict.update(sec_angles)

    # distance from port to aim
    dist_aim = 0.166
    # distance from port to the Beta3 center
    dist_B3 = 0.222
    # distance from Beta3 to the Alpha3 center
    dist_A3 = 0.2  # 0.19  # + 0.6
    # distance from Beta3 to the entrance slit of the analyzer
    dist_s = 0.63

    # coordinates of the center of the new aim point
    # geom.add_coords('aim', 'port_out', dist_B3-0.1, geom.angles_dict['A3'])
    # coordinates of the center of the Alpha3 plates
    geom.add_coords('B3', 'port_out', dist_B3, geom.angles_dict['A3'])
    geom.add_coords('aim', 'B3', dist_A3-0.075, geom.angles_dict['A3'])
    # coordinates of the center of the Beta3 plates
    geom.add_coords('A3', 'B3', dist_A3, geom.angles_dict['A3'])
    # coordinates of the slit
    geom.add_coords('slit', 'B3', dist_s, geom.angles_dict['A3'])
    geom.r_dict['an'] = geom.r_dict['slit']

    # print info
    print('\nPrimary beamline angles: ', geom.angles_dict['r0'])
    print('Secondary beamline angles: ', geom.angles_dict['A3'])
    print('r0 = ', np.round(geom.r_dict['r0'], 3))
    print('r_aim = ', np.round(geom.r_dict['aim'], 3))
    print('r_slit = ', np.round(geom.r_dict['slit'], 3))

    # TJ-II GEOMETRY
    # chamber entrance and exit coordinates
    geom.chamb_ent = [(0.8, 0.5805), (1.1, 0.5805),
                      (1.43, 0.5805), (1.8, 0.5805)]
    geom.chamb_ext = [(1.89, -0.28), (1.89, 0.0),
                      (1.89, -0.66), (1.89, -0.9),
                      (1.58, -0.52), (1.58, -0.9)]
    geom.chamb = [(1.415, -0.07136), (1.4007, -0.04931),
                  (1.4007, -0.04931), (1.3919, -0.02453),
                  (1.3919, -0.02453), (1.389, 0.00162),
                  (1.389, 0.00162), (1.3925, 0.0277),
                  (1.3925, 0.0277), (1.4021, 0.05218),
                  (1.4021, 0.05218), (1.416, 0.07456),
                  (1.416, 0.07456), (1.4302, 0.09681),
                  (1.4302, 0.09681), (1.4443, 0.11909)]

    # Camera contour
    geom.camera = np.loadtxt('TJII_camera.dat')
    # Separatrix contour
    geom.sep = np.loadtxt('configs//' + config + '.txt')

    for key in geom.r_dict.keys():
        # shift along X, Y or Z axis
        geom.r_dict[key][0] += 0.0  # 0.0025
        geom.r_dict[key][1] += 0.0  # 0.05
        geom.r_dict[key][2] += 0.0

    return geom
