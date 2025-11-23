# Purchase Request Module for Odoo 18

## Overview

This is a custom Odoo 18 module that implements a **Purchase Request** system, allowing employees to create formal requests for purchasing items before actual purchase orders are generated. This module streamlines the procurement process by providing a structured workflow for requesting purchases, tracking approval status, and managing vendor quotations.

## What is a Purchase Request?

A **Purchase Request** is a formal document that employees create when they need to purchase goods or services. Think of it as an internal requisition form that:
- Documents what needs to be purchased
- Specifies quantities, vendors, and required dates
- Tracks the approval and procurement workflow
- Can be converted into actual Purchase Orders later

### Real-World Analogy
Imagine you work in an office and need new office supplies. Instead of directly placing an order with a vendor, you first create a "Purchase Request" that includes:
- What you need (e.g., 50 reams of paper)
- From which vendor
- When you need it
- Your department/branch information

This request then goes through an approval process, and once approved, the procurement team converts it into an actual Purchase Order.

## Module Architecture

### 1. **Purchase Request Model** (`purchase.request`)
The main document that represents a purchase request.

**Key Fields:**
- `name`: Unique request number (auto-generated, e.g., PRQ/2024/0001)
- `requester_id`: The employee who created the request
- `branch` & `department`: Organizational information
- `posting_date`, `document_date`, `required_date`, `valid_until`: Date tracking
- `line_ids`: The list of items being requested (One2many relationship)
- `purchase_order_id`: Link to the actual Purchase Order if one is created
- `state`: Workflow status (RFQ → RFQ Sent → Purchase Order)

**Key Methods:**
- `action_confirm_requisition()`: Moves request from RFQ to RFQ Sent status
- `action_print_requisition()`: Generates a PDF report of the request
- `create()`: Auto-generates unique sequence number on creation

### 2. **Purchase Request Line Model** (`purchase.request.line`)
Individual items within a purchase request. Each request can have multiple lines.

**Key Fields:**
- `request_id`: Link back to the parent Purchase Request
- `product_id`: The product being requested
- `vendor_id`: Preferred vendor (filtered to show only suppliers)
- `required_qty`: Quantity needed
- `required_date`: When the item is needed
- `info_price`: Estimated/reference price
- `product_uom_id`: Unit of measure (e.g., pieces, kg, liters)
- `item_description`: Additional description
- `sequence`: For ordering lines within a request

## How It Works - Step by Step

### Step 1: Creating a Purchase Request
1. User navigates to **Purchase → Purchase Request** menu
2. Clicks "Create" to start a new request
3. System auto-generates a unique request number (e.g., PRQ/2024/0001)
4. User fills in:
   - Branch and Department
   - Dates (posting, document, required, valid until)
   - Adds line items (products, quantities, vendors)

### Step 2: Adding Request Lines
1. In the "Products" tab, user adds multiple line items
2. For each line, specifies:
   - Product
   - Quantity
   - Preferred vendor
   - Required date
   - Reference price
   - Unit of measure

### Step 3: Workflow States
The request moves through three states:
- **RFQ (Request for Quotation)**: Initial state when created
- **RFQ Sent**: When the requisition is confirmed and sent to vendors
- **Purchase Order**: When converted to an actual purchase order

### Step 4: Confirming Requisition
- User clicks "Confirm Requisition" button
- State changes from RFQ to RFQ Sent
- This indicates the request has been sent to vendors for quotations

### Step 5: Printing/Reporting
- User can click "Print Purchase Requisition" to generate a PDF
- PDF includes all request details and line items in a formatted report

## Technical Implementation Details

### Sequence Generation
The module uses Odoo's sequence system to auto-generate request numbers:
- Format: `PRQ/YYYY/####` (e.g., PRQ/2024/0001)
- Configured in `data/purchase_request_sequence.xml`
- Implemented in the `create()` method override

### Security & Access Rights
- **Purchase Users**: Can read, write, create, and delete their own requests
- **Purchase Managers**: Full access to all requests
- Defined in `security/ir.model.access.csv`

### User Interface
- **Kanban View**: Visual card-based view showing request status
- **List View**: Tabular view with key fields
- **Form View**: Detailed view with tabs for products and other information
- **Search View**: Filters for state, requester, and search by name

### Reports
- PDF report template using QWeb
- Displays request header information and all line items in a table format
- Accessible via "Print Purchase Requisition" button

## Dependencies
- **purchase**: Core Odoo purchase module (for purchase orders and vendor management)

## Installation

1. Place this module in your Odoo addons directory
2. Update the apps list in Odoo
3. Install "Purchase Request" module
4. The menu will appear under **Purchase → Purchase Request**

## Use Cases

1. **Department Requisitions**: Employees request items needed for their department
2. **Budget Approval**: Requests can be reviewed before actual purchase orders are created
3. **Vendor Selection**: Track preferred vendors for each item
4. **Procurement Workflow**: Structured process from request to purchase order
5. **Audit Trail**: Complete history of what was requested, when, and by whom

## Key Benefits

- **Structured Workflow**: Clear process from request to purchase
- **Multi-Item Support**: One request can contain multiple products
- **Vendor Management**: Track preferred vendors per item
- **Date Tracking**: Multiple date fields for planning and tracking
- **Reporting**: Professional PDF reports for documentation
- **Integration Ready**: Can be extended to link with Purchase Orders

## Future Enhancement Possibilities

- Approval workflow (multi-level approvals)
- Budget checking and validation
- Automatic conversion to Purchase Orders
- Email notifications
- Integration with inventory management
- Cost center and accounting integration

## Author
**Arman Rehman**

## License
LGPL-3

