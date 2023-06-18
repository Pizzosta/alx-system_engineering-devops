# manifest to accept a high number of request
exec {'replace':
  provider => shell,
  command  => "sudo sed -i 's/ULIMIT=\"-n 15\"/ULIMIT=\"-n 5000\"/' /etc/default/nginx",
  before   => Exec['restart'],
}

exec {'restart':
  provider => shell,
  command  => 'sudo service nginx restart',
}
