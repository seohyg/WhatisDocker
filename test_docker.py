import os
import platform
import socket

def get_container_id():
    try:
        with open('/proc/self/cgroup', 'r') as f:
            for line in f:
                if 'docker' in line:
                    return line.split('/')[-1].strip()
    except FileNotFoundError:
        return "Not in a Docker container"

print("=== System Information ===")
print(f"Operating System: {platform.system()}")
print(f"OS Version: {platform.version()}")
print(f"Architecture: {platform.machine()}")
print(f"Python Version: {platform.python_version()}")
print(f"Hostname: {socket.gethostname()}")
print(f"Container ID: {get_container_id()}")
print(f"Current Working Directory: {os.getcwd()}")

print("\n=== Environment Variables ===")
for key, value in os.environ.items():
    print(f"{key}: {value}")

# 파일 생성 테스트
test_file = '/tmp/docker_test.txt'
try:
    with open(test_file, 'w') as f:
        f.write("Docker test successful!")
    print(f"\nSuccessfully created file: {test_file}")
except Exception as e:
    print(f"\nFailed to create file: {e}")

# 추가: Docker 환경 확인
print("\n=== Docker Environment Check ===")
if os.path.exists('/.dockerenv'):
    print("This is running inside a Docker container!")
else:
    print("This is not running in a Docker container.")

# 추가: Docker-specific 환경 변수 확인
docker_env_var = os.environ.get('DOCKER_ENV_TEST')
if docker_env_var:
    print(f"Docker-specific environment variable found: DOCKER_ENV_TEST = {docker_env_var}")
else:
    print("No Docker-specific environment variable found.")