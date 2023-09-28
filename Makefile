install:
	poetry install

brain-games:
	poetry run brain-games

brain-even:
	poetry run brain-even

brain-calc:
	poetry run brain-calc

brain-hcf:
	poetry run brain-hcf

brain-ap:
	poetry run brain-ap

brain-prime:
	poetry run brain-prime

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl

.PHONY: install