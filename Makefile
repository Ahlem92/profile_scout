# ----------------------------------
#          INSTALL & TEST
# ----------------------------------
install_requirements:
	@pip install -r requirements.txt

check_code:
	@flake8 scripts/* profile_scout/*.py

black:
	@black scripts/* profile_scout/*.py

test:
	@coverage run -m pytest tests/*.py
	@coverage report -m --omit="${VIRTUAL_ENV}/lib/python*"

ftest:
	@Write me

clean:
	@rm -f */version.txt
	@rm -f .coverage
	@rm -fr */__pycache__ */*.pyc __pycache__
	@rm -fr build dist
	@rm -fr profile_scout-*.dist-info
	@rm -fr profile_scout.egg-info

install:
	@pip install . -U

all: clean install test black check_code

count_lines:
	@find ./ -name '*.py' -exec  wc -l {} \; | sort -n| awk \
        '{printf "%4s %s\n", $$1, $$2}{s+=$$0}END{print s}'
	@echo ''
	@find ./scripts -name '*-*' -exec  wc -l {} \; | sort -n| awk \
		        '{printf "%4s %s\n", $$1, $$2}{s+=$$0}END{print s}'
	@echo ''
	@find ./tests -name '*.py' -exec  wc -l {} \; | sort -n| awk \
        '{printf "%4s %s\n", $$1, $$2}{s+=$$0}END{print s}'
	@echo ''

# ----------------------------------
#      UPLOAD PACKAGE TO PYPI
# ----------------------------------
PYPI_USERNAME=<AUTHOR>
build:
	@python setup.py sdist bdist_wheel

pypi_test:
	@twine upload -r testpypi dist/* -u $(PYPI_USERNAME)

pypi:
	@twine upload dist/* -u $(PYPI_USERNAME)

run_api:
	uvicorn profile_scout.api.fast:app --reload


build_docker:
	docker build -t ${GCR_MULTI_REGION}/${PROJECT}/${IMAGE} .

push_docker:
	docker push ${GCR_MULTI_REGION}/${PROJECT}/${IMAGE}

run_docker:
	docker run -e PORT=8000 -p 8000:8000 --env-file .env ${GCR_MULTI_REGION}/${PROJECT}/${IMAGE}

deploy_docker:
	gcloud run deploy --image ${GCR_MULTI_REGION}/${PROJECT}/${IMAGE} --memory ${MEMORY} --region ${REGION} --env-vars-file .env.yaml
