<?php
    $db_conn = pg_connect("host=IP_SERVER port=PORT_SERVER dbname=DBNAME user=USER password=PASSWOR") or die('Could not connect: ' . pg_last_error());
    $sql = pg_query("SELECT token FROM users WHERE id_chat = {$_POST['id_chat']}") or die('Could not connect: ' . pg_last_error());
    if(!($row = pg_fetch_row($sql))){
        $result = pg_query("INSERT INTO users(token,social,ttl,id_user,id_chat) VALUES('{$_POST['token']}','{$_POST['social']}',{$_POST['ttl']},{$_POST['id_user']},{$_POST['id_chat']})") or die('Could not connect: ' . pg_last_error());
    } else {
        $result = pg_query("UPDATE users SET token = '{$_POST['token']}' WHERE id_chat = {$_POST['id_chat']}") or die('Could not connect: ' . pg_last_error());
    }
    pg_free_result($result);
    pg_close($db_conn);
?> 
