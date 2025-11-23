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

## Prerequisites

- Odoo 18 installed
- PostgreSQL database running
- Python 3.12+ with virtual environment
- Purchase module installed in Odoo

## Setup

1. **Place module in addons path**: Clone this repository or copy the `purchase_request` folder to your Odoo `custom-addons` directory
2. **Start Odoo server**:
   ```bash
   python3 -m odoo -c odoo.conf
   ```
   Or use your IDE's run configuration
3. **Access Odoo**: Open browser and go to `http://localhost:8069`
4. **Create database** (if first time): Follow Odoo setup wizard to create database
5. **Login**: Use admin credentials to log in

## Installation

1. Go to **Apps** menu
2. Click **Update Apps List** (top right)
3. Search for "Purchase Request"
4. Click **Install**
5. Menu will appear under **Purchase → Purchase Request**

## How to Use

1. **Install**: Go to Apps → Update Apps List → Search "Purchase Request" → Install
2. **Access**: Navigate to Purchase → Purchase Request
3. **Create Request**: Click Create → Fill in branch, department, dates → Save
4. **Add Products**: Go to Products tab → Add lines with product, quantity, vendor, price → Save
5. **Confirm**: Click "Confirm Requisition" button → Status changes to RFQ Sent
6. **Print**: Click "Print Purchase Requisition" to generate PDF report

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
