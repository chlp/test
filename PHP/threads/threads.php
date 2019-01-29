<?php

if (!file_put_contents(__DIR__ . "/out", "It is correct?\r\n")) {
    echo "can not create file " . __DIR__ . "/out";
    exit;
}

const ITERATIONS = 5;
for ($i = 1; $i <= ITERATIONS; ++$i) {
    echo "$i of " . ITERATIONS . "\r\n";
    exec("php " . __DIR__ . "/thread.php $i &");
}

echo "end threads.php\r\n";