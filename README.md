# Ansible Role-Based Log Analysis and Error Reporting

**Duration:** 2 days  
**Stack:** Ansible, Python 3, Linux, YAML, Jinja2, Git/GitHub

## Scenario
Automate log collection from Linux servers, parse collected logs with Python, and generate a report of errors and warnings.

## Workflow
1. Ansible connects to target Linux servers.
2. The `log_collector` role fetches configured log files to the control node.
3. The `log_parser` role runs `scripts/parse_logs.py` locally against collected logs.
4. The `report_validation` role verifies that report files exist and contain expected data.

## Repository layout
See the directory tree in this repository. The files marked `TODO` are intentionally incomplete and are the team's implementation tasks.

## Prerequisites
- Ansible installed on the control node.
- Python 3 available on the control node.
- One or more reachable Linux target servers with SSH access.
- Permission to read the configured log files on target servers.

## Setup
1. Copy `inventory.ini.example` to `inventory.ini`.
2. Update host addresses, SSH username, and private-key path for your lab.
3. Do not commit private keys or credentials.
4. Review `group_vars/all.yml` and configure the log paths.
5. Implement the TODO items in `TASK.md`.

## Run (after implementation)
```bash
ansible-playbook site.yml --syntax-check
ansible-playbook site.yml
```

## Expected output
The team should generate:
- `artifacts/raw_logs/` — collected logs grouped by host
- `artifacts/reports/log_summary.txt` — human-readable summary
- `artifacts/reports/matches.csv` — matching error and warning lines

## Safety notes
Use this project only on systems you are authorized to administer. Log files may contain usernames, IP addresses, session details, or other sensitive information. Redact sensitive data before committing reports or screenshots.
