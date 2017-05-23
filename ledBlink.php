<!DOCTYPE html>
<html>
<?php
if (!empty($_GET["count"])) {
  $output = shell_exec("sudo python /var/www/html/webBlinkLED.py ".strtolower($_GET["count"])) ;
  echo "No of times to blink LED : ". strtoupper($_GET["count"]);
}
?>
<form action="<?php echo $_SERVER['PHP_SELF'];?>" method="get">
# times to blink LED 
<input type="text" name="count"/>
<br/>
<input type="submit"/>
</form>
</html>
