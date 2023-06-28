.PHONY: api.generate
api.generate: openapi.yaml
	openapi-generator \
		generate \
		--skip-validate-spec \
		--enable-post-process-file \
		--git-user-id crmne \
		--git-repo-id slskd-python-client \
		--package-name slskd \
		--input-spec $^ \
		--generator-name python-nextgen \
		--library asyncio \
		--additional-properties=removeEnumValuePrefix=false \
		--output .
	pre-commit run -a
