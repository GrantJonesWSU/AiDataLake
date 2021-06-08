<?php
include 'init.php';

//Request Handling

//Database Connection
if(isset($_POST['connectToDatabase']))
{
    echo ("Button saved for linking of AI to be developed in next sprint. DB in init.php is strictly for user query and login information storage.");
    
}

    //User Search History
if(isset($_POST['userHistory']))
{
    if($db)
    {
        //Gets Active User
        $sqlActiveUser= "SELECT id FROM userLogin WHERE loginStatus='1';";
        $row=mysqli_fetch_array(mysqli_query($db,$sqlActiveUser));
        $userId=($row['id']);
        
        //Displays User History
        $sqlUserHistory= "SELECT * FROM userTable WHERE id='$userId' ORDER BY requestDateTime DESC;";
        
        $historyResult=mysqli_query($db,$sqlUserHistory);
        
        //Itemizes query results for placement into a table
        while($row2=mysqli_fetch_assoc($historyResult))
        {
            echo $row2['requestText'];
            echo ("  |*|  ");
            echo $row2['metaGeneration'];
            echo ("  |*|  ");
            echo $row2['sqlOutput'];
            echo ("  |*|  ");
            echo $row2['requestDateTime'];
            echo ("  |*|  ");
        
        }
    
    }
}


//Recent Meta
if(isset($_POST['recentMeta']))
{
    if($db)
    {
        //Gets Active User
        $sqlActiveUser= "SELECT id FROM userLogin WHERE loginStatus='1';";
        $row=mysqli_fetch_array(mysqli_query($db,$sqlActiveUser));
        $userId=($row['id']);
        
        //Displays Recent Meta
        $sqlMetaRecent= "SELECT * FROM userTable WHERE id='$userId' ORDER BY requestDateTime DESC;";
        
        $metaResult=mysqli_query($db,$sqlMetaRecent);
        $row2=mysqli_fetch_assoc($metaResult);
        
        echo ("  Meta Generation For Your Most Recent Query:      ");
        echo $row2['metaGeneration'];
        
        
        
        
    }
    
}

?>