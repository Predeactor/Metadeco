import unittest

import metadeco


class TestMetadata(unittest.TestCase):
    def test_define_metadata(self):
        def to_test():
            pass

        metadeco.define_metadata(to_test, "meta_test", True)

        self.assertIsInstance(to_test.metadata, dict)  # type: ignore
        self.assertIs(to_test.metadata["meta_test"], True)  # type: ignore

    def test_metadata_decorator(self) -> None:
        @metadeco.metadata("meta_test", True)
        def to_test():
            pass

        self.assertIsInstance(to_test.metadata, dict)  # type: ignore
        self.assertIs(to_test.metadata["meta_test"], True)  # type: ignore

    def test_has_metadata(self) -> None:
        @metadeco.metadata("meta_test", True)
        def to_test():
            pass

        self.assertTrue(metadeco.has_metadata(to_test))
        metadeco.delete_metadata(to_test, "meta_test")

        self.assertFalse(metadeco.has_metadata(to_test))

    def test_get_metadata(self) -> None:
        @metadeco.metadata("meta_test", True)
        def to_test():
            pass

        self.assertIs(metadeco.get_metadata(to_test, "meta_test"), True)

    def test_delete_metadata(self) -> None:
        @metadeco.metadata("meta_test", True)
        def to_test():
            pass

        metadeco.delete_metadata(to_test, "meta_test")
        with self.assertRaises(ValueError):
            metadeco.get_metadata(to_test, "meta_test")

    def test_metadata_class(self) -> None:
        @metadeco.metadata("meta_test", True)
        class C:
            pass

        self.assertTrue(metadeco.has_metadata(C))
