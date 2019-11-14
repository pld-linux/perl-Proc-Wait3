#
# Conditional build:
%bcond_without	tests		# do not perform "make test"

%define		pdir	Proc
%define		pnam	Wait3
%include	/usr/lib/rpm/macros.perl
Summary:	Proc::Wait3 - Perl extension for wait3 system call
Name:		perl-Proc-Wait3
Version:	0.05
Release:	1
License:	unknown
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Proc/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	41e6db9547b3f2c858d1982f6c278a1b
URL:		http://search.cpan.org/dist/Proc-Wait3/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
If any child processes have exited, this call will "reap" the zombies
similar to the perl "wait" function.

By default, it will return immediately and if there are no dead
children, everything will be undefined.  If you pass in a true
argument, it will block until a child exits (or it gets a signal).

 $pid         PID of exiting child

 $status      exit status of child, just like C<$?>

 $utime       floating point user cpu seconds

 $stime       floating point system cpu seconds

 $maxrss      the maximum resident set size utilized (in kilobytes).

 $minflt      the number of page faults serviced without any I/O
              activity; here I/O activity is avoided by "reclaiming" a
              page frame from the list of pages awaiting reallocation.

 $majflt      the number of page faults serviced that required I/O
              activity.

 $nswap       the number of times a process was "swapped" out of main
              memory.

 $inblock     the number of times the file system had to perform input.

 $oublock     the number of times the file system had to perform output.

 $msgsnd      the number of messages sent over sockets.

 $msgrcv      the number of messages received from sockets.

 $nsignals    the number of signals delivered.

 $nvcsw       the number of times a context switch resulted due to a
              process voluntarily giving up the processor before its
              time slice was completed (usually to await availability of
              a resource).

 $nivcsw      the number of times a context switch resulted due to a
              higher priority process becoming runnable or because the
              current process exceeded its time slice.



# %description -l pl.UTF-8
# TODO

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	CC="%{__cc}" \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorarch}/Proc/*.pm
%dir %{perl_vendorarch}/auto/Proc/Wait3
%attr(755,root,root) %{perl_vendorarch}/auto/Proc/Wait3/*.so
%{_mandir}/man3/*
