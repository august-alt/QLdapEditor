%define _unpackaged_files_terminate_build 1
%set_verify_elf_method unresolved=relaxed

Name: qldapeditor
Version: 0.1.0
Release: alt1

Summary: LDAP editor
License: GPLv2+
Group: Other
Url: https://github.com/august-alt/QLdapEditor

BuildRequires: cmake
BuildRequires: rpm-macros-cmake
BuildRequires: cmake-modules
BuildRequires: gcc-c++
BuildRequires: qt5-base-devel
BuildRequires: qt5-declarative-devel
BuildRequires: qt5-tools-devel
BuildRequires: libsmbclient-devel libsmbclient
BuildRequires: libsasl2-devel openldap-devel openssl-devel

BuildRequires: qt5-base-common

Source0: %name-%version.tar

%description
LDAP Editor based on Qt and ldapc++ wrapper

%prep
%setup -q

%build
%cmake
%cmake_build

%install
%cmakeinstall_std

%files
%doc README.md
%_bindir/*

%_libdir/*

%_desktopdir/LdapEditorApp.desktop
%_datadir/icons/LdapEditorApp.png

%changelog
* Tue Jan 10 2022 Vladimir Rubanov <august@altlinux.org> 0.1.0-alt1
- Initial build
