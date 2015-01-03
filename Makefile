deb: setup.py
	fakeroot dpkg --build pkg-root mochad-logger.deb

setup.py: pkg-root
	python setup.py install --install-layout=deb --prefix=/usr --root=pkg-root
	cp -r DEBIAN pkg-root
#	mv pkg-root/etc/init/mochad_logger.upstart pkg-root/etc/init/mochad_logger.conf
	mv pkg-root/etc/init.d/mochad_logger.sysvinit pkg-root/etc/init.d/mochad_logger

pkg-root:
	mkdir pkg-root

clean:
	rm -rf build *.egg-info pkg-root
