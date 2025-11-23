# Purchase Request Module for Odoo 18

A custom Odoo 18 module I built for managing purchase requests. This module lets employees create purchase requests with multiple items before actual purchase orders are made.

## What It Does

This module adds a Purchase Request feature to Odoo where users can:
- Create purchase requests with request numbers
- Add multiple products/items to each request
- Track vendor preferences for each item
- Manage workflow states (RFQ → RFQ Sent → Purchase Order)
- Generate PDF reports of requests

## Module Structure

The module has two main models:

### Purchase Request (`purchase.request`)
Main model that stores the purchase request information:
- Auto-generated request number (PRQ/2024/0001 format)
- Requester (who created it)
- Branch and department info
- Various dates (posting, document, required, valid until)
- State field for workflow tracking
- Links to purchase request lines

### Purchase Request Line (`purchase.request.line`)
Stores individual items in a purchase request:
- Product being requested
- Quantity needed
- Preferred vendor
- Required date
- Reference price
- Unit of measure

## Features

- **Auto-numbering**: Request numbers are automatically generated using Odoo sequences
- **Multiple views**: Kanban, List, and Form views for different ways to view requests
- **PDF Reports**: Can print purchase requisitions as PDF
- **Security**: Access control for purchase users and managers
- **Workflow**: Three states to track request progress

## Installation

1. Put this folder in your Odoo addons directory
2. Update apps list in Odoo
3. Install "Purchase Request" module
4. Menu appears under Purchase → Purchase Request

## How to Use

1. Create a new purchase request
2. Fill in branch, department, and dates
3. Add line items in the Products tab (products, quantities, vendors)
4. Click "Confirm Requisition" to change state to RFQ Sent
5. Use "Print Purchase Requisition" to generate PDF

## Technical Details

- Built with Python using Odoo's ORM
- Views defined in XML
- Uses Odoo's sequence system for auto-numbering
- Security rules in CSV file
- PDF reports using QWeb templates

## Dependencies

- Requires Odoo's `purchase` module

## Files

- `models/purchase_request.py` - Main request model
- `models/purchase_request_line.py` - Line items model
- `views/purchase_request_views.xml` - UI views
- `security/ir.model.access.csv` - Access permissions
- `data/purchase_request_sequence.xml` - Sequence configuration
- `reports/purchase_request_report.xml` - PDF report template

## Author

Arman Rehman

## License

LGPL-3
