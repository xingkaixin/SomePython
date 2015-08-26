import pysftp

host = 'pinpin.in'
username = 'root'


srv = pysftp.Connection(host=host, username=username)


srv.cwd('tmp')
print srv.listdir()
print srv.listdir_attr()
print srv.stat('.')
print srv.pwd
print srv.exists('test.cfg')


srv.close()
