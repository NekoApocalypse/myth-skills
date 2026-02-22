# Project Stash Operations

Detailed procedures for managing projects in the stash.

---

## Stash a Project

Add a new project to `PROJECTS.md` with these standard fields:

```markdown
### Project Name

- **Status:** Active | Paused | Blocked
- **Phase:** Discovery | Design | Implementation | Testing | Deployment
- **Context:** One-line context about what this is
- **Progress:** Brief progress statement
- **Next:** The very next action to take
```

Place new projects at the top of the active projects list.

---

## Update a Project

Edit the relevant entry in `PROJECTS.md`:

1. Locate the project by name
2. Update any changed fields (Status, Phase, Progress, Next)
3. Preserve the structure

---

## Complete a Project

When a project is finished:

1. **Write summary archive** to `vault/myth-projects-stash/completed/{YYYY-MM-DD}_{Project_Name}.md`
   - Use CST (Asia/Shanghai) date
   - Replace spaces in project name with underscores
   - Include: what was accomplished, key decisions, lessons learned

2. **Append to COMPLETED_LOG.md** (workspace root):
   ```
   date,project_name,archive_path
   2026-02-22,Mem0 Trial,vault/myth-projects-stash/completed/2026-02-22_Mem0_Trial.md
   ```

3. **Remove from PROJECTS.md** active section

---

## Drop a Project

When abandoning a project without completion:

1. Remove the project entry from `PROJECTS.md`
2. Do NOT create an archive file
3. Do NOT append to `COMPLETED_LOG.md`

This creates an intentional distinction: dropped projects leave no trace, completed projects are logged.

---

## Small-Talk Redirect

If the user mentions a project idea in a small-talk channel:

> "That sounds like a project worth stashing. Record it in PROJECTS.md in a dedicated channel so it doesn't get lost."

Encourage moving from ephemeral chat to structured project tracking.
