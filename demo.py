from daytona_sdk import Daytona, DaytonaConfig, CreateSandboxParams, SandboxResources, SandboxTargetRegion, CodeLanguage
from dotenv import load_dotenv
import os

load_dotenv()


# Initial connection
daytona = Daytona(
    config=DaytonaConfig(
        organization_id=os.getenv("DAYTONA_ORGANIZATION_ID"),
        api_key=os.getenv("DAYTONA_API_KEY"),
        api_url=os.getenv("DAYTONA_API_URL"),
        jwt_token=None,
        target=SandboxTargetRegion.US,
    )
)


# Create sandbox
sandbox = daytona.create(
    params=CreateSandboxParams(
        language=CodeLanguage.PYTHON,
        # image="daytonaio/workspace-project:v0.46.0",
        name="demo-daytona",
        os_user="paul",
        env_vars={
            # "DEBUG": "true",
            # "NODE_ENV": "development",
            # "YOUR_ENVIRONMENT": os.getenv("YOUR_ENVIRONMENT")
        },
        labels={
            "project": "demo-daytona",
            # "environment": "development",
            # "owner": "paulpham157",
            # "purpose": "testing",
            # "department": "devops",
            # "version": "0.1",
        },
        public=False,
        target=SandboxTargetRegion.US,
        auto_stop_interval = 0,
        # command="sudo apt update && sudo apt install -y build-essential checkinstall zlib1g-dev libssl-dev cmake",
    ),
    timeout=50.0
)


# # Get sandbox informations
# sandbox_info = sandbox.instance.info
# print(f"Sandbox informations:\n${sandbox_info}\n")

# # Clone git
# sandbox_root_dir = sandbox.get_user_root_dir()
# sandbox.git.clone(
#     url="https://github.com/mindverse/Second-Me.git",
#     path=sandbox_root_dir,
#     branch="master"
# )
# command = f"""cd {sandbox_root_dir} && make docker-up"""
# response = sandbox.process.exec(command)
# print(response.result)
# preview_info = sandbox.get_preview_link(3000)

# print(f"Preview link url: {preview_info.url}")
# print(f"Preview link token: {preview_info.token}")

# Remove sandbox
# daytona.remove(sandbox)