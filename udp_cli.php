<?php
function udp_send($send_msg = '', $ip = '127.0.0.1', $port = '8800'){
  $handle = stream_socket_client("udp://{$ip}:{$port}", $errno, $errstr);
  if( !$handle ){
    die("ERROR: {$errno} - {$errstr}\n");
  }
  fwrite($handle, $send_msg);
  $result = fread($handle, 1024);
  fclose($handle);
  return $result;
}
$result = udp_send('Hello World');
echo $result;