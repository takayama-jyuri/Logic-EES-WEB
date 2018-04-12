# envelope performance simple unit test
import unittest
import nbimporter

from EnvelopePerformanceSimple import simpleEnvPerformanceSelected as SEPS

class TestSEPS(unittest.TestCase):
    
    def test_gen_includingQdashMhMc(self):
        
        test_patterns = [
                ('region6', 'base_ins', 'bath_base_ins',  0.240, 0.530, 0.000, 0.480, 2.330, 3.490, 0.510, 0.510, 'yes', 1.0, 1.0, 'yes', 1.8, 1.8, 1.8, 2.8794288888888886, 0.94, 3.3, 3.1, 0.09495988888888889, 0.10108633333333332)
                ]
        for region, house_type, bath_ins_type, U_roof, U_wall, U_floorBath, U_floorOther, U_door, U_window, eta_d_cooling, eta_d_heating, fValue_useDefault, fValue_heating, fValue_cooling, psi_useDefault, psi_perimeterEntrance, psi_perimeterBath, psi_perimeterOther, expected_Qdash, expected_UA, expected_etaAH, expected_etaAC, expected_muC, expected_muH in test_patterns:
            with self.subTest():
                spec = {
                        'house_type'    : house_type,
                        'bath_ins_type' : bath_ins_type,
                        'region'        : region,
                        'U' : {
                                'roof'         : U_roof,
                                'wall'         : U_wall,
                                'door'         : U_door,
                                'window'       : U_window,
                                'floorBath'    : U_floorBath,
                                'floorOther'   : U_floorOther,
                                },
                        'psi' : {
                                'useDefaultEtrc' : psi_useDefault,
                                'prmEtrc'        : psi_perimeterEntrance,
                                'prmBath'        : psi_perimeterBath,
                                'prmOther'       : psi_perimeterOther,
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
    