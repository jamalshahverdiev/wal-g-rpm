%global _prefix /usr/local

Name:    wal-g
Version: 0.2.9
Release: 1
Summary: Archival and Restoration for Postgres

Group:   Development Tools
License: ASL 2.0
#URL: https://github.com/wal-g/wal-g/releases/download/v%{version}/wal-g.linux-amd64.tar.gz
Source0: https://codeload.github.com/wal-g/wal-g/tar.gz/v%{version}

%description
WAL-G is the successor of WAL-E with a number of key differences. WAL-G uses LZ4, LZMA or Brotli compression, multiple processors
and non-exclusive base backups for Postgres. More information on the design and implementation of WAL-G can be found on the
Citus Data blog post "Introducing WAL-G by Citus: Faster Disaster Recovery for Postgres".

%prep
%setup -c
ls %{_sourcedir}

%install
%{__install} -m 0755 -d %{buildroot}%{_bindir}
ls %{_sourcedir}/v%{version}
cp v%{version}/wal-g %{buildroot}%{_bindir}/%{name}

%files
%{_bindir}/%{name}
