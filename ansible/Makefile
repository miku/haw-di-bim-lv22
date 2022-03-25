
SHELL := /bin/bash
ANSIBLE_OPTS = ANSIBLE_RETRY_FILES_ENABLED=false ANSIBLE_NOCOWS=true ANSIBLE_HOST_KEY_CHECKING=false

.PHONY: deploy
deploy: ## deploy to site
	$(ANSIBLE_OPTS) ansible-playbook -b -vvv -i hosts site.yml


