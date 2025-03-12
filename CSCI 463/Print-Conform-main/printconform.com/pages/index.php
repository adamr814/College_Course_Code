<?php
    @ini_set('session.cookie_secure', 1);
    @session_start();
    //Start PHP session
?>
<!-- PrintConform Index Version 1.0
Purpose: The homepage of the website where the user will land.
Author: Isaac Barta 
Creation Date: 5-4-2024
Modification History:
    5-4-2024: Initial Version
    5-4-2024: Updated for demo version
    5-9-2024: Changed to .php file for unification
    5-10-2024: Removed unfinished features to reduce bloat
-->
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link rel="stylesheet" href="../styles/style.css"/>
        <link rel="icon" href="../images/icon.png"/>
        <title>Print Conform</title>
    </head>
    <body>
        <?php 
            if(!isset($_SESSION['userid'])) {
                include 'header_login.php'; 
            } else {
                include 'header.php';
            }
        
        
        ?>

        <main>
            <div class="suggested">
                <h1>Most Popular Products</h1>
                <div class="products">
                    <a href="#">Photo Prints</a>
                    <a href="#">Photo Prints</a>
                    <a href="#">Photo Prints</a>
                    <a href="#">Photo Prints</a>
                    <a href="#">Photo Prints</a>
                </div>
            </div>
            <p class="warning">This is an unfinished prototype version of Print Conform for CSCI 463 - Software Engineering.</p>
        </main>

        <script>
            const toggleBtn = document.querySelector('.toggle_btn')
            const toggleBtnIcon = document.querySelector('.toggle_btn i')
            const dropDownMenu = document.querySelector('.dropdown_menu')

            toggleBtn.onclick = function () {
                dropDownMenu.classList.toggle('open')
                const isOpen = dropDownMenu.classList.contains('open')

                toggleBtnIcon.classList = isOpen
                    ? "images/x.png"
                    : "images/burger.png"
            }
        </script>
    </body>
    <style>
        .suggested {
            display: flex;
            flex-direction: column;
            transform: translate(0px, 56px);
        }
        .suggested h1 {
            margin-left: 20px;
            margin-top: 20px;
            color: white;
        }
        .products {
            display: flex;
            justify-content: space-evenly;
            margin-top: 20px;
        }
        .products a {
            background-image: url(../images/happy_family.jpg);
            background-size: 350px 210px;
            background-repeat: no-repeat;
            height: 270px;
            width: 350px;
            background-color: rgb(50, 50, 50);
            border-radius: 25px;
            text-align: center;
            line-height: 482px;
        }
    </style>
</html>