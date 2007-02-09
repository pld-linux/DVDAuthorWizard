Summary:	KDE DVD Authoring Wizard
Name:		DVDAuthorWizard
Version:	1.4.3
Release:	0.1
License:	GPL
Group:		X11/Applications/Multimedia
Source0:	http://dl.sourceforge.net/dvdauthorwizard/%{name}-%{version}.tar.bz2
# Source0-md5:	4d7c4920a46fb448c787c38c728e7c8b
URL:		http://dvdauthorwizard.sourceforge.net/
Requires:	ImageMagick >= 6.2
Requires:	dvdauthor >= 0.6.11
Requires:	kdewebdev-kommander
Requires:	mjpegtools
Requires:	sox
Requires:	transcode
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This wizard will allow you to create a DVD from one or more DVD compatible 
MPEG-2 files. It is designed to be very easy to use. All you need to do is 
add one or multiple files to the playlist and answer the questions that 
follow.

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_prefix}
install -d $RPM_BUILD_ROOT%{_desktopdir}/kde
cp -r bin share $RPM_BUILD_ROOT%{_prefix}

cat > $RPM_BUILD_ROOT%{_desktopdir}/kde/KDVDAuthoringWizard.desktop << EOF
[Desktop Entry]
Name=KDE DVDAuthor Wizard
GenericName=DVD Authoring Application
Exec=kmdr-executor '%{_prefix}/bin/DVDAuthorWizard.kmdr'
Type=Application
icon=dvd_unmount
Categories=Qt;KDE;AudioVideo;
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changelog README *.txt
%attr(755,root,root) %{_bindir}/*.sh
%{_bindir}/*.kmdr
%{_desktopdir}/kde/*.desktop
%dir %{_datadir}/apps/dvdauthorwizard
%dir %{_datadir}/apps/dvdauthorwizard/Pictures
%{_datadir}/apps/dvdauthorwizard/Pictures/*.png
