# Fatmug

## Introduction

This project is a comprehensive API backend solution designed to manage vendors and purchase orders effectively. It provides a set of RESTful API endpoints for creating, updating, retrieving, and deleting vendor and purchase order information. Additionally, it offers features such as vendor performance metrics calculation and purchase order acknowledgment.

1. Clone the repository:
   ```bash
   git clone <https://github.com/gaharivatsa/fatmug.git>
   cd <fatmug>

2.pip install -r requirements.txt


Usage

Once  is installed, you can start the development server and begin using the API endpoints.

1.Start the development server:
  python manage.py runserver 
  
2.Testing
To ensure the reliability and functionality of , a test suite has been included. To run the test suite, execute the following command:
python manage.py test

3.API Endpoints

Vendor Endpoints
POST /api/vendors/: Create a new vendor.
GET /api/vendors/: List all vendors.
GET /api/vendors/<vendor_id>/: Retrieve details of a specific vendor.
PUT /api/vendors/<vendor_id>/: Update a vendor.
DELETE /api/vendors/<vendor_id>/: Delete a vendor.

Purchase Order Endpoints
POST /api/purchase_orders/: Create a purchase order.
GET /api/purchase_orders/: List all purchase orders.
GET /api/purchase_orders/<po_id>/: Retrieve details of a specific purchase order.
PUT /api/purchase_orders/<po_id>/: Update a purchase order.
DELETE /api/purchase_orders/<po_id>/: Delete a purchase order.

Other Endpoints
GET /api/vendors/<vendor_id>/performance/: Retrieve performance metrics for a vendor.
POST /api/purchase_orders/<po_id>/acknowledge/: Acknowledge a purchase order.

#Contributing
Contributions are welcomed! To contribute, please follow these steps:

Fork the repository.
Create a new branch for your feature or fix.
Make your changes and commit them.
Push your changes to your fork.
Submit a pull request.
