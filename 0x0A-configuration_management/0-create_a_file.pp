# Create a file in/tmp
file {'/tmp/school':
mode     => '0744',
owner    => 'www-data',
group    => 'www-dat',
contents => 'I love Puppet',
}
