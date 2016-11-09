# Disable the stupid stuff rpm distros include in the build process by default:
#   Disable any prep shell actions. replace them with simply 'true'
%define __spec_prep_post true
%define __spec_prep_pre true
#   Disable any build shell actions. replace them with simply 'true'
%define __spec_build_post true
%define __spec_build_pre true
#   Disable any install shell actions. replace them with simply 'true'
%define __spec_install_post true
%define __spec_install_pre true
#   Disable any clean shell actions. replace them with simply 'true'
%define __spec_clean_post true
%define __spec_clean_pre true
# Disable checking for unpackaged files ?
#%undefine __check_files

# Use md5 file digest method.
# The first macro is the one used in RPM v4.9.1.1
%define _binary_filedigest_algorithm 1
# This is the macro I find on OSX when Homebrew provides rpmbuild (rpm v5.4.14)
%define _build_binary_file_digest_algo 1

# Use bzip2 payload compression
%define _binary_payload w9.bzdio

# Enable bash specific commands (eg. pushd)
%define _buildshell /bin/bash

#
# The Preamble
#
Name: palette-supervisor
Version: %{version}
Release: %{buildrelease}
Summary: Palette Supervisor
Group: Productivity/Other
License: commercial
Vendor: Palette Software
URL: http://www.palette-software.com
Packager: Palette Developers <developers@palette-software.com>
BuildArch: noarch
# Disable Automatic Dependency Processing
AutoReqProv: no
# Add prefix, must not end with / except for root (/)
Prefix: /
# Seems specifying BuildRoot is required on older rpmbuild (like on CentOS 5)
# fpm passes '--define buildroot ...' on the commandline, so just reuse that.
# BuildRoot: %buildroot

Requires: initscripts
Requires: python python-pip

# Make sure the supervisor is not installed
Conflicts: supervisor
Provides: supervisor

%description
This package contains a newer version of Supervisor for Centos6

%install
mkdir -p %{buildroot}/etc/supervisord.d
mkdir -p %{buildroot}/var/run/supervisor
mkdir -p %{buildroot}/var/log/supervisor

%clean
# noop

%post

# Install latest Supervisor via PIP
pip install meld3==1.0.1
pip install supervisor==%{version}

chkconfig --add supervisord
service supervisord start

%files
%defattr(-,root,root,-)

%attr(755, -, -) /etc/init.d/supervisord
/etc/supervisord.conf
%dir /etc/supervisord.d
%dir /var/run/supervisor
%dir /var/log/supervisor

%changelog
