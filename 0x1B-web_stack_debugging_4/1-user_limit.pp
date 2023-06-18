# manifest to be able to login with the holberton user and open a file without any error message.
exec {'change-os-configuration-for-holberton-user':
  provider => shell,
  command  => 'sudo sed -i "s/nofile 5/nofile 50000/" /etc/security/limits.conf',
  before   => Exec['replace-configuration-for-holberton-user'],
}

exec {'replace-configuration-for-holberton-user':
  provider => shell,
  command  => 'sudo sed -i "s/nofile 4/nofile 40000/" /etc/security/limits.conf',
}
