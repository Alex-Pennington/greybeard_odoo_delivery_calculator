# -*- coding: utf-8 -*-
{
    'name': 'Greybeard Delivery Calculator',
    'version': '19.0.1.0.0',
    'category': 'Sales',
    'summary': 'Automatic delivery cost calculation with GPS distance-based routing',
    'description': """
        Greybeard Delivery Calculator
        ==============================
        
        Automatically calculates delivery costs when a "Delivery" product is added to sales orders.
        
        Features:
        ---------
        * Automatic GPS geocoding for customers without coordinates
        * Accurate distance calculation using Haversine formula
        * Google Maps API integration for precise road distances (optional)
        * Configurable rate per mile via environment variables
        * Price locking to prevent recalculation on address changes
        * Manual recalculation option
        * Works with both manual quotes and website orders
        * Custom GPS delivery carrier for website checkout
        * Smart availability rules (configurable distance and quantity limits)
        * Comprehensive error handling and user feedback
        
        Website Checkout:
        -----------------
        * GPS Distance-Based Delivery appears as shipping option if:
          - Customer within configured max distance
          - Order quantity below configured limit
          - Valid geocodable address
        * Automatically calculates exact shipping cost
        * Silently hides if conditions not met
        * Requires website_sale_delivery module for e-commerce integration
        
        Configuration:
        --------------
        All settings configured via .env file:
        * Origin coordinates (latitude/longitude)
        * Rate per mile
        * Max delivery distance
        * Max order quantity
        * Google Maps API key (optional)
        * Road distance multiplier (when not using Google Maps)
        
        See .env.example for all configuration options.
    """,
    'author': 'Greybeard Solutions',
    'website': 'https://Greybeard.solutions',
    'license': 'LGPL-3',
    'depends': [
        'sale',
        'base_geolocalize',
        'delivery',
    ],
    'data': [
        'data/delivery_carrier_data.xml',
        'views/sale_order_views.xml',
        'views/delivery_carrier_views.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}
