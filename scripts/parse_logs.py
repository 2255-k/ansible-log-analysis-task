#!/usr/bin/env python3
"""
TODO: Implement a log parser.

Required command-line interface:
  python3 scripts/parse_logs.py \
    --input-dir artifacts/raw_logs \
    --summary-out artifacts/reports/log_summary.txt \
    --csv-out artifacts/reports/matches.csv

Requirements:
- Recursively read text files under input-dir.
- Match ERROR and WARNING case-insensitively.
- Count each severity separately.
- CSV columns: source_file, line_number, severity, message.
- Summary must include total errors and warnings.
- Handle invalid/missing input directories and unreadable files gracefully.
- Exit non-zero for invalid input or a fatal failure.
"""
import argparse


def main():
    parser = argparse.ArgumentParser(description="Parse collected logs for errors and warnings.")
    parser.add_argument("--input-dir", required=True, help="Directory containing collected log files")
    parser.add_argument("--summary-out", required=True, help="Path for the text summary")
    parser.add_argument("--csv-out", required=True, help="Path for the CSV report")
    args = parser.parse_args()

    # TODO: validate input directory
    # TODO: recursively discover and read files
    # TODO: identify ERROR and WARNING lines case-insensitively
    # TODO: write CSV and summary reports
    # TODO: return a non-zero exit code for fatal errors
    raise NotImplementedError("Complete the parser as part of the assignment.")


if __name__ == "__main__":
    main()
