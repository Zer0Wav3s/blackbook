# Try a skill

These prompts show when each skill can help. The expected behavior describes the method, not a measured result. Install the skill first. In Claude Code, use `/skill-name` in place of `Use $skill-name`.

## OUTBOX

```text
Use $outside-the-box. Our dashboard is slow. We're considering Redis,
Memcached, or a database cache. Data can be an hour old, but users need
all of it. Find different approaches and a small test to choose between them.
```

The agent should recognize that all three proposals use caching, consider a different mechanism such as scheduled computation, and suggest a useful comparison.

## LLM Council

```text
Use $llm-council. Should we ship a migration Friday?
Friday is a hard customer deadline, but rollback hasn't been tested.
Keep the decision under 250 words.
```

Advisors should review the decision independently, then examine each other's assumptions. The final recommendation should preserve the deadline and identify untested rollback as a gap. Agreement doesn't prove recovery will work.

## Jev Assist

```text
Use $jev-assist. I have 200 support tickets to group by likely cause.
Decide whether Jev would help and propose a small evaluation.
Don't make API calls yet.
```

The agent should define the evidence and judgments needed, compare the work with simpler methods, and propose a bounded trial. It shouldn't claim a cause is confirmed from a ranking alone.

## Retitle

```text
Use $retitle.
```

Run this in a conversation with existing work. The agent should choose a short title from the recent substantive context and apply it through a supported tool. If it can't, it should give you the title and a manual step.

## Plainspoken

```text
Use $plainspoken to rewrite this update.
Facts: the patch stopped duplicate rows in 20 test files.
Large files haven't been tested.
Draft: We're excited to unveil a robust enhancement that guarantees
seamless imports for every customer.
```

A suitable rewrite would be “The patch stopped duplicate rows in the 20 files we tested. We still need to test larger files.” The untested scope should survive the edit.
