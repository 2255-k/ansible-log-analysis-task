# Two-Day Assignment: Automated Log Analysis and Error Reporting with Ansible Roles

## Objective
Create an Ansible role-based automation workflow that collects selected logs from Linux hosts, parses them using Python, and generates a report of `ERROR` and `WARNING` entries.

## Day 1 — Repository, Inventory, and Log Collection
1. Clone the starter repository.
2. Configure `inventory.ini` for the authorized lab hosts.
3. Verify Ansible connectivity to every host.
4. Complete `roles/log_collector/tasks/main.yml` so it:
   - creates a local artifact directory on the control node;
   - fetches the configured log files from each target;
   - stores logs in host-specific directories;
   - handles missing or unreadable log files clearly.
5. Review `group_vars/all.yml` and ensure log paths are configurable.
6. Run syntax checks and test log collection.

**Day 1 deliverable:** Inventory works and selected logs are collected from the target host(s).

## Day 2 — Python Parsing, Reporting, and Validation
1. Complete `scripts/parse_logs.py`.
2. The parser must:
   - accept an input directory argument;
   - recursively read text log files;
   - identify lines containing `ERROR` or `WARNING` case-insensitively;
   - count errors and warnings separately;
   - write a human-readable summary file;
   - write matching entries to a CSV file with source filename, line number, severity, and message;
   - handle missing directories and unreadable files gracefully;
   - return a non-zero exit code for invalid input or an execution failure.
3. Complete `roles/log_parser/tasks/main.yml` to run the parser on the control node.
4. Complete `roles/report_validation/tasks/main.yml` to verify the report files exist and contain expected output.
5. Run the complete playbook twice and record whether the second run causes unnecessary changes.
6. Update the README with setup, execution commands, sample output, and screenshots.
7. Commit and push the completed work to GitHub.

**Day 2 deliverable:** Working collection and parsing pipeline, generated reports, validation results, and documentation.

## Acceptance criteria
- Ansible connectivity succeeds for the configured hosts.
- Logs are collected into host-specific folders on the control node.
- The parser finds `ERROR` and `WARNING` lines without depending on capitalization.
- Counts in the summary match the parsed entries.
- CSV output includes source file and line number.
- Missing input and unreadable files are handled without an unhelpful traceback.
- The playbook syntax check passes.
- The full workflow runs successfully.
- No credentials, private keys, or sensitive logs are committed.

## Suggested grading (100 points)
- Inventory and connectivity: 10
- Role structure and Ansible quality: 20
- Log collection: 20
- Python parser and reporting: 25
- Validation and error handling: 15
- GitHub README, evidence, and safe handling of logs: 10
