<!DOCTYPE html>
<!-- Print Conform Orders Webpage
    Version: 0.3
    Purpose: Displays a list of orders for a printing service or a user dependent on who is logged in. Includes the ability to download which grabs the files directly from R2 bypassing the webserver. 
    - Pre-requisites: User is logged in. 
    Author: Isaac Barta, Brandon Veen
    Creation Date: 4-30-2024
    Modification History:
    - 4-30-2024 - Initial Version
    - 5-3-2024 - Added MySQL Table Logic via php.
    - 5-4-2024 - Implmented R2 Link Generation for User Downloads
-->

<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="../styles/style.css"/>
    <link rel="icon" href="images/icon.png"/>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.2/css/all.min.css" integrity="sha512-SnH5WK+bZxgPHs44uWIX+LLJAJ9/2PkPKZ5QiAj6Ta86w+fsb2TkcmfRyVX3pBnMFcV7oQPJkl9QevSCWr3W6A==" crossorigin="anonymous" referrerpolicy="no-referrer" />
    <title>Orders - Print Conform</title>
    <!-- Placing a style change here temporarily -->
    <style>
        .table_div {
            border: 1px outset #454545;
            width: 75%;
        }
        table {
            border-collapse: collapse;
            width: 100%;
        }
        thead {
            background-color: #454545
        }
        td, th {
            /* border: 1px solid #263f3f; */
            text-align: left;
            padding: 10px;
        }
        tr:nth-child(even) {
            background-color: #2c2c2c;
        }
        a:link {
            color: green;
            background-color: transparent;
            text-decoration: none;
        }
        /* a:visited {
            color: pink;
            background-color: transparent;
            text-decoration: none;
        }
        a:hover {
            color: red;
            background-color: transparent;
            text-decoration: underline;
        }
        a:active {
        color: yellow;
        background-color: transparent;
        text-decoration: underline;
        } */

    </style>

</head>
<body>
    <!-- Session Information: Needs to be updated for cookie or later authentication procedures -->
    <?php
        $user_id = 2; //Should grab this from cookie for demo and use user authentication to grab from MySQL in finished prototype.
        $comp_id = 2; //Same as above.
        $login_type = 1; //0 = User, 1 = Print Provider
    ?>
    <?php 
        //require '../../scripts/php/aws.phar'; 
        include '../../scripts/php/connect_r2.php';
    ?>
    
    <?php include 'header.php'; ?>

    <main>
        <section id="hero">
            <h1>Orders</h1>
            
            <div class="table_div"> 
                <table style="width:100%">
                    <thead>
                        <tr>
                            <th>Order Number</th>
                            <!-- <th>Service Provider</th> -->
                            <?php 
                                if ($login_type == 0) {
                                    //echo('<h1>LOGGED IN AS USER</h1>');
                                    echo '<th>Service Provider</th>';
                                } 
                                else if ($login_type == 1) {
                                    echo '<th>Name</th>';
                                }
                            ?>
                            <th>Order Date</th>
                            <th>Price</th>
                            <th>Status</th>
                            <th>Tracking</th>
                            <th>Download</th>
                        </tr>
                    </thead>
                    <tbody>
                        <?php 
                            //Load database information into variable $conn. Others used are $servername, $username, $password, $schema
                            include '../../scripts/php/connect_db.php';

                            if ( $conn->connect_error) {
                                die ('Could not connect: ' . $conn->connect_error);
                            } else {
                                //SQL Queries for Print Provider and User
                                if ($login_type == 0) {
                                    //echo('<h1>RUNNING USER QUERY</h1>');
                                    $sql = "SELECT o1.order_id, s2.sname, o1.order_date, o1.price, o1.order_status, o1.tracking, o1.r2_link, o1.user_id 
                                        FROM pcorder o1, printservice s2
                                        WHERE user_id=$user_id AND s2.sid = o1.comp_id;";
                                } else if ($login_type == 1) {
                                    //echo('<h1>RUNNING PROVIDER QUERY</h1>');
                                    $sql = "SELECT o1.order_id, CONCAT(p3.first_name, \" \", p3.last_name) AS users_name, o1.order_date, o1.price, o1.order_status, o1.tracking, o1.r2_link, o1.user_id
                                    FROM pcorder o1, printservice s2, pcuser p3
                                    WHERE s2.sid=$comp_id AND o1.comp_id = s2.sid AND o1.user_id = p3.uid;";
                                }

                                //Build Table
                                if ($result = $conn->query($sql)) {
                                    //Count Number of Rows 
                                    $rowcount=mysqli_num_rows($result);

                                    //Display "No Orders" if there are 0 rows, otherwise generate rows and links
                                    if ($rowcount == 0) {
                                        echo '<tr><th><h3>No Orders</h3></th></tr>';
                                    } else {
                                        while ($row = $result->fetch_assoc() ) {
                                            echo '<tr>';
                                            echo '<th>' . htmlspecialchars($row['order_id']);
                                            //Conditional Echo based on Login Type
                                            if ($login_type == 0) {
                                                echo '<th>' . htmlspecialchars($row['sname']);
                                            } else if ($login_type == 1) {
                                                echo '<th>' . htmlspecialchars($row['users_name']);
                                            }
                                            echo '<th>' . htmlspecialchars($row['order_date']);
                                            echo '<th>' . htmlspecialchars($row['price']);
                                            echo '<th>' . htmlspecialchars($row['order_status']);
                                            echo '<th>' . htmlspecialchars($row['tracking']);
                                            //R2 Logic Row
                                            $r2_link = $row['r2_link'];
                                            $result_user = $row['user_id']; //Can't use $user_id because the logged in user could be a print provider and not a regular user.
                                            $result_order = $row['order_id'];
                                            //$result_username = $row['username'];

                                            //Create Pre-Signed URL
                                            $cmd = $s3_client->getCommand('GetObject', [
                                                'Bucket' => $bucket_name,
                                                'Key' => 'pcuser/' . $result_user . '/' . $result_order . '/' . $r2_link
                                            ]);
                                            $request = $s3_client->createPresignedRequest($cmd, '+3 minutes');

                                            //Generate Pre-signed URL
                                            $presignedUrl = (string)$request->getUri();
                                            echo '<th>' . '<a href=' . $presignedUrl . ' download="' . $r2_link .'" target="_blank" type="application/octet-stream">' . $r2_link . '</a>';
                                            
                                        }
                                    }
                                }
                            } 

                            //Close the connection
                            $conn->close();
                        ?>
                    </tbody>
                </table>
            </div>
            <!-- <p style="padding:10px">"6 Orders For Some Reason"</p> -->
        </section>
    </main>

    <script>
        const toggleBtn = document.querySelector('.toggle_btn')
        const toggleBtnIcon = document.querySelector('.toggle_btn i')
        const dropDownMenu = document.querySelector('.dropdown_menu')

        toggleBtn.onclick = function () {
            dropDownMenu.classList.toggle('open')
            const isOpen = dropDownMenu.classList.contains('open')

            toggleBtnIcon.classList = isOpen
                ? "fa-solid fa-xmark"
                : "fa-solid fa-bars"
        }
    </script>
</body>
</html>