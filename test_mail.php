<?php
$_SERVER["REQUEST_METHOD"] = "POST";
$_POST['Name'] = 'Test User from Antigravity';
$_POST['Title'] = 'Automated Test';
$_POST['Email'] = 'test@example.com';
$_POST['Contact_number'] = '9876543210';
$_POST['Company'] = 'Sanciti AI Test';

echo "Running test...\n";
require 'submit_form.php';
echo "\nTest complete.\n";
?>
