%global packname  fields
%global rlibdir  %{_libdir}/R/library

Name:             R-%{packname}
Version:          6.7
Release:          2
Summary:          Tools for spatial data
Group:            Sciences/Mathematics
License:          GPL (>= 2)
URL:              https://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/fields_6.7.tar.gz
Requires:         R-methods R-spam 
BuildRequires:    R-devel Rmath-devel texlive-collection-latex R-methods R-spam

%description
Fields is for curve, surface and function fitting with an emphasis on
splines, spatial data and spatial statistics. The major methods include
cubic, robust, and thin plate splines, and Kriging for large data sets.
The splines and Kriging methods are supporting by functions that can
determine the smoothing parameter (nugget and sill variance) by cross
validation and also by restricted maximum likelihood.  A major feature is
that any covariance function implemented in R with the fields interface
can be used for spatial prediction. Some tailored optimization functions
are supplied for find the MLEs for the Matern family of covariances. There
are also many useful functions for plotting and working with spatial data
as images. This package also contains an implementation of a sparse matrix
methods for large data sets and currently requires the sparse matrix
(spam) package for testing (but not for the standard spatial functions.)
Use help(fields) to get started and for an overview.  The fields source
code is heavily commented and should provide useful explanation of
numerical details in addition to the manual pages.

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%check
%{_bindir}/R CMD check %{packname}

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/libs
