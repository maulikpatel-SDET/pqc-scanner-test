# Optional edge cases (not part of the main testbed)

Copy into the repo on a separate branch, one at a time, and run the QA workflow.

- truncated_key.pem: a PEM block with BEGIN and no END. action.yml says this can hang the scan for about 5 minutes. Record the job time, and whether the job summary reports the file as skipped or timed out.
- over_1mb.py: over 1 MB and full of MD5 calls. The README says files over 1 MB are skipped. Expected: no findings, and the summary lists it as skipped. If it says "clean" with no skip notice, that's a bug.
