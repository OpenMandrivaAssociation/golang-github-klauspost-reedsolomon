# https://github.com/klauspost/reedsolomon
%global goipath github.com/klauspost/reedsolomon
%global commit  925cb01d65108f2c935e02fdb79ff4a055a4a20d
%global date    20180704

%gometa

Name:           %{goname}
Version:        1.6
Release:        6%{?dist}
Summary:        Reed-Solomon Erasure Coding in Go
License:        MIT

URL:            %{gourl}
Source0:        %{gosource}


%description
%{summary}


%package        devel
Summary:        %{summary}

BuildRequires:  golang(github.com/klauspost/cpuid)

%description    devel
%{summary}

This package contains library source intended for
building other packages which use import path with
%{goipath} prefix.


%prep
%gosetup -q


%install
%goinstall


%check
%gochecks


%files devel -f devel.file-list
%license LICENSE
%doc README.md


%changelog
* Sun Sep 02 2018 Fabio Valentini <decathorpe@gmail.com> - 1.6-6.20180704git925cb01
- Bump to commit 925cb01.
- Update to use spec 3.0.

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-5.20171219.git0b30fa7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-4.20171219.git0b30fa7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 09 2018 Fabio Valentini <decathorpe@gmail.com> - 1.6-3.20171219.git0b30fa7
- Bump to commit 0b30fa7.

* Sat Dec 09 2017 Fabio Valentini <decathorpe@gmail.com> - 1.6-2.20171118.gite52c150
- Bump to commit e52c150.

* Tue Oct 03 2017 Fabio Valentini <decathorpe@gmail.com> - 1.6-1
- Update to version 1.6.

* Sat Aug 26 2017 Fabio Valentini <decathorpe@gmail.com> - 1.5-1
- Update to version 1.5.

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jul 16 2017 Fabio Valentini <decathorpe@gmail.com> - 1.4-1
- Update to version 1.4.

* Tue Mar 21 2017 Fabio Valentini <decathorpe@gmail.com> - 1.3-1
- First package for Fedora

