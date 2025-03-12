<?php
    @ini_set('session.cookie_secure', 1);
    @session_start();
    //Start Session
?>
<?php
    /* PrintConform Login PHP Code Version 1.0
     * Purpose: To allow for the user to login to their account with their credentials.
     * Author: Isaac Barta (Front End), Brandon Veen (Back End) 
     * Creation Date: 5-9-2024
     * Modification History:
     * 5-9-2024: Initial Version
     * 5-10-2024: Modified to store a PHP session.
     * 5-10-2024: Further modified to start the session as the very first item on load.
    */
    $error_output = ""; //Initial State

    if (!isset($_POST['username'])) {
        //Do nothing
    } else {
        //Grab POST Data
        $email = $_POST['username'];
        $provided_password = $_POST['password'];

        //PHP Includes
        include '../../scripts/php/connect_db.php';
        include '../../scripts/php/path_python.php';

        //Open Connection to MySQL
        if ( $conn->connect_error) {
            die ('<p>Could not connect: ' . $conn->connect_error . '</p>');
        } else {
            //Prepare Login Statement
            $statement = $conn->prepare("SELECT * FROM pcuser WHERE email=?");
            $statement->bind_param("s", $email);
            //Execute and Error Catch
            try {
                //Execute MySQL Query
                $statement->execute();
                $result = $statement->get_result();
                $row = $result->fetch_assoc();
                
                //Check for entry
                if($result->num_rows == 0) {
                    $error_output = 'Invalid email or password';
                } else {
                    //$row = $result->fetch_assoc();
                    $userid = $row['uid'];
                    $hashedpassword = $row['user_password'];
                    
                    //Close the MySQL connection
                    $conn->close();

                    //Run python script
                    //echo '<p>Before Python Script</p>';
                    $command = escapeshellcmd($path_to_python . ' ../../scripts/python/compare_password.py ' . $provided_password . ' ' . $userid);
                    $output = shell_exec($command);
                    $str_authenticated = intval($output);
                    if($str_authenticated == 1) {
                        //Login User
                        $_SESSION['userid'] = $userid;
                        $_SESSION['usermode'] = $row['user_type'];
                        $_SESSION['username'] = $row['username'];
                        $_SESSION['first'] = $row['first_name'];
                        $_SESSION['last'] = $row['last_name'];

                        //Unset Variables
                        unset($statement);
                        unset($email);
                        unset($provided_password);
                        unset($str_authenticated);
                        unset($output);
                        unset($command);
                        unset($hashedpassword);
                        unset($userid);
                        unset($row);
                        unset($conn);
                        
                        //Load Index instead of Login
                        include 'index.php';
                        exit;

                    } else {
                        //Do Not Login
                        //usleep(50000);
                        $error_output = 'Invalid email or password';
                        //Do Not Login
                    }
                }  
            } catch (Exception $e) {
                $error = $e->getMessage();
                $error_output = $error;
            }
        }
        //Unset Variables
        unset($statement);
        unset($email);
        unset($provided_password);
        unset($str_authenticated);
        unset($output);
        unset($command);
        unset($hashedpassword);
        unset($userid);
        unset($row);
        unset($conn);
    }
?>

<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link rel="stylesheet" href="../styles/style.css"/>
        <link rel="icon" href="images/icon.png"/>
        <title>Print Conform</title>
        <script type="text/javascript">
            function Redirect() {
                window.location.href = "index.php";
            }
        </script>

    </head>
    <body>
        <main>
            <div class="login_container">
                <form method="post" action="login.php">
                    <div class="logo"><a href="index.php">Print Conform</a></div>
                    <h1>Log in</h1>
                    <p class="login_prompt">To continue to Print Conform</p>
                    <h2>Email</h2>
                    <input class="input_box" type="text" name="username" placeholder="Username" required>
                    <h2>Password</h2>
                    <input class="input_box" type="password" name="password" placeholder="Password" required>
                    <div class="remember_forgot">
                        <label><input type="checkbox">Keep me signed in</label>
                        <a href="#">Forgot password?</a>
                    </div>
                    <button type="submit" name="act" value="Login" class="login_btn">Log in</button>
                    <div class="register_link">
                        <a href="register.php">Create an account</a>
                    </div>
                    <center><p class="error" style="padding-top:12px;"><?php echo $error_output ?></p></center>
                </form>
            </div>
        </main>
        <script>

        </script>
        <style>
            .login_container {
                /* Set size and position */
                height: 650px;
                width: 600px;
                position: absolute;
                top: 50%;
                left: 50%;
                transform: translate(-50%, -50%);
                /* Set color and style */
                background-color: var(--gray2);
                color: white;
                border-radius: 25px;
                box-shadow: 0px 0px 20px 15px rgba(0, 0, 0, 0.25);
            }

            .login_container .logo a {
                /*Set size and image*/
                background-image: url("../images/logo.png");
                background-size: 300px;
                background-repeat: no-repeat;
                text-indent: -999999px; /*Hides screen reader text*/
                height: 76.8px;
                width: 300px;
                /**/
                display: flex;
                background-position: center;
                margin-left: 20px;
                margin-top: 20px;
                cursor: pointer;
            }

            .login_container h1 {
                font-size: 32px;
                margin-left: 20px;
                margin-top: 20px;
            }

            .login_container .login_prompt {
                margin-left: 20px;
                margin-top: 10px;
            }

            .login_container h2 {
                font-size: 20px;
                margin-left: 20px;
                margin-top: 30px;
            }

            .login_container .input_box {
                width: 560px;
                height: 50px;
                background-color: var(--gray3);
                margin-left: 20px;
                border: 1px solid var(--gray0);
                outline: none;
                border-radius: 10px;
                margin-top: 5px;

                color: white;
                font-size: 16px;
                padding: 10px;
            }

            .login_container .remember_forgot {
                display: flex;
                justify-content: space-between;
                margin-top: 5px;
            }

            .login_container label {
                font-size: 16px;
                cursor: pointer;
            }

            .login_container label input {
                margin-left: 20px;
                margin-right: 10px;
                margin-top: 40px;
                accent-color: var(--pcpurple);
                cursor: pointer;
            }

            .login_container a {
                color: var(--pcpurple);
            }

            .login_container .remember_forgot a {
                margin-right: 20px;
            }

            .login_container .remember_forgot a:hover {
                text-decoration: underline;
            }

            .login_container .login_btn {
                height: 50px;
                width: 560px;
                min-width: 110px;    
                text-align: center;
                line-height: 50px;
                font-size: 20px;
                background-color: var(--pcpurple);
                color: white;
                border: none;
                border-radius: 10px;
                cursor: pointer;
                margin-left: 20px;
                margin-top: 45px;
                font-weight: bold;
            }

            .login_container .login_btn:hover {
                background-color: white;
                color: var(--pcpurple);
            }

            .login_container .login_btn:active {
                scale: 0.95;
            }

            .login_container .register_link a {
                margin-top: 35px;
                display: flex;
                justify-content: center;
            }

            .login_container .register_link a:hover {
                text-decoration: underline;
            }
        </style>
    </body>
</html>