---
name: retitle
description: Rename the current conversation from its recent substantive context when the user asks to refresh the chat or thread title. Does not rename files, projects, or other conversations.
---

# Retitle

Give the current conversation a short title that makes its recent work easy to find again. Invoking this skill authorizes that title change. Creating or discussing the skill alone does not.

## Choose the title

Use the latest substantive goal and enough earlier context to identify its subject. Ignore the rename request itself, acknowledgments, pasted instructions, and brief tangents. Follow a genuine change of topic instead of clinging to the opening prompt. If recent work still belongs to a broader task, retain that task's name.

Prefer a concrete subject and action in roughly three to seven words. Use the conversation's language and keep useful project or feature names. Avoid generic labels such as “Help with coding,” sensitive personal details, and claims of completion the conversation doesn't support. Honor a title or naming style supplied by the user.

Choose one title without offering a menu. If the existing title already fits, leave it alone. If there is no substantive context, ask for the topic instead of inventing one.

## Apply it in the current host

Use an available native conversation-title tool and its documented arguments. Target the current conversation, not whichever thread happens to be first in a list.

- In Codex, when `mcp__codex_app__set_thread_title` is available, supply `title` and omit `threadId` to target the calling thread. Other Codex hosts may expose a different tool or none.
- In Claude Code, use an exposed session-renaming tool if one exists. The documented `/rename <title>` command can be entered by the user in the session. Its presence does not mean the agent has a callable rename tool. If the agent cannot execute a supported rename action, give the user that exact command with the chosen title. See the [Claude Code command reference](https://code.claude.com/docs/en/commands).
- In other hosts, use a supported rename action only when the current conversation can be identified reliably. Otherwise return the proposed title and briefly state that it must be applied manually.

Do not edit session databases, transcript files, or terminal window titles as a substitute. Do not start another conversation or claim a rename happened just because a command was printed.

After a successful tool result, confirm the applied title in one line. If the call fails or its outcome is unclear, report that and preserve the proposed title. Don't keep retrying automatically.
