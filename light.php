<head>
</head>
<body>
<form action="light.php" method="post">
Choose Color:<br>
<input type="color" name="color">
<br>
Brightness:
<br>
<input type="text" name="bright" value="255">
<br>
<input type="submit" value="submit">
</form>
</body>


<?php

if ($_POST['color']) {
$color = hex2rgb($_POST['color']);
$bright = $_POST['bright'];
$out = $bright . ',' . $color[0] . ',' . $color[1] . ',' . $color[2] . ',255,0';

$fp = fsockopen('192.168.50.82','9999');
fwrite($fp, $out);
}

function hex2rgb($hex) {
   $hex = str_replace("#", "", $hex);

   if(strlen($hex) == 3) {
      $r = hexdec(substr($hex,0,1).substr($hex,0,1));
      $g = hexdec(substr($hex,1,1).substr($hex,1,1));
      $b = hexdec(substr($hex,2,1).substr($hex,2,1));
   } else {
      $r = hexdec(substr($hex,0,2));
      $g = hexdec(substr($hex,2,2));
      $b = hexdec(substr($hex,4,2));
   }
   $rgb = array($r, $g, $b);
   //return implode(",", $rgb); // returns the rgb values separated by commas
   return $rgb; // returns an array with the rgb values
}