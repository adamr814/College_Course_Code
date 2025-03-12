<!-- PrintConform Checkout PHP Code Version 1.0
Purpose: To allow for the user to edit photos.
Author: Isaac Barta 
Creation Date: 5-10-2024
Modification History:
    5-10-2024: Initial Version
-->
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link rel="stylesheet" href="../styles/style.css"/>
        <link rel="icon" href="images/icon.png"/>
        <title>Checkout - Print Conform</title>
    </head>
    <?php include "../pages/header.php"; ?>
    <body>
        <h1>Checkout</h1>
        <div class="content">
            <div class="items">
                <h2>Items</h2>
            </div>
            <div class="shipping_and_payment">
                <h2>Shipping and Payment</h2>
                <h3>Shipping Address</h3>
                <p class="shipping street">1234 Main Street</p>
                <p class="shipping city_state_zip">Grand Forks, ND 58201</p>
                <h3>Shipping Method</h3>
                <p class="shipping_method">Standard Shipping (Free) (7-9 business days)</p>
                <a class="change_shipping" href="#">Change Shipping</a>
                <h3>Payment Method</h3>
                <p class="payment_method">Mastercard (x1234)</p>
                <h3>Billing Address</h3>
                <p class="billing street">1234 Main Street</p>
                <p class="billing city_state_zip">Grand Forks, ND 58201</p>
                <a class="change_payment" href="#">Change Payment</a>
                <h3 class="total_prompt">Total</h3>
                <p class="total">$75.63</p>
                <a class="place_order" href="#">Place Order</a>
            </div>
        </div>
    </body>
    <style>
        body {
            display: inline-block;
        }
        h1 {
            margin-top: 76px;
            margin-left: 20px;
            color: white;
        }
        h2, h3 {
            margin-top: 20px;
            margin-left: 20px;
            color: white;
        }
        p {
            margin-left: 20px;
            color: white;
        }
        .content {
            display: flex;
            justify-content: space-between;
            margin-top: 20px;
            margin-left: 20px;
        }
        .content .items {
            background-color: rgb(50, 50, 50);
            height: calc(100vh - 150px);
            width: calc(50vw - 30px);
            border-radius: 25px;
            margin-right: 20px;
        }
        .content .shipping_and_payment {
            background-color: rgb(50, 50, 50);
            height: calc(100vh - 150px);
            width: calc(50vw - 30px);
            border-radius: 25px;
        }
        .street, .shipping_method, .payment_method {
            margin-top: 10px;
        }
        .change_shipping, .change_payment, .place_order {
            display: inline-block;
            height: 40px;
            width: 250px;
            text-align: center;
            line-height: 40px;
            background-color: var(--pcpurple);
            color: white;
            border-radius: 10px;
            cursor: pointer;
            font-weight: bold;
            position: absolute;
            transform: translate(calc(50vw - 300px), -40px);
        }
        .change_shipping:hover, .change_payment:hover, .place_order:hover {
            background-color: white;
            color: var(--pcpurple);
        }
        .total_prompt {
            font-size: 20px;
            width: 10px;
            transform: translate(calc(50vw - 122px), calc(100vh - 650px));
        }
        .total {
            font-size: 20px;
            width: 10px;
            transform: translate(calc(50vw - 135px), calc(100vh - 645px)); 
        }
        .place_order {
            transform: translate(calc(50vw - 300px), calc(100vh - 635px));
        }
    </style>
</html>