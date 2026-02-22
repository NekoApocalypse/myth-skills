# Data Model

File formats and naming conventions for the Project Stash.

All paths are relative to workspace root: `/home/node/.openclaw/workspace/`

---

## PROJECTS.md

Active project board. Markdown format with H3 project headers.

### Project Entry Format

```markdown
### Project Name

- **Status:** Active | Paused | Blocked
- **Phase:** Discovery | Design | Implementation | Testing | Deployment
- **Context:** One-line description of what this project is about
- **Progress:** Current state of the work
- **Next:** The immediate next action to take
```

### Example

```markdown
### Mem0 Trial

- **Status:** Active
- **Phase:** Implementation
- **Context:** Evaluating Mem0 memory layer for Claude Code integration
- **Progress:** Basic setup complete, testing API calls
- **Next:** Run integration tests and document findings
```

---

## COMPLETED_LOG.md

Append-only ledger tracking completed projects. CSV format with header.

### Format

```csv
date,project_name,archive_path
2026-02-22,Mem0 Trial,vault/myth-projects-stash/completed/2026-02-22_Mem0_Trial.md
2026-02-20,Homepage Redesign,vault/myth-projects-stash/completed/2026-02-20_Homepage_Redesign.md
```

### Fields

| Field | Description |
|-------|-------------|
| `date` | Completion date in YYYY-MM-DD format (CST) |
| `project_name` | Original project name from PROJECTS.md |
| `archive_path` | Relative path to the archive file |

### Notes

- File is created on first use (do not pre-create)
- Always append, never edit existing lines
- No entry for dropped projects (intentional distinction)

---

## Daily Snapshots

Periodic copies of PROJECTS.md for momentum analysis.

### Naming Convention

```
{YYYY-MM-DD}_PROJECTS.md
```

### Example

```
vault/myth-projects-stash/daily-snapshots/2026-02-22_PROJECTS.md
```

### Storage Location

```
vault/myth-projects-stash/daily-snapshots/
```

### Timezone

All dates use CST (Asia/Shanghai, UTC+8).

---

## Completed Project Archives

Full project summaries archived on completion.

### Naming Convention

```
{YYYY-MM-DD}_{Project_Name}.md
```

- Spaces in project name → underscores
- Date is completion date (CST)

### Example

```
vault/myth-projects-stash/completed/2026-02-22_Mem0_Trial.md
```

### Storage Location

```
vault/myth-projects-stash/completed/
```

### Content

Archive files should include:
- What was accomplished
- Key decisions made
- Lessons learned
- Links to relevant artifacts

---

## Path Summary

| File Type | Path Pattern |
|-----------|--------------|
| Active board | `PROJECTS.md` |
| Completion log | `COMPLETED_LOG.md` |
| Daily snapshots | `vault/myth-projects-stash/daily-snapshots/{YYYY-MM-DD}_PROJECTS.md` |
| Completed archives | `vault/myth-projects-stash/completed/{YYYY-MM-DD}_{Project_Name}.md` |
