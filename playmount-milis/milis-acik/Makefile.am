themedir = $(datadir)/plymouth/themes/milis-acik
nodist_theme_DATA = \
                    milis-acik.plymouth

dist_theme_DATA =                                                     \
                    milis-acik.script                                  \
                    logo_blurred.png                              \
                    logo.png


MAINTAINERCLEANFILES = Makefile.in milis-acik.plymouth
CLEANFILES = milis-acik.plymouth

milis-acik.plymouth: $(srcdir)/milis-acik.plymouth.in
	sed -e 's,[@]PLYMOUTH_THEME_PATH[@],$(PLYMOUTH_THEME_PATH),g' \
	       $(srcdir)/milis-acik.plymouth.in > milis-acik.plymouth

EXTRA_DIST = milis-acik.plymouth.in
