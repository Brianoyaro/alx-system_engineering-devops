# puppet for creating a file
file { '/tmp/school':
  content => 'I love Puppet',
  owner   => 'www-data',
  group   => 'www-data',
  mode    => '0744'
}
