<?php
//Loading Of Database Connection
  $dbHostname="localhost";
  $dbUser="id16988493_seniorprojectwsu";
  $dbPass="Y2OIoKH6>#O9[&-b";
  $dbID= "id16988493_amazondatalake";

  //create connection
  $db = mysqli_connect($dbHostname,$dbUser,$dbPass,$dbID);
  // Check connection
  if (mysqli_connect_errno())
  {
    echo '<br>Server: ' . $dbHostname;
    echo '<br>Username:' . $dbUser;
    echo '<br>Password: ' . $dbPass;
    echo '<br>Database: ' . $dbID . '<br>';
    die("Failed to connect to MySQL: " . mysqli_connect_error() . "<br>");
  }
  else
  {
      //echo ('Connection successful');
  }
?>