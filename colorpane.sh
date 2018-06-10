#!/usr/bin/env bash
#
# display colorscheme

f=3
b=4

for i in f b; do
    for j in {0..7}; do
        printf -v "$i$j" "%b" "\e[${!i}${j}m"
    done
done

b=$'\e[1m'

# output
cat << EOF

$f1██  $f2██  $f3██  $f4██  $f5██  $f6██  $f7██  $f8
$b$f1██  $f2██  $f3██  $f4██  $f5██  $f6██  $f7██  $f8
0   1   2   3   4   5   6   

EOF
