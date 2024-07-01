from tests.integration.integration_test_case import IntegrationTestCase
from tests.integration.it_utils import test_async_and_sync
from xrpl.models.requests import Feature

AMENDMENT = "8CC0774A3BF66D1D22E76BBDA8E8A232E6B6313834301B3B23E8601196AE6455"


class TestAMMInfo(IntegrationTestCase):
    @test_async_and_sync(globals())
    async def test_basic_functionality(self, client):
        response = await client.request(Feature())
        features = response.result["features"]

        self.assertIn(AMENDMENT, features)
        feature_info = features[AMENDMENT]
        self.assertEqual(feature_info["name"], "AMM")
        self.assertEqual(feature_info["enabled"], False)
        self.assertEqual(feature_info["supported"], True)

    @test_async_and_sync(globals())
    async def test_single_feature(self, client):
        response = await client.request(Feature(feature=AMENDMENT))
        features = response.result

        self.assertIn(AMENDMENT, features)
        feature_info = features[AMENDMENT]
        self.assertEqual(feature_info["name"], "AMM")
        self.assertEqual(feature_info["enabled"], False)
        self.assertEqual(feature_info["supported"], True)
