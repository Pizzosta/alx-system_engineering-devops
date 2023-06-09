# Fix problem with apache2 settings

exec {'replace':
  provider => shell,
  command  => 'sudo sed -i "s/class-wp-locale.phpp/class-wp-locale.php/g" /var/www/html/wp-settings.php',
  before   => Exec['restart'],
}

exec {'restart':
  provider => shell,
  command  => 'sudo service apache2 restart',
}
