SCRIPT_NAME=ssh_keeper.py
DATA_DIR=$(HOME)/.ssh_keeper
ALIAS_NAME=s
BIN_DIR=$(HOME)/bin/

all: uninstall
	mkdir -p $(DATA_DIR)
	mkdir -p $(BIN_DIR)
	cp $(SCRIPT_NAME) $(DATA_DIR)
	ln -s $(DATA_DIR)/$(SCRIPT_NAME) $(BIN_DIR)$(ALIAS_NAME)
	chmod +x $(SCRIPT_NAME) $(BIN_DIR)$(ALIAS_NAME)
	@echo "* Install done"
uninstall:
	rm -f $(BIN_DIR)$(ALIAS_NAME)
	rm -rf $(DATA_DIR)
	@echo "* Clean done"
