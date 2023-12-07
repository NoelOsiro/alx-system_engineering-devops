# Puppet manifest to configure custom HTTP header in Nginx

# Install Nginx
class { 'nginx':
  ensure => 'installed',
}

# Create directories and files
file { '/etc/nginx/html':
  ensure => 'directory',
}

file { '/etc/nginx/html/index.html':
  content => 'Best School',
}

file { '/etc/nginx/html/404.html':
  content => "Ceci n'est pas une page",
}

# Configure Nginx
file { '/etc/nginx/sites-available/default':
  content => "server {
    listen 80;
    listen [::]:80 default_server;
    root   /etc/nginx/html;
    index  index.html index.htm;

    location /redirect_me {
        return 301 http://cuberule.com/;
    }

    error_page 404 /404.html;
    location /404 {
        root /etc/nginx/html;
        internal;
    }

    add_header X-Served-By $hostname;
  }",
}

# Create a symbolic link to enable the site
file { '/etc/nginx/sites-enabled/default':
  ensure => 'link',
  target => '/etc/nginx/sites-available/default',
}

# Restart Nginx to apply changes
service { 'nginx':
  ensure    => 'running',
  enable    => true,
  subscribe => File['/etc/nginx/sites-available/default'],
}
