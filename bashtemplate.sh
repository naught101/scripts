#!/bin/bash

# Check args
# $# = num args, $0 = program name
if [[ $1 !~ ".*/nh???" || $# != 2 ]] then
  echo "Usage: $0 rundir outdir"
  exit 65
fi

# For loop
for i in $( ls ); do
  echo item: $i
done

# While loop
COUNTER=0
while [  $COUNTER -lt 10 ]; do
  echo The counter is $COUNTER
  let COUNTER=COUNTER+1 
done

# If else
if [ "$T1" = "$T2" ]; then
  echo expression evaluated as true
else
  echo expression evaluated as false
fi

# Arrays use Zero based indexing
# Another way of assigning array variables...
array_name=( XXX YYY ZZZ )
# $array[2]=="ZZZ". Assign:
$array[3]=="000"
 
# Function definition
function quit {
  exit
}
