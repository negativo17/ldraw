Name:           ldraw
Version:        2019.03
Release:        1%{?dist}
Summary:        LDraw parts library
License:        CC-BY
URL:            http://www.ldraw.org/
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

%build
# Nothing to build

%install
mkdir -p %{buildroot}%{_datadir}/%{name}
cp -fra models parts p %{buildroot}%{_datadir}/%{name}

%files
%license CAlicense.txt CAreadme.txt
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/parts
%{_datadir}/%{name}/p

%files models
%{_datadir}/%{name}/models

%changelog
* Thu Jan 23 2020 Simone Caronni <negativo17@gmail.com> - 2019.03-1
- First build.
