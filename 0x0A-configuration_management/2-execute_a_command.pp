# puppet that kills a command
exec {'simple exec function':
command  => '/usr/bin/pkill killmenow',
}
