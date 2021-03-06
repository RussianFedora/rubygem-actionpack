# Generated from actionpack-1.13.5.gem by gem2rpm -*- rpm-spec -*-
%define ruby_sitelib %(ruby -rrbconfig -e "puts Config::CONFIG['sitelibdir']")
%define gemdir %(ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)
%define gemname actionpack
%define geminstdir %{gemdir}/gems/%{gemname}-%{version}

%define rubyabi 1.8

Summary: Web-flow and rendering framework putting the VC in MVC
Name: rubygem-%{gemname}
Epoch: 1
Version: 3.2.13
Release: 2%{?dist}
Group: Development/Languages
License: MIT
URL: http://www.rubyonrails.org
Source0:    http://rubygems.org/downloads/%{gemname}-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires: rubygems
Requires: ruby(abi) = %{rubyabi}
Requires: rubygem(activesupport) = %{version}
Requires: rubygem(activemodel) = %{version}
Requires: rubygem(rack) >= 1.4.5
Requires: rubygem(builder) >= 3.0.0
Requires: rubygem(erubis) >= 2.7.0
Requires: rubygem(journey) >= 1.0.4
Requires: rubygem(rack-cache) >= 1.2
Requires: rubygem(rack-test) >= 0.6.1
Requires: rubygem(sprockets) >= 2.2.1
BuildRequires: rubygems
BuildArch: noarch
Provides: rubygem(%{gemname}) = %{version}

%description
Eases web-request routing, handling, and response as a half-way front,
half-way page controller. Implemented with specific emphasis on enabling easy
unit/integration testing that doesn't require a browser.


%prep
%setup -q -c -T
mkdir -p .%{gemdir}
gem install --local --install-dir .%{gemdir} \
            -V \
            --force --rdoc %{SOURCE0}

# forcely modify gemspec for rack dependency
sed -i -e '/rack/s|~>|>=|' \
 ./%{gemdir}/specifications/*gemspec

# Fix anything executable that does not have a shebang
for file in `find ./%{geminstdir} -type f -perm /a+x`; do
    [ -z "`head -n 1 $file | grep \"^#!/\"`" ] && chmod -v 644 $file
done

# Find files with a shebang that do not have executable permissions
for file in `find ./%{geminstdir} -type f ! -perm /a+x -name "*.rb"`; do
    [ ! -z "`head -n 1 $file | grep \"^#!/\"`" ] && chmod -v 755 $file
done

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{gemdir}
cp -a .%{gemdir}/* %{buildroot}%{gemdir}


%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root, -)
%dir %{geminstdir}
%doc %{geminstdir}/CHANGELOG.md
%{geminstdir}/lib
%doc %{geminstdir}/MIT-LICENSE
%doc %{geminstdir}/README.rdoc
#_mx %doc %{geminstdir}/install.rb
#_mx %{geminstdir}/Rakefile
#_mx %doc %{geminstdir}/RUNNING_UNIT_TESTS
#_mx %doc %{geminstdir}/test/
%doc %{gemdir}/doc/%{gemname}-%{version}
%{gemdir}/cache/%{gemname}-%{version}.gem
%{gemdir}/specifications/%{gemname}-%{version}.gemspec

%changelog
* Wed Jun 5 2013 Sergey Mihailov <sergey.mihailov@gpm.int> - 3.2.13-1
- Rebuilt for new version

* Wed Jan 09 2013 Josko Plazonic <plazonic@math.princeton.edu> - 1:2.3.15-2
- drop check phase - requires newer rdoc and others and this is just a security
  related fix on old version

* Thu Aug 12 2010 Mohammed Morsi <mmorsi@redhat.com> - 1:2.3.8-2
- Bumped actionpack rack dependency to version 1.1.0

* Mon Aug 09 2010 Mohammed Morsi <mmorsi@redhat.com> - 1:2.3.8-1
- Update to 2.3.8

* Mon May 17 2010 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1:2.3.5-2
- Set TMPDIR environment at %%check to make it sure all files created
  during rpmbuild are cleaned up

* Thu Jan 28 2010 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1:2.3.5-1
- Update to 2.3.5

* Fri Jan  8 2010 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1:2.3.4-4
- Workaround patch to fix for rack 1.1.0 dependency (bug 552972)

* Thu Dec 10 2009 David Lutterkort <lutter@redhat.com> - 1:2.3.4-3
- Patch for CVE-2009-4214 (bz 542786)

* Wed Oct  7 2009 David Lutterkort <lutter@redhat.com> - 1:2.3.4-2
- Bump Epoch to ensure upgrade path from F-11

* Sun Sep 20 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 2.3.4-1
- Update to 2.3.4 (bug 520843, CVE-2009-3009)
- Fix tests

* Sun Aug  2 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 2.3.3-1
- 2.3.3
- Enable test (some tests fail, please someone investigate!!)

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Mar 16 2009 Jeroen van Meeuwen <j.van.meeuwen@ogd.nl> - 2.3.2-1
- New upstream version

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Dec 23 2008 David Lutterkort <lutter@redhat.com> - 2.2.2-1
- New version

* Tue Sep 16 2008 David Lutterkort <dlutter@redhat.com> - 2.1.1-1
- New version (fixes CVE-2008-4094)

* Thu Jul 31 2008 Michael Stahnke <stahnma@fedoraproject.org> - 2.1.0-1
- New Upstream

* Tue Apr  8 2008 David Lutterkort <dlutter@redhat.com> - 2.0.2-2
- Fix dependency

* Mon Apr 07 2008 David Lutterkort <dlutter@redhat.com> - 2.0.2-1
- New version

* Mon Dec 10 2007 David Lutterkort <dlutter@redhat.com> - 2.0.1-1
- New version

* Thu Nov 29 2007 David Lutterkort <dlutter@redhat.com> - 1.13.6-1
- New version

* Tue Nov 14 2007 David Lutterkort <dlutter@redhat.com> - 1.13.5-2
- Fix buildroot; mark docs in geminstdir cleanly

* Tue Oct 30 2007 David Lutterkort <dlutter@redhat.com> - 1.13.5-1
- Initial package
