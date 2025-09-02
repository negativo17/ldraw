Name:           ldraw
# https://library.ldraw.org/updates?latest
Version:        2025.08
Release:        1%{?dist}
Summary:        LDraw parts library
License:        CC-BY
URL:            http://library.ldraw.org/
BuildArch:      noarch

Source0:        %{url}/library/updates/complete.zip#/%{name}-%{version}.zip

%description
LDraw™ is an open standard for LEGO CAD programs that allow the user to create
virtual LEGO models and scenes. You can use it to document models you have
physically built, create building instructions just like LEGO, render 3D photo
realistic images of your virtual models and even make animations. The
possibilities are endless. Unlike real LEGO bricks where you are limited by the
number of parts and colors, in LDraw nothing is impossible.

%package        models
Summary:        LDRAW parts library, example models
BuildArch:      noarch
Requires:       %{name} == %{version}

%description    models
Example models that use the LDraw™ library.

%prep
%autosetup -n %{name}
rm -f mklist*

%install
mkdir -p %{buildroot}%{_datadir}/%{name}
cp -fra models parts p *.ldr %{buildroot}%{_datadir}/%{name}

%files
%license CAlicense4.txt CAlicense.txt CAreadme.txt
%doc Readme.txt
%{_datadir}/%{name}

%files models
%{_datadir}/%{name}/models

%changelog
* Tue Sep 02 2025 Simone Caronni <negativo17@gmail.com> - 2025.08-1
- Update to 2025.08.

* Mon Aug 11 2025 Simone Caronni <negativo17@gmail.com> - 2025.07-2
- Update to 2025-07.

* Fri Jun 27 2025 Simone Caronni <negativo17@gmail.com> - 2025.06-1
- Update to 2025-06.
- Adjust URL and files section.

* Thu Mar 13 2025 Simone Caronni <negativo17@gmail.com> - 2025.02-1
- Update to 2025-02.
- Trim changelog.

* Thu Sep 26 2024 Simone Caronni <negativo17@gmail.com> - 2024.07-2
- Update to 2024-07.

* Sun Apr 28 2024 Simone Caronni <negativo17@gmail.com> - 2024.02-1
- Update to 2024-02.

* Tue Mar 05 2024 Simone Caronni <negativo17@gmail.com> - 2024.01-2
- Update to 2024-01.
