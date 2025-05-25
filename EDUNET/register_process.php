<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Retrieve user input
    $username = $_POST["username"];
    $email = $_POST["email"];
    $password = $_POST["password"];

    // Validate email format
    if (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
        // Redirect back to the registration page with an error message
        header("Location: register.html?error=invalid_email");
        exit();
    }

    // Process registration - in a real application, this is where you would add the user to a database and send a verification email
    // For now, let's just display a success message
    echo "Registration successful!";

    // You can redirect to a success page if needed
    // header("Location: registration_success.html");
    // exit();
} else {
    // If the request method is not POST, redirect to the registration page
    header("Location: register.html");
    exit();
}
?>
