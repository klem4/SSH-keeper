SCRIPT_NAME=ssh_keeper.py
DATA_DIR=$(HOME)/.ssh_keeper
ALIAS_NAME=s
BIN_DIR=/usr/local/bin/

all: uninstall
	mkdir -p $(DATA_DIR)
	cp $(SCRIPT_NAME) $(DATA_DIR)
	ln -s $(DATA_DIR)/$(SCRIPT_NAME) $(BIN_DIR)$(ALIAS_NAME)

	chmod +x $(SCRIPT_NAME) $(BIN_DIR)$(ALIAS_NAME)
	chown $(USER) $(BIN_DIR)$(ALIAS_NAME)
	chown -R $(USER) $(DATA_DIR)

	@echo "* Install done"
uninstall:
	rm -f $(BIN_DIR)$(ALIAS_NAME)
	rm -rf $(DATA_DIR)
	@echo "* Clean done"
