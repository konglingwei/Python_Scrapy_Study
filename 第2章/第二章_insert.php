<?php
session_start();
$_SESSION['Username']="admin";
?>
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<title>Document</title>
</head>
<body>
	<form action="denglu.php" method="post">
		用户名: <input type="text" name="Username" >
		<br>
		密码：<input type="text" name="Password" >
		<br>
		<input type="submit" name="submit" value="Submit">
	</form>
</body>
</html>