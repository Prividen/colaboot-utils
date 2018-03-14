Name: colaboot-utils
Version: 0.5
Release: alt1

Summary: Utils that helps to prepare CoLaBoot images
License: GPL
Group: System/Base
Packager: Michael A. Kangin <prividen@altlinux.org>

Source0: %name-%version.tar

Requires: squashfs-tools docker-io

BuildArch: noarch

%description
CoLaBoot (Compressed Layers Boot) allow to boot host with a separate
compressed (squashfs) layers, mounted as overlayfs.
There are scripts in this package that help to convert docker container
or image into squashfs image, and prepare squashfs/cpio image with
kernel modules.

%prep
%setup

%install
mkdir -p %buildroot%_bindir/
install -m 755 modlist2image docker2squash %buildroot%_bindir/

%files 
%_bindir/*
%doc docs/*

%changelog
* Tue Mar 13 2018 Michael A. Kangin <prividen@altlinux.org> 0.5-alt1
- Initial build

