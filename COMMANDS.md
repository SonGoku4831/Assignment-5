# Command record
The evidence/*.txt files contain the actual experimental commands and output; their PNG counterparts are faithful text renderings.

Preparation commands run in the workspace:
```bash
pdftotext -layout Mod4_Assignment_Student.pdf work/assignment.txt
python -m venv --system-site-packages work/venv
work/venv/bin/pip install 'mlflow>=3' 'ray[serve]>=2.40' pytest
```
The uploaded starter files were copied into the solution directory. Python modules and documentation were written with shell heredocs. The capture helper invokes each experiment with subprocess, stores its combined stdout/stderr and status, and uses Pillow with DejaVu Sans Mono to generate PNG pages. Captured commands use this environment's absolute Python path; use `.venv/bin/python` in your own checkout.

The first MLflow launch failed due to the base uvicorn interpreter; a corrected run prepended the virtual environment to PATH. Its initial capture is omitted because the overlapping retry reused the same output file; only 08_shadow_retry is used as shadow evidence. The Ray assertion summary is retained; verbose internal startup and deployment logs are omitted from the GitHub export.

To regenerate a command PNG: `python capture_commands.py my_run "python -m pytest partA/test_eta_app.py -q"` from the solution directory.
