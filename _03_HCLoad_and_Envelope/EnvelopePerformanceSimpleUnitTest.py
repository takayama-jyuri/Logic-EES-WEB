# envelope performance simple unit test
import unittest
import nbimporter

from EnvelopePerformanceSimple import simpleEnvPerformanceSelected as SEPS

class TestSEPS(unittest.TestCase):
    
    def test_gen(self):
        
        test_patterns = [
                ('base_ins', 'region6', 0.240, 0.530, 2.330, 3.490, 0.480, 0.000, 0.000, 'yes', 1.8, 1.8, 0.510, 0.510, 'yes', 1.0, 1.0, 2.879428888888888)
#                ('base_and_floor_ins', 0.240)
                ]
        for house_type, region, U_roof, U_wall, U_door, U_window, U_floorOther, U_baseOther, U_baseEntrance, psi_useDefault, psi_perimeterOther, psi_perimeterEntrance, eta_d_heating, eta_d_cooling, fValue_useDefault, fValue_heating, fValue_cooling, expected in test_patterns:
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
                actual = SEPS(spec)['Qdash']
                self.assertAlmostEqual(actual, expected, delta = 0.000001)        

if __name__ == "__main__":
    unittest.main()
    