# SwiftParcel ETA — Assignment 5

[Download all files as a ZIP](https://github.com/SonGoku4831/Assignment-5/archive/refs/heads/module4-solution.zip) · [Download command PNGs](downloads/Command_PNGs.zip?raw=true) · [Report](REPORT.md) · [Requirements checklist](REQUIREMENTS.md)

# SwiftParcel Module 4 solution
Run all commands from this directory. Python 3.10+ and at least 2 CPU cores are required; Python 3.12 was tested.

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python eta_data.py
python -m pytest partA/test_eta_app.py partB/test_gate.py -q
uvicorn partA.eta_app:app --host 127.0.0.1 --port 8000
# In another activated terminal:
python partD/smoke_eta.py --url http://127.0.0.1:8000/v1/models/eta:predict --expect-version v1
```

Stop the API before running the automated measurements (they manage their own servers):

```bash
python measure.py
export MLFLOW_TRACKING_URI=sqlite:///mlflow.db
PYTHONPATH=. python partB/eta_mlflow.py
PYTHONPATH=. python partB/shadow.py
PYTHONPATH=. python partC/verify_ray.py
```

`ETA_MODEL` selects the REST bundle, default `data/eta_v1.joblib`.
`MLFLOW_TRACKING_URI` selects the tracking/registry store, default SQLite in the current directory.
MLflow's local environment manager uses the already installed pinned environment.
`requirements.txt` lists the direct requirements; `requirements-lock.txt` records the actual environment (including preinstalled tools and unrelated packages), so use the direct requirements for a clean install.
The assignment's interface files live under partA–partD as requested; keep the root on PYTHONPATH when invoking scripts directly.

Evidence PNGs are rendered from real captured stdout/stderr, with the exact execution command and exit status. They are terminal-style command records, not desktop screenshots. Long outputs span multiple PNGs; corresponding text files preserve searchable output. Setup/source-writing commands are summarized in COMMANDS.md; experimental commands are captured individually.
No model bundles, datasets, tracking databases or model registry artifacts are included; regenerate them using the commands above.
Rename the ZIP to Module4_<your_rollno>.zip before submission and review the report under your course's individual-work rules. This implementation and prose were generated with AI assistance; starter data and load scripts were supplied with the assignment. No lecture notebook fragments were used.

GitHub export note: verbose internal Ray startup/deployment logs and their PNG pages are excluded. `partC/verify_output.txt` preserves the actual five assertion results and exit status. The archives and remaining PNG records contain the solution and non-sensitive experiment evidence.

Delivery note: the individual project files and approved PNG archive are published here. A separate bulk solution archive was omitted by automatic approval review. Use GitHub's Code → Download ZIP for a copy of the published branch.
