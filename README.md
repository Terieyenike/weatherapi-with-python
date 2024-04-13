# Weather API and Infobip SMS Integration

This Flask application integrates with a weather API ([Open Weather Map](https://openweathermap.org/)) to provide real-time weather information of a location based on the city name, state code, and country code. It also sends [SMS](https://www.infobip.com/docs/api/channels/sms) using Infobip Python SDK to your phone.

![Weather SMS report](https://github.com/Terieyenike/weatherapi-with-python/assets/25850598/f6247b7e-7bd8-4204-ab10-ec8d05952932)

## Prerequisites

Before running the application, ensure you have the following:

- Python installed on your system
- Flask framework installed (`pip install Flask`)
- Weather API credentials
- Infobip API credentials
- Destination phone number for SMS notifications

## Running locally

### Clone this repository:

```
git clone https://github.com/Terieyenike/weatherapi-with-python
cd weatherapi-with-python
```

### Install dependencies

```
pip install -r requirements.txt
```

### Set up environment variables:

In the `.env` file, replace the value of your openweathermap API key

```
OWM_API_KEY="<open-weather-map-api-key>"
IB_BASE_URL="<your API Base URL>"
IB_API_KEY="<your API Key>"
DESTINATION_NUMBER="<your phone number>"
```

## Tech stack

- Python
- Flask
- Infobip Python SDK
- Tailwind CSS

## Usage

Once you have the requirements installed, `flask run` from the top-level directory will serve the app on `127.0.0.1:5000`.

## Contributors

- [Teri Eyenike](https://x.com/terieyenike)

## License

This project is licensed under the MIT License
