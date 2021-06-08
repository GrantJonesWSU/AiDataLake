<?php
include 'init.php';

//Handles Request
if(isset($_POST['searchSubmit'])) 
{
    $requestTextInput=$_POST['search'];
    $requestDateTime= date("y-m-d h:i:s");

    //Handles databse connection
    if($db)
    {
     
        //Clear Request Queue
        $sqlDeleteQuery="DELETE FROM requestTable;";
            
        if(mysqli_query($db,$sqlDeleteQuery))
        {
            echo ("Delete Successful|");
        }
        else
        {
            die(mysqli_error($db));
        }
     
        
        //Get Active User Username
        $sqlActiveUser= "SELECT id FROM userLogin WHERE loginStatus='1';";
       
        if(mysqli_query($db,$sqlActiveUser))
        {
            echo ("id Gained Successfully|");
            $row=mysqli_fetch_array(mysqli_query($db,$sqlActiveUser));
            $idInput=($row['id']);
            
            //Test echo for obtaining id
            //echo($idInput);
        }
        else
        {
            die(mysqli_error($db));
        }
    
        //Update Request Queue 
        $sqlQuery= "INSERT INTO requestTable (requestTimeStamp,requestText,id) VALUES ('$requestDateTime','$requestTextInput','$idInput');";
                
        if(mysqli_query($db,$sqlQuery))
        {
            echo ("Insert Successful|");
        }
        else
        {
            die(mysqli_error($db));
        }
    }
}
?>