# nginx_config.pp
# Install Nginx package
package { 'nginx':
  ensure => installed,
}

# Define Nginx service
service { 'nginx':
  ensure    => running,
  enable    => true,
  hasstatus => true,
  hasrestart => true,
}

# Configure Nginx site with root page
file { '/var/www/html/index.html':
  ensure  => present,
  content => 'Hello World!',
}

# Create a Puppet template for the Nginx default site configuration
file { '/etc/puppetlabs/code/environments/production/modules/nginx_config/templates/default.erb':
  ensure => present,
  content => '# This file is managed by Puppet
server {
    listen 80 default_server;
    listen [::]:80 default_server;

    root /var/www/html;
    index index.html;

    location / {
        try_files $uri $uri/ =404;
    }

    location /redirect_me {
        return 301 http://example.com/;
    }
}
',
}

# Create a symbolic link to enable the site
file { '/etc/nginx/sites-enabled/default':
  ensure => link,
  target => '/etc/nginx/sites-available/default',
  notify => Service['nginx'],
}

# End of manifest
