# Generated outputs

Save generated analysis reports and temporary workflow files under `./_results/`, preferably in a descriptive per-run subfolder. This includes `task_plan.md`, `findings.md`, `progress.md`, research notes, and exported artifacts. Do not place these files in the repository root or `reports/`.

Treat `_results/` as local, temporary output; it is excluded from Git. Apply this location preference even when a skill specifies another default output or planning directory.

# Working in this repo

After editing anything under `skills/`, run `python3 tests/validate_skills.py` — it's the CI gate and the only thing that catches a broken sibling reference or a frontmatter mismatch.

After any change to this repo's content, bump `version` in `.claude-plugin/plugin.json`. `claude plugin update` only compares that field, not file contents — an unbumped version means a directory-sourced install silently never picks up the change.

See the README's `## Contributing` section for naming conventions, the sibling-reference format, and the steps for adding or renaming a skill.
