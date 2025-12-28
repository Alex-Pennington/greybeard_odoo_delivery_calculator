# Changelog

All notable changes to Greybeard Delivery Calculator will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).

## [19.0.1.0.0] - 2025-12-28

### Added
- Environment variable configuration system (.env)
- .env.example template with all configuration options
- Complete documentation for environment-based setup
- WORK_PLAN.md for tracking remaining tasks
- REPO_VS_SERVER_COMPARISON.md documenting migration source

### Changed
- **BREAKING**: Migrated from Odoo 17 to Odoo 19
- **BREAKING**: All configuration now via environment variables instead of Odoo Settings UI
- Module name: `delivery_cost_calculator` → `Greybeard_delivery_calculator`
- Author: "Your Company" → "Greybeard Solutions"
- Website: https://www.yourcompany.com → https://Greybeard.solutions
- Version: 17.0.5.0.0 → 19.0.1.0.0
- Configuration loading: `ir.config_parameter` → `os.environ`
- Updated README.md with environment-based installation instructions
- Improved security by externalizing all sensitive configuration

### Removed
- Odoo Settings UI (res_config_settings.py and views)
- Hardcoded configuration values (now in .env)
- Phoenix Nest branding and references
- Legacy documentation files:
  - INSTALLATION.md (replaced by README.md)
  - GOOGLE_MAPS_SETUP.md (integrated into .env.example)
  - GOOGLE_MAPS_IMPLEMENTATION.md (integrated into .env.example)
  - SETTINGS_LOCATION.md (no longer applicable)
  - PRE_UPLOAD_CHECKLIST.md (outdated)
  - MIGRATION.md (outdated)
  - TROUBLESHOOTING.md (integrated into README.md)
  - DATABASE_FIX.sql (no longer needed)

### Security
- Google Maps API key now stored in environment variables (not in database)
- All sensitive configuration externalized to .env file
- .env file properly excluded via .gitignore

### Migration Notes
This release represents a complete rebrand and modernization from the Phoenix Nest delivery_cost_calculator module:

**Configuration Migration:**
Old Odoo 17 installations using Settings UI must migrate to .env:
1. Copy current settings from Odoo Settings > Delivery Calculator
2. Create .env file based on .env.example
3. Transfer all settings to environment variables
4. Restart Odoo to load new configuration

**Breaking Changes:**
- Settings UI completely removed
- All configuration must be in .env before installation
- Module will use default values if .env not configured

**Compatibility:**
- Requires Odoo 19.0+
- Python 3.8+ recommended
- Requires `base_geolocalize`, `delivery` modules

---

## [17.0.5.0.0] - 2024-10-16 (Phoenix Nest - Final Version)

Final version before Greybeard rebrand. Used Odoo Settings UI for configuration.

### Features (Pre-Migration)
- GPS-based delivery cost calculation
- Haversine distance formula
- Google Maps Distance Matrix API integration
- Odoo Settings UI configuration
- Configurable origin coordinates, rate per mile, distance limits
- Custom GPS delivery carrier for website checkout
- Automatic geocoding for customer addresses
