.PHONY: test conda-activate conda-update synth deploy destroy

 # Run tests in the terminal
test:
	PYTHONPATH=. pytest


# Python environment
conda-activate:
	conda activate pillow

conda-update:
	conda env update --file environment.yaml --prune


# API Service
# AWS Cloud Development Kit commands
#
# mkdocstrings errors when the `cdk.out` dir is in the `service/` dir.
# It seems to be confused by dots in the directory names (`cdk.out`, `asset.`)
# workaround: cdk.json sets the cdk outpupt directory to the root
synth:
	cd service && npx cdk synth

deploy:
	cd service && npx cdk deploy

destroy:
	cd service && npx cdk destroy