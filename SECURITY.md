# Security Policy

## Supported versions

| Version | Supported |
|---------|-----------|
| latest release | yes |
| older releases | best effort |

## Reporting a vulnerability

Please **do not** open a public GitHub issue for security problems.

Email: **security@quanvio.com** (or founder@quanvio.com if security@ is not yet active)

Include:

- Description of the issue
- Steps to reproduce
- Impact assessment
- Suggested fix (optional)

We aim to acknowledge reports within **72 hours** and provide a timeline within **7 days**.

## Safe defaults

- API keys belong in environment variables, never in git
- Use the `native` deploy profile on trusted machines; use `isolated` for untrusted code
- Rotate keys if exposed in logs or chat
