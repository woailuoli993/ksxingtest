# a makefile sample

pre-test:
	@echo "i'm pre test for test...."

LIST = 1 2 3 ONE TWO THREE

test check: pre-test
	@echo a test make file
	@echo now at $@

	for i in $(LIST); do \
		echo $$i; \
	done
