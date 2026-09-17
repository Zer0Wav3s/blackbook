# Using Blackbook

## Installation

The [Skills CLI](https://github.com/vercel-labs/skills) installs directly from this repository. It requires Node.js and Git.

```bash
# Choose skills and agents for a global installation.
npx skills add Zer0Wav3s/blackbook -g

# List the available skills without installing them.
npx skills add Zer0Wav3s/blackbook --list

# Install Plainspoken globally for Codex and Claude Code.
npx skills add Zer0Wav3s/blackbook --skill plainspoken -g -a codex -a claude-code

# Install every Blackbook skill for Codex in the current project.
npx skills add Zer0Wav3s/blackbook --skill '*' -a codex
```

The first command installs globally for the agents you choose. Omit `-g` for a project-only installation. You can choose symlinks or copies during installation. Use `--copy` if you need separate copies.

For CLI-managed installations, use these commands. Check local edits before updating.

```bash
npx skills list
npx skills update
npx skills remove
```

The update command can update skills from other libraries too. The remove command lets you select what to remove.

### Manual installation

Clone the repository, then copy a whole skill folder into your agent's skill directory.

```bash
git clone https://github.com/Zer0Wav3s/blackbook.git
cd blackbook
```

For a personal Codex installation, run this from the checkout.

```bash
mkdir -p "${CODEX_HOME:-$HOME/.codex}/skills"
if [ ! -e "${CODEX_HOME:-$HOME/.codex}/skills/plainspoken" ]; then
  cp -R skills/plainspoken "${CODEX_HOME:-$HOME/.codex}/skills/plainspoken"
fi
```

For Claude Code, run this from the project where you'll use the skill. Replace the source path with your checkout's location.

```bash
mkdir -p .claude/skills
if [ ! -e .claude/skills/plainspoken ]; then
  cp -R /path/to/blackbook/skills/plainspoken .claude/skills/plainspoken
fi
```

For Codex on Windows, run this in PowerShell from the checkout.

```powershell
$skillRoot = if ($env:CODEX_HOME) { Join-Path $env:CODEX_HOME "skills" } else { Join-Path $HOME ".codex/skills" }
$destination = Join-Path $skillRoot "plainspoken"
New-Item -ItemType Directory -Force -Path $skillRoot | Out-Null
if (-not (Test-Path $destination)) {
  Copy-Item -Recurse "skills/plainspoken" $destination
}
```

Replace `plainspoken` with any skill's folder name. These commands won't overwrite an existing installation. To update one, review the differences and copy the intended changes, including its supporting files.

For other hosts, use their documented skill location and invocation syntax. Blackbook uses the [Agent Skills format](https://agentskills.io/specification). Tool availability still depends on the host.

## Troubleshooting

If a skill doesn't appear, check that its installed folder contains `SKILL.md`. Reload skills or start a new session as your host supports. Use the folder name when invoking it, such as `outside-the-box` for OUTBOX.

If installation fails while fetching the repository, check your Git connection and repository access. If symlink creation fails, try the installer with `--copy`.

Installing a skill doesn't add tools to your agent. Check the [requirements in the README](../README.md#requirements) when a skill can't perform an action.

## Validation

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements-dev.txt
python3 scripts/validate_skills.py
```

On Windows, create the environment with `py -m venv .venv` and activate it with `.\.venv\Scripts\Activate.ps1`. Use `python` for the validation commands.

The validator checks skill metadata and local links. It needs PyYAML only for repository development. Jev Assist includes an optional Python 3 runner. The other skills do not require Python.

These checks don't measure answer quality. Test changed skills with realistic requests, including a case where they should stop or use a simpler approach.
