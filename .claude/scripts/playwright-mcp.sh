#!/bin/sh
# Starts the Playwright MCP server. In Claude Code cloud sessions, reuse the
# preinstalled Chromium instead of downloading one (no sandbox: the container
# runs as root); elsewhere use the default.
set -eu
if [ -x /opt/pw-browsers/chromium ]; then
  exec npx -y @playwright/mcp@0.0.83 --headless --isolated --no-sandbox \
    --executable-path /opt/pw-browsers/chromium "$@"
fi
exec npx -y @playwright/mcp@0.0.83 --isolated "$@"
