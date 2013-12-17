#!/bin/sh

# Absolute path to this script, e.g. /home/user/bin/foo.sh
SCRIPT=$(readlink -f "$0")
# Absolute path this script is in, thus /home/user/bin
SCRIPTPATH=$(dirname "$SCRIPT")
echo $SCRIPTPATH
export PYTHONPATH=$PYTHONPATH:$SCRIPTPATH
echo ''
test_files=$(eval 'ls $SCRIPTPATH/test/*py');
test_cmd='python -3 '
for file in $test_files; do
    echo $test_cmd $file
    eval '$test_cmd $file'
    echo ''
done
echo ''
