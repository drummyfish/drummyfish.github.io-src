# use make ... GIT_MSG to set the git message for all commits

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
endif

clean:
	[ ! -d $(OUTPUTDIR) ] || rm -rf $(OUTPUTDIR)

local:
	$(PELICAN) $(INPUTDIR) -o $(OUTPUTDIR) -s $(CONFFILE) $(PELICANOPTS)

publish:
	$(PELICAN) $(INPUTDIR) -o $(OUTPUTDIR) -s $(PUBLISHCONF) $(PELICANOPTS)

upload_src:
	git add * || :
	git commit -m "source update: $$GIT_MSG"
	git push

upload_web:
	cd $(OUTPUTDIR); \
	git add * || : ; \
	git commit -m "web update: $$GIT_MSG"; \
	git push

upload_all: publish upload_src upload_web
	
