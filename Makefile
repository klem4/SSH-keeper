SCRIPT_NAME=ssh_keeper.py
DATA_DIR=$(HOME).ssh_keeper
ALIAS_NAME=s
BIN_DIR=/usr/local/bin/

all: clean
	mkdir -p $(DATA_DIR)
	cp $(SCRIPT_NAME) $(DATA_DIR)
	ln -s $(DATA_DIR)/$(SCRIPT_NAME) $(BIN_DIR)$(ALIAS_NAME)
	chmod a+rx $(DATA_DIR)/$(SCRIPT_NAME) $(BIN_DIR)$(ALIAS_NAME)
	@echo "* Install done"
clean:
	rm -f $(BIN_DIR)$(ALIAS_NAME)
	rm -rf $(DATA_DIR)
	@echo "* Clean done"
