SCRIPT_NAME=ss.py
ALIAS_NAME = s
BIN_DIR=/usr/local/bin/

all:
	cp $(SCRIPT_NAME) $(BIN_DIR)
	ln -s $(SCRIPT_NAME) $(BIN_DIR)$(ALIAS_NAME)
	chmod a+rx $(SCRIPT_NAME)

clean:
	rm -f $(BIN_DIR)$(SCRIPT_NAME)
	rm -f $(BIN_DIR)$(ALIAS_NAME)
