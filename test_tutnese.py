import tutnese
import unittest

class TestTutnese (unittest.TestCase):
    # Testing for endcoding for provided string
    def test_TutneseEncoding_0(self):
        self.assertEqual(tutnese.encode("Over hill, over dale, Thorough bush, thorough brier, Over park, over pale, Thorough flood, thorough fire!"), "ovuverur hashisqual, ovuverur dudalule, tuthashorurougughash bubusushash, tuthashorurougughash bubrurierur, ovuverur puparurkuck, ovuverur pupalule, tuthashorurougughash fufluloodud, tuthashorurougughash fufirure!")

    # Testing for endcoding for simple string with only constants
    def test_TutneseEncoding_1(self):
        self.assertEqual(tutnese.encode("vwbc"),"vuvwackbubcoch")

    # Testing for endcoding for simple string with only vowels
    def test_TutneseEncoding_2(self):
        self.assertEqual(tutnese.encode("aeiou"),"aeiou")

    # Testing for endcoding for simple string with mix of constants and vowels
    def test_TutneseEncoding_3(self):
        self.assertEqual(tutnese.encode("abeviwou"),"abubevuviwackou")

    # Testing for endcoding for simple string with only punctuation
    def test_TutneseEncoding_4(self):
        self.assertEqual(tutnese.encode("?!.?!"),"?!.?!")

    # Testing for endcoding for simple string with only special characters
    def test_TutneseEncoding_5(self):
        self.assertEqual(tutnese.encode("@#$%"),"@#$%")

    # Testing for endcoding for simple string with only numbers
    def test_TutneseEncoding_6(self):
        self.assertEqual(tutnese.encode("345234"),"345234")

    # Testing for endcoding for complex string with mutiple vowels in a row
    def test_TutneseEncoding_7(self):
        self.assertEqual(tutnese.encode("&Ov!er hill, ovoooer daleee,"),"&ovuv!erur hashisqual, ovuvoooerur dudaluleee,")

    # Testing for endcoding for complex string with two constants in a row
    def test_TutneseEncoding_8(self):
        self.assertEqual(tutnese.encode("Thorough bushh, thorough brier,"),"tuthashorurougughash bubusussquah, tuthashorurougughash bubrurierur,")

    # Testing for endcoding for complex string with multiple constants in a row
    def test_TutneseEncoding_9(self):
        self.assertEqual(tutnese.encode("Thorrrough bushh, thorough"),"tuthashosquarrurougughash bubusussquah, tuthashorurougughash")

    # Testing for endcoding for '|' in the middle
    # Should tests for '|' fail or pass with a None
    def test_TutneseEncoding_10(self):
        self.assertEqual(tutnese.encode("Over hill, over dale, Thorough bush, thorough brier, Over park, over pale, Thorough flo|od, thorough fire!"), None)

    # Testing for endcoding for '|' in the first
    def test_TutneseEncoding_11(self):
        self.assertEqual(tutnese.encode("|Over hill, over dale, Thorough bush, thorough brier, Over park, over pale, Thorough flood, thorough fire!"), None)

    # Testing for endcoding for '|' in the last
    def test_TutneseEncoding_12(self):
        self.assertEqual(tutnese.encode("Over hill, over dale, Thorough bush, thorough brier, Over park, over pale, Thorough flood, thorough fire!|"), None)

    # Testing for endcoding for '|' with mutiple locations
    def test_TutneseEncoding_13(self):
        self.assertEqual(tutnese.encode("Over hil|l, over dale, Tho|rough bush, thorough brier, Over park, over pale, Thorough flo|od, thorough fire!|"), None)

    # Testing for endcoding for '|' with more than one in a row
    def test_TutneseEncoding_14(self):
        self.assertEqual(tutnese.encode("Over hill, over dale, Thoro|||ugh bush, thorough brier, Over park, over pale, Thorough flood, thorough fire!"), None)

# Testing for Decoding starts here:::

    # Testing for decoding for provided string
    def test_TutneseDecoding_15(self):
        self.assertEqual(tutnese.decode("ovuverur hashisqual, ovuverur dudalule, tuthashorurougughash bubusushash, tuthashorurougughash bubrurierur, ovuverur puparurkuck, ovuverur pupalule, tuthashorurougughash fufluloodud, tuthashorurougughash fufirure!"), "over hill, over dale, thorough bush, thorough brier, over park, over pale, thorough flood, thorough fire!")

    # Testing for decoding for simple string with only constants
    def test_TutneseDecoding_16(self):
        self.assertEqual(tutnese.decode("vuvwackbubcoch"),"vwbc")

    # Testing for decoding for simple string with only vowels
    def test_TutneseDecoding_17(self):
        self.assertEqual(tutnese.decode("aeiou"),"aeiou")

    # Testing for decoding for simple string with mix of constants and vowels
    def test_TutneseDecoding_18(self):
        self.assertEqual(tutnese.decode("abubevuviwackou"),"abeviwou")

    # Testing for decoding for simple string with only punctuation
    def test_TutneseDecoding_19(self):
        self.assertEqual(tutnese.decode("?!.?!"),"?!.?!")

    # Testing for decoding for simple string with only special characters
    def test_TutneseDecoding_20(self):
        self.assertEqual(tutnese.decode("@#$%"),"@#$%")

    # Testing for decoding for simple string with only numbers
    def test_TutneseDecoding_21(self):
        self.assertEqual(tutnese.decode("345234"),"345234")

    # Testing for decoding for complex string with mutiple vowels in a row
    def test_TutneseDecoding_22(self):
        self.assertEqual(tutnese.decode("&ovuv!erur hashisqual, ovuvoooerur dudaluleee,"),"&ov!er hill, ovoooer daleee,")

    # Testing for decoding for complex string with two constants in a row
    def test_TutneseDecoding_23(self):
        self.assertEqual(tutnese.decode("tuthashorurougughash bubusussquah, tuthashorurougughash bubrurierur,"),"thorough bushh, thorough brier,")

    # Testing for decoding for complex string with multiple constants in a row
    def test_TutneseDecoding_24(self):
        self.assertEqual(tutnese.decode("tuthashosquarrurougughash bubusussquah, tuthashorurougughash"),"thorrrough bushh, thorough")

    # Testing for decoding for '|' in the middle
    # Should tests for '|' fail or pass with a None
    def test_TutneseDecoding_25(self):
        self.assertEqual(tutnese.decode("ovuverur hashisqual, ovuverur dudalule, tuthashorurougughash bubusushash, tuthashorurougughash bubrurierur, ovuverur puparurkuck, ovuverur pupalule, tuthashorurougughash fufluloodud, tuthashorur|ougughash fufirure!"), None)

    # Testing for decoding for '|' in the first
    def test_TutneseDecoding_26(self):
        self.assertEqual(tutnese.decode("|ovuverur hashisqual, ovuverur dudalule, tuthashorurougughash bubusushash, tuthashorurougughash bubrurierur, ovuverur puparurkuck, ovuverur pupalule, tuthashorurougughash fufluloodud, tuthashorurougughash fufirure!"), None)

    # Testing for decoding for '|' in the last
    def test_TutneseDecoding_27(self):
        self.assertEqual(tutnese.decode("ovuverur hashisqual, ovuverur dudalule, tuthashorurougughash bubusushash, tuthashorurougughash bubrurierur, ovuverur puparurkuck, ovuverur pupalule, tuthashorurougughash fufluloodud, tuthashorurougughash fufirure!|"), None)

    # Testing for decoding for '|' with mutiple locations
    def test_TutneseDecoding_28(self):
        self.assertEqual(tutnese.decode("ovuverur hashisq|ual, ovuverur dudalule, tuthashorurougughash bubusushash, tuthashorurougughash bubrurierur, o|vuverur puparurkuck, ovuverur pupalule, tuthashorurougughash fufluloodud, tuthashorurougug|hash fufirure!"), None)

    # Testing for decoding for '|' with more than one in a row
    def test_TutneseDecoding_29(self):
        self.assertEqual(tutnese.decode("ovuverur hashisqual, ovuverur dudalule, tuthashorurougughash bubusushash, tuthashorurougughash bubrurierur, ovuverur puparu||||rkuck, ovuverur pupalule, tuthashorurougughash fufluloodud, tuthashorurougughash fufirure!"), None)
