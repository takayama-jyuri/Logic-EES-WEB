# envelope performance simple unit test
import unittest
import nbimporter

from EnvelopePerformanceSimple import simpleEnvPerformanceSelected as SEPS

class TestSEPS(unittest.TestCase):
    
    def test_gen_includingQdashMhMc(self):
        
        test_patterns = [
                ('region6', 'base_ins',  0.240, 0.530, 0.480, 2.330, 3.490, 0.510, 0.510, 'yes', 1.0, 1.0, 'yes', 0.0, 0.0, 2.8794288888888886, 0.94, 3.3, 3.1, 0.09495988888888889, 0.10108633333333332)
                ]
        for region, house_type, U_roof, U_wall, U_floorOther, U_door, U_window, eta_d_cooling, eta_d_heating, fValue_useDefault, fValue_heating, fValue_cooling, psi_useDefault, psi_perimeterOther, psi_perimeterEntrance, expected_Qdash, expected_UA, expected_etaAH, expected_etaAC, expected_muC, expected_muH in test_patterns:
            with self.subTest():
                spec = {
                        'house_type' : house_type,
                        'region'     : region,
                        'U' : {
                                'roof'         : U_roof,
                                'wall'         : U_wall,
                                'door'         : U_door,
                                'window'       : U_window,
                                'floorOther'   : U_floorOther,
                                'baseOther'    : 0.000,
                                'baseEntrance' : 0.000
                                },
                        'psi' : {
                                'useDefault'        : psi_useDefault,
                                'perimeterOther'    : psi_perimeterOther,
                                'perimeterEntrance' : psi_perimeterEntrance
                                },
                        'eta_d' : {
                                'heating' : eta_d_heating,
                                'cooling' : eta_d_cooling
                                },
                        'fValue' : {
                                'useDefault' : fValue_useDefault,
                                'heating'    : fValue_heating,
                                'cooling'    : fValue_cooling
                                }
                        }
                actual_Qdash = SEPS(spec)['Qdash']
                actual_UA    = SEPS(spec)['UA']
                actual_etaAH = SEPS(spec)['etaAH']
                actual_etaAC = SEPS(spec)['etaAC']
                actual_muH   = SEPS(spec)['muH']
                actual_muC   = SEPS(spec)['muC']
                self.assertAlmostEqual(actual_Qdash, expected_Qdash, delta = 0.000001)        
                self.assertAlmostEqual(actual_UA,    expected_UA,    delta = 0.000001)
                self.assertAlmostEqual(actual_etaAH, expected_etaAH, delta = 0.000001)
                self.assertAlmostEqual(actual_etaAC, expected_etaAC, delta = 0.000001)
                self.assertAlmostEqual(actual_muC,   expected_muC,   delta = 0.000001)
                self.assertAlmostEqual(actual_muH,   expected_muH,   delta = 0.000001)

    def test_gen(self):
        
        test_patterns = [
                ('region1', 'floor_ins',          7.700, 6.670, 5.270, 4.650, 6.510, 0.700, 0.700, 'yes', 1.00, 1.00, 'yes', 0.000, 0.000, 6.13, 13.9, 14.7),
                ('region2', 'floor_ins',          7.700, 6.670, 5.270, 4.650, 6.510, 0.700, 0.700, 'yes', 1.00, 1.00, 'yes', 0.000, 0.000, 6.13, 14.0, 14.3),
                ('region3', 'floor_ins',          7.700, 6.670, 5.270, 4.650, 6.510, 0.700, 0.700, 'yes', 1.00, 1.00, 'yes', 0.000, 0.000, 6.13, 13.8, 14.3),
                ('region4', 'floor_ins',          7.700, 6.670, 5.270, 4.650, 6.510, 0.700, 0.700, 'yes', 1.00, 1.00, 'yes', 0.000, 0.000, 6.13, 13.4, 13.9),
                ('region5', 'floor_ins',          7.700, 6.670, 5.270, 4.650, 6.510, 0.700, 0.700, 'yes', 1.00, 1.00, 'yes', 0.000, 0.000, 6.13, 13.8, 14.8),
                ('region6', 'floor_ins',          7.700, 6.670, 5.270, 4.650, 6.510, 0.700, 0.700, 'yes', 1.00, 1.00, 'yes', 0.000, 0.000, 6.13, 13.5, 14.4),
                ('region7', 'floor_ins',          7.700, 6.670, 5.270, 4.650, 6.510, 0.700, 0.700, 'yes', 1.00, 1.00, 'yes', 0.000, 0.000, 6.13, 13.2, 14.8),
#                ('region8', 'floor_ins',          7.700, 6.670, 5.270, 4.650, 6.510, 0.700, 0.700, 'yes', 1.00, 1.00, 'yes', 0.000, 0.000, 6.13, 13.7,  0.0),
                ('region1', 'base_ins',           7.700, 6.670, 5.270, 4.650, 6.510,  0.70,  0.70, 'yes', 1.00, 1.00, 'yes', 0.000, 0.000, 5.44, 13.5, 14.1),
                ('region1', 'floor_and_base_ins', 7.700, 6.670, 5.270, 4.650, 6.510,  0.70,  0.70, 'yes', 1.00, 1.00, 'yes', 0.000, 0.000, 6.13, 13.9, 14.7),
                ('region1', 'floor_ins',          0.000, 6.670, 5.270, 4.650, 6.510,  0.70,  0.70, 'yes', 1.00, 1.00, 'yes', 0.000, 0.000, 4.66,  8.9,  9.7),
                ('region1', 'floor_ins',          7.700, 6.670, 5.270, 4.650, 6.510,  0.70,  0.70, 'yes', 1.00, 1.00, 'yes', 0.000, 0.000, 6.13, 13.9, 14.7),
                ('region1', 'floor_ins',          9.999, 6.670, 5.270, 4.650, 6.510,  0.70,  0.70, 'yes', 1.00, 1.00, 'yes', 0.000, 0.000, 6.57, 15.4, 16.2),
                ('region1', 'floor_ins',          7.700, 0.000, 5.270, 4.650, 6.510,  0.70,  0.70, 'yes', 1.00, 1.00, 'yes', 0.000, 0.000, 3.05,  9.0,  9.1),
                ('region1', 'floor_ins',          7.700, 6.670, 5.270, 4.650, 6.510,  0.70,  0.70, 'yes', 1.00, 1.00, 'yes', 0.000, 0.000, 6.13, 13.9, 14.7),
                ('region1', 'floor_ins',          7.700, 9.999, 5.270, 4.650, 6.510,  0.70,  0.70, 'yes', 1.00, 1.00, 'yes', 0.000, 0.000, 7.67, 16.4, 17.5),
                ('region1', 'floor_ins',          7.700, 6.670, 0.000, 4.650, 6.510,  0.70,  0.70, 'yes', 1.00, 1.00, 'yes', 0.000, 0.000, 5.51, 13.9, 14.7),
                ('region1', 'floor_ins',          7.700, 6.670, 5.270, 4.650, 6.510,  0.70,  0.70, 'yes', 1.00, 1.00, 'yes', 0.000, 0.000, 6.13, 13.9, 14.7),
                ('region1', 'floor_ins',          7.700, 6.670, 9.999, 4.650, 6.510,  0.70,  0.70, 'yes', 1.00, 1.00, 'yes', 0.000, 0.000, 6.69, 13.9, 14.7),
                ('region1', 'floor_ins',          7.700, 6.670, 5.270, 4.650, 0.000,  0.70,  0.70, 'yes', 1.00, 1.00, 'yes', 0.000, 0.000, 5.32, 13.9, 14.7),
                ('region1', 'floor_ins',          7.700, 6.670, 5.270, 4.650, 6.510,  0.70,  0.70, 'yes', 1.00, 1.00, 'yes', 0.000, 0.000, 6.13, 13.9, 14.7),
                ('region1', 'floor_ins',          7.700, 6.670, 5.270, 4.650, 9.999,  0.70,  0.70, 'yes', 1.00, 1.00, 'yes', 0.000, 0.000, 6.57, 13.9, 14.7),
                ('region1', 'floor_ins',          7.700, 6.670, 5.270, 4.650, 6.510,  0.00,  0.70, 'yes', 1.00, 1.00, 'yes', 0.000, 0.000, 6.13, 10.1, 14.7),
                ('region1', 'floor_ins',          7.700, 6.670, 5.270, 4.650, 6.510,  0.70,  0.00, 'yes', 1.00, 1.00, 'yes', 0.000, 0.000, 6.13, 13.9, 10.6),
                ('region1', 'floor_ins',          7.700, 6.670, 5.270, 4.650, 6.510,  0.70,  0.70,  'no', 0.00, 0.51, 'yes', 0.000, 0.000, 6.13, 10.1, 13.8),
                ('region1', 'floor_ins',          7.700, 6.670, 5.270, 4.650, 6.510,  0.70,  0.70,  'no', 0.93, 0.51, 'yes', 0.000, 0.000, 6.13, 14.2, 13.8),
                ('region1', 'floor_ins',          7.700, 6.670, 5.270, 4.650, 6.510,  0.70,  0.70,  'no', 0.93, 0.00, 'yes', 0.000, 0.000, 6.13, 14.2, 10.6),
                ('region1', 'floor_ins',          7.700, 6.670, 5.270, 4.650, 6.510,  0.70,  0.70,  'no', 0.93, 0.51, 'yes', 0.000, 0.000, 6.13, 14.2, 13.8),
                ('region1', 'floor_ins',          7.700, 6.670, 5.270, 4.650, 6.510,  0.70,  0.70, 'yes', 1.00, 1.00,  'no', 0.000, 1.800, 6.09, 13.9, 14.7),
                ('region1', 'floor_ins',          7.700, 6.670, 5.270, 4.650, 6.510,  0.70,  0.70, 'yes', 1.00, 1.00,  'no', 1.800, 1.800, 6.13, 13.9, 14.7),
                ('region1', 'floor_ins',          7.700, 6.670, 5.270, 4.650, 6.510,  0.70,  0.70, 'yes', 1.00, 1.00,  'no', 9.999, 1.800, 6.32, 13.9, 14.7),
                ('region1', 'floor_ins',          7.700, 6.670, 5.270, 4.650, 6.510,  0.70,  0.70, 'yes', 1.00, 1.00,  'no', 1.800, 0.000, 6.10, 13.9, 14.7),
                ('region1', 'floor_ins',          7.700, 6.670, 5.270, 4.650, 6.510,  0.70,  0.70, 'yes', 1.00, 1.00,  'no', 1.800, 1.800, 6.13, 13.9, 14.7),
                ('region1', 'floor_ins',          7.700, 6.670, 5.270, 4.650, 6.510,  0.70,  0.70, 'yes', 1.00, 1.00,  'no', 1.800, 9.999, 6.30, 13.9, 14.7),
                ]
        for region, house_type, U_roof, U_wall, U_floorOther, U_door, U_window, eta_d_cooling, eta_d_heating, fValue_useDefault, fValue_cooling, fValue_heating, psi_useDefault, psi_perimeterOther, psi_perimeterEntrance, expected_UA, expected_etaAC, expected_etaAH in test_patterns:
            with self.subTest():
                spec = {
                        'house_type' : house_type,
                        'region'     : region,
                        'U' : {
                                'roof'         : U_roof,
                                'wall'         : U_wall,
                                'door'         : U_door,
                                'window'       : U_window,
                                'floorOther'   : U_floorOther,
                                'baseOther'    : 0.000,
                                'baseEntrance' : 0.000
                                },
                        'psi' : {
                                'useDefault'        : psi_useDefault,
                                'perimeterOther'    : psi_perimeterOther,
                                'perimeterEntrance' : psi_perimeterEntrance
                                },
                        'eta_d' : {
                                'heating' : eta_d_heating,
                                'cooling' : eta_d_cooling
                                },
                        'fValue' : {
                                'useDefault' : fValue_useDefault,
                                'heating'    : fValue_heating,
                                'cooling'    : fValue_cooling
                                }
                        }
                actual_UA    = SEPS(spec)['UA']
                actual_etaAH = SEPS(spec)['etaAH']
                actual_etaAC = SEPS(spec)['etaAC']
                self.assertAlmostEqual(actual_UA,    expected_UA,    delta = 0.000001)
                self.assertAlmostEqual(actual_etaAH, expected_etaAH, delta = 0.000001)
                self.assertAlmostEqual(actual_etaAC, expected_etaAC, delta = 0.000001)

if __name__ == "__main__":
    unittest.main()
    