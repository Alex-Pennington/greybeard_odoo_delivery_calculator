# Delivery Cost Calculator: Repo vs Server Comparison

**Date:** 2025-12-28  
**Repo:** https://github.com/Alex-Pennington/odoo-delivery-cost-calculator  
**Server:** www.organicengineer.com (root-web-1:/mnt/extra-addons/delivery_cost_calculator)

---

## Files on Server NOT in Repository

**⚠️ Server has additional documentation files:**
- `GOOGLE_MAPS_IMPLEMENTATION.md`
- `GOOGLE_MAPS_SETUP.md`
- `PRE_UPLOAD_CHECKLIST.md`
- `SETTINGS_LOCATION.md`

**These are server-specific docs - need to review for migration.**

---

## Files in Both Repo and Server

- `__init__.py`
- `__manifest__.py`
- `DATABASE_FIX.sql`
- `INSTALLATION.md`
- `MIGRATION.md`
- `README.md`
- `TROUBLESHOOTING.md`
- `data/` directory
- `models/` directory  
- `views/` directory

---

## Recommendation for Greybeard Migration

**Use SERVER version as base** - includes additional documentation.

Server has 4 extra docs that may contain important Google Maps API setup info needed for the module to work.
