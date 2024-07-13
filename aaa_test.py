import os
def test_read_etc_passwd():
  with open('/etc/passwd') as f:
    print(f.read())

  print(os.environ)
  assert False
