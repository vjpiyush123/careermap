#!/usr/bin/env python3
"""CareerGuide Administration Script.

Usage:
    python admin.py start   — Start the application
    python admin.py stop    — Stop the application
    python admin.py status  — Show application status
"""

from __future__ import annotations

import os
import platform
import signal
import subprocess
import sys
from pathlib import Path

import httpx
import yaml

PID_FILE = Path(__file__).resolve().parent / ".careerguide.pid"
LOG_FILE = Path(__file__).resolve().parent / "careerguide.log"
CONFIG_FILE = Path(__file__).resolve().parent / "config" / "settings.yaml"


def _load_config() -> dict:
    if CONFIG_FILE.exists():
        with open(CONFIG_FILE) as f:
            return yaml.safe_load(f) or {}
    return {}


def _get_app_info(config: dict) -> tuple[str, int]:
    app = config.get("app", {})
    host = app.get("host", "0.0.0.0")
    port = app.get("port", 8000)
    return host, port


def _check_ollama(config: dict) -> dict:
    """Check Ollama LLM connectivity."""
    llm = config.get("llm", {})
    provider = llm.get("provider", "ollama")
    base_url = llm.get("ollama_base_url", "http://localhost:11434")
    model = llm.get("tier1_model", "unknown")

    result = {
        "provider": provider,
        "model": model,
        "base_url": base_url,
        "status": "unknown",
    }

    try:
        resp = httpx.get(f"{base_url}/api/tags", timeout=5)
        if resp.status_code == 200:
            models = resp.json().get("models", [])
            model_names = [m.get("name", "") for m in models]
            result["status"] = "connected"
            result["available_models"] = model_names
            result["model_available"] = any(model in n for n in model_names)
        else:
            result["status"] = "error"
            result["error"] = f"HTTP {resp.status_code}"
    except Exception as e:
        result["status"] = "unreachable"
        result["error"] = str(e)

    return result


def _is_running() -> tuple[bool, int | None]:
    """Check if app is running by PID file."""
    if not PID_FILE.exists():
        return False, None
    try:
        pid = int(PID_FILE.read_text().strip())
        if platform.system() == "Windows":
            result = subprocess.run(
                ["tasklist", "/FI", f"PID eq {pid}", "/NH"],
                capture_output=True, text=True,
            )
            if str(pid) in result.stdout:
                return True, pid
        else:
            os.kill(pid, 0)
            return True, pid
    except (ValueError, OSError, ProcessLookupError):
        pass
    # Stale PID file
    PID_FILE.unlink(missing_ok=True)
    return False, None


def cmd_start():
    """Start the CareerGuide application."""
    running, pid = _is_running()
    if running:
        print(f"Application is already running (PID: {pid})")
        return

    config = _load_config()
    host, port = _get_app_info(config)

    # Check Ollama connectivity
    ollama_info = _check_ollama(config)
    print(f"AI Provider: {ollama_info['provider']}")
    print(f"AI Model: {ollama_info['model']}")
    print(f"Ollama Status: {ollama_info['status']}")

    if ollama_info["status"] == "unreachable":
        fallback = config.get("llm", {}).get("fallback_to_templates", True)
        if not fallback:
            print("ERROR: Ollama is unreachable and fallback is disabled. Cannot start.")
            sys.exit(1)
        print("WARNING: Ollama unreachable — will use template fallback narratives")
    elif ollama_info["status"] == "connected" and not ollama_info.get("model_available", False):
        print(f"WARNING: Model '{ollama_info['model']}' not found in Ollama. Available: {ollama_info.get('available_models', [])}")

    print(f"\nStarting CareerGuide on {host}:{port}...")
    print(f"Log file: {LOG_FILE}")

    log_fh = open(LOG_FILE, "a")
    proc = subprocess.Popen(
        [
            sys.executable, "-m", "uvicorn",
            "careerguide.app:app",
            "--host", host,
            "--port", str(port),
        ],
        stdout=log_fh,
        stderr=log_fh,
        cwd=str(Path(__file__).resolve().parent / "src"),
    )
    PID_FILE.write_text(str(proc.pid))
    print(f"Application started (PID: {proc.pid})")
    print(f"Access at: http://localhost:{port}")


def cmd_stop():
    """Stop the CareerGuide application."""
    running, pid = _is_running()
    if not running:
        print("Application is not running.")
        return

    print(f"Stopping PID {pid}...")
    try:
        if platform.system() == "Windows":
            subprocess.run(["taskkill", "/F", "/PID", str(pid)], capture_output=True)
        else:
            os.kill(pid, signal.SIGTERM)
        PID_FILE.unlink(missing_ok=True)
        print("Application stopped.")
    except Exception as e:
        print(f"Error stopping application: {e}")


def cmd_status():
    """Show application status."""
    config = _load_config()
    host, port = _get_app_info(config)
    running, pid = _is_running()

    print("=" * 50)
    print("CareerGuide Application Status")
    print("=" * 50)
    print(f"Status: {'RUNNING' if running else 'STOPPED'}")
    if running:
        print(f"PID: {pid}")
        print(f"URL: http://localhost:{port}")
    print(f"Log file: {LOG_FILE}")
    print(f"PID file: {PID_FILE}")
    print()

    # AI info
    ollama_info = _check_ollama(config)
    print("AI Configuration:")
    print(f"  Provider: {ollama_info['provider']}")
    print(f"  Model: {ollama_info['model']}")
    print(f"  Base URL: {ollama_info['base_url']}")
    print(f"  Connection: {ollama_info['status']}")
    if ollama_info.get("error"):
        print(f"  Error: {ollama_info['error']}")
    if ollama_info.get("available_models"):
        print(f"  Available Models: {', '.join(ollama_info['available_models'][:5])}")
    print()

    # App config
    app_conf = config.get("app", {})
    print("Application Configuration:")
    print(f"  Name: {app_conf.get('name', 'CareerGuide')}")
    print(f"  Version: {app_conf.get('version', '0.1.0')}")
    print(f"  Host: {host}")
    print(f"  Port: {port}")
    print(f"  Debug: {app_conf.get('debug', False)}")
    print()

    # DB config
    db_conf = config.get("persistence", {})
    print(f"Database: {db_conf.get('db_url', 'sqlite+aiosqlite:///./careerguide.db')}")
    print("=" * 50)


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)

    cmd = sys.argv[1].lower()
    if cmd == "start":
        cmd_start()
    elif cmd == "stop":
        cmd_stop()
    elif cmd == "status":
        cmd_status()
    else:
        print(f"Unknown command: {cmd}")
        print(__doc__)
        sys.exit(1)


if __name__ == "__main__":
    main()
