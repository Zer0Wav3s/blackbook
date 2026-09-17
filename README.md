<div align="center">

<img src="assets/banner.jpg" alt="Blackbook banner" width="100%">

# Blackbook

A growing collection of skills for AI agents.

</div>

Skills are instructions your agent follows for a specific task. Blackbook includes methods for exploring ideas, reviewing decisions, and editing prose. Install the ones you need. More will be added as the collection grows.

[Skills](#skills) · [Install](#install) · [Usage](#usage) · [Requirements](#requirements) · [Contributing](#contributing) · [License](#license)

## Skills

Pick a skill below to read how it works and what it needs.

| Skill | What it does |
|---|---|
| [OUTBOX](skills/outside-the-box/SKILL.md) | Finds different ways to solve a problem when you're stuck, then suggests a small test to choose between them. |
| [LLM Council](skills/llm-council/SKILL.md) | Asks advisor agents to review a decision independently, challenge each other's assumptions, and recommend a next step. |
| [Jev Assist](skills/jev-assist/SKILL.md) | Helps your agent decide when to use TypeSafe's Jev to sort, rank, or check information, then verify the result. |
| [Retitle](skills/retitle/SKILL.md) | Renames the current conversation based on its recent work. Gives you a manual step if the app can't apply the title. |
| [Plainspoken](skills/plainspoken/SKILL.md) | Removes formulaic phrasing so writing sounds natural, while keeping your meaning and facts intact. |

## Install

With Node.js and Git installed, run this in your terminal.

```bash
npx skills add Zer0Wav3s/blackbook -g
```

Choose the skills you want and the agents you use from the installer's prompts. The `-g` flag installs them globally so they're available across your projects. The installer supports Codex, Claude Code, Cursor, and other agents listed in its picker.

To install one skill globally, name it directly.

```bash
npx skills add Zer0Wav3s/blackbook -g --skill plainspoken
```

Replace `plainspoken` with `outside-the-box`, `llm-council`, `jev-assist`, or `retitle`. Omit `-g` if you want a project-only installation.

See the [setup guide](docs/getting-started.md#installation) for listing, updating, removing, and manually copying skills. The installer is maintained by [Vercel Labs](https://github.com/vercel-labs/skills).

## Usage

Use the folder name to invoke a skill. OUTBOX's folder name is `outside-the-box`.

In Codex, try this after installing Plainspoken.

```text
Use $plainspoken to rewrite this paragraph without changing its meaning.
```

In Claude Code, use the slash form.

```text
/plainspoken Rewrite this paragraph without changing its meaning.
```

Add your paragraph to the request. If the skill doesn't appear, check its installation path and reload skills or start a new session as your host supports. Browse the [worked examples](docs/examples.md) for other tasks.

## Requirements

| Skill | What it needs |
|---|---|
| OUTBOX and Plainspoken | An agent that can read skill instructions. |
| LLM Council | Native subagents. Uses your host's models and usage quota. |
| Jev Assist | TypeSafe API access and `TYPESAFE_API_KEY` for live calls. Can assess whether Jev would help before making a call. |
| Retitle | A conversation rename tool for automatic changes. Otherwise, it gives you a manual step. |

Tool support varies by host. Each skill describes its requirements and limits. Packaging checks don't measure the quality of an agent's answers.

## Contributing

Suggest a skill or improvement through an issue or pull request. Describe the task it helps with, include an example, and explain where it can fail. Keep each skill's instructions and supporting files in its own folder, and credit any sources.

Follow the [validation steps](docs/getting-started.md#validation) before submitting changes. Test the skill on a realistic request and report what worked and what failed.

## License

[MIT](LICENSE). Source credits are included in the relevant skills.
