# usage: 
# make target [args], args:
#
#    GIT_MSG="..."         - message for git comments
#    NO_PRETTY=1           - do not prettify
#
# Tidy is required to be installed for HTML prettifying.

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
ifndef NO_PRETTY
	$(MAKE) prettify
endif

publish:
	$(PELICAN) $(INPUTDIR) -o $(OUTPUTDIR) -s $(PUBLISHCONF) $(PELICANOPTS)
ifndef NO_PRETTY
	$(MAKE) prettify
endif

prettify:
	@-$(foreach f,$(shell find $(OUTPUTDIR) -iname "*.html"),echo "prettifying $f"; tidy -i -wrap 120 -m "$f" 2>&1 | grep --color -E "Warning|Error" || :;)

upload_src:
	git add -A || :
	git commit -m "source update: $$GIT_MSG"
	git push

upload_web:
	cd $(OUTPUTDIR); \
	git add -A || : ; \
	git commit -m "web update: $$GIT_MSG"; \
	git push

upload_all: publish upload_src upload_web
	
