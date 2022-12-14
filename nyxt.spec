%global         debug_package %{nil}
%global         __strip       /bin/true

Name:           nyxt
Version:        2.2.4
Release:        1%{?dist}
Summary:        Keyboard-oriented, infinitely extensible web browser

%global quicklisp_commit b525ae5

# The additional --eval flag is needed to avoid an error with UTF-8
# characters in /etc/mime.types
%global lisp_flags "--no-userinit --non-interactive --eval '(setf sb-impl::*default-external-format* :UTF8)'"

License:        BSD
URL:            https://nyxt.atlas.engineer/
Source0:        https://github.com/atlas-engineer/%{name}/archive/refs/tags/%{version}.tar.gz
Source1:        https://github.com/quicklisp/quicklisp-client/tarball/%{quicklisp_commit}

BuildRequires:  gcc-c++ git make sbcl
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  libfixposix-devel
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(webkit2gtk-4.0)

Requires:       pkgconfig(gobject-introspection-1.0)
Requires:       pkgconfig(webkit2gtk-4.0)
Requires:       libfixposix-devel

%description
Nyxt is a keyboard-oriented, infinitely extensible web browser designed for
power users. Conceptually inspired by Emacs and Vim, it has familiar
key-bindings (Emacs, vi, CUA), and is fully configurable in Lisp.

%prep
%autosetup
echo $PWD
tar xvz -C _build/quicklisp-client --strip-components=1 -f %{SOURCE1}

%build
make PREFIX=/usr LISP_FLAGS=%{lisp_flags} all

%install
make PREFIX=/usr DESTDIR=$RPM_BUILD_ROOT LISP_FLAGS=%{lisp_flags} install

%files
/usr/bin/nyxt
/usr/share/applications/nyxt.desktop
/usr/share/icons/hicolor/*/apps/nyxt.png


%changelog
* Thu Sep 23 2021 teervo <teervo_at_protonmail.com>
- version bump
* Wed Sep 14 2021 teervo <teervo_at_protonmail.com>
- version bump
* Sun Jun 13 2021 teervo <teervo_at_protonmail.com>
- initial release

