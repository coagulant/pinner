Initial setup:

  $ [ -n "$PYTHON" ] || PYTHON="`which python`"
  $ export PYTHONPATH=$TMPDIR
  $ cd ${TESTDIR}/../../
  $ $PYTHON setup.py develop --install-dir=$TMPDIR > /dev/null 2>&1
  $ alias pinner="$TMPDIR/pinner"

Pinner founds 4 problems with dependencies:

  $ cd $TESTDIR/../../test_project
  $ pinner
  ./requirements.txt:1:1: R001 Dependency PIL not pinned
  ./requirements.txt:2:1: R002 Dependency coveralls should be pinned to exact version
  ./requirements.txt:6:1: R004 VCS dependency django_assets specifies branch/tag, commit expected
  ./requirements.txt:8:1: R003 VCS dependency django_recommends lacks revision specifier
  [4]
