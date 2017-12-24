#!python3.6
import unittest
from MusicTheory.scale.Scale import Scale
from MusicTheory.scale.ScaleKey import ScaleKey
#import MusicTheory.scale.ScaleKey
#from MusicTheory.scale.Scale.Scale.ScaleKey import ScaleKey
from MusicTheory.pitch.PitchClass import PitchClass
from MusicTheory.pitch.Accidental import Accidental
"""
ScaleKeyのテスト。
"""
class TestScaleKey(unittest.TestCase):
    def test_init_Default(self):
        s = ScaleKey()
        self.assertEqual('C', s.Name)
        self.assertEqual(0, s.PitchClass)
    def test_init_set(self):
        keys = {'C':0, 'D':2, 'E':4, 'F':5, 'G':7, 'A':9, 'B':11}
        for k, kp in keys.items():
            for acc_count in range(1, 4):
                for a, ap in Accidental.Accidentals.items():
                    name = k + a*acc_count
                    pitch = PitchClass.Get(kp + (ap*acc_count))[0]
                    with self.subTest(name=name):
                        s = ScaleKey(name)
                        self.assertEqual(name, s.Name)
                        self.assertEqual(pitch, s.PitchClass)
    def test_Name_set(self):
        s = ScaleKey()
        keys = {'C':0, 'D':2, 'E':4, 'F':5, 'G':7, 'A':9, 'B':11}
        for k, kp in keys.items():
            for acc_count in range(1, 4):
                for a, ap in Accidental.Accidentals.items():
                    name = k + a*acc_count
                    pitch = PitchClass.Get(kp + (ap*acc_count))[0]
                    with self.subTest(name=name):
                        s.Name = name
                        self.assertEqual(name, s.Name)
                        self.assertEqual(pitch, s.PitchClass)
    def test_init_Invalid_Type_Name(self):
        with self.assertRaises(TypeError) as ex:
            s = ScaleKey(0)
        self.assertIn('引数nameはstr型にしてください。', str(ex.exception))
    def test_init_Invalid_Value_Name(self):
        with self.assertRaises(ValueError) as ex:
            s = ScaleKey('無効値')
        self.assertIn('keyは次のうちのいずれかにしてください。', str(ex.exception))
    def test_Name_set_int(self):
        s = ScaleKey()
        with self.assertRaises(TypeError) as ex:
            s.Name = 0
        self.assertIn('引数nameはstr型にしてください。', str(ex.exception))
    def test_PitchClass_set(self):
        s = ScaleKey()
        with self.assertRaises(AttributeError) as ex:
            s.PitchClass = 0
        self.assertIn("can't set attribute", str(ex.exception))


if __name__ == '__main__':
    unittest.main()

