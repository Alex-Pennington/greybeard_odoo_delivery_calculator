# Graybeard Delivery Calculator

Automatic delivery cost calculation for Odoo 19+ based on GPS distance routing.

## Features

- ✅ Automatic GPS geocoding for customers without coordinates
- ✅ Accurate distance calculation using Haversine formula
- ✅ Optional Google Maps API integration for precise road distances
- ✅ Environment-based configuration (.env)
- ✅ Price locking - calculated cost doesn't change on address updates
- ✅ Manual recalculation option
- ✅ Works with manual quotes and website/e-commerce orders
- ✅ Custom GPS delivery carrier for website checkout
- ✅ Smart availability rules (configurable distance and quantity limits)
- ✅ Comprehensive error handling and logging

## Installation

### 1. Copy Module
Copy the module folder to your Odoo addons directory

### 2. Configure Environment
Copy `.env.example` to `.env` and configure:

```bash
cp .env.example .env
```

Edit `.env` with your settings:
```bash
# Required - Your delivery origin location
DELIVERY_ORIGIN_LATITUDE=38.48358903556404
DELIVERY_ORIGIN_LONGITUDE=-82.7803864690895

# Required - Pricing
DELIVERY_RATE_PER_MILE=2.5

# Required - Distance limits
DELIVERY_MAX_DISTANCE=75.0
DELIVERY_GPS_CARRIER_MAX_DISTANCE=60.0

# Optional - Google Maps API for accurate road distances
DELIVERY_USE_GOOGLE_MAPS=false
DELIVERY_GOOGLE_API_KEY=
```

### 3. Install Module
1. Restart Odoo server
2. Update Apps List (Apps → Update Apps List)
3. Search for "Graybeard Delivery Calculator"
4. Click Install

## Prerequisites

- Odoo 19+
- `base_geolocalize` module (for GPS geocoding)
- `delivery` module (for delivery carriers)
- `website_sale_delivery` module (optional, for e-commerce integration)

## Configuration

All configuration is done via environment variables in `.env` file:

| Variable | Description | Default |
|----------|-------------|---------|
| `DELIVERY_ORIGIN_LATITUDE` | Origin latitude (decimal degrees) | 38.48358903556404 |
| `DELIVERY_ORIGIN_LONGITUDE` | Origin longitude (decimal degrees) | -82.7803864690895 |
| `DELIVERY_RATE_PER_MILE` | Cost per mile | 2.5 |
| `DELIVERY_MAX_DISTANCE` | Max delivery distance (miles) | 75.0 |
| `DELIVERY_GPS_CARRIER_MAX_DISTANCE` | Max distance for website orders | 60.0 |
| `DELIVERY_MAX_ORDER_QUANTITY` | Max items for GPS delivery | 8 |
| `DELIVERY_ROAD_MULTIPLIER` | Road distance multiplier | 1.3 |
| `DELIVERY_USE_GOOGLE_MAPS` | Use Google Maps API | false |
| `DELIVERY_GOOGLE_API_KEY` | Google Maps API key | (empty) |

## Usage

### Manual Sales Orders

1. Create sales order
2. Add products
3. Add "Delivery" product line
4. Module automatically:
   - Geocodes customer address (if needed)
   - Calculates distance
   - Sets delivery price based on distance × rate

### Website Checkout

GPS delivery appears as shipping option if:
- Customer within configured max distance
- Order quantity below configured limit
- Customer has valid geocodable address

Otherwise option is silently hidden.

## Google Maps Integration (Optional)

For accurate road distances instead of straight-line estimates:

1. Create Google Cloud Platform account
2. Enable Distance Matrix API
3. Get API key
4. Set in `.env`:
```bash
DELIVERY_USE_GOOGLE_MAPS=true
DELIVERY_GOOGLE_API_KEY=your_api_key_here
```

**Cost**: ~$0.005 per distance calculation

## Troubleshooting

### Geocoding Fails
- Verify customer has complete address (street, city, state, ZIP, country)
- Check Odoo geocoding service is accessible
- Review logs for detailed error messages

### Distance Not Calculating
- Verify `.env` file is loaded
- Check origin coordinates are valid
- Review Odoo logs for errors

### GPS Carrier Not Appearing
- Verify `website_sale_delivery` module installed
- Check customer is within max distance
- Verify order quantity is below limit
- Check customer address is geocodable

## License

LGPL-3

## Author

Graybeard Solutions  
https://graybeard.solutions
