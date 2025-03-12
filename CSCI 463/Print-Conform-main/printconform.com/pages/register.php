<?php
@ini_set('session.cookie_secure', 1);
@session_start();
?>
<!-- PrintConform Register PHP Code Version 1.0
Purpose: To allow for the user to create an account.
Author: Isaac Barta 
Creation Date: 5-9-2024
Modification History:
    5-9-2024: Initial Version
-->
<?php $update_text = "" ?>
<?php
    //Import MySQL Information
    if (!isset($_POST['email'])) {
        //Do nothing
        echo 'Doing Nothing <br>';
    } else {
        //Grab $_POST Data
        $first = $_POST['first'];
        $last = $_POST['last'];
        $pc_username = $_POST['username'];
        $email = $_POST['email'];
        $user_password1 = $_POST['password1'];
        $user_password2 = $_POST['password2'];
        echo 'Grabbed Post Data <br>';
        //PHP Includes
        include '../../scripts/php/connect_db.php';
        include '../../scripts/php/path_python.php';
        echo 'PHP included <br>';

        do {
            //Check that password1 == password2
            if($user_password1 != $user_password2) {
                $update_text = "Passwords do not match.";
                echo 'Passwords do not match';
                break;
            }
            echo 'Passwords match both fields <br>';
            //Open MySQL Connection
            if ( $conn->connect_error) {
                die ('<p>Could not connect: ' . $conn->connect_error . '</p>');
                echo "Did not connect. <br>";
            } else {
                //Check if email is already taken.
                $statement = $conn->prepare("SELECT * FROM pcuser WHERE email=?");
                $statement->bind_param("s", $email);
                //Execute MySQL Query
                $statement->execute();
                $result = $statement->get_result();
                $row = $result->fetch_assoc();
                echo 'RESULT ROWS FOR EMAIL QUERY: ' . $result->num_rows;
                if($result->num_rows != 0) {
                    $update_text = 'Email is already taken.';
                    $conn->close();
                    break;
                }
                echo 'Email SQL passed';
                //Check if username is already taken.
                $statement = $conn->prepare("SELECT * FROM pcuser WHERE username=?");
                $statement->bind_param("s", $pc_username);
                //Execute MySQL Query
                $statement->execute();
                $result = $statement->get_result();
                $row = $result->fetch_assoc();
                if($result->num_rows != 0) {
                    $update_text = 'Username is already taken.';
                    $conn->close();
                    break;
                }
                echo 'Username SQL passed';
                //Create User in MySQL
                $statement = $conn->prepare("INSERT INTO pcuser(uid, username, email, user_password, first_name, last_name, user_type, salt) VALUES (null, ?, ?, null, ?, ?, 1, null)");
                $statement->bind_param("ssss", $pc_username, $email, $first, $last);
                try {
                    //Execute MySQL Query
                    $statement->execute();
                    //$result = $statement->get_result();
                    $userid = $conn->insert_id;
                    echo 'Create User Passed';

                    //Run salt.py
                    $command = escapeshellcmd($path_to_python . ' ../../scripts/python/generate_salt.py');
                    $output = shell_exec($command);
                    $new_salt = substr($output, 0, -1);

                    //Insert Salt into MySQL
                    $statement = $conn->prepare("UPDATE pcuser SET salt=? WHERE uid=?");
                    $statement->bind_param("si", $new_salt, $userid);
                    $statement->execute();

                    //Hash Password
                    $command = escapeshellcmd($path_to_python . ' ../../scripts/python/hash.py ' . $user_password1 . ' ' . $userid);
                    $output = shell_exec($command);
                    $hashed_password = substr($output, 0, -1);

                    //Update MySQL with password hash.
                    $statement = $conn->prepare("UPDATE pcuser SET user_password=? WHERE uid=?");
                    $statement->bind_param("si", $hashed_password, $userid);
                    $statement->execute();

                    $update_text = $first . ' ' . $last . ' registered!';

                } catch (Exception $e) {
                    $error = $e->getMessage();
                    $error_output = $error;
                    echo 'Exception Detected <br>';
                }
            }

            //Close the MySQL Connection
            $conn->close();

        } while (false);
        
    }

?>

<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link rel="stylesheet" href="../styles/style.css"/>
        <link rel="icon" href="../images/icon.png"/>
        <title>Register - Print Conform</title>
    </head>
    <body>
        <main>
            <div class="register_container">
                <form method="post" action="register.php">
                    <div class="logo"><a href="index.php">Print Conform</a></div>
                    <h1>Register</h1>
                    <h2>First Name</h2>
                    <input class="input_box" type="text" name='first' value='' placeholder="First Name" required>
                    <h2>Last Name</h2>
                    <input class="input_box" type="text" name='last' value='' placeholder="Last Name" required>
                    <h2>Username</h2>
                    <input class="input_box" type="text" name='username' value='' placeholder="Username" required>
                    <h2>Email</h2>
                    <input class="input_box" type="text" name='email' value='' placeholder="Email" required>
                    <h2>Password</h2>
                    <input class="input_box" name='password1' type="password" placeholder="Password" required>
                    <h2>Confirm Password</h2>
                    <input class="input_box" name='password2' type="password" placeholder="Password" required>
                    <div class="remember_forgot">
                        <label><input type="checkbox" required>I have read and agree to the <a href="#">terms and conditions</a></label>
                    </div>
        
                    <button type="submit" class="register_btn">Register</button>
        
                    <div class="login_link">
                        <a href="login.php">Have an account? Log in</a>
                    </div>
                    <center><p style="padding-top:5px;"><?php echo $update_text; ?></p></center>
                </form>
            </div>
        </main>
        <script>

        </script>
        <style>
            .register_container {
                /* Set size and position */
                height: 900px;
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

            .register_container .logo a {
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

            .register_container h1 {
                font-size: 32px;
                margin-left: 20px;
                margin-top: 20px;
            }

            .register_container .register_prompt {
                margin-left: 20px;
                margin-top: 10px;
            }

            .register_container h2 {
                font-size: 20px;
                margin-left: 20px;
                margin-top: 22px;
            }

            .register_container .input_box {
                width: 560px;
                height: 40px;
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

            .register_container .remember_forgot {
                display: flex;
                justify-content: space-between;
                margin-top: 5px;
            }

            .register_container label {
                font-size: 16px;
                cursor: pointer;
            }

            .register_container label input {
                margin-left: 20px;
                margin-right: 10px;
                margin-top: 20px;
                accent-color: var(--pcpurple);
                cursor: pointer;
            }

            .register_container a {
                color: var(--pcpurple);
            }

            .register_container .remember_forgot a {
                margin-right: 20px;
            }

            .register_container .remember_forgot a:hover {
                text-decoration: underline;
            }

            .register_container .register_btn {
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
                margin-top: 25px;
                font-weight: bold;
            }

            .register_container .register_btn:hover {
                background-color: white;
                color: var(--pcpurple);
            }

            .register_container .register_btn:active {
                scale: 0.95;
            }

            .register_container .login_link a {
                margin-top: 35px;
                display: flex;
                justify-content: center;
            }

            .register_container .login_link a:hover {
                text-decoration: underline;
            }
        </style>
    </body>
</html>