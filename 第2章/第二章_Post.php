<?php
setcookie('username','linda');
setcookie('password','123456');
$name = $_COOKIE['username']?$_COOKIE['username']:" ";
$password = $_COOKIE['password']?$_COOKIE['password']:" ";

?>
<!DOCTYPE>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<title>get_cookie</title>
</head>
<body>
	<?php
		echo $name."\n";
		echo $password;
	?>
</body>
</html>
