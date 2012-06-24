
%define		snap		20030412

Summary:	An image viewer and browser for GNOME
Summary(pl):	Przegl�darka obrazk�w dla GNOME
Name:		gthumb
Version:	2.1.5
Release:	1
License:	GPL
Vendor:		GNOME
Group:		X11/Applications/Graphics
#Source0:	%{name}-%{version}-%{snap}.tar.bz2
Source0:	http://ftp.gnome.org/pub/gnome/sources/%{name}/2.1/%{name}-%{version}.tar.bz2
# Source0-md5:	f483bbbe8974719634e46794c3210704
URL:		http://gthumb.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	glib2-devel >= 2.2.0
BuildRequires:	gnome-vfs2-devel >= 2.2.0
BuildRequires:	gtk+2-devel >= 2.2.0
BuildRequires:	intltool
BuildRequires:	libbonoboui-devel >= 2.3.3-2
BuildRequires:	libglade2-devel >= 2.0.1
BuildRequires:	libgnomeprintui-devel >= 2.2.0
BuildRequires:	libgnomeui-devel >= 2.3.3.1-2
BuildRequires:	libpng-devel
BuildRequires:	libtool
BuildRequires:	libxml2-devel >= 2.4.0
Requires(post):	GConf2
Requires(post):	scrollkeeper
Requires:	libbonobo
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
gThumb lets you browse your hard disk, showing you thumbnails of image
files. It also lets you view single files (including GIF animations),
add comments to images, organize images in catalogs, print images,
view slideshows, set your desktop background, and more.

%description -l pl
gThumb pozwala na przegl�danie twardego dysku z pokazywaniem
miniaturek plik�w z obrazkami. Pozwala tak�e ogl�da� pojedyncze pliki
(w tym animacje GIF), dodawa� komentarze do obrazk�w, uk�ada� obrazki
w katalogi, drukowa� obrazki, ogl�da� slajdy, ustawia� t�o biurka itd.

%prep
%setup -q

%build
glib-gettextize --copy --force
intltoolize --copy --force
%{__libtoolize}
%{__aclocal} -I %{_aclocaldir}/gnome2-macros
%{__autoheader}
%{__automake}
%{__autoconf}
%configure \
	--disable-schemas-install
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm $RPM_BUILD_ROOT%{_libdir}/%{name}/modules/*.{a,la}
rm $RPM_BUILD_ROOT%{_libdir}/*.{a,la}

%find_lang %{name} --with-gnome --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%post
/usr/bin/scrollkeeper-update
%gconf_schema_install

%postun	-p /usr/bin/scrollkeeper-update

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/gthumb
%attr(755,root,root) %{_libdir}/libgthumb.so
%attr(755,root,root) %{_libdir}/gthumb-image-viewer
%attr(755,root,root) %{_libdir}/gthumb-catalog-view
%{_libdir}/%{name}
%{_libdir}/bonobo/servers/*.server
%{_datadir}/gnome-2.0/ui/*.xml
%{_datadir}/gthumb
%{_datadir}/application-registry/gthumb.applications
%{_mandir}/man1/gthumb.1*
%{_omf_dest_dir}/%{name}
%{_sysconfdir}/gconf/schemas/gthumb.schemas
%{_pixmapsdir}/gthumb.png
%{_desktopdir}/gthumb.desktop
