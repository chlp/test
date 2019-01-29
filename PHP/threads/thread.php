<?php

function worker()
{
    global $argv;
    if (!isset($argv[1])) {
        exit;
    }
    $i = (int)$argv[1];
    file_put_contents(__DIR__ . '/out', "$i+1=", FILE_APPEND);
    try {
        sleep(random_int(0, 2));
    } catch (Exception $e) {
    }
    ++$i;
    file_put_contents(__DIR__ . '/out', "$i\r\n", FILE_APPEND);
}

worker();