PY?=python
PELICAN?=pelican
PELICANOPTS=

BASEDIR=$(CURDIR)
INPUTDIR=$(BASEDIR)/content
OUTPUTDIR=../drummyfish.github.io
CONFFILE=$(BASEDIR)/pelicanconf.py
PUBLISHCONF=$(BASEDIR)/publishconf.py
SOURCEDIR=sources
OUTPUTSOURCEDIR = $(OUTPUTDIR)/$(SOURCEDIR)
THEMEDIR=$(BASEDIR)/themes
PLUGINDIR=$(BASEDIR)/plugins

GITHUB_PAGES_BRANCH=master

DEBUG ?= 0
ifeq ($(DEBUG), 1)
	PELICANOPTS += -D
endif

RELATIVE ?= 0
ifeq ($(RELATIVE), 1)
	PELICANOPTS += --relative-urls
endif                                                                       '

local:
	$(PELICAN) $(INPUTDIR) -o $(OUTPUTDIR) -s $(CONFFILE) $(PELICANOPTS)

clean:
	[ ! -d $(OUTPUTDIR) ] || rm -rf $(OUTPUTDIR)

publish:
	$(PELICAN) $(INPUTDIR) -o $(OUTPUTDIR) -s $(PUBLISHCONF) $(PELICANOPTS)

github: publish
	ghp-import -m "Generate Pelican site" -b $(GITHUB_PAGES_BRANCH) $(OUTPUTDIR)
	git push origin $(GITHUB_PAGES_BRANCH)

upload_src:
	git add * || :
	git commit -m "update"
	git push

upload_web:
	cd $(OUTPUTDIR); \
	git add * || : ; \
	git commit -m "update"; \
	git push

upload_all: upload_src upload_web
	
