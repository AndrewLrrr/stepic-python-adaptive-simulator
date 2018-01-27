from unittest import TestCase
from unicode_caesar_cipher import unicode_caesar_cipher


class TestUnicodeCaesarCipher(TestCase):
    def test1(self):
        self.assertEqual('😁😀😈', unicode_caesar_cipher('😀🙏😇', 1))

    def test2(self):
        self.assertEqual('😂😃😄😅😆😇😈😉😊', unicode_caesar_cipher('😀😁😂😃😄😅😆😇😈', 2))

    def test3(self):
        self.assertEqual('🙎🙏😀😁😂😃😄😅😆', unicode_caesar_cipher('😀😁😂😃😄😅😆😇😈', -2))

    def test4(self):
        codes = '😀😁😂😃😄😅😆😇😈😉😊😋😌😍😎😏😐😑😒😓😔😕😖😗😘😙😚😛😜😝😞😟😠😡😢😣😤😥😦😧😨😩😪😫😬😭😮😯😰😱😲😳😴😵😶😷😸😹😺😻😼😽😾😿🙀🙁🙂🙃🙄🙅🙆🙇🙈🙉🙊🙋🙌🙍🙎🙏'
        expected = '😁😂😃😄😅😆😇😈😉😊😋😌😍😎😏😐😑😒😓😔😕😖😗😘😙😚😛😜😝😞😟😠😡😢😣😤😥😦😧😨😩😪😫😬😭😮😯😰😱😲😳😴😵😶😷😸😹😺😻😼😽😾😿🙀🙁🙂🙃🙄🙅🙆🙇🙈🙉🙊🙋🙌🙍🙎🙏😀'
        self.assertEqual(expected, unicode_caesar_cipher(codes, 1))

    def test5(self):
        self.assertEqual('😔😕😖😗😘😙😚😛😜', unicode_caesar_cipher('😀😁😂😃😄😅😆😇😈', -1500))

    def test6(self):
        self.assertEqual('😀😁😂😃😄😅😆😇😈', unicode_caesar_cipher('😀😁😂😃😄😅😆😇😈', 80))
