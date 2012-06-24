Summary:	KDE DVD Authoring Wizard
Summary(pl.UTF-8):	Narzędzie KDE do przygotowywania DVD
Name:		DVDAuthorWizard
Version:	1.4.6
Release:	0.1
License:	GPL
Group:		X11/Applications/Multimedia
Source0:	http://dl.sourceforge.net/dvdauthorwizard/%{name}-%{version}.tar.bz2
# Source0-md5:	2998a159c515c6dd67b4da7af2810e52
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
This wizard will allow you to create a DVD from one or more DVD
compatible MPEG-2 files. It is designed to be very easy to use. All
you need to do is add one or multiple files to the playlist and answer
the questions that follow.

%description -l pl.UTF-8
To narzędzie pozwala utworzyć DVD z jednego lub większej liczby plików
MPEG-2 kompatybilnych z DVD. Zostało zaprojektowane z myślą o bardzo
łatwym użyciu. Wszystko co trzeba zrobić to dodać jeden lub więcej
plików do playlisty i odpowiadać na kolejne pytania.

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_prefix}
install -d $RPM_BUILD_ROOT%{_desktopdir}/kde
cp -r bin share $RPM_BUILD_ROOT%{_prefix}

cat > $RPM_BUILD_ROOT%{_desktopdir}/kde/KDVDAuthoringWizard.desktop << EOF
[Desktop Entry]
Encoding
Name=KDE DVDAuthor Wizard
Name[pl]=Narzędzie KDE do tworzenia DVD
GenericName=DVD Authoring Application
GenericName[pl]=Aplikacja do tworzenia DVD
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
