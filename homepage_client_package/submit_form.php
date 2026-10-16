<?php
// submit_form.php

// Define the path to PHPMailer classes
require 'assets/PHPMailer/PHPMailer-master/src/Exception.php';
require 'assets/PHPMailer/PHPMailer-master/src/PHPMailer.php';
require 'assets/PHPMailer/PHPMailer-master/src/SMTP.php';

use PHPMailer\PHPMailer\PHPMailer;
use PHPMailer\PHPMailer\Exception;

header('Content-Type: application/json');

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Get form data
    $name = isset($_POST['Name']) ? htmlspecialchars(trim($_POST['Name'])) : (isset($_POST['name']) ? htmlspecialchars(trim($_POST['name'])) : '');
    $title = isset($_POST['Title']) ? htmlspecialchars(trim($_POST['Title'])) : (isset($_POST['title']) ? htmlspecialchars(trim($_POST['title'])) : '');
    $email = isset($_POST['Email']) ? htmlspecialchars(trim($_POST['Email'])) : (isset($_POST['email']) ? htmlspecialchars(trim($_POST['email'])) : '');
    $contact = isset($_POST['Contact_number']) ? htmlspecialchars(trim($_POST['Contact_number'])) : (isset($_POST['Contact number']) ? htmlspecialchars(trim($_POST['Contact number'])) : (isset($_POST['phone']) ? htmlspecialchars(trim($_POST['phone'])) : ''));
    $company = isset($_POST['Company']) ? htmlspecialchars(trim($_POST['Company'])) : (isset($_POST['company']) ? htmlspecialchars(trim($_POST['company'])) : '');

    if(empty($name) || empty($email)) {
        echo json_encode(["success" => false, "message" => "Name and Email are required."]);
        exit;
    }

    // List of personal/consumer and temporary email domains
    $personalDomains = [
        'gmail.com', 'googlemail.com',
        'yahoo.com', 'yahoo.co.in', 'yahoo.co.uk', 'yahoo.ca', 'yahoo.fr', 'yahoo.de', 'yahoo.it', 'yahoo.es', 'yahoo.com.br', 'yahoo.co.jp', 'ymail.com', 'rocketmail.com',
        'hotmail.com', 'outlook.com', 'live.com', 'msn.com', 'passport.com', 'hotmail.co.uk', 'hotmail.fr', 'hotmail.de', 'hotmail.it', 'hotmail.es',
        'outlook.co.uk', 'outlook.fr', 'outlook.de', 'outlook.in', 'live.co.uk',
        'icloud.com', 'me.com', 'mac.com',
        'aol.com', 'aim.com',
        'protonmail.com', 'proton.me', 'pm.me',
        'zoho.com', 'zohomail.com',
        'mail.com', 'email.com', 'usa.com', 'post.com',
        'gmx.com', 'gmx.net', 'gmx.de', 'gmx.at', 'gmx.ch',
        'yandex.com', 'yandex.ru', 'ya.ru',
        'tutanota.com', 'tuta.io', 'tuta.com',
        'fastmail.com', 'fastmail.fm',
        'rediffmail.com',
        'inbox.com', 'qq.com', '163.com', '126.com', 'sina.com',
        'sbcglobal.net', 'att.net', 'verizon.net', 'comcast.net', 'cox.net', 'charter.net', 'bellsouth.net', 'earthlink.net', 'juno.com',
        'tempmail.com', 'guerrillamail.com', '10minutemail.com', 'mailinator.com', 'throwawaymail.com', 'trashmail.com', 'yopmail.com'
    ];

    $source = isset($_POST['source']) ? trim($_POST['source']) : '';

    // Enforce corporate email validation across all form submissions
    $emailDomain = strtolower(substr(strrchr($email, "@"), 1));
    $isPersonal = false;
    foreach ($personalDomains as $pDomain) {
        if ($emailDomain === $pDomain || substr($emailDomain, -strlen('.' . $pDomain)) === '.' . $pDomain) {
            $isPersonal = true;
            break;
        }
    }

    if ($isPersonal || empty($emailDomain) || strpos($emailDomain, '.') === false) {
        echo json_encode([
            "success" => false,
            "message" => "✕ Must be Business email."
        ]);
        exit;
    }

    $mail = new PHPMailer(true);

    try {
        // =====================================================================
        // SMTP CONFIGURATION - YOU NEED TO EDIT THIS SECTION
        // =====================================================================
        // Enable verbose debug output (set to 0 for production)
        $mail->SMTPDebug = 0; 
        
        // Send using SMTP
        $mail->isSMTP(); 
        
        // Set the SMTP server to send through (e.g., smtp.gmail.com)
        $mail->Host       = 'smtp.gmail.com'; 
        
        // Enable SMTP authentication
        $mail->SMTPAuth   = true; 
        
        // SMTP username (your email address)
        $mail->Username   = 'raveendrapm.cse@gmail.com'; 
        
        // SMTP password (for Gmail, use an App Password, NOT your regular password)
        $mail->Password   = 'wjcgykcvitkgfysg'; 
        
        // Enable TLS encryption; `PHPMailer::ENCRYPTION_SMTPS` encouraged
        $mail->SMTPSecure = PHPMailer::ENCRYPTION_STARTTLS; 
        
        // TCP port to connect to, use 465 for `PHPMailer::ENCRYPTION_SMTPS` above
        $mail->Port       = 587; 
        // =====================================================================

        // Recipients
        $mail->setFrom('raveendrapm.cse@gmail.com', 'Sanciti AI Website Form');
        $mail->addAddress('info@sanciti.ai', 'Sanciti AI Info'); // Add a recipient (destination)

        // Content
        $mail->isHTML(true);
        $mail->Subject = 'New Free Assessment Request - ' . $name;
        
        $emailBody = "<h2>New Assessment Request</h2>";
        $emailBody .= "<p><strong>Name:</strong> {$name}</p>";
        $emailBody .= "<p><strong>Title:</strong> {$title}</p>";
        $emailBody .= "<p><strong>Email:</strong> {$email}</p>";
        $emailBody .= "<p><strong>Contact Number:</strong> {$contact}</p>";
        $emailBody .= "<p><strong>Company:</strong> {$company}</p>";

        $mail->Body    = $emailBody;
        $mail->AltBody = strip_tags(str_replace(['<p>', '</p>'], ["\n", "\n"], $emailBody));

        $mail->send();
        echo json_encode(["success" => true, "message" => "Email sent successfully"]);
    } catch (Exception $e) {
        echo json_encode(["success" => false, "message" => "Message could not be sent. Mailer Error: {$mail->ErrorInfo}"]);
    }
} else {
    echo json_encode(["success" => false, "message" => "Invalid request method."]);
}
?>