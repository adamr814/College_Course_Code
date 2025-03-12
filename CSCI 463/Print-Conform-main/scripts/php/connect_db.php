<?php 
    /* Print Conform Connect DB
        * Version: 1.0
        * Purpose: For inclusion in python scripts, stores database connection information.
        * Author: Brandon Veen
        * Creation Date: 05-04-2024
    */
    // MySQL Connection Information
    $servername = "mysql.printconform.com";
    $username = "printconform";
    $password = "FUtBt!4Oqs";
    $schema = "printconform";
    $conn = new mysqli($servername, $username, $password, $schema);
    unset($servername);
    unset($username);
    unset($password);
    unset($schema);
?>
