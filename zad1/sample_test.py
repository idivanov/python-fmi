import unittest
import solution


class TestSigns(unittest.TestCase):
    #na kiro testa
    def test_chinese_signs(self):
        self.assertEqual(solution.interpret_chinese_sign(1986), 'tiger')

    def test_western_signs(self):
        self.assertEqual(solution.interpret_western_sign(1, 5), 'taurus')

    def test_intersect(self):
        self.assertEqual(
            solution.interpret_both_signs(8, 5, 1989),
            ('taurus', 'snake')
        )

    #na vtoroto bratle testa
    def test_taurus_signs(self):
        self.assertEqual(solution.interpret_western_sign(1, 5), 'taurus')

    def test_capricorn(self):
        self.assertEqual(solution.interpret_western_sign(23, 12), 'capricorn')

    def test_gemini(self):
        self.assertEqual(solution.interpret_western_sign(18, 6), 'gemini')

    def test_cancer(self):
        self.assertEqual(solution.interpret_western_sign(19, 7), 'cancer')

    #na tretoto bratle testa
    def test_western_signs_aquarius(self):
        self.assertEqual(solution.interpret_western_sign(21, 1), 'aquarius')
        self.assertEqual(solution.interpret_western_sign(18, 2), 'aquarius')
        self.assertNotEqual(solution.interpret_western_sign(20, 1), 'aquarius')
        self.assertNotEqual(solution.interpret_western_sign(21, 2), 'aquarius')

    def test_western_signs_pisces(self):
        self.assertEqual(solution.interpret_western_sign(20, 2), 'pisces')
        self.assertEqual(solution.interpret_western_sign(20, 3), 'pisces')
        self.assertNotEqual(solution.interpret_western_sign(18, 1), 'pisces')
        self.assertNotEqual(solution.interpret_western_sign(21, 3), 'pisces')

    def test_western_signs_aries(self):
        self.assertEqual(solution.interpret_western_sign(21, 3), 'aries')
        self.assertEqual(solution.interpret_western_sign(20, 4), 'aries')
        self.assertNotEqual(solution.interpret_western_sign(20, 3), 'aries')
        self.assertNotEqual(solution.interpret_western_sign(21, 4), 'aries')

    def test_western_signs_taurus(self):
        self.assertEqual(solution.interpret_western_sign(21, 4), 'taurus')
        self.assertEqual(solution.interpret_western_sign(20, 5), 'taurus')
        self.assertNotEqual(solution.interpret_western_sign(20, 4), 'taurus')
        self.assertNotEqual(solution.interpret_western_sign(21, 5), 'taurus')

    def test_western_signs_gemini(self):
        self.assertEqual(solution.interpret_western_sign(21, 5), 'gemini')
        self.assertEqual(solution.interpret_western_sign(20, 6), 'gemini')
        self.assertNotEqual(solution.interpret_western_sign(20, 5), 'gemini')
        self.assertNotEqual(solution.interpret_western_sign(21, 6), 'gemini')

    def test_western_signs_cancer(self):
        self.assertEqual(solution.interpret_western_sign(21, 6), 'cancer')
        self.assertEqual(solution.interpret_western_sign(22, 7), 'cancer')
        self.assertNotEqual(solution.interpret_western_sign(20, 6), 'cancer')
        self.assertNotEqual(solution.interpret_western_sign(23, 7), 'cancer')

    def test_western_signs_leo(self):
        self.assertEqual(solution.interpret_western_sign(23, 7), 'leo')
        self.assertEqual(solution.interpret_western_sign(22, 8), 'leo')
        self.assertNotEqual(solution.interpret_western_sign(22, 7), 'leo')
        self.assertNotEqual(solution.interpret_western_sign(23, 8), 'leo')

    def test_western_signs_virgo(self):
        self.assertEqual(solution.interpret_western_sign(23, 8), 'virgo')
        self.assertEqual(solution.interpret_western_sign(22, 9), 'virgo')
        self.assertNotEqual(solution.interpret_western_sign(22, 8), 'virgo')
        self.assertNotEqual(solution.interpret_western_sign(23, 9), 'virgo')

    def test_western_signs_libra(self):
        self.assertEqual(solution.interpret_western_sign(23, 9), 'libra')
        self.assertEqual(solution.interpret_western_sign(22, 10), 'libra')
        self.assertNotEqual(solution.interpret_western_sign(22, 9), 'libra')
        self.assertNotEqual(solution.interpret_western_sign(23, 10), 'libra')

    def test_western_signs_scorpio(self):
        self.assertEqual(solution.interpret_western_sign(23, 10), 'scorpio')
        self.assertEqual(solution.interpret_western_sign(21, 11), 'scorpio')
        self.assertNotEqual(solution.interpret_western_sign(22, 10), 'scorpio')
        self.assertNotEqual(solution.interpret_western_sign(22, 11), 'scorpio')

    def test_western_signs_sagittarius(self):
        self.assertEqual(solution.interpret_western_sign(22, 11), 'sagittarius')
        self.assertEqual(solution.interpret_western_sign(21, 12), 'sagittarius')
        self.assertNotEqual(solution.interpret_western_sign(21, 11), 'sagittarius')
        self.assertNotEqual(solution.interpret_western_sign(22, 12), 'sagittarius')

    def test_western_signs_capricorn(self):
        self.assertEqual(solution.interpret_western_sign(22, 12), 'capricorn')
        self.assertEqual(solution.interpret_western_sign(20, 1), 'capricorn')
        self.assertNotEqual(solution.interpret_western_sign(21, 12), 'capricorn')
        self.assertNotEqual(solution.interpret_western_sign(21, 1), 'capricorn')

    def test_chinese_signs(self):
        self.assertEqual(solution.interpret_chinese_sign(1986), 'tiger')

    def test_western_signs(self):
        self.assertEqual(solution.interpret_western_sign(1, 5), 'taurus')

    def test_intersect(self):
        self.assertEqual(
            solution.interpret_both_signs(8, 5, 1989),
            ('taurus', 'snake')
        )

    def test_aries_sign(self):
        self.assertEqual(solution.interpret_western_sign(2, 4), 'aries')

    def test_taurus_sign(self):
        self.assertEqual(solution.interpret_western_sign(21, 4), 'taurus')

    def test_gemini_sign(self):
        self.assertEqual(solution.interpret_western_sign(21, 5), 'gemini')

    def test_cancer_sign(self):
        self.assertEqual(solution.interpret_western_sign(10, 7), 'cancer')

    def test_leo_sign(self):
        self.assertEqual(solution.interpret_western_sign(27, 7), 'leo')

    def test_virgo_sign(self):
        self.assertEqual(solution.interpret_western_sign(1, 9), 'virgo')

    def test_libra_sign(self):
        self.assertEqual(solution.interpret_western_sign(7, 10), 'libra')

    def test_scorpio_sign(self):
        self.assertEqual(solution.interpret_western_sign(20, 11), 'scorpio')

    def test_saggitarius_sign(self):
        self.assertEqual(solution.interpret_western_sign(24, 11), 'sagittarius')

    def test_aquarius_sign(self):
        self.assertEqual(solution.interpret_western_sign(8, 2), 'aquarius')

    def test_pisces_sign(self):
        self.assertEqual(solution.interpret_western_sign(16, 3), 'pisces')

    def test_cancer_sign(self):
        self.assertEqual(solution.interpret_western_sign(10, 7), 'cancer')

    # not a good practice just showing that this is possbile too.
    # also noone posted tests with years before 1900 and after 2015 so.. yea
    def test_chinese_signs(self):
        self.assertEqual(solution.interpret_chinese_sign(2000), 'dragon')
        self.assertEqual(solution.interpret_chinese_sign(1994), 'dog')
        self.assertEqual(solution.interpret_chinese_sign(1992), 'monkey')
        self.assertEqual(solution.interpret_chinese_sign(1893), 'snake')
        self.assertEqual(solution.interpret_chinese_sign(1723), 'rabbit')
        self.assertEqual(solution.interpret_chinese_sign(982), 'horse')
        self.assertEqual(solution.interpret_chinese_sign(123), 'pig')
        self.assertEqual(solution.interpret_chinese_sign(124), 'rat')
        self.assertEqual(solution.interpret_chinese_sign(11285), 'ox')
        self.assertEqual(solution.interpret_chinese_sign(2015), 'sheep')
        self.assertEqual(solution.interpret_chinese_sign(2017), 'rooster')
        self.assertEqual(solution.interpret_chinese_sign(-547), 'ox')

    def test_aries_snake_signs(self):
        self.assertEqual(
            solution.interpret_both_signs(18, 4, 1989),
            ('aries', 'snake')
        )

    def test_aquarius_pig(self):
        self.assertEqual(
            solution.interpret_both_signs(23, 1, 2007),
            ('aquarius', 'pig')
        )

    def test_leo_rat(self):
        self.assertEqual(
            solution.interpret_both_signs(26, 7, 1936),
            ('leo', 'rat')
        )

    #na bratleto neraboteshtite testove
    #deto uj gi opravih
    def test_aries_snake_signs(self):
        self.assertEqual(
            solution.interpret_both_signs(18, 4, 1989),
            ('aries', 'snake')
        )

    def test_aquarius_pig(self):
        self.assertEqual(
            solution.interpret_both_signs(23, 1, 2007),
            ('aquarius', 'pig')
        )

    def test_leo_rat(self):
        self.assertEqual(
            solution.interpret_both_signs(26, 7, 1936),
            ('leo', 'rat')
        )
        
    def test_tiger_sign(self):
        self.assertEqual(solution.interpret_chinese_sign(1986), 'tiger')

    def test_dragon_sign(self):
        self.assertEqual(solution.interpret_chinese_sign(2000), 'dragon')

    def test_dog_sign(self):
        self.assertEqual(solution.interpret_chinese_sign(1994), 'dog')

    def test_monkey_sign(self):
        self.assertEqual(solution.interpret_chinese_sign(1992), 'monkey')
        
    def test_aries_snake_signs(self):
        self.assertEqual(
            solution.interpret_both_signs(18, 4, 1989),
            ('aries', 'snake')
        )

    def test_aquarius_pig(self):
        self.assertEqual(
            solution.interpret_both_signs(23, 1, 2007),
            ('aquarius', 'pig')
        )

    def test_leo_rat(self):
        self.assertEqual(
            solution.interpret_both_signs(26, 7, 1936),
            ('leo', 'rat')
        )
        
        
    #oshte testove da ima
    def test_aries_sign(self):
        self.assertEqual(solution.interpret_western_sign(2, 4), 'aries')

    def test_taurus_sign(self):
        self.assertEqual(solution.interpret_western_sign(21, 4), 'taurus')

    def test_gemini_sign(self):
        self.assertEqual(solution.interpret_western_sign(21, 5), 'gemini')

    def test_cancer_sign(self):
        self.assertEqual(solution.interpret_western_sign(10, 7), 'cancer')

    def test_leo_sign(self):
        self.assertEqual(solution.interpret_western_sign(27, 7), 'leo')

    def test_virgo_sign(self):
        self.assertEqual(solution.interpret_western_sign(1, 9), 'virgo')

    def test_libra_sign(self):
        self.assertEqual(solution.interpret_western_sign(7, 10), 'libra')

    def test_scorpio_sign(self):
        self.assertEqual(solution.interpret_western_sign(20, 11), 'scorpio')

    def test_saggitarius_sign(self):
        self.assertEqual(solution.interpret_western_sign(24, 11), 'sagittarius')

    def test_aquarius_sign(self):
        self.assertEqual(solution.interpret_western_sign(8, 2), 'aquarius')

    def test_pisces_sign(self):
        self.assertEqual(solution.interpret_western_sign(16, 3), 'pisces')

    def test_cancer_sign(self):
        self.assertEqual(solution.interpret_western_sign(10, 7), 'cancer')

    # not a good practice just showing that this is possbile too.
    # also noone posted tests with years before 1900 and after 2015 so.. yea
    def test_chinese_signs(self):
        self.assertEqual(solution.interpret_chinese_sign(2000), 'dragon')
        self.assertEqual(solution.interpret_chinese_sign(1994), 'dog')
        self.assertEqual(solution.interpret_chinese_sign(1992), 'monkey')
        self.assertEqual(solution.interpret_chinese_sign(1893), 'snake')
        self.assertEqual(solution.interpret_chinese_sign(1723), 'rabbit')
        self.assertEqual(solution.interpret_chinese_sign(982), 'horse')
        self.assertEqual(solution.interpret_chinese_sign(123), 'pig')
        self.assertEqual(solution.interpret_chinese_sign(124), 'rat')
        self.assertEqual(solution.interpret_chinese_sign(11285), 'ox')
        self.assertEqual(solution.interpret_chinese_sign(2015), 'sheep')
        self.assertEqual(solution.interpret_chinese_sign(2017), 'rooster')
        self.assertEqual(solution.interpret_chinese_sign(-547), 'ox')

    def test_aries_snake_signs(self):
        self.assertEqual(
            solution.interpret_both_signs(18, 4, 1989),
            ('aries', 'snake')
        )

    def test_aquarius_pig(self):
        self.assertEqual(
            solution.interpret_both_signs(23, 1, 2007),
            ('aquarius', 'pig')
        )

    def test_leo_rat(self):
        self.assertEqual(
            solution.interpret_both_signs(26, 7, 1936),
            ('leo', 'rat')
        )

if __name__ == '__main__':
    unittest.main()
