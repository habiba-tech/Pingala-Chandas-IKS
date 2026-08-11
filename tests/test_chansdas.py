import unittest

from src.chandas import (
    generate_patterns,
    pattern_to_binary,
    pattern_to_decimal,
    total_patterns,
)


class TestChandas(unittest.TestCase):

    # Test 1
    def test_single_syllable_count(self):
        self.assertEqual(total_patterns(1), 2)

    # Test 2
    def test_two_syllable_count(self):
        self.assertEqual(total_patterns(2), 4)

    # Test 3
    def test_three_syllable_count(self):
        self.assertEqual(total_patterns(3), 8)

    # Test 4
    def test_four_syllable_count(self):
        self.assertEqual(total_patterns(4), 16)

    # Test 5
    def test_five_syllable_count(self):
        self.assertEqual(total_patterns(5), 32)

    # Test 6
    def test_laghu_conversion(self):
        self.assertEqual(pattern_to_binary("L"), "0")

    # Test 7
    def test_guru_conversion(self):
        self.assertEqual(pattern_to_binary("G"), "1")

    # Test 8
    def test_laghu_guru_conversion(self):
        self.assertEqual(pattern_to_binary("LG"), "01")

    # Test 9
    def test_glg_conversion(self):
        self.assertEqual(pattern_to_binary("GLG"), "101")

    # Test 10
    def test_lglg_decimal(self):
        self.assertEqual(pattern_to_decimal("LGLG"), 5)

    # Test 11
    def test_gggg_decimal(self):
        self.assertEqual(pattern_to_decimal("GGGG"), 15)

    # Test 12
    def test_pattern_count(self):
        patterns = generate_patterns(3)
        self.assertEqual(len(patterns), 8)

    # Test 13
    def test_first_pattern(self):
        patterns = generate_patterns(3)
        self.assertEqual(patterns[0]["pattern"], "LLL")

    # Test 14
    def test_last_pattern(self):
        patterns = generate_patterns(3)
        self.assertEqual(patterns[-1]["pattern"], "GGG")

    # Test 15
    def test_invalid_pattern(self):
        with self.assertRaises(ValueError):
            pattern_to_binary("LXL")

    # Test 16
    def test_empty_pattern(self):
        with self.assertRaises(ValueError):
            pattern_to_binary("")

    # Test 17
    def test_zero_syllables(self):
        with self.assertRaises(ValueError):
            generate_patterns(0)

    # Test 18
    def test_negative_syllables(self):
        with self.assertRaises(ValueError):
            generate_patterns(-3)


if __name__ == "__main__":
    unittest.main()
