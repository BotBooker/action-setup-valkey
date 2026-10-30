# Setup Valkey GitHub Action

[![CI][ci-status-image]][ci-status-url]

This GitHub Action starts a Valkey instance on Ubuntu (via apt) or macOS (via Homebrew). It is specifically designed for CI/CD pipelines and integration testing when your application requires a Redis-compatible caching or data store layer.
Since Valkey is a fully open-source drop-in replacement for Redis™, this action allows you to test applications built for Redis without changing your code structure.

## Features

- Redis™ Compatibility: Perfect for integration testing of systems relying on Redis-like caching, sessions, or key-value storage.
- Multi-platform support: Works seamlessly on ubuntu-latest and macos-latest runners.
- Zero configuration needed: Starts a Valkey instance on the default port right out of the box.
- Customizable: Allows you to easily change the default port if needed.

## Usage

See [action.yml](action.yml)

### Basic Usage (Testing with Default Port 6379)

```yaml
name: CI with Valkey Cache

on: [push, pull_request]

jobs:
  integration-tests:
    strategy:
      matrix:
        os: [ubuntu, macos]
    runs-on: ${{ matrix.os }}-latest

    steps:
      - name: Checkout repository
        uses: actions/checkout@v4

      # Starts Valkey as a background service for your tests
      - name: Startup Valkey
        id: valkey
        uses: BotBooker/action-setup-valkey@v1

      # Example for Node.js application using redis/valkey client
      - name: Install Dependencies
        run: npm ci

      - name: Run Integration Tests
        run: npm test
        env:
          CACHE_URL: ${{ steps.valkey.outputs.connection-uri }}
# Use the code with caution.
```

### Custom Port Usage

If your local or containerized test configuration expects a different port, customize it using the port input:

```yaml
      - name: Startup Valkey on Custom Port
        uses: BotBooker/action-setup-valkey@v1
        with:
          port: 5555
# Use the code with caution.
```

### Inputs

| Input | Description | Required | Default |
| ----- | ----------- | -------- | ------- |
| `port` | The port number on which the Valkey instance will listen. | No | 6379 |

### Outputs

| Output | Description |
| ------ | ----------- |
| `connection-uri` | The connection URI to connect to Valkey (e.g., redis://localhost:6379). |

## Roadmap & Upcoming Features

We are actively working on expanding the capabilities of this action. The following features are currently planned:

- Windows Support: Extending the matrix to support windows-latest runners.
- mTLS Support: Adding mutual TLS configuration capabilities (CA, certificate, and private key inputs) for secure cluster and client simulation.

## Contributors

Contributions are welcome! Whether it's reporting bugs, suggesting features, or submitting pull requests, your help is highly appreciated.

1. Fork the repository.
2. Create your feature branch (`git checkout -b feature/amazing-feature`).
3. Commit your changes (`git commit -m 'feat(): Add some amazing feature'`).
4. Push to the branch (`git push origin feature/amazing-feature`).
5. Open a Pull Request.
Special thanks to everyone contributing to the development and maintenance of this action!

## Disclaimer

Redis is a trademark of Redis Ltd. Any core software components used here are based on the open-source Valkey project.

## License

The scripts and documentation in this project are released under the Apache License.

---
[ci-status-image]: https://github.com/BotBooker/action-setup-valkey/actions/workflows/ci.yml/badge.svg
[ci-status-url]: https://github.com/BotBooker/action-setup-valkey/actions/workflows/ci.yml
