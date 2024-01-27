# Install an especific version of flask (2.1.0)

package { 'python3-pip':
  ensure => installed,
}

package { 'Flask':
  ensure   => '2.1.0',
  provider => 'pip3',
}

package { 'Werkzeug':
  ensure   => '2.1.1',  # Update this version to the one compatible with Flask 2.1.0
  provider => 'pip3',
}
