import subprocess

# Option A: Restart Docker container
subprocess.run(["docker", "restart", "test-app"])
# Option B: Restart systemd service
# subprocess.run(["sudo", "systemctl", "restart", "your-service-name"])

print("✅ Remediation: Restarted container/service.")
