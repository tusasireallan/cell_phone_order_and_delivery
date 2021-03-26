from configara import *

def record_category():
    #this is a method for the admin to Capture the flights booked or reserved for departing customers
    print("Welcome to====JAVSPHONE========")
    print("==============================")
    sql = "INSERT INTO category_tbl (categoryID,category_name,category_type_id,category_status )  VALUES (%s,%s,%s,%s)"
    categoryID = int (input("Please Enter CategoryID: "))
    category_name = input('Please Enter Category name:')
    category_type_id= int (input("Please Enter Category typeID: "))
    category_status = input("Please Enter category Status: ") 
    values = (categoryID,category_name,category_type_id,category_status)
    mypointer.execute(sql, values)
    mydatabase.commit()
    print(mypointer.rowcount,"New Category Captured successfully............................................................")
#record_category()


def catalog_Record():
    #this is a method for a customer when he's going to use the app for booking a flight
    print("======== AVSPHONE Phone Catalog =======")
    print("================================================================")
    sql = "INSERT INTO catalog_tbl(category_type_id,catalogID,phone_name,phone_description,phone_features,phone_dimension,phone_price,weigh_height_widith,phone_availability,phone_color)  VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    category_type_id =  int (input('Enter Phone Category type id: '))
    catalogID = int (input('Enter CatelogID:'))
    phone_name = input ('Enter Phone Name:')
    phone_description = input ('Enter phone Description:')
    phone_features = input ('Enter Phone Features:')
    phone_dimension = float (input('Enter Phone Dimension: '))
    phone_price = float (input('Enter phone price:'))
    weigh_height_widith = float (input('Enter Phone weight,widith and Height: '))
    phone_availability = input('Enter phone availability Status(Yes or No): ')
    phone_color = input('Enter phone color:')
    values = (category_type_id,catalogID,phone_name,phone_description,phone_features,phone_dimension,phone_price,weigh_height_widith,phone_availability,phone_color)
    mypointer.execute(sql, values)
    mydatabase.commit()
    print(mypointer.rowcount,"New Phone Captured successfully.")
#catalog_Record()

def customer_details():
    print("================================================================")
    sql = "INSERT INTO customer_tbl (customer_id,customer_first_name,customer_last_name,customer_middle_name,customer_email,customer_phone_number,customer_username,customer_password,account_status,customer_order_date)  VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    customer_id = int (input('Enter customer_id: '))
    customer_first_name = input ('Enter first Name:')
    customer_last_name = input ('Enter last Name:')
    customer_middle_name = input ('Enter Middle Name:')
    customer_email = input ('Enter customer email:')
    customer_phone_number = int (input ('Customer Phone Number:'))
    customer_username = input ('Customer Username:')
    customer_password = input ('Cutomer Password:')
    account_status = input ('Enter whether still Active or Not:')
    customer_order_date = input('Enter flight arrival Date  in YYYY-MM-DD format: ')
    year,month,day = map(int, customer_order_date.split('-'))
    values = (customer_id,customer_first_name,customer_last_name,customer_middle_name,customer_email,customer_phone_number,customer_username,customer_password,account_status,customer_order_date)
    mypointer.execute(sql, values)
    mydatabase.commit()
    print(mypointer.rowcount,"New Customer Ordered  successfully.")

#customer_details()

def adminsRecords():
    print("================================================================")
    sql = "INSERT INTO admins_tbl (admins_id,full_name,admin_contact,admin_email,admins_username,admins_password)  VALUES (%s,%s,%s,%s,%s,%s)"
    admins_id = int (input(' admin_id: '))
    full_name = input ('Full Name:')
    admin_contact = int (input ('Phone Number:'))
    admin_email = input ('email ddress:')
    admins_username = input ('Username:')
    admins_password = input ('pass_word:')
    values = (admins_id,full_name,admin_contact,admin_email,admins_username,admins_password)
    mypointer.execute(sql, values)
    mydatabase.commit()
    print(mypointer.rowcount,"New Admin  successfully Registered.")

#adminsRecords()


def orders_capture():
    print("=============================")
    sql = "INSERT INTO order_tbl(order_id,customer_id,total_amount,order_status,sold_by,sold_order_date)  VALUES (%s,%s,%s,%s,%s,%s)"
    order_id = int(input('Enter Order ID:'))
    customer_id = int(input('Enter Customer ID:')) 
    total_amount = float (input('Enter Amount:'))
    order_status = int(input('Enter Order Status (0-pending, 1-confirmed, 2-cancelled):'))
    sold_by = int(input("Enter the code of the sales person:"))
    sold_order_date = input('Enter the order Date  in YYYY-MM-DD format: ')
    year,month,day = map(int, sold_order_date.split('-'))
    values = (order_id,customer_id,total_amount,order_status,sold_by,sold_order_date)
    mypointer.execute(sql, values)
    mydatabase.commit()
    print(mypointer.rowcount,"New Order Captured successfully Registered.")

#orders_capture()


def customer_invoice():
    print("=============================")
    sql = "INSERT INTO orderdetails_tbl(order_details_id,order_id,categoryID,amount,no_of_items,total_amount)  VALUES (%s,%s,%s,%s,%s,%s)"
    order_details_id = int(input('Enter Customer InvoiceID:'))
    order_id = int(input('Enter Order ID:'))
    categoryID = int (input('Enter categoryID:'))
    amount = float(input('Enter amount of the phone or Category:'))
    no_of_items = int(input('Enter Quantity:'))
    total_amount = float(input('Enter amount of paid by a customer:'))
    values = (order_details_id,order_id,categoryID,amount,no_of_items,total_amount)
    mypointer.execute(sql, values)
    mydatabase.commit()
    print(mypointer.rowcount,"New Invoice Captured successfully Registered.")

#customer_invoice()

def paymentRecord ():
    print("=============================")
    sql = "INSERT INTO payment_tbl(payment_id ,order_id,amount,paid_by,payment_date,sold_by )  VALUES (%s,%s,%s,%s,%s,%s)"
    payment_id = int(input('Enter paymentID:'))
    order_id = int(input('Enter orderID:'))
    amount = float (input('Enter Amount :'))
    paid_by = input('Enter Amount Paid by:')
    payment_date = input('Enter the payment Date  in YYYY-MM-DD format: ')
    year,month,day = map(int, payment_date.split('-'))
    sold_by = int(input('Enter Sales Person code:'))
    values = (payment_id ,order_id,amount,paid_by,payment_date,sold_by)
    mypointer.execute(sql, values)
    mydatabase.commit()
    print(mypointer.rowcount,"New Paymennt Captured successfully Registered.")

#paymentRecord()


def addressesRecord ():
    print("=============================")
    sql = "INSERT INTO addresses_tbl(address_id,order_details_id,line_1,line_2 ,city_name, post_code ,customer_id )  VALUES (%s,%s,%s,%s,%s,%s,%s)"
    address_id = int(input('Enter  addressID:'))
    order_details_id = int(input('order_detailsID:'))
    line_1 = input('Enter Address 1:')
    line_2 = input('Enter Address 2:')
    city_name = input('Enter city_name:')
    post_code = int(input('Enter Postcode:'))
    customer_id = int(input('Enter customerID:'))
    values = (address_id,order_details_id,line_1,line_2 ,city_name, post_code ,customer_id)
    mypointer.execute(sql, values)
    mydatabase.commit()
    print(mypointer.rowcount,"New Customer Adderess Captured successfully Registered.")

#addressesRecord()

def deliveryRecords():
    print("=============================")
    sql = "INSERT INTO order_delivery_tbl(order_delivery_id,admins_id,order_details_id,customer_id,delivery_status_code,delivery_address,delivery_type,delivery_by,delivery_time_and_date,address_id)  VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    order_delivery_id = int(input('Enter order_deliveryID:'))
    admins_id = int(input('Enter adminsID:')) 
    order_details_id = int(input('Enter  InvoiceID:'))
    customer_id = int(input('Enter  customerID:'))
    delivery_status_code = int(input('Enter  status code:'))
    delivery_address = input('Enter Delivery address:')
    delivery_type = input('Enter type of delivery:')
    delivery_by = input('Enter  delivery agent:')
    delivery_time_and_date = input('Enter the payment Date  in YYYY-MM-DD format: ')
    year,month,day = map(int, delivery_time_and_date.split('-'))
    address_id = int (input('Enter  addressID:'))
    values = (order_delivery_id,admins_id,order_details_id,customer_id,delivery_status_code,delivery_address,delivery_type,delivery_by,delivery_time_and_date,address_id)
    mypointer.execute(sql, values)
    mydatabase.commit()
    print(mypointer.rowcount,"New Order Delivery Captured successfully Registered.")

#deliveryRecords()

def getFeedback():
    print("=============================")
    sql = "INSERT INTO odernotes_feedback_tbl(feedback_id,categoryID,delivery_service,customer_remarks,date_recorded,customer_id )  VALUES (%s,%s,%s,%s,%s,%s)"
    feedback_id = int(input('Enter feedbackID:'))
    categoryID = int(input('Enter categoryID:'))
    delivery_service = int(input('Enter delivery_serviceID:'))
    customer_remarks = input('Enter customer_remarks:')
    date_recorded = input('Enter the payment Date  in YYYY-MM-DD format: ')
    year,month,day = map(int, date_recorded.split('-'))
    customer_id  = int(input('Enter customerID:'))
    values = (feedback_id,categoryID,delivery_service,customer_remarks,date_recorded,customer_id)
    mypointer.execute(sql, values)
    mydatabase.commit()
    print(mypointer.rowcount,"New Customer feeback Captured successfully Registered.")

#getFeedback()


