#!/bin/bash
black ./**/*.py
isort ./**/*.py
autoflake --in-place --remove-all-unused-imports ./**/*.py
