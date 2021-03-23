"""
    Sat4Envi backend API

    The API documentation of the backend.  Access to definition group `public` is unrestricted. To access group `provider` you need extra permissions and group `private` isn't made available publicly.  # noqa: E501

    The version of the OpenAPI document: v1
    Generated by: https://openapi-generator.tech
"""


import unittest

import py4envi
from py4envi.api.scene_api import SceneApi  # noqa: E501


class TestSceneApi(unittest.TestCase):
    """SceneApi unit test stubs"""

    def setUp(self):
        self.api = SceneApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_generate_download_link(self):
        """Test case for generate_download_link

        Redirect to a presigned download url for a scene's artifact  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
