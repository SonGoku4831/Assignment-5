# Assignment and runtime requirements

## Runtime
Python 3.10+ (tested 3.12), CPU only, at least two CPU cores; 8 GiB RAM was the test limit. Install the exact direct dependency versions from requirements.txt in a virtual environment. Ports: 8000 for REST or Ray (run separately), 5101/5102 for MLflow shadow servers. No GPU, Docker or external service is required. SQLite and model artifacts are local and regenerated, not submitted.

## Submission checklist
- REPORT.md: measured tables, hardware, explanations, abort criteria and untested list.
- partA: eta_app.py, at least 10 test cases, loadtest_results.json. REST validation, request IDs, metrics, health, generic 500.
- partB: eta_mlflow.py, at least 6 gate cases, gate_output.txt and shadow_output.txt. Signature/example/dependency pins, prod/candidate aliases, four-criterion gate, 200 matching shadow requests.
- partC: eta_ray.py, verify_ray.py, verify_output.txt. Stable customer hash, override, two prod replicas, autoscaled candidate, fractional CPUs, five verification assertions.
- partD: smoke_eta.py with at least five checks, including two model-sanity checks and invalid input; exit 0/1.
- Shared eta_schema.py and original eta_data.py/load_test.py are required to reproduce this solution.
- Rename archive Module4_<your_rollno>.zip. Do not submit model files or databases. Report should fit four pages of prose plus tables when formatted; Markdown pagination depends on your renderer.

The attached PDF supplies the assignment specification. The user's additional deliverables are requirements documentation and PNG records of commands run, supplied here as requirements.txt, this checklist, and evidence/*.png.
