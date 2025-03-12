<?php
@ini_set('session.cookie_secure', 1);
@session_start();
?>
<?php
/* PrintConform Profile/Logout Page
 * Version: 0.8
 * Purpose: Provide user a way to logout (implemented) and for later development display a user's information (not in prototype)
 * Inputs: $_SESSION data from PHP.
 *          If called via $_POST with 'value'='Logout' with 'name'='act' will destroy the PHP session
 * Outputs: HTML Profile Page or an included index.php
 * Author: Isaac Barta (Front-end), Brandon Veen (Back-end)
*/

//Page Accessed without logging in first.
if(!isset($_SESSION['userid'])) {
    include 'index.php';
    exit;
}
//Determine if an $_POST event was sent to this page with action "Logout"
if (!isset($_POST['act']) ) {
    //Do Nothing
} else {
    if($_POST['act'] === 'Logout') {
        session_destroy();
        include 'index.php';
        exit;
    }
}
?>

<!DOCTYPE HTML>
<head>
    <link rel="stylesheet" href="../styles/style.css"/>
    <link rel="icon" href="../images/icon.png"/>
    <title>Profile - Print Conform</title>
</head>
<body>
    <?php include "header.php"; ?>
    <h1>Profile</h1>
    <h2>UserID: <?php echo $_SESSION['userid']; ?></h2>
    <h2>Name: <?php echo $_SESSION['first'] . " " . $_SESSION['last']; ?></h2>
    <h2>User Mode: <?php echo $_SESSION['usermode']; ?></h2>
    <form method='post' action='profile.php'>
        <button class="button" type="submit" name="act" value="Logout">Log Out</button>
    </form>
</body>
<style>
    h1 {
        color: white;
        transform: translate(20px, 76px);
        width: 200px;
    }
    h2 {
        padding-top: 20px;
        padding-left: 20px;
        color: white;
        transform: translate(20px, 76px);
        width: 400px;
    }
    h3 {
        color: white;
        transform: translate(20px, 76px);
        width: 400px;
    }
    button {
        height: 40px;
        width: 110px;
        min-width: 110px;
        text-align: center;
        line-height: 40px;
        background-color: var(--pcpurple);
        color: white;
        border-radius: 10px;
        cursor: pointer;
        font-weight: bold;
        font-size: 16px;
        border: none;
        transform: translate(20px, 96px);
    }
    button:hover {
        background-color: white;
        color: var(--pcpurple);
    }
</style>