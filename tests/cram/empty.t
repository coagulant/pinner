Initial setup:

  $ [ -n "$PYTHON" ] || PYTHON="`which python`"
  $ export PYTHONPATH=$TMPDIR
  $ cd ${TESTDIR}/../../
  $ $PYTHON setup.py develop --install-dir=$TMPDIR > /dev/null 2>&1
  $ alias pinner="$TMPDIR/pinner"

Pinner didn't find any requirements files and exits with code 1:

  $ cd $TESTDIR/../../
  $ pinner
  No requirements files found in path: .
  [1]
