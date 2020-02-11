# dnf-plugin-releasemods
Dnf plugin that can prevent specific release packages to install any repo files.

## Building the RPM as non-root

The following instructions have been tested on CentOS8:
* Download a tagged release (tar.gz) into `$HOME/rpmbuild/SOURCES`, e.g.
```bash
sdir=$HOME/rpmbuild/SOURCES
[ -d $sdir ] || mkdir -p $sdir
v=1.0.0
curl -Lo $sdir/dnf-plugin-releasemods-${v}.tar.gz https://github.com/man-hep-tier2/dnf-plugin-releasemods/archive/v${v}.tar.gz
```
* Extract the spec file from the archive, e.g.
```bash
tar xvf $sdir/dnf-plugin-releasemods-${v}.tar.gz dnf-plugin-releasemods-${v}/dnf-plugin-releasemods.spec
```
* Run rpmbuild on the spec file, e.g.
```bash
rpmbuild -ba dnf-plugin-releasemods-${v}/dnf-plugin-releasemods.spec
```

The above example will create a binary rpm (in `$HOME/rpmbuild/RPMS/noarch`) and a source rpm (in `$HOME/rpmbuild/SRPMS`).
