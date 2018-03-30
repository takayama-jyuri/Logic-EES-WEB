# envelope performance simple unit test
import unittest
import nbimporter

from EnvelopePerformanceSimple import simpleEnvPerformanceSelected as SEPS

class TestSEPS(unittest.TestCase):
    
    def test_gen(self):
        
        test_patterns = [
                ('base_ins', 'region6', 0.240, 0.530, 2.330, 3.490, 0.480, 0.000, 0.000, 'yes', 1.8, 1.8, 0.510, 0.510, 'yes', 1.0, 1.0, 2.8794288888888886, 0.94, 3.3, 3.1, 0.09495988888888889, 0.10108633333333332)
#                ('base_and_floor_ins', 0.240)
                ]
        for house_type, region, U_roof, U_wall, U_door, U_window, U_floorOther, U_baseOther, U_baseEntrance, psi_useDefault, psi_perimeterOther, psi_perimeterEntrance, eta_d_heating, eta_d_cooling, fValue_useDefault, fValue_heating, fValue_cooling, expected_Qdash, expected_UA, expected_etaAH, expected_etaAC, expected_muC, expected_muH in test_patterns:
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
                                'baseOther'    : U_baseOther,
                                'baseEntrance' : U_baseEntrance
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

if __name__ == "__main__":
    unittest.main()
    