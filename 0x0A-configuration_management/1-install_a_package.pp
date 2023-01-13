# Download puppet-lint 2.1.1

exec { 'apt-get update':
  command => '/usr/bin/apt-get update'
}

package { 'pip3':
  ensure  => 'installed',
  require => Exec['apt-get update']
}

package { 'Flask':
  ensure   => '2.1.0',
  require  => Package['pip3'],
  provider => 'gem'
}
