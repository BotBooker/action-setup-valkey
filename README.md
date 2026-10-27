# Starts a Valkey instance on Ubuntu or macOS GitHub Actions

[![CI][ci-status-image]][ci-status-url]

## Basic usage

See [action.yml](action.yml)

**Valkey**

```yaml
  - name: Startup Valkey
    uses: BotBooker/action-setup-valkey@v1
```

The `port` input is optional.

```yaml
  - name: Startup Valkey
    uses: BotBooker/action-setup-valkey@v1
    with:
      port: 5555
```

---
[ci-status-image]: https://github.com/BotBooker/action-setup-valkey/actions/workflows/ci.yml/badge.svg
[ci-status-url]: https://github.com/BotBooker/action-setup-valkey/actions/workflows/ci.yml
