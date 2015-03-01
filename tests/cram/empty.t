Initial setup:

  $ [ -n "$PYTHON" ] || PYTHON="`which python`"
  $ export PYTHONPATH=$TMPDIR
  $ cd ${TESTDIR}/../../
  $ $PYTHON setup.py develop --install-dir=$TMPDIR > /dev/null 2>&1

Test normal behavior without write:

  $ cd $TESTDIR/../../
  $ pinner
  No requirements files found in path: .
  [1]
