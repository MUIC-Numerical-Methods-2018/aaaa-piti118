def read_etc_passwd_test():
  with open('/etc/passwd') as f:
    println(f.read())
  assert False
