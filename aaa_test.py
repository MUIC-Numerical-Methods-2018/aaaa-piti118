def test_read_etc_passwd():
  with open('/etc/passwd') as f:
    println(f.read())

  println(os.environ)
  assert False
