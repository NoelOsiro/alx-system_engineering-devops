# Filename: kill_process.pp

exec { 'killmenow_process':
  command     => '/usr/bin/pkill killmenow',
  path        => '/usr/bin',
  refreshonly => true,
  onlyif      => '/usr/bin/pgrep killmenow',
}
