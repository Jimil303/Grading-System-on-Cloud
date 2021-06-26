<?php
    // Loads Database Details
    include("config.php");

    // Creates Connection
    $db = pg_connect("$db_host $db_name $db_username $db_password");

    // Grabs Selection
    $userInput = $_GET['typed'];

    // Runs Query On Database
    $query = "SELECT name FROM university";

    // Runs Query And Places It
    $result = pg_query($query);

    // Kills Script If No Results
    if (!$result) {
        echo "Problem with query " . $query . "<br/>";
        echo pg_last_error();

        return json_encode(array());

        die();
    }

    $list = pg_fetch($result);

    return json_encode($list);
?>
