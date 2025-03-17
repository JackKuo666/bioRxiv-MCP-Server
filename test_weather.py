import unittest
from unittest.mock import patch, AsyncMock
from weather import get_alerts, get_forecast

class TestWeatherServer(unittest.IsolatedAsyncioTestCase):
    @patch('weather.make_nws_request')
    async def test_get_alerts(self, mock_make_nws_request):
        mock_make_nws_request.return_value = {
            "features": [
                {
                    "properties": {
                        "event": "Flood Warning",
                        "areaDesc": "Test Area",
                        "severity": "Moderate",
                        "description": "Test description",
                        "instruction": "Test instruction"
                    }
                }
            ]
        }
        result = await get_alerts("CA")
        self.assertIn("Event: Flood Warning", result)
        self.assertIn("Area: Test Area", result)

    @patch('weather.make_nws_request')
    async def test_get_forecast(self, mock_make_nws_request):
        mock_make_nws_request.side_effect = [
            {
                "properties": {
                    "forecast": "https://api.weather.gov/gridpoints/MTR/84,105/forecast"
                }
            },
            {
                "properties": {
                    "periods": [
                        {
                            "name": "Tonight",
                            "temperature": 55,
                            "temperatureUnit": "F",
                            "windSpeed": "10 mph",
                            "windDirection": "NW",
                            "detailedForecast": "Clear skies"
                        }
                    ]
                }
            }
        ]
        result = await get_forecast(37.7749, -122.4194)
        self.assertIn("Tonight:", result)
        self.assertIn("Temperature: 55°F", result)
        self.assertIn("Wind: 10 mph NW", result)
        self.assertIn("Forecast: Clear skies", result)

if __name__ == '__main__':
    unittest.main()
