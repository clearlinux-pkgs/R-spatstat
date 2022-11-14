#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-spatstat
Version  : 3.0.2
Release  : 64
URL      : https://cran.r-project.org/src/contrib/spatstat_3.0-2.tar.gz
Source0  : https://cran.r-project.org/src/contrib/spatstat_3.0-2.tar.gz
Summary  : Spatial Point Pattern Analysis, Model-Fitting, Simulation, Tests
Group    : Development/Tools
License  : GPL-2.0+
Requires: R-spatstat.data
Requires: R-spatstat.explore
Requires: R-spatstat.geom
Requires: R-spatstat.linnet
Requires: R-spatstat.model
Requires: R-spatstat.random
Requires: R-spatstat.utils
BuildRequires : R-spatstat.data
BuildRequires : R-spatstat.explore
BuildRequires : R-spatstat.geom
BuildRequires : R-spatstat.linnet
BuildRequires : R-spatstat.model
BuildRequires : R-spatstat.random
BuildRequires : R-spatstat.utils
BuildRequires : buildreq-R

%description
Contains over 2000 functions for plotting spatial data, exploratory data analysis, model-fitting, simulation, spatial sampling, model diagnostics, and formal inference. 
	Data types include point patterns, line segment patterns, spatial windows, pixel images, tessellations, and linear networks. 
	Exploratory methods include quadrat counts, K-functions and their simulation envelopes, nearest neighbour distance and empty space statistics, Fry plots, pair correlation function, kernel smoothed intensity, relative risk estimation with cross-validated bandwidth selection, mark correlation functions, segregation indices, mark dependence diagnostics, and kernel estimates of covariate effects. Formal hypothesis tests of random pattern (chi-squared, Kolmogorov-Smirnov, Monte Carlo, Diggle-Cressie-Loosmore-Ford, Dao-Genton, two-stage Monte Carlo) and tests for covariate effects (Cox-Berman-Waller-Lawson, Kolmogorov-Smirnov, ANOVA) are also supported.
	Parametric models can be fitted to point pattern data using the functions ppm(), kppm(), slrm(), dppm() similar to glm(). Types of models include Poisson, Gibbs and Cox point processes, Neyman-Scott cluster processes, and determinantal point processes. Models may involve dependence on covariates, inter-point interaction, cluster formation and dependence on marks. Models are fitted by maximum likelihood, logistic regression, minimum contrast, and composite likelihood methods. 
	A model can be fitted to a list of point patterns (replicated point pattern data) using the function mppm(). The model can include random effects and fixed effects depending on the experimental design, in addition to all the features listed above.
	Fitted point process models can be simulated, automatically. Formal hypothesis tests of a fitted model are supported (likelihood ratio test, analysis of deviance, Monte Carlo tests) along with basic tools for model selection (stepwise(), AIC()) and variable selection (sdr). Tools for validating the fitted model include simulation envelopes, residuals, residual plots and Q-Q plots, leverage and influence diagnostics, partial residuals, and added variable plots.

%prep
%setup -q -n spatstat
cd %{_builddir}/spatstat

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1668455904

%install
export SOURCE_DATE_EPOCH=1668455904
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --install-tests --use-LTO --built-timestamp=${SOURCE_DATE_EPOCH} --data-compress=none --compress=none --build  -l %{buildroot}/usr/lib64/R/library .
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper -mprefer-vector-width=512 " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper -mprefer-vector-width=512 " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper -mprefer-vector-width=512  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --use-LTO --no-test-load --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --use-LTO --install-tests --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc . || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/spatstat/CITATION
/usr/lib64/R/library/spatstat/DESCRIPTION
/usr/lib64/R/library/spatstat/INDEX
/usr/lib64/R/library/spatstat/Meta/Rd.rds
/usr/lib64/R/library/spatstat/Meta/demo.rds
/usr/lib64/R/library/spatstat/Meta/features.rds
/usr/lib64/R/library/spatstat/Meta/hsearch.rds
/usr/lib64/R/library/spatstat/Meta/links.rds
/usr/lib64/R/library/spatstat/Meta/nsInfo.rds
/usr/lib64/R/library/spatstat/Meta/package.rds
/usr/lib64/R/library/spatstat/Meta/vignette.rds
/usr/lib64/R/library/spatstat/NAMESPACE
/usr/lib64/R/library/spatstat/NEWS
/usr/lib64/R/library/spatstat/R/spatstat
/usr/lib64/R/library/spatstat/R/spatstat.rdb
/usr/lib64/R/library/spatstat/R/spatstat.rdx
/usr/lib64/R/library/spatstat/demo/data.R
/usr/lib64/R/library/spatstat/demo/diagnose.R
/usr/lib64/R/library/spatstat/demo/spatstat.R
/usr/lib64/R/library/spatstat/demo/sumfun.R
/usr/lib64/R/library/spatstat/doc/BEGINNER.txt
/usr/lib64/R/library/spatstat/doc/Nickname.txt
/usr/lib64/R/library/spatstat/doc/bugfixes.R
/usr/lib64/R/library/spatstat/doc/bugfixes.Rnw
/usr/lib64/R/library/spatstat/doc/bugfixes.pdf
/usr/lib64/R/library/spatstat/doc/datasets.R
/usr/lib64/R/library/spatstat/doc/datasets.Rnw
/usr/lib64/R/library/spatstat/doc/datasets.pdf
/usr/lib64/R/library/spatstat/doc/getstart.R
/usr/lib64/R/library/spatstat/doc/getstart.Rnw
/usr/lib64/R/library/spatstat/doc/getstart.pdf
/usr/lib64/R/library/spatstat/doc/index.html
/usr/lib64/R/library/spatstat/doc/packagesizes.txt
/usr/lib64/R/library/spatstat/doc/replicated.R
/usr/lib64/R/library/spatstat/doc/replicated.Rnw
/usr/lib64/R/library/spatstat/doc/replicated.pdf
/usr/lib64/R/library/spatstat/doc/shapefiles.R
/usr/lib64/R/library/spatstat/doc/shapefiles.Rnw
/usr/lib64/R/library/spatstat/doc/shapefiles.pdf
/usr/lib64/R/library/spatstat/doc/spatstatKnetsize.txt
/usr/lib64/R/library/spatstat/doc/spatstatcoreNEWS
/usr/lib64/R/library/spatstat/doc/spatstatcoresize.txt
/usr/lib64/R/library/spatstat/doc/spatstatguisize.txt
/usr/lib64/R/library/spatstat/doc/spatstatlocalsize.txt
/usr/lib64/R/library/spatstat/doc/umbrella.txt
/usr/lib64/R/library/spatstat/doc/updates.R
/usr/lib64/R/library/spatstat/doc/updates.Rnw
/usr/lib64/R/library/spatstat/doc/updates.pdf
/usr/lib64/R/library/spatstat/help/AnIndex
/usr/lib64/R/library/spatstat/help/aliases.rds
/usr/lib64/R/library/spatstat/help/macros/defns.Rd
/usr/lib64/R/library/spatstat/help/paths.rds
/usr/lib64/R/library/spatstat/help/spatstat.rdb
/usr/lib64/R/library/spatstat/help/spatstat.rdx
/usr/lib64/R/library/spatstat/html/00Index.html
/usr/lib64/R/library/spatstat/html/R.css
