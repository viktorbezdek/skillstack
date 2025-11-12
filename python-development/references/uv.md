# Uv - Uv

**Pages:** 63

---

## CLI Reference

**URL:** https://docs.astral.sh/uv/reference/cli/

**Contents:**
- CLI Reference
- uv
  - Usage
  - Commands
- uv auth
  - Usage
  - Commands
  - uv auth login
  - Usage
  - Arguments

An extremely fast Python package manager.

Manage authentication

Run a command or script

Add dependencies to the project

Remove dependencies from the project

Read or update the project's version

Update the project's environment

Update the project's lockfile

Export the project's lockfile to an alternate format

Display the project's dependency tree

Format Python code in the project

Run and install commands provided by Python packages

Manage Python versions and installations

Manage Python packages with a pip-compatible interface

Create a virtual environment

Build Python packages into source distributions and wheels

Upload distributions to an index

Manage the uv executable

Display documentation for a command

Manage authentication

Show the authentication token for a service

Show the path to the uv credentials directory

The domain or URL of the service to log into

Allow insecure connections to a host.

Can be provided multiple times.

Expects to receive either a hostname (e.g., localhost), a host-port pair (e.g., localhost:8080), or a URL (e.g., https://localhost).

WARNING: Hosts included in this list will not be verified against the system's certificate store. Only use --allow-insecure-host in a secure network with verified sources, as it bypasses SSL verification and could expose you to MITM attacks.

May also be set with the UV_INSECURE_HOST environment variable.

Path to the cache directory.

Defaults to $XDG_CACHE_HOME/uv or $HOME/.cache/uv on macOS and Linux, and %LOCALAPPDATA%\uv\cache on Windows.

To view the location of the cache directory, run uv cache dir.

May also be set with the UV_CACHE_DIR environment variable.

Control the use of color in output.

By default, uv will automatically detect support for colors when writing to a terminal.

The path to a uv.toml file to use for configuration.

While uv configuration can be included in a pyproject.toml file, it is not allowed in this context.

May also be set with the UV_CONFIG_FILE environment variable.

Change to the given directory prior to running the command.

Relative paths are resolved with the given directory as the base.

See --project to only change the project root directory.

May also be set with the UV_WORKING_DIRECTORY environment variable.

Display the concise help for this command

The keyring provider to use for storage of credentials.

Only --keyring-provider native is supported for login, which uses the system keyring via an integration built into uv.

May also

*[Content truncated]*

**Examples:**

Example 1 (unknown):
```unknown
uv [OPTIONS] <COMMAND>
```

Example 2 (unknown):
```unknown
uv auth [OPTIONS] <COMMAND>
```

Example 3 (unknown):
```unknown
uv auth login [OPTIONS] <SERVICE>
```

Example 4 (unknown):
```unknown
uv auth logout [OPTIONS] <SERVICE>
```

---

## Installing uv

**URL:** https://docs.astral.sh/uv/getting-started/installation/

**Contents:**
- Installing uv
- Installation methods
  - Standalone installer
  - PyPI
  - Homebrew
  - WinGet
  - Scoop
  - Docker
  - GitHub Releases
  - Cargo

Install uv with our standalone installers or your package manager of choice.

uv provides a standalone installer to download and install uv:

Use curl to download the script and execute it with sh:

If your system doesn't have curl, you can use wget:

Request a specific version by including it in the URL:

Use irm to download the script and execute it with iex:

Changing the execution policy allows running a script from the internet.

Request a specific version by including it in the URL:

The installation script may be inspected before use:

Alternatively, the installer or binaries can be downloaded directly from GitHub.

See the reference documentation on the installer for details on customizing your uv installation.

For convenience, uv is published to PyPI.

If installing from PyPI, we recommend installing uv into an isolated environment, e.g., with pipx:

However, pip can also be used:

uv ships with prebuilt distributions (wheels) for many platforms; if a wheel is not available for a given platform, uv will be built from source, which requires a Rust toolchain. See the contributing setup guide for details on building uv from source.

uv is available in the core Homebrew packages.

uv is available via WinGet.

uv is available via Scoop.

uv provides a Docker image at ghcr.io/astral-sh/uv.

See our guide on using uv in Docker for more details.

uv release artifacts can be downloaded directly from GitHub Releases.

Each release page includes binaries for all supported platforms as well as instructions for using the standalone installer via github.com instead of astral.sh.

uv is available via Cargo, but must be built from Git rather than crates.io due to its dependency on unpublished crates.

This method builds uv from source, which requires a compatible Rust toolchain.

When uv is installed via the standalone installer, it can update itself on-demand:

Updating uv will re-run the installer and can modify your shell profiles. To disable this behavior, set UV_NO_MODIFY_PATH=1.

When another installation method is used, self-updates are disabled. Use the package manager's upgrade method instead. For example, with pip:

You can run echo $SHELL to help you determine your shell.

To enable shell autocompletion for uv commands, run one of the following:

To enable shell autocompletion for uvx, run one of the following:

Then restart the shell or source the shell config file.

If you need to remove uv from your system, follow these steps:

Clean up stored data

*[Content truncated]*

**Examples:**

Example 1 (unknown):
```unknown
$ curl -LsSf https://astral.sh/uv/install.sh | sh
```

Example 2 (unknown):
```unknown
$ wget -qO- https://astral.sh/uv/install.sh | sh
```

Example 3 (unknown):
```unknown
$ curl -LsSf https://astral.sh/uv/0.9.5/install.sh | sh
```

Example 4 (unknown):
```unknown
PS> powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

---

## Configuring projects

**URL:** https://docs.astral.sh/uv/concepts/projects/config/

**Contents:**
- Configuring projects
- Python version requirement
- Entry points
  - Command-line interfaces
  - Graphical user interfaces
  - Plugin entry points
- Build systems
- Project packaging
- Project environment path
- Build isolation

Projects may declare the Python versions supported by the project in the project.requires-python field of the pyproject.toml.

It is recommended to set a requires-python value:

The Python version requirement determines the Python syntax that is allowed in the project and affects selection of dependency versions (they must support the same Python version range).

Entry points are the official term for an installed package to advertise interfaces. These include:

Using the entry point tables requires a build system to be defined.

Projects may define command line interfaces (CLIs) for the project in the [project.scripts] table of the pyproject.toml.

For example, to declare a command called hello that invokes the hello function in the example module:

Then, the command can be run from a console:

Projects may define graphical user interfaces (GUIs) for the project in the [project.gui-scripts] table of the pyproject.toml.

These are only different from command-line interfaces on Windows, where they are wrapped by a GUI executable so they can be started without a console. On other platforms, they behave the same.

For example, to declare a command called hello that invokes the app function in the example module:

Projects may define entry points for plugin discovery in the [project.entry-points] table of the pyproject.toml.

For example, to register the example-plugin-a package as a plugin for example:

Then, in example, plugins would be loaded with:

The group key can be an arbitrary value, it does not need to include the package name or "plugins". However, it is recommended to namespace the key by the package name to avoid collisions with other packages.

A build system determines how the project should be packaged and installed. Projects may declare and configure a build system in the [build-system] table of the pyproject.toml.

uv uses the presence of a build system to determine if a project contains a package that should be installed in the project virtual environment. If a build system is not defined, uv will not attempt to build or install the project itself, just its dependencies. If a build system is defined, uv will build and install the project into the project environment.

The --build-backend option can be provided to uv init to create a packaged project with an appropriate layout. The --package option can be provided to uv init to create a packaged project with the default build system.

While uv will not build and install the current project wi

*[Content truncated]*

**Examples:**

Example 1 (unknown):
```unknown
[project]
name = "example"
version = "0.1.0"
requires-python = ">=3.12"
```

Example 2 (unknown):
```unknown
[project.scripts]
hello = "example:hello"
```

Example 3 (unknown):
```unknown
$ uv run hello
```

Example 4 (unknown):
```unknown
[project.gui-scripts]
hello = "example:app"
```

---

## The uv auth CLI

**URL:** https://docs.astral.sh/uv/concepts/authentication/cli/

**Contents:**
- The uv auth CLI
- Logging in to a service
- Logging out of a service
- Showing credentials for a service
- Configuring the storage backend

uv provides a high-level interface for storing and retrieving credentials from services.

To add credentials for service, use the uv auth login command:

This will prompt for the credentials.

The credentials can also be provided using the --username and --password options, or the --token option for services which use a __token__ or arbitrary username.

We recommend providing the secret via stdin. Use - to indicate the value should be read from stdin, e.g., for --password:

The same pattern can be used with --token.

Once credentials are added, uv will use them for packaging operations that require fetching content from the given service. At this time, only HTTPS Basic authentication is supported. The credentials will not yet be used for Git requests.

The credentials will not be validated, i.e., incorrect credentials will not fail.

To remove credentials, use the uv auth logout command:

The credentials will not be invalidated with the remote server, i.e., they will only be removed from local storage not rendered unusable.

To show the credential stored for a given URL, use the uv auth token command:

If a username was used to log in, it will need to be provided as well, e.g.:

Credentials are persisted to the uv credentials store.

By default, credentials are written to a plaintext file. An encrypted system-native storage backend can be enabled with UV_PREVIEW_FEATURES=native-auth.

**Examples:**

Example 1 (unknown):
```unknown
$ uv auth login example.com
```

Example 2 (unknown):
```unknown
$ echo 'my-password' | uv auth login example.com --password -
```

Example 3 (unknown):
```unknown
$ uv auth logout example.com
```

Example 4 (unknown):
```unknown
$ uv auth token example.com
```

---

## Troubleshooting build failures

**URL:** https://docs.astral.sh/uv/reference/troubleshooting/build-failures/

**Contents:**
- Troubleshooting build failures
- Recognizing a build failure
- Confirming that a build failure is specific to uv
- Why does uv build a package?
- Common build failures
  - Command is not found
  - Header or library is missing
  - Module is missing or cannot be imported
  - Old version of the package is built
  - Old Version of a build dependency is used

uv needs to build packages when there is not a compatible wheel (a pre-built distribution of the package) available. Building packages can fail for many reasons, some of which may be unrelated to uv itself.

An example build failure can be produced by trying to install and old version of numpy on a new, unsupported version of Python:

Notice that the error message is prefaced by "The build backend returned an error".

The build failure includes the [stderr] (and [stdout], if present) from the build backend that was used for the build. The error logs are not from uv itself.

The message following the ╰─▶ is a hint provided by uv, to help resolve common build failures. A hint will not be available for all build failures.

Build failures are usually related to your system and the build backend. It is rare that a build failure is specific to uv. You can confirm that the build failure is not related to uv by attempting to reproduce it with pip:

The --use-pep517 flag should be included with the pip install invocation to ensure the same build isolation behavior. uv always uses build isolation by default.

We also recommend including the --force-reinstall and --no-cache options when reproducing failures.

Since this build failure occurs in pip too, it is not likely to be a bug with uv.

If a build failure is reproducible with another installer, you should investigate upstream (in this example, numpy or setuptools), find a way to avoid building the package in the first place, or make the necessary adjustments to your system for the build to succeed.

When generating the cross-platform lockfile, uv needs to determine the dependencies of all packages, even those only installed on other platforms. uv tries to avoid package builds during resolution. It uses any wheel if exist for that version, then tries to find static metadata in the source distribution (mainly pyproject.toml with static project.version, project.dependencies and project.optional-dependencies or METADATA v2.2+). Only if all of that fails, it builds the package.

When installing, uv needs to have a wheel for the current platform for each package. If no matching wheel exists in the index, uv tries to build the source distribution.

You can check which wheels exist for a PyPI project under “Download Files”, e.g. https://pypi.org/project/numpy/2.1.1.md#files. Wheels with ...-py3-none-any.whl filenames work everywhere, others have the operating system and platform in the filename. In the linked numpy examp

*[Content truncated]*

**Examples:**

Example 1 (python):
```python
$ uv pip install -p 3.13 'numpy<1.20'
Resolved 1 package in 62ms
  × Failed to build `numpy==1.19.5`
  ├─▶ The build backend returned an error
  ╰─▶ Call to `setuptools.build_meta:__legacy__.build_wheel()` failed (exit status: 1)

      [stderr]
      Traceback (most recent call last):
        File "<string>", line 8, in <module>
          from setuptools.build_meta import __legacy__ as backend
        File "/home/konsti/.cache/uv/builds-v0/.tmpi4bgKb/lib/python3.13/site-packages/setuptools/__init__.py", line 9, in <module>
          import distutils.core
      ModuleNotFoundError: No module n
...
```

Example 2 (unknown):
```unknown
$ uv venv -p 3.13 --seed
$ source .venv/bin/activate
$ pip install --use-pep517 --no-cache --force-reinstall 'numpy==1.19.5'
Collecting numpy==1.19.5
  Using cached numpy-1.19.5.zip (7.3 MB)
  Installing build dependencies ... done
  Getting requirements to build wheel ... done
ERROR: Exception:
Traceback (most recent call last):
  ...
  File "/Users/example/.cache/uv/archive-v0/3783IbOdglemN3ieOULx2/lib/python3.13/site-packages/pip/_vendor/pyproject_hooks/_impl.py", line 321, in _call_hook
    raise BackendUnavailable(data.get('traceback', ''))
pip._vendor.pyproject_hooks._impl.BackendUnavail
...
```

Example 3 (unknown):
```unknown
× Failed to build `pysha3==1.0.2`
├─▶ The build backend returned an error
╰─▶ Call to `setuptools.build_meta:__legacy__.build_wheel` failed (exit status: 1)

    [stdout]
    running bdist_wheel
    running build
    running build_py
    creating build/lib.linux-x86_64-cpython-310
    copying sha3.py -> build/lib.linux-x86_64-cpython-310
    running build_ext
    building '_pysha3' extension
    creating build/temp.linux-x86_64-cpython-310/Modules/_sha3
    gcc -Wno-unused-result -Wsign-compare -DNDEBUG -g -fwrapv -O3 -Wall -fPIC -DPY_WITH_KECCAK=1 -I/root/.cache/uv/builds-v0/.tmp8V4iEk/includ
...
```

Example 4 (unknown):
```unknown
$ apt install gcc
```

---

## Using uv in pre-commit

**URL:** https://docs.astral.sh/uv/guides/integration/pre-commit/

**Contents:**
- Using uv in pre-commit

An official pre-commit hook is provided at astral-sh/uv-pre-commit.

To use uv with pre-commit, add one of the following examples to the repos list in the .pre-commit-config.yaml.

To make sure your uv.lock file is up to date even if your pyproject.toml file was changed:

To keep a requirements.txt file in sync with your uv.lock file:

To compile requirements files:

To compile alternative requirements files, modify args and files:

To run the hook over multiple files at the same time, add additional entries:

**Examples:**

Example 1 (unknown):
```unknown
repos:
  - repo: https://github.com/astral-sh/uv-pre-commit
    # uv version.
    rev: 0.9.5
    hooks:
      - id: uv-lock
```

Example 2 (unknown):
```unknown
repos:
  - repo: https://github.com/astral-sh/uv-pre-commit
    # uv version.
    rev: 0.9.5
    hooks:
      - id: uv-export
```

Example 3 (unknown):
```unknown
repos:
  - repo: https://github.com/astral-sh/uv-pre-commit
    # uv version.
    rev: 0.9.5
    hooks:
      # Compile requirements
      - id: pip-compile
        args: [requirements.in, -o, requirements.txt]
```

Example 4 (unknown):
```unknown
repos:
  - repo: https://github.com/astral-sh/uv-pre-commit
    # uv version.
    rev: 0.9.5
    hooks:
      # Compile requirements
      - id: pip-compile
        args: [requirements-dev.in, -o, requirements-dev.txt]
        files: ^requirements-dev\.(in|txt)$
```

---

## Reproducible examples

**URL:** https://docs.astral.sh/uv/reference/troubleshooting/reproducible-examples/

**Contents:**
- Reproducible examples
- Why reproducible examples are important
- How to write a reproducible example
- Strategies for reproducible examples
  - Docker image
  - Script
  - Git repository

A minimal reproducible example (MRE) is essential for fixing bugs. Without an example that can be used to reproduce the problem, a maintainer cannot debug it or test if it is fixed. If the example is not minimal, i.e., if it includes lots of content which is not related to the issue, it can take a maintainer much longer to identify the root cause of the problem.

When writing a reproducible example, the goal is to provide all the context necessary for someone else to reproduce your example. This includes:

To ensure your reproduction is minimal, remove as many dependencies, settings, and files as possible. Be sure to test your reproduction before sharing it. We recommend including verbose logs from your reproduction; they may differ on your machine in a critical way. Using a Gist can be helpful for very long logs.

Below, we'll cover several specific strategies for creating and sharing reproducible examples.

There's a great guide to the basics of creating MREs on Stack Overflow.

Writing a Docker image is often the best way to share a reproducible example because it is entirely self-contained. This means that the state from the reproducer's system does not affect the problem.

Using a Docker image is only feasible if the issue is reproducible on Linux. When using macOS, it's prudent to ensure your image is not reproducible on Linux but some bugs are specific to the operating system. While using Docker to run Windows containers is feasible, it's not commonplace. These sorts of bugs are expected to be reported as a script instead.

When writing a Docker MRE with uv, it's best to start with one of uv's Docker images. When doing so, be sure to pin to a specific version of uv.

While Docker images are isolated from the system, the build will use your system's architecture by default. When sharing a reproduction, you can explicitly set the platform to ensure a reproducer gets the expected behavior. uv publishes images for linux/amd64 (e.g., Intel or AMD) and linux/arm64 (e.g., Apple M Series or ARM)

Docker images are best for reproducing issues that can be constructed with commands, e.g.:

However, you can also write files into the image inline:

If you need to write many files, it's better to create and publish a Git repository. You can combine these approaches and include a Dockerfile in the repository.

When sharing a Docker reproduction, it's helpful to include the build logs. You can see more output from the build steps by disabling caching and the fancy 

*[Content truncated]*

**Examples:**

Example 1 (unknown):
```unknown
FROM ghcr.io/astral-sh/uv:0.5.24-debian-slim
```

Example 2 (unknown):
```unknown
FROM --platform=linux/amd64 ghcr.io/astral-sh/uv:0.5.24-debian-slim
```

Example 3 (unknown):
```unknown
FROM --platform=linux/amd64 ghcr.io/astral-sh/uv:0.5.24-debian-slim

RUN uv init /mre
WORKDIR /mre
RUN uv add pydantic
RUN uv sync
RUN uv run -v python -c "import pydantic"
```

Example 4 (unknown):
```unknown
FROM --platform=linux/amd64 ghcr.io/astral-sh/uv:0.5.24-debian-slim

COPY <<EOF /mre/pyproject.toml
[project]
name = "example"
version = "0.1.0"
description = "Add your description here"
readme = "README.md"
requires-python = ">=3.12"
dependencies = ["pydantic"]
EOF

WORKDIR /mre
RUN uv lock
```

---

## Using uv with Jupyter

**URL:** https://docs.astral.sh/uv/guides/integration/jupyter/

**Contents:**
- Using uv with Jupyter
- Using Jupyter within a project
  - Creating a kernel
  - Installing packages without a kernel
- Using Jupyter as a standalone tool
- Using Jupyter with a non-project environment
- Using Jupyter from VS Code

The Jupyter notebook is a popular tool for interactive computing, data analysis, and visualization. You can use Jupyter with uv in a few different ways, either to interact with a project, or as a standalone tool.

If you're working within a project, you can start a Jupyter server with access to the project's virtual environment via the following:

By default, jupyter lab will start the server at http://localhost:8888/lab.

Within a notebook, you can import your project's modules as you would in any other file in the project. For example, if your project depends on requests, import requests will import requests from the project's virtual environment.

If you're looking for read-only access to the project's virtual environment, then there's nothing more to it. However, if you need to install additional packages from within the notebook, there are a few extra details to consider.

If you need to install packages from within the notebook, we recommend creating a dedicated kernel for your project. Kernels enable the Jupyter server to run in one environment, with individual notebooks running in their own, separate environments.

In the context of uv, we can create a kernel for a project while installing Jupyter itself in an isolated environment, as in uv run --with jupyter jupyter lab. Creating a kernel for the project ensures that the notebook is hooked up to the correct environment, and that any packages installed from within the notebook are installed into the project's virtual environment.

To create a kernel, you'll need to install ipykernel as a development dependency:

Then, you can create the kernel for project with:

From there, start the server with:

When creating a notebook, select the project kernel from the dropdown. Then use !uv add pydantic to add pydantic to the project's dependencies, or !uv pip install pydantic to install pydantic into the project's virtual environment without persisting the change to the project pyproject.toml or uv.lock files. Either command will make import pydantic work within the notebook.

If you don't want to create a kernel, you can still install packages from within the notebook. However, there are a few caveats to consider.

Though uv run --with jupyter runs in an isolated environment, within the notebook itself, !uv add and related commands will modify the project's environment, even without a kernel.

For example, running !uv add pydantic from within a notebook will add pydantic to the project's dependencies and vi

*[Content truncated]*

**Examples:**

Example 1 (unknown):
```unknown
$ uv run --with jupyter jupyter lab
```

Example 2 (unknown):
```unknown
$ uv add --dev ipykernel
```

Example 3 (unknown):
```unknown
$ uv run ipython kernel install --user --env VIRTUAL_ENV $(pwd)/.venv --name=project
```

Example 4 (unknown):
```unknown
$ uv run --with jupyter jupyter lab
```

---

## Guides overview

**URL:** https://docs.astral.sh/uv/guides/

**Contents:**
- Guides overview

Check out one of the core guides to get started:

Or, explore the concept documentation for comprehensive breakdown of each feature.

---

## Preview features

**URL:** https://docs.astral.sh/uv/concepts/preview/

**Contents:**
- Preview features
- Enabling preview features
- Using preview features
- Available preview features
- Disabling preview features

uv includes opt-in preview features to provide an opportunity for community feedback and increase confidence that changes are a net-benefit before enabling them for everyone.

To enable all preview features, use the --preview flag:

Or, set the UV_PREVIEW environment variable:

To enable specific preview features, use the --preview-features flag:

The --preview-features flag can be repeated to enable multiple features:

Or, features can be provided in a comma separated list:

The UV_PREVIEW_FEATURES environment variable can be used similarly, e.g.:

For backwards compatibility, enabling preview features that do not exist will warn, but not error.

Often, preview features can be used without changing any preview settings if the behavior change is gated by some sort of user interaction, For example, while pylock.toml support is in preview, you can use uv pip install with a pylock.toml file without additional configuration because specifying the pylock.toml file indicates you want to use the feature. However, a warning will be displayed that the feature is in preview. The preview feature can be enabled to silence the warning.

Other preview features change behavior without changes to your use of uv. For example, when the python-upgrade feature is enabled, the default behavior of uv python install changes to allow uv to upgrade Python versions transparently. This feature requires enabling the preview flag for proper usage.

The following preview features are available:

The --no-preview option can be used to disable preview features.

**Examples:**

Example 1 (unknown):
```unknown
$ uv run --preview ...
```

Example 2 (unknown):
```unknown
$ UV_PREVIEW=1 uv run ...
```

Example 3 (unknown):
```unknown
$ uv run --preview-features foo ...
```

Example 4 (unknown):
```unknown
$ uv run --preview-features foo --preview-features bar ...
```

---

## Running commands in projects

**URL:** https://docs.astral.sh/uv/concepts/projects/run/

**Contents:**
- Running commands in projects
- Requesting additional dependencies
- Running scripts
- Legacy scripts on Windows
- Signal handling

When working on a project, it is installed into the virtual environment at .venv. This environment is isolated from the current shell by default, so invocations that require the project, e.g., python -c "import example", will fail. Instead, use uv run to run commands in the project environment:

When using run, uv will ensure that the project environment is up-to-date before running the given command.

The given command can be provided by the project environment or exist outside of it, e.g.:

Additional dependencies or different versions of dependencies can be requested per invocation.

The --with option is used to include a dependency for the invocation, e.g., to request a different version of httpx:

The requested version will be respected regardless of the project's requirements. For example, even if the project requires httpx==0.24.0, the output above would be the same.

Scripts that declare inline metadata are automatically executed in environments isolated from the project. See the scripts guide for more details.

For example, given a script:

The invocation uv run example.py would run isolated from the project with only the given dependencies listed.

Support is provided for legacy setuptools scripts. These types of scripts are additional files installed by setuptools in .venv\Scripts.

Currently only legacy scripts with the .ps1, .cmd, and .bat extensions are supported.

For example, below is an example running a Command Prompt script.

In addition, you don't need to specify the extension. uv will automatically look for files ending in .ps1, .cmd, and .bat in that order of execution on your behalf.

uv does not cede control of the process to the spawned command in order to provide better error messages on failure. Consequently, uv is responsible for forwarding some signals to the child process the requested command runs in.

On Unix systems, uv will forward SIGINT and SIGTERM to the child process. Since terminals send SIGINT to the foreground process group on Ctrl-C, uv will only forward a SIGINT to the child process if it is sent more than once or the child process group differs from uv's.

On Windows, these concepts do not apply and uv ignores Ctrl-C events, deferring handling to the child process so it can exit cleanly.

**Examples:**

Example 1 (unknown):
```unknown
$ uv run python -c "import example"
```

Example 2 (unknown):
```unknown
$ # Presuming the project provides `example-cli`
$ uv run example-cli foo

$ # Running a `bash` script that requires the project to be available
$ uv run bash scripts/foo.sh
```

Example 3 (unknown):
```unknown
$ uv run --with httpx==0.26.0 python -c "import httpx; print(httpx.__version__)"
0.26.0
$ uv run --with httpx==0.25.0 python -c "import httpx; print(httpx.__version__)"
0.25.0
```

Example 4 (unknown):
```unknown
# /// script
# dependencies = [
#   "httpx",
# ]
# ///

import httpx

resp = httpx.get("https://peps.python.org/api/peps.json")
data = resp.json()
print([(k, v["title"]) for k, v in data.items()][:10])
```

---

## The pip interface

**URL:** https://docs.astral.sh/uv/pip/

**Contents:**
- The pip interface

uv provides a drop-in replacement for common pip, pip-tools, and virtualenv commands. These commands work directly with the virtual environment, in contrast to uv's primary interfaces where the virtual environment is managed automatically. The uv pip interface exposes the speed and functionality of uv to power users and projects that are not ready to transition away from pip and pip-tools.

The following sections discuss the basics of using uv pip:

Please note these commands do not exactly implement the interfaces and behavior of the tools they are based on. The further you stray from common workflows, the more likely you are to encounter differences. Consult the pip-compatibility guide for details.

uv does not rely on or invoke pip. The pip interface is named as such to highlight its dedicated purpose of providing low-level commands that match pip's interface and to separate it from the rest of uv's commands which operate at a higher level of abstraction.

---

## Working on projects

**URL:** https://docs.astral.sh/uv/guides/projects/

**Contents:**
- Working on projects
- Creating a new project
- Project structure
  - pyproject.toml
  - .python-version
  - .venv
  - uv.lock
- Managing dependencies
- Viewing your version
- Running commands

uv supports managing Python projects, which define their dependencies in a pyproject.toml file.

You can create a new Python project using the uv init command:

Alternatively, you can initialize a project in the working directory:

uv will create the following files:

The main.py file contains a simple "Hello world" program. Try it out with uv run:

A project consists of a few important parts that work together and allow uv to manage your project. In addition to the files created by uv init, uv will create a virtual environment and uv.lock file in the root of your project the first time you run a project command, i.e., uv run, uv sync, or uv lock.

A complete listing would look like:

The pyproject.toml contains metadata about your project:

You'll use this file to specify dependencies, as well as details about the project such as its description or license. You can edit this file manually, or use commands like uv add and uv remove to manage your project from the terminal.

See the official pyproject.toml guide for more details on getting started with the pyproject.toml format.

You'll also use this file to specify uv configuration options in a [tool.uv] section.

The .python-version file contains the project's default Python version. This file tells uv which Python version to use when creating the project's virtual environment.

The .venv folder contains your project's virtual environment, a Python environment that is isolated from the rest of your system. This is where uv will install your project's dependencies.

See the project environment documentation for more details.

uv.lock is a cross-platform lockfile that contains exact information about your project's dependencies. Unlike the pyproject.toml which is used to specify the broad requirements of your project, the lockfile contains the exact resolved versions that are installed in the project environment. This file should be checked into version control, allowing for consistent and reproducible installations across machines.

uv.lock is a human-readable TOML file but is managed by uv and should not be edited manually.

See the lockfile documentation for more details.

You can add dependencies to your pyproject.toml with the uv add command. This will also update the lockfile and project environment:

You can also specify version constraints or alternative sources:

If you're migrating from a requirements.txt file, you can use uv add with the -r flag to add all dependencies from the file:

To remove a

*[Content truncated]*

**Examples:**

Example 1 (unknown):
```unknown
$ uv init hello-world
$ cd hello-world
```

Example 2 (unknown):
```unknown
$ mkdir hello-world
$ cd hello-world
$ uv init
```

Example 3 (unknown):
```unknown
├── .gitignore
├── .python-version
├── README.md
├── main.py
└── pyproject.toml
```

Example 4 (unknown):
```unknown
$ uv run main.py
Hello from hello-world!
```

---

## Creating projects

**URL:** https://docs.astral.sh/uv/concepts/projects/init/

**Contents:**
- Creating projects
- Target directory
- Applications
- Packaged applications
- Libraries
- Projects with extension modules
- Creating a minimal project

uv supports creating a project with uv init.

When creating projects, uv supports two basic templates: applications and libraries. By default, uv will create a project for an application. The --lib flag can be used to create a project for a library instead.

uv will create a project in the working directory, or, in a target directory by providing a name, e.g., uv init foo. If there's already a project in the target directory, i.e., if there's a pyproject.toml, uv will exit with an error.

Application projects are suitable for web servers, scripts, and command-line interfaces.

Applications are the default target for uv init, but can also be specified with the --app flag.

The project includes a pyproject.toml, a sample file (main.py), a readme, and a Python version pin file (.python-version).

Prior to v0.6.0, uv created a file named hello.py instead of main.py.

The pyproject.toml includes basic metadata. It does not include a build system, it is not a package and will not be installed into the environment:

The sample file defines a main function with some standard boilerplate:

Python files can be executed with uv run:

Many use-cases require a package. For example, if you are creating a command-line interface that will be published to PyPI or if you want to define tests in a dedicated directory.

The --package flag can be used to create a packaged application:

The source code is moved into a src directory with a module directory and an __init__.py file:

A build system is defined, so the project will be installed into the environment:

The --build-backend option can be used to request an alternative build system.

A command definition is included:

The command can be executed with uv run:

A library provides functions and objects for other projects to consume. Libraries are intended to be built and distributed, e.g., by uploading them to PyPI.

Libraries can be created by using the --lib flag:

Using --lib implies --package. Libraries always require a packaged project.

As with a packaged application, a src layout is used. A py.typed marker is included to indicate to consumers that types can be read from the library:

A src layout is particularly valuable when developing libraries. It ensures that the library is isolated from any python invocations in the project root and that distributed library code is well separated from the rest of the project source.

A build system is defined, so the project will be installed into the environment:

You can selec

*[Content truncated]*

**Examples:**

Example 1 (unknown):
```unknown
$ uv init example-app
```

Example 2 (unknown):
```unknown
$ tree example-app
example-app
├── .python-version
├── README.md
├── main.py
└── pyproject.toml
```

Example 3 (unknown):
```unknown
[project]
name = "example-app"
version = "0.1.0"
description = "Add your description here"
readme = "README.md"
requires-python = ">=3.11"
dependencies = []
```

Example 4 (python):
```python
def main():
    print("Hello from example-app!")


if __name__ == "__main__":
    main()
```

---

## Concepts overview

**URL:** https://docs.astral.sh/uv/concepts/

**Contents:**
- Concepts overview

Read the concept documents to learn more about uv's features:

Looking for a quick introduction to features? See the guides instead.

---

## HTTP credentials

**URL:** https://docs.astral.sh/uv/concepts/authentication/http/

**Contents:**
- HTTP credentials
- netrc files
- The uv credentials store
- Keyring providers
- Persistence of credentials
- Learn more

uv supports credentials over HTTP when querying package registries.

Authentication can come from the following sources, in order of precedence:

Authentication may be used for hosts specified in the following contexts:

.netrc files are a long-standing plain text format for storing credentials on a system.

Reading credentials from .netrc files is always enabled. The target file path will be loaded from the NETRC environment variable if defined, falling back to ~/.netrc if not.

uv can read and write credentials from a store using the uv auth commands.

Credentials are stored in a plaintext file in uv's state directory, e.g., ~/.local/share/uv/credentials/credentials.toml on Unix. This file is currently not intended to be edited manually.

A secure, system native storage mechanism is in preview — it is still experimental and being actively developed. In the future, this will become the default storage mechanism.

When enabled, uv will use the secret storage mechanism native to your operating system. On macOS, it uses the Keychain Services. On Windows, it uses the Windows Credential Manager. On Linux, it uses the DBus-based Secret Service API.

Currently, uv only searches the native store for credentials it has added to the secret store — it will not retrieve credentials persisted by other applications.

Set UV_PREVIEW_FEATURES=native-auth to use this storage mechanism.

A keyring provider is a concept from pip allowing retrieval of credentials from an interface matching the popular keyring Python package.

The "subprocess" keyring provider invokes the keyring command to fetch credentials. uv does not support additional keyring provider types at this time.

Set --keyring-provider subprocess, UV_KEYRING_PROVIDER=subprocess, or tool.uv.keyring-provider = "subprocess" to use the provider.

If authentication is found for a single index URL or net location (scheme, host, and port), it will be cached for the duration of the command and used for other queries to that index or net location. Authentication is not cached across invocations of uv.

When using uv add, uv will not persist index credentials to the pyproject.toml or uv.lock. These files are often included in source control and distributions, so it is generally unsafe to include credentials in them. However, uv will persist credentials for direct URLs, i.e., package @ https://username:password:example.com/foo.whl, as there is not currently a way to otherwise provide those credentials.

If credentials were

*[Content truncated]*

---

## Using uv with marimo

**URL:** https://docs.astral.sh/uv/guides/integration/marimo/

**Contents:**
- Using uv with marimo
- Using marimo as a standalone tool
- Using marimo with inline script metadata
- Using marimo within a project
- Using marimo in a non-project environment
- Running marimo notebooks as scripts

marimo is an open-source Python notebook that blends interactive computing with the reproducibility and reusability of traditional software, letting you version with Git, run as scripts, and share as apps. Because marimo notebooks are stored as pure Python scripts, they are able to integrate tightly with uv.

You can readily use marimo as a standalone tool, as self-contained scripts, in projects, and in non-project environments.

For ad-hoc access to marimo notebooks, start a marimo server at any time in an isolated environment with:

Start a specific notebook with:

Because marimo notebooks are stored as Python scripts, they can encapsulate their own dependencies using inline script metadata, via uv's support for scripts. For example, to add numpy as a dependency to your notebook, use this command:

To interactively edit a notebook containing inline script metadata, use:

marimo will automatically use uv to start your notebook in an isolated virtual environment with your script's dependencies. Packages installed from the marimo UI will automatically be added to the notebook's script metadata.

You can optionally run these notebooks as Python scripts, without opening an interactive session:

If you're working within a project, you can start a marimo notebook with access to the project's virtual environment via the following command (assuming marimo is a project dependency):

To make additional packages available to your notebook, either add them to your project with uv add, or use marimo's built-in package installation UI, which will invoke uv add on your behalf.

If marimo is not a project dependency, you can still run a notebook with the following command:

This will let you import your project's modules while editing your notebook. However, packages installed via marimo's UI when running in this way will not be added to your project, and may disappear on subsequent marimo invocations.

To run marimo in a virtual environment that isn't associated with a project, add marimo to the environment directly:

From here, import numpy will work within the notebook, and marimo's UI installer will add packages to the environment with uv pip install on your behalf.

Regardless of how your dependencies are managed (with inline script metadata, within a project, or with a non-project environment), you can run marimo notebooks as scripts with:

This executes your notebook as a Python script, without opening an interactive session in your browser.

**Examples:**

Example 1 (unknown):
```unknown
$ uvx marimo edit
```

Example 2 (unknown):
```unknown
$ uvx marimo edit my_notebook.py
```

Example 3 (unknown):
```unknown
$ uv add --script my_notebook.py numpy
```

Example 4 (unknown):
```unknown
$ uvx marimo edit --sandbox my_notebook.py
```

---

## Using uv with Coiled

**URL:** https://docs.astral.sh/uv/guides/integration/coiled/

**Contents:**
- Using uv with Coiled
- Managing script dependencies with uv
- Running scripts on the cloud with Coiled

Coiled is a serverless, UX-focused cloud computing platform that makes it easy to run code on cloud hardware (AWS, GCP, and Azure).

This guide shows how to run Python scripts on the cloud using uv for dependency management and Coiled for cloud deployment.

We'll use this concrete example throughout this guide, but any Python script can be used with uv and Coiled.

We'll use the following script as an example:

The script uses pandas to load a Parquet file hosted in a public bucket on S3, then prints the first few rows. It uses inline script metadata to enumerate its dependencies.

When running this script locally, e.g., with:

uv will automatically create a virtual environment and installs its dependencies.

To learn more about using inline script metadata with uv, see the script guide.

Using inline script metadata makes the script fully self-contained: it includes the information that is needed to run it. This makes it easier to run on other machines, like a machine in the cloud.

There are many use cases where resources beyond what's available on a local workstation are needed, e.g.:

Coiled makes it simple to run code on cloud hardware.

First, authenticate with Coiled using coiled login :

You'll be prompted to create a Coiled account if you don't already have one — it's free to start using Coiled.

To instruct Coiled to run the script on a virtual machine on AWS, add two comments to the top:

While Coiled supports AWS, GCP, and Azure, this example assumes AWS is being used (see the region option above). If you're new to Coiled, you'll automatically have access to a free account running on AWS. If you're not running on AWS, you can either use a valid region for your cloud provider or remove the region line above.

The comments tell Coiled to use the official uv Docker image when running the script (ensuring uv is available) and to run in the us-east-2 region on AWS (where this example data file happens to live) to avoid any data egress.

To submit a batch job for Coiled to run, use coiled batch run to execute the uv run command in the cloud:

The same process that previously ran locally is now running on a remote cloud VM on AWS.

You can monitor the progress of the batch job in the UI at cloud.coiled.io or from the terminal using the coiled batch status, coiled batch wait, and coiled batch logs commands.

Note there's additional configuration we could have specified, e.g., the instance type (the default is a 4-core virtual machine with 16 GiB of mem

*[Content truncated]*

**Examples:**

Example 1 (unknown):
```unknown
# /// script
# requires-python = ">=3.12"
# dependencies = [
#   "pandas",
#   "pyarrow",
#   "s3fs",
# ]
# ///

import pandas as pd

df = pd.read_parquet(
    "s3://coiled-data/uber/part.0.parquet",
    storage_options={"anon": True},
)
print(df.head())
```

Example 2 (unknown):
```unknown
$ uv run process.py
```

Example 3 (unknown):
```unknown
$ uvx coiled login
```

Example 4 (unknown):
```unknown
# COILED container ghcr.io/astral-sh/uv:debian-slim
# COILED region us-east-2

# /// script
# requires-python = ">=3.12"
# dependencies = [
#   "pandas",
#   "pyarrow",
#   "s3fs",
# ]
# ///

import pandas as pd

df = pd.read_parquet(
    "s3://coiled-data/uber/part.0.parquet",
    storage_options={"anon": True},
)
print(df.head())
```

---

## Integration guides

**URL:** https://docs.astral.sh/uv/guides/integration/

**Contents:**
- Integration guides

Learn how to integrate uv with other software:

Or, explore the concept documentation for comprehensive breakdown of each feature.

---

## Features

**URL:** https://docs.astral.sh/uv/getting-started/features/

**Contents:**
- Features
- Python versions
- Scripts
- Projects
- Tools
- The pip interface
- Utility
- Next steps

uv provides essential features for Python development — from installing Python and hacking on simple scripts to working on large projects that support multiple Python versions and platforms.

uv's interface can be broken down into sections, which are usable independently or together.

Installing and managing Python itself.

See the guide on installing Python to get started.

Executing standalone Python scripts, e.g., example.py.

See the guide on running scripts to get started.

Creating and working on Python projects, i.e., with a pyproject.toml.

See the guide on projects to get started.

Running and installing tools published to Python package indexes, e.g., ruff or black.

See the guide on tools to get started.

Manually managing environments and packages — intended to be used in legacy workflows or cases where the high-level commands do not provide enough control.

Creating virtual environments (replacing venv and virtualenv):

See the documentation on using environments for details.

Managing packages in an environment (replacing pip and pipdeptree):

See the documentation on managing packages for details.

Locking packages in an environment (replacing pip-tools):

See the documentation on locking environments for details.

These commands do not exactly implement the interfaces and behavior of the tools they are based on. The further you stray from common workflows, the more likely you are to encounter differences. Consult the pip-compatibility guide for details.

Managing and inspecting uv's state, such as the cache, storage directories, or performing a self-update:

Read the guides for an introduction to each feature, check out the concept pages for in-depth details about uv's features, or learn how to get help if you run into any problems.

---

## Caching

**URL:** https://docs.astral.sh/uv/concepts/cache/

**Contents:**
- Caching
- Dependency caching
- Dynamic metadata
- Cache safety
- Clearing the cache
- Caching in continuous integration
- Cache directory
- Cache versioning

uv uses aggressive caching to avoid re-downloading (and re-building) dependencies that have already been accessed in prior runs.

The specifics of uv's caching semantics vary based on the nature of the dependency:

If you're running into caching issues, uv includes a few escape hatches:

As a special case, uv will always rebuild and reinstall any local directory dependencies passed explicitly on the command-line (e.g., uv pip install .).

By default, uv will only rebuild and reinstall local directory dependencies (e.g., editables) if the pyproject.toml, setup.py, or setup.cfg file in the directory root has changed, or if a src directory is added or removed. This is a heuristic and, in some cases, may lead to fewer re-installs than desired.

To incorporate additional information into the cache key for a given package, you can add cache key entries under tool.uv.cache-keys, which covers both file paths and Git commit hashes. Setting tool.uv.cache-keys will replace defaults, so any necessary files (like pyproject.toml) should still be included in the user-defined cache keys.

For example, if a project specifies dependencies in pyproject.toml but uses setuptools-scm to manage its version, and should thus be rebuilt whenever the commit hash or dependencies change, you can add the following to the project's pyproject.toml:

If your dynamic metadata incorporates information from the set of Git tags, you can expand the cache key to include the tags:

Similarly, if a project reads from a requirements.txt to populate its dependencies, you can add the following to the project's pyproject.toml:

Globs are supported for file keys, following the syntax of the glob crate. For example, to invalidate the cache whenever a .toml file in the project directory or any of its subdirectories is modified, use the following:

The use of globs can be expensive, as uv may need to walk the filesystem to determine whether any files have changed. This may, in turn, requiring traversal of large or deeply nested directories.

Similarly, if a project relies on an environment variable, you can add the following to the project's pyproject.toml to invalidate the cache whenever the environment variable changes:

Finally, to invalidate a project whenever a specific directory (like src) is created or removed, add the following to the project's pyproject.toml:

Note that the dir key will only track changes to the directory itself, and not arbitrary changes within the directory.

As an escape hatc

*[Content truncated]*

**Examples:**

Example 1 (unknown):
```unknown
[tool.uv]
cache-keys = [{ file = "pyproject.toml" }, { git = { commit = true } }]
```

Example 2 (unknown):
```unknown
[tool.uv]
cache-keys = [{ file = "pyproject.toml" }, { git = { commit = true, tags = true } }]
```

Example 3 (unknown):
```unknown
[tool.uv]
cache-keys = [{ file = "pyproject.toml" }, { file = "requirements.txt" }]
```

Example 4 (unknown):
```unknown
[tool.uv]
cache-keys = [{ file = "**/*.toml" }]
```

---

## Using Python environments

**URL:** https://docs.astral.sh/uv/pip/environments/

**Contents:**
- Using Python environments
- Creating a virtual environment
- Using a virtual environment
- Deactivating an environment
- Using arbitrary Python environments
- Discovery of Python environments

Each Python installation has an environment that is active when Python is used. Packages can be installed into an environment to make their modules available from your Python scripts. Generally, it is considered best practice not to modify a Python installation's environment. This is especially important for Python installations that come with the operating system which often manage the packages themselves. A virtual environment is a lightweight way to isolate packages from a Python installation's environment. Unlike pip, uv requires using a virtual environment by default.

uv supports creating virtual environments, e.g., to create a virtual environment at .venv:

A specific name or path can be specified, e.g., to create a virtual environment at my-name:

A Python version can be requested, e.g., to create a virtual environment with Python 3.11:

Note this requires the requested Python version to be available on the system. However, if unavailable, uv will download Python for you. See the Python version documentation for more details.

When using the default virtual environment name, uv will automatically find and use the virtual environment during subsequent invocations.

The virtual environment can be "activated" to make its packages available:

The default activation script on Unix is for POSIX compliant shells like sh, bash, or zsh. There are additional activation scripts for common alternative shells.

To exit a virtual environment, use the deactivate command:

Since uv has no dependency on Python, it can install into virtual environments other than its own. For example, setting VIRTUAL_ENV=/path/to/venv will cause uv to install into /path/to/venv, regardless of where uv is installed. Note that if VIRTUAL_ENV is set to a directory that is not a PEP 405 compliant virtual environment, it will be ignored.

uv can also install into arbitrary, even non-virtual environments, with the --python argument provided to uv pip sync or uv pip install. For example, uv pip install --python /path/to/python will install into the environment linked to the /path/to/python interpreter.

For convenience, uv pip install --system will install into the system Python environment. Using --system is roughly equivalent to uv pip install --python $(which python), but note that executables that are linked to virtual environments will be skipped. Although we generally recommend using virtual environments for dependency management, --system is appropriate in continuous integration and

*[Content truncated]*

**Examples:**

Example 1 (unknown):
```unknown
$ uv venv my-name
```

Example 2 (unknown):
```unknown
$ uv venv --python 3.11
```

Example 3 (unknown):
```unknown
$ uv venv

$ # Install a package in the new virtual environment
$ uv pip install ruff
```

Example 4 (unknown):
```unknown
$ source .venv/bin/activate
```

---

## Authentication

**URL:** https://docs.astral.sh/uv/concepts/authentication/

**Contents:**
- Authentication

Authentication is required when working with private repositories or package indexes.

Learn more about authentication in uv:

---

## Inspecting environments

**URL:** https://docs.astral.sh/uv/pip/inspection/

**Contents:**
- Inspecting environments
- Listing installed packages
- Inspecting a package
- Verifying an environment

To list all the packages in the environment:

To list the packages in a JSON format:

To list all the packages in the environment in a requirements.txt format:

To show information about an installed package, e.g., numpy:

Multiple packages can be inspected at once.

It is possible to install packages with conflicting requirements into an environment if installed in multiple steps.

To check for conflicts or missing dependencies in the environment:

**Examples:**

Example 1 (unknown):
```unknown
$ uv pip list
```

Example 2 (unknown):
```unknown
$ uv pip list --format json
```

Example 3 (unknown):
```unknown
$ uv pip freeze
```

Example 4 (unknown):
```unknown
$ uv pip show numpy
```

---

## Using tools

**URL:** https://docs.astral.sh/uv/guides/tools/

**Contents:**
- Using tools
- Running tools
- Commands with different package names
- Requesting specific versions
- Requesting extras
- Requesting different sources
- Commands with plugins
- Installing tools
- Upgrading tools
- Requesting Python versions

Many Python packages provide applications that can be used as tools. uv has specialized support for easily invoking and installing tools.

The uvx command invokes a tool without installing it.

For example, to run ruff:

This is exactly equivalent to:

uvx is provided as an alias for convenience.

Arguments can be provided after the tool name:

Tools are installed into temporary, isolated environments when using uvx.

If you are running a tool in a project and the tool requires that your project is installed, e.g., when using pytest or mypy, you'll want to use uv run instead of uvx. Otherwise, the tool will be run in a virtual environment that is isolated from your project.

If your project has a flat structure, e.g., instead of using a src directory for modules, the project itself does not need to be installed and uvx is fine. In this case, using uv run is only beneficial if you want to pin the version of the tool in the project's dependencies.

When uvx ruff is invoked, uv installs the ruff package which provides the ruff command. However, sometimes the package and command names differ.

The --from option can be used to invoke a command from a specific package, e.g., http which is provided by httpie:

To run a tool at a specific version, use command@<version>:

To run a tool at the latest version, use command@latest:

The --from option can also be used to specify package versions, as above:

Or, to constrain to a range of versions:

Note the @ syntax cannot be used for anything other than an exact version.

The --from option can be used to run a tool with extras:

This can also be combined with version selection:

The --from option can also be used to install from alternative sources.

For example, to pull from git:

You can also pull the latest commit from a specific named branch:

Or pull a specific tag:

Or even a specific commit:

Additional dependencies can be included, e.g., to include mkdocs-material when running mkdocs:

If a tool is used often, it is useful to install it to a persistent environment and add it to the PATH instead of invoking uvx repeatedly.

uvx is a convenient alias for uv tool run. All of the other commands for interacting with tools require the full uv tool prefix.

When a tool is installed, its executables are placed in a bin directory in the PATH which allows the tool to be run without uv. If it's not on the PATH, a warning will be displayed and uv tool update-shell can be used to add it to the PATH.

After installing ruff, 

*[Content truncated]*

**Examples:**

Example 1 (unknown):
```unknown
$ uv tool run ruff
```

Example 2 (unknown):
```unknown
$ uvx pycowsay hello from uv

  -------------
< hello from uv >
  -------------
   \   ^__^
    \  (oo)\_______
       (__)\       )\/\
           ||----w |
           ||     ||
```

Example 3 (unknown):
```unknown
$ uvx --from httpie http
```

Example 4 (unknown):
```unknown
$ uvx [email protected] check
```

---

## Project structure and files

**URL:** https://docs.astral.sh/uv/concepts/projects/layout/

**Contents:**
- Project structure and files
- The pyproject.toml
- The project environment
- The lockfile
  - Relationship to pylock.toml

Python project metadata is defined in a pyproject.toml file. uv requires this file to identify the root directory of a project.

uv init can be used to create a new project. See Creating projects for details.

A minimal project definition includes a name and version:

Additional project metadata and configuration includes:

When working on a project with uv, uv will create a virtual environment as needed. While some uv commands will create a temporary environment (e.g., uv run --isolated), uv also manages a persistent environment with the project and its dependencies in a .venv directory next to the pyproject.toml. It is stored inside the project to make it easy for editors to find — they need the environment to give code completions and type hints. It is not recommended to include the .venv directory in version control; it is automatically excluded from git with an internal .gitignore file.

To run a command in the project environment, use uv run. Alternatively the project environment can be activated as normal for a virtual environment.

When uv run is invoked, it will create the project environment if it does not exist yet or ensure it is up-to-date if it exists. The project environment can also be explicitly created with uv sync. See the locking and syncing documentation for details.

It is not recommended to modify the project environment manually, e.g., with uv pip install. For project dependencies, use uv add to add a package to the environment. For one-off requirements, use uvx or uv run --with.

If you don't want uv to manage the project environment, set managed = false to disable automatic locking and syncing of the project. For example:

uv creates a uv.lock file next to the pyproject.toml.

uv.lock is a universal or cross-platform lockfile that captures the packages that would be installed across all possible Python markers such as operating system, architecture, and Python version.

Unlike the pyproject.toml, which is used to specify the broad requirements of your project, the lockfile contains the exact resolved versions that are installed in the project environment. This file should be checked into version control, allowing for consistent and reproducible installations across machines.

A lockfile ensures that developers working on the project are using a consistent set of package versions. Additionally, it ensures when deploying the project as an application that the exact set of used package versions is known.

The lockfile is automaticall

*[Content truncated]*

**Examples:**

Example 1 (unknown):
```unknown
[project]
name = "example"
version = "0.1.0"
```

Example 2 (unknown):
```unknown
[tool.uv]
managed = false
```

---

## Managing dependencies

**URL:** https://docs.astral.sh/uv/concepts/projects/dependencies/

**Contents:**
- Managing dependencies
- Dependency fields
- Adding dependencies
  - Importing dependencies from requirements files
- Removing dependencies
- Changing dependencies
- Platform-specific dependencies
- Project dependencies
- Dependency sources
  - Index

Dependencies of the project are defined in several fields:

The project.dependencies and project.optional-dependencies fields can be used even if project isn't going to be published. dependency-groups are a recently standardized feature and may not be supported by all tools yet.

uv supports modifying the project's dependencies with uv add and uv remove, but dependency metadata can also be updated by editing the pyproject.toml directly.

An entry will be added in the project.dependencies field:

The --dev, --group, or --optional flags can be used to add dependencies to an alternative field.

The dependency will include a constraint, e.g., >=0.27.2, for the most recent, compatible version of the package. The kind of bound can be adjusted with --bounds, or the constraint can be provided directly:

When adding a dependency from a source other than a package registry, uv will add an entry in the sources field. For example, when adding httpx from GitHub:

The pyproject.toml will include a Git source entry:

If a dependency cannot be used, uv will display an error.:

Dependencies declared in a requirements.txt file can be added to the project with the -r option:

See the pip migration guide for more details.

To remove a dependency:

The --dev, --group, or --optional flags can be used to remove a dependency from a specific table.

If a source is defined for the removed dependency, and there are no other references to the dependency, it will also be removed.

To change an existing dependency, e.g., to use a different constraint for httpx:

In this example, we are changing the constraints for the dependency in the pyproject.toml. The locked version of the dependency will only change if necessary to satisfy the new constraints. To force the package version to update to the latest within the constraints, use --upgrade-package <name>, e.g.:

See the lockfile documentation for more details on upgrading packages.

Requesting a different dependency source will update the tool.uv.sources table, e.g., to use httpx from a local path during development:

To ensure that a dependency is only installed on a specific platform or on specific Python versions, use environment markers.

For example, to install jax on Linux, but not on Windows or macOS:

The resulting pyproject.toml will then include the environment marker in the dependency definition:

Similarly, to include numpy on Python 3.11 and later:

See Python's environment marker documentation for a complete enumeration of 

*[Content truncated]*

**Examples:**

Example 1 (unknown):
```unknown
$ uv add httpx
```

Example 2 (unknown):
```unknown
[project]
name = "example"
version = "0.1.0"
dependencies = ["httpx>=0.27.2"]
```

Example 3 (unknown):
```unknown
$ uv add "httpx>=0.20"
```

Example 4 (unknown):
```unknown
$ uv add "httpx @ git+https://github.com/encode/httpx"
```

---

## Locking and syncing

**URL:** https://docs.astral.sh/uv/concepts/projects/sync/

**Contents:**
- Locking and syncing
- Automatic lock and sync
- Checking the lockfile
- Creating the lockfile
- Syncing the environment
  - Editable installation
  - Retaining extraneous packages
  - Syncing optional dependencies
  - Syncing development dependencies
- Upgrading locked package versions

Locking is the process of resolving your project's dependencies into a lockfile. Syncing is the process of installing a subset of packages from the lockfile into the project environment.

Locking and syncing are automatic in uv. For example, when uv run is used, the project is locked and synced before invoking the requested command. This ensures the project environment is always up-to-date. Similarly, commands which read the lockfile, such as uv tree, will automatically update it before running.

To disable automatic locking, use the --locked option:

If the lockfile is not up-to-date, uv will raise an error instead of updating the lockfile.

To use the lockfile without checking if it is up-to-date, use the --frozen option:

Similarly, to run a command without checking if the environment is up-to-date, use the --no-sync option:

When considering if the lockfile is up-to-date, uv will check if it matches the project metadata. For example, if you add a dependency to your pyproject.toml, the lockfile will be considered outdated. Similarly, if you change the version constraints for a dependency such that the locked version is excluded, the lockfile will be considered outdated. However, if you change the version constraints such that the existing locked version is still included, the lockfile will still be considered up-to-date.

You can check if the lockfile is up-to-date by passing the --check flag to uv lock:

This is equivalent to the --locked flag for other commands.

uv will not consider lockfiles outdated when new versions of packages are released — the lockfile needs to be explicitly updated if you want to upgrade dependencies. See the documentation on upgrading locked package versions for details.

While the lockfile is created automatically, the lockfile may also be explicitly created or updated using uv lock:

While the environment is synced automatically, it may also be explicitly synced using uv sync:

Syncing the environment manually is especially useful for ensuring your editor has the correct versions of dependencies.

When the environment is synced, uv will install the project (and other workspace members) as editable packages, such that re-syncing is not necessary for changes to be reflected in the environment.

To opt-out of this behavior, use the --no-editable option.

If the project does not define a build system, it will not be installed. See the build systems documentation for details.

Syncing is "exact" by default, which means it will r

*[Content truncated]*

**Examples:**

Example 1 (unknown):
```unknown
$ uv run --locked ...
```

Example 2 (unknown):
```unknown
$ uv run --frozen ...
```

Example 3 (unknown):
```unknown
$ uv run --no-sync ...
```

Example 4 (unknown):
```unknown
$ uv lock --check
```

---

## Using uv with AWS Lambda

**URL:** https://docs.astral.sh/uv/guides/integration/aws-lambda/

**Contents:**
- Using uv with AWS Lambda
- Getting started
- Deploying a Docker image
  - Workspace support
- Deploying a zip archive
  - Using a Lambda layer

AWS Lambda is a serverless computing service that lets you run code without provisioning or managing servers.

You can use uv with AWS Lambda to manage your Python dependencies, build your deployment package, and deploy your Lambda functions.

Check out the uv-aws-lambda-example project for an example of best practices when using uv to deploy an application to AWS Lambda.

To start, assume we have a minimal FastAPI application with the following structure:

Where the pyproject.toml contains:

And the main.py file contains:

We can run this application locally with:

From there, opening http://127.0.0.1:8000/ in a web browser will display "Hello, world!"

To deploy to AWS Lambda, we need to build a container image that includes the application code and dependencies in a single output directory.

We'll follow the principles outlined in the Docker guide (in particular, a multi-stage build) to ensure that the final image is as small and cache-friendly as possible.

In the first stage, we'll populate a single directory with all application code and dependencies. In the second stage, we'll copy this directory over to the final image, omitting the build tools and other unnecessary files.

To deploy to ARM-based AWS Lambda runtimes, replace public.ecr.aws/lambda/python:3.13 with public.ecr.aws/lambda/python:3.13-arm64.

We can build the image with, e.g.:

The core benefits of this Dockerfile structure are as follows:

Concretely, rebuilding the image after modifying the application source code can reuse the cached layers, resulting in millisecond builds:

After building, we can push the image to Elastic Container Registry (ECR) with, e.g.:

Finally, we can deploy the image to AWS Lambda using the AWS Management Console or the AWS CLI, e.g.:

Where the execution role is created via:

Or, update an existing function with:

To test the Lambda, we can invoke it via the AWS Management Console or the AWS CLI, e.g.:

Where event.json contains the event payload to pass to the Lambda function:

And response.json contains the response from the Lambda function:

For details, see the AWS Lambda documentation.

If a project includes local dependencies (e.g., via Workspaces), those too must be included in the deployment package.

We'll start by extending the above example to include a dependency on a locally-developed library named library.

First, we'll create the library itself:

Running uv init within the project directory will automatically convert project to a workspace an

*[Content truncated]*

**Examples:**

Example 1 (unknown):
```unknown
project
├── pyproject.toml
└── app
    ├── __init__.py
    └── main.py
```

Example 2 (unknown):
```unknown
[project]
name = "uv-aws-lambda-example"
version = "0.1.0"
requires-python = ">=3.13"
dependencies = [
    # FastAPI is a modern web framework for building APIs with Python.
    "fastapi",
    # Mangum is a library that adapts ASGI applications to AWS Lambda and API Gateway.
    "mangum",
]

[dependency-groups]
dev = [
    # In development mode, include the FastAPI development server.
    "fastapi[standard]>=0.115",
]
```

Example 3 (python):
```python
import logging

from fastapi import FastAPI
from mangum import Mangum

logger = logging.getLogger()
logger.setLevel(logging.INFO)

app = FastAPI()
handler = Mangum(app)


@app.get("/")
async def root() -> str:
    return "Hello, world!"
```

Example 4 (unknown):
```unknown
$ uv run fastapi dev
```

---

## Tools

**URL:** https://docs.astral.sh/uv/concepts/tools/

**Contents:**
- Tools
- The uv tool interface
- Execution vs installation
- Tool environments
- Tool versions
- Tools directory
- Upgrading tools
- Including additional dependencies
- Installing executables from additional packages
- Python versions

Tools are Python packages that provide command-line interfaces.

See the tools guide for an introduction to working with the tools interface — this document discusses details of tool management.

uv includes a dedicated interface for interacting with tools. Tools can be invoked without installation using uv tool run, in which case their dependencies are installed in a temporary virtual environment isolated from the current project.

Because it is very common to run tools without installing them, a uvx alias is provided for uv tool run — the two commands are exactly equivalent. For brevity, the documentation will mostly refer to uvx instead of uv tool run.

Tools can also be installed with uv tool install, in which case their executables are available on the PATH — an isolated virtual environment is still used, but it is not removed when the command completes.

In most cases, executing a tool with uvx is more appropriate than installing the tool. Installing the tool is useful if you need the tool to be available to other programs on your system, e.g., if some script you do not control requires the tool, or if you are in a Docker image and want to make the tool available to users.

When running a tool with uvx, a virtual environment is stored in the uv cache directory and is treated as disposable, i.e., if you run uv cache clean the environment will be deleted. The environment is only cached to reduce the overhead of repeated invocations. If the environment is removed, a new one will be created automatically.

When installing a tool with uv tool install, a virtual environment is created in the uv tools directory. The environment will not be removed unless the tool is uninstalled. If the environment is manually deleted, the tool will fail to run.

Unless a specific version is requested, uv tool install will install the latest available of the requested tool. uvx will use the latest available version of the requested tool on the first invocation. After that, uvx will use the cached version of the tool unless a different version is requested, the cache is pruned, or the cache is refreshed.

For example, to run a specific version of Ruff:

A subsequent invocation of uvx will use the latest, not the cached, version.

But, if a new version of Ruff was released, it would not be used unless the cache was refreshed.

To request the latest version of Ruff and refresh the cache, use the @latest suffix:

Once a tool is installed with uv tool install, uvx will use the in

*[Content truncated]*

**Examples:**

Example 1 (unknown):
```unknown
$ uvx [email protected] --version
ruff 0.6.0
```

Example 2 (unknown):
```unknown
$ uvx ruff --version
ruff 0.6.2
```

Example 3 (unknown):
```unknown
$ uvx ruff@latest --version
0.6.2
```

Example 4 (unknown):
```unknown
$ uv tool install ruff==0.5.0
```

---

## Migrating from pip to a uv project

**URL:** https://docs.astral.sh/uv/guides/migration/pip-to-project/

**Contents:**
- Migrating from pip to a uv project
- Understanding pip workflows
  - Project dependencies
  - Requirements files
  - Development dependencies
  - Platform-specific dependencies
- Migrating to a uv project
  - The pyproject.toml
  - The uv lockfile
  - Importing requirements files

This guide will discuss converting from a pip and pip-tools workflow centered on requirements files to uv's project workflow using a pyproject.toml and uv.lock file.

If you're looking to migrate from pip and pip-tools to uv's drop-in interface or from an existing workflow where you're already using a pyproject.toml, those guides are not yet written. See #5200 to track progress.

We'll start with an overview of developing with pip, then discuss migrating to uv.

If you're familiar with the ecosystem, you can jump ahead to the requirements file import instructions.

When you want to use a package in your project, you need to install it first. pip supports imperative installation of packages, e.g.:

This installs the package into the environment that pip is installed in. This may be a virtual environment, or, the global environment of your system's Python installation.

Then, you can run a Python script that requires the package:

It's best practice to create a virtual environment for each project, to avoid mixing packages between them. For example:

We will revisit this topic in the project environments section below.

When sharing projects with others, it's useful to declare all the packages you require upfront. pip supports installing requirements from a file, e.g.:

Notice above that fastapi is not "locked" to a specific version — each person working on the project may have a different version of fastapi installed. pip-tools was created to improve this experience.

When using pip-tools, requirements files specify both the dependencies for your project and lock dependencies to a specific version — the file extension is used to differentiate between the two. For example, if you require fastapi and pydantic, you'd specify these in a requirements.in file:

Notice there's a version constraint on pydantic — this means only pydantic versions later than 2.0.0 can be used. In contrast, fastapi does not have a version constraint — any version can be used.

These dependencies can be compiled into a requirements.txt file:

Here, all the versions constraints are exact. Only a single version of each package can be used. The above example was generated with uv pip compile, but could also be generated with pip-compile from pip-tools.

Though less common, the requirements.txt can also be generated using pip freeze, by first installing the input dependencies into the environment then exporting the installed versions:

After compiling dependencies into a locked set of vers

*[Content truncated]*

**Examples:**

Example 1 (unknown):
```unknown
$ pip install fastapi
```

Example 2 (unknown):
```unknown
import fastapi
```

Example 3 (unknown):
```unknown
$ python -m venv
$ source .venv/bin/activate
$ pip ...
```

Example 4 (unknown):
```unknown
$ pip install -r requirements.txt
```

---

## Locking environments

**URL:** https://docs.astral.sh/uv/pip/compile/

**Contents:**
- Locking environments
- Locking requirements
- Upgrading requirements
- Syncing an environment
- Adding constraints
- Adding build constraints
- Overriding dependency versions

Locking is to take a dependency, e.g., ruff, and write an exact version to use to a file. When working with many dependencies, it is useful to lock the exact versions so the environment can be reproduced. Without locking, the versions of dependencies could change over time, when using a different tool, or across platforms.

uv allows dependencies to be locked in the requirements.txt format. It is recommended to use the standard pyproject.toml to define dependencies, but other dependency formats are supported as well. See the documentation on declaring dependencies for more details on how to define dependencies.

To lock dependencies declared in a pyproject.toml:

Note by default the uv pip compile output is just displayed and --output-file / -o argument is needed to write to a file.

To lock dependencies declared in a requirements.in:

To lock dependencies declared in multiple files:

uv also supports legacy setup.py and setup.cfg formats. To lock dependencies declared in a setup.py:

To lock dependencies from stdin, use -:

To lock with optional dependencies enabled, e.g., the "foo" extra:

To lock with all optional dependencies enabled:

Note extras are not supported with the requirements.in format.

To lock a dependency group in the current project directory's pyproject.toml, for example the group foo:

A --group flag has to be added to pip-tools' pip compile, although they're considering it. We expect to support whatever syntax and semantics they adopt.

To specify the project directory where groups should be sourced from:

Alternatively, you can specify a path to a pyproject.toml for each group:

--group flags do not apply to other specified sources. For instance, uv pip compile some/path/pyproject.toml --group foo sources foo from ./pyproject.toml and not some/path/pyproject.toml.

When using an output file, uv will consider the versions pinned in an existing output file. If a dependency is pinned it will not be upgraded on a subsequent compile run. For example:

To upgrade a dependency, use the --upgrade-package flag:

To upgrade all dependencies, there is an --upgrade flag.

Dependencies can be installed directly from their definition files or from compiled requirements.txt files with uv pip install. See the documentation on installing packages from files for more details.

When installing with uv pip install, packages that are already installed will not be removed unless they conflict with the lockfile. This means that the environment can have dep

*[Content truncated]*

**Examples:**

Example 1 (unknown):
```unknown
$ uv pip compile pyproject.toml -o requirements.txt
```

Example 2 (unknown):
```unknown
$ uv pip compile requirements.in -o requirements.txt
```

Example 3 (unknown):
```unknown
$ uv pip compile pyproject.toml requirements-dev.in -o requirements-dev.txt
```

Example 4 (unknown):
```unknown
$ uv pip compile setup.py -o requirements.txt
```

---

## Getting help

**URL:** https://docs.astral.sh/uv/getting-started/help/

**Contents:**
- Getting help
- Help menus
- Displaying verbose output
- Viewing the version
- Troubleshooting issues
- Open an issue on GitHub
- Chat on Discord

The --help flag can be used to view the help menu for a command, e.g., for uv:

To view the help menu for a specific command, e.g., for uv init:

When using the --help flag, uv displays a condensed help menu. To view a longer help menu for a command, use uv help:

To view the long help menu for a specific command, e.g., for uv init:

When using the long help menu, uv will attempt to use less or more to "page" the output so it is not all displayed at once. To exit the pager, press q.

The -v flag can be used to display verbose output for a command, e.g., for uv sync:

The -v flag can be repeated to increase verbosity, e.g.:

Often, the verbose output will include additional information about why uv is behaving in a certain way.

When seeking help, it's important to determine the version of uv that you're using — sometimes the problem is already solved in a newer version.

To check the installed version:

The following are also valid:

Before uv 0.7.0, uv version was used instead of uv self version.

The reference documentation contains a troubleshooting guide for common issues.

The issue tracker on GitHub is a good place to report bugs and request features. Make sure to search for similar issues first, as it is common for someone else to encounter the same problem.

Astral has a Discord server, which is a great place to ask questions, learn more about uv, and engage with other community members.

**Examples:**

Example 1 (unknown):
```unknown
$ uv --help
```

Example 2 (unknown):
```unknown
$ uv init --help
```

Example 3 (unknown):
```unknown
$ uv help init
```

Example 4 (unknown):
```unknown
$ uv sync -v
```

---

## Using uv in GitLab CI/CD

**URL:** https://docs.astral.sh/uv/guides/integration/gitlab/

**Contents:**
- Using uv in GitLab CI/CD
- Using the uv image
- Caching
- Using uv pip

Astral provides Docker images with uv preinstalled. Select a variant that is suitable for your workflow.

If you are using a distroless image, you have to specify the entrypoint: uv: image: name: ghcr.io/astral-sh/uv:$UV_VERSION entrypoint: [""] # ...

Persisting the uv cache between workflow runs can improve performance.

See the GitLab caching documentation for more details on configuring caching.

Using uv cache prune --ci at the end of the job is recommended to reduce cache size. See the uv cache documentation for more details.

If using the uv pip interface instead of the uv project interface, uv requires a virtual environment by default. To allow installing packages into the system environment, use the --system flag on all uv invocations or set the UV_SYSTEM_PYTHON variable.

The UV_SYSTEM_PYTHON variable can be defined in at different scopes. You can read more about how variables and their precedence works in GitLab here

Opt-in for the entire workflow by defining it at the top level:

To opt-out again, the --no-system flag can be used in any uv invocation.

When persisting the cache, you may want to use requirements.txt or pyproject.toml as your cache key files instead of uv.lock.

**Examples:**

Example 1 (unknown):
```unknown
variables:
  UV_VERSION: "0.5"
  PYTHON_VERSION: "3.12"
  BASE_LAYER: bookworm-slim
  # GitLab CI creates a separate mountpoint for the build directory,
  # so we need to copy instead of using hard links.
  UV_LINK_MODE: copy

uv:
  image: ghcr.io/astral-sh/uv:$UV_VERSION-python$PYTHON_VERSION-$BASE_LAYER
  script:
    # your `uv` commands
```

Example 2 (unknown):
```unknown
uv:
  image:
    name: ghcr.io/astral-sh/uv:$UV_VERSION
    entrypoint: [""]
  # ...
```

Example 3 (unknown):
```unknown
uv-install:
  variables:
    UV_CACHE_DIR: .uv-cache
  cache:
    - key:
        files:
          - uv.lock
      paths:
        - $UV_CACHE_DIR
  script:
    # Your `uv` commands
    - uv cache prune --ci
```

Example 4 (unknown):
```unknown
variables:
  UV_SYSTEM_PYTHON: 1

# [...]
```

---

## Managing packages

**URL:** https://docs.astral.sh/uv/pip/packages/

**Contents:**
- Managing packages
- Installing a package
- Editable packages
- Installing packages from files
- Uninstalling a package

To install a package into the virtual environment, e.g., Flask:

To install a package with optional dependencies enabled, e.g., Flask with the "dotenv" extra:

To install multiple packages, e.g., Flask and Ruff:

To install a package with a constraint, e.g., Ruff v0.2.0 or newer:

To install a package at a specific version, e.g., Ruff v0.3.0:

To install a package from the disk:

To install a package from GitHub:

To install a package from GitHub at a specific reference:

See the Git authentication documentation for installation from a private repository.

Editable packages do not need to be reinstalled for changes to their source code to be active.

To install the current project as an editable package

To install a project in another directory as an editable package:

Multiple packages can be installed at once from standard file formats.

Install from a requirements.txt file:

See the uv pip compile documentation for more information on requirements.txt files.

Install from a pyproject.toml file:

Install from a pyproject.toml file with optional dependencies enabled, e.g., the "foo" extra:

Install from a pyproject.toml file with all optional dependencies enabled:

To install dependency groups in the current project directory's pyproject.toml, for example the group foo:

To specify the project directory where groups should be sourced from:

Alternatively, you can specify a path to a pyproject.toml for each group:

As in pip, --group flags do not apply to other sources specified with flags like -r or -e. For instance, uv pip install -r some/path/pyproject.toml --group foo sources foo from ./pyproject.toml and not some/path/pyproject.toml.

To uninstall a package, e.g., Flask:

To uninstall multiple packages, e.g., Flask and Ruff:

**Examples:**

Example 1 (unknown):
```unknown
$ uv pip install flask
```

Example 2 (unknown):
```unknown
$ uv pip install "flask[dotenv]"
```

Example 3 (unknown):
```unknown
$ uv pip install flask ruff
```

Example 4 (unknown):
```unknown
$ uv pip install 'ruff>=0.2.0'
```

---

## Using uv with FastAPI

**URL:** https://docs.astral.sh/uv/guides/integration/fastapi/

**Contents:**
- Using uv with FastAPI
- Migrating an existing FastAPI project
- Deployment

FastAPI is a modern, high-performance Python web framework. You can use uv to manage your FastAPI project, including installing dependencies, managing environments, running FastAPI applications, and more.

You can view the source code for this guide in the uv-fastapi-example repository.

As an example, consider the sample application defined in the FastAPI documentation, structured as follows:

To use uv with this application, inside the project directory run:

This creates a project with an application layout and a pyproject.toml file.

Then, add a dependency on FastAPI:

You should now have the following structure:

And the contents of the pyproject.toml file should look something like this:

From there, you can run the FastAPI application with:

uv run will automatically resolve and lock the project dependencies (i.e., create a uv.lock alongside the pyproject.toml), create a virtual environment, and run the command in that environment.

Test the app by opening http://127.0.0.1:8000/?token=jessica in a web browser.

To deploy the FastAPI application with Docker, you can use the following Dockerfile:

Build the Docker image with:

Run the Docker container locally with:

Navigate to http://127.0.0.1:8000/?token=jessica in your browser to verify that the app is running correctly.

For more on using uv with Docker, see the Docker guide.

**Examples:**

Example 1 (unknown):
```unknown
project
└── app
    ├── __init__.py
    ├── main.py
    ├── dependencies.py
    ├── routers
    │   ├── __init__.py
    │   ├── items.py
    │   └── users.py
    └── internal
        ├── __init__.py
        └── admin.py
```

Example 2 (unknown):
```unknown
$ uv init --app
```

Example 3 (unknown):
```unknown
$ uv add fastapi --extra standard
```

Example 4 (unknown):
```unknown
project
├── pyproject.toml
└── app
    ├── __init__.py
    ├── main.py
    ├── dependencies.py
    ├── routers
    │   ├── __init__.py
    │   ├── items.py
    │   └── users.py
    └── internal
        ├── __init__.py
        └── admin.py
```

---

## Using workspaces

**URL:** https://docs.astral.sh/uv/concepts/projects/workspaces/

**Contents:**
- Using workspaces
- Getting started
- Workspace sources
- Workspace layouts
- When (not) to use workspaces

Inspired by the Cargo concept of the same name, a workspace is "a collection of one or more packages, called workspace members, that are managed together."

Workspaces organize large codebases by splitting them into multiple packages with common dependencies. Think: a FastAPI-based web application, alongside a series of libraries that are versioned and maintained as separate Python packages, all in the same Git repository.

In a workspace, each package defines its own pyproject.toml, but the workspace shares a single lockfile, ensuring that the workspace operates with a consistent set of dependencies.

As such, uv lock operates on the entire workspace at once, while uv run and uv sync operate on the workspace root by default, though both accept a --package argument, allowing you to run a command in a particular workspace member from any workspace directory.

To create a workspace, add a tool.uv.workspace table to a pyproject.toml, which will implicitly create a workspace rooted at that package.

By default, running uv init inside an existing package will add the newly created member to the workspace, creating a tool.uv.workspace table in the workspace root if it doesn't already exist.

In defining a workspace, you must specify the members (required) and exclude (optional) keys, which direct the workspace to include or exclude specific directories as members respectively, and accept lists of globs:

Every directory included by the members globs (and not excluded by the exclude globs) must contain a pyproject.toml file. However, workspace members can be either applications or libraries; both are supported in the workspace context.

Every workspace needs a root, which is also a workspace member. In the above example, albatross is the workspace root, and the workspace members include all projects under the packages directory, except seeds.

By default, uv run and uv sync operates on the workspace root. For example, in the above example, uv run and uv run --package albatross would be equivalent, while uv run --package bird-feeder would run the command in the bird-feeder package.

Within a workspace, dependencies on workspace members are facilitated via tool.uv.sources, as in:

In this example, the albatross project depends on the bird-feeder project, which is a member of the workspace. The workspace = true key-value pair in the tool.uv.sources table indicates the bird-feeder dependency should be provided by the workspace, rather than fetched from PyPI or anothe

*[Content truncated]*

**Examples:**

Example 1 (unknown):
```unknown
[project]
name = "albatross"
version = "0.1.0"
requires-python = ">=3.12"
dependencies = ["bird-feeder", "tqdm>=4,<5"]

[tool.uv.sources]
bird-feeder = { workspace = true }

[tool.uv.workspace]
members = ["packages/*"]
exclude = ["packages/seeds"]
```

Example 2 (unknown):
```unknown
[project]
name = "albatross"
version = "0.1.0"
requires-python = ">=3.12"
dependencies = ["bird-feeder", "tqdm>=4,<5"]

[tool.uv.sources]
bird-feeder = { workspace = true }

[tool.uv.workspace]
members = ["packages/*"]

[build-system]
requires = ["uv_build>=0.9.5,<0.10.0"]
build-backend = "uv_build"
```

Example 3 (unknown):
```unknown
[project]
name = "albatross"
version = "0.1.0"
requires-python = ">=3.12"
dependencies = ["bird-feeder", "tqdm>=4,<5"]

[tool.uv.sources]
bird-feeder = { workspace = true }
tqdm = { git = "https://github.com/tqdm/tqdm" }

[tool.uv.workspace]
members = ["packages/*"]

[build-system]
requires = ["uv_build>=0.9.5,<0.10.0"]
build-backend = "uv_build"
```

Example 4 (unknown):
```unknown
albatross
├── packages
│   ├── bird-feeder
│   │   ├── pyproject.toml
│   │   └── src
│   │       └── bird_feeder
│   │           ├── __init__.py
│   │           └── foo.py
│   └── seeds
│       ├── pyproject.toml
│       └── src
│           └── seeds
│               ├── __init__.py
│               └── bar.py
├── pyproject.toml
├── README.md
├── uv.lock
└── src
    └── albatross
        └── main.py
```

---

## Projects

**URL:** https://docs.astral.sh/uv/concepts/projects/

**Contents:**
- Projects

Projects help manage Python code spanning multiple files.

Looking for an introduction to creating a project with uv? See the projects guide first.

Working on projects is a core part of the uv experience. Learn more about using projects:

---

## TLS certificates

**URL:** https://docs.astral.sh/uv/concepts/authentication/certificates/

**Contents:**
- TLS certificates
- System certificates
- Custom certificates
- Insecure hosts

By default, uv loads certificates from the bundled webpki-roots crate. The webpki-roots are a reliable set of trust roots from Mozilla, and including them in uv improves portability and performance (especially on macOS, where reading the system trust store incurs a significant delay).

In some cases, you may want to use the platform's native certificate store, especially if you're relying on a corporate trust root (e.g., for a mandatory proxy) that's included in your system's certificate store. To instruct uv to use the system's trust store, run uv with the --native-tls command-line flag, or set the UV_NATIVE_TLS environment variable to true.

If a direct path to the certificate is required (e.g., in CI), set the SSL_CERT_FILE environment variable to the path of the certificate bundle, to instruct uv to use that file instead of the system's trust store.

If client certificate authentication (mTLS) is desired, set the SSL_CLIENT_CERT environment variable to the path of the PEM formatted file containing the certificate followed by the private key.

If you're using a setup in which you want to trust a self-signed certificate or otherwise disable certificate verification, you can instruct uv to allow insecure connections to dedicated hosts via the allow-insecure-host configuration option. For example, adding the following to pyproject.toml will allow insecure connections to example.com:

allow-insecure-host expects to receive a hostname (e.g., localhost) or hostname-port pair (e.g., localhost:8080), and is only applicable to HTTPS connections, as HTTP connections are inherently insecure.

Use allow-insecure-host with caution and only in trusted environments, as it can expose you to security risks due to the lack of certificate verification.

**Examples:**

Example 1 (unknown):
```unknown
[tool.uv]
allow-insecure-host = ["example.com"]
```

---

## Running scripts

**URL:** https://docs.astral.sh/uv/guides/scripts/

**Contents:**
- Running scripts
- Running a script without dependencies
- Running a script with dependencies
- Creating a Python script
- Declaring script dependencies
- Using a shebang to create an executable file
- Using alternative package indexes
- Locking dependencies
- Improving reproducibility
- Using different Python versions

A Python script is a file intended for standalone execution, e.g., with python <script>.py. Using uv to execute scripts ensures that script dependencies are managed without manually managing environments.

If you are not familiar with Python environments: every Python installation has an environment that packages can be installed in. Typically, creating virtual environments is recommended to isolate packages required by each script. uv automatically manages virtual environments for you and prefers a declarative approach to dependencies.

If your script has no dependencies, you can execute it with uv run:

Similarly, if your script depends on a module in the standard library, there's nothing more to do:

Arguments may be provided to the script:

Additionally, your script can be read directly from stdin:

Or, if your shell supports here-documents:

Note that if you use uv run in a project, i.e., a directory with a pyproject.toml, it will install the current project before running the script. If your script does not depend on the project, use the --no-project flag to skip this:

See the projects guide for more details on working in projects.

When your script requires other packages, they must be installed into the environment that the script runs in. uv prefers to create these environments on-demand instead of using a long-lived virtual environment with manually managed dependencies. This requires explicit declaration of dependencies that are required for the script. Generally, it's recommended to use a project or inline metadata to declare dependencies, but uv supports requesting dependencies per invocation as well.

For example, the following script requires rich.

If executed without specifying a dependency, this script will fail:

Request the dependency using the --with option:

Constraints can be added to the requested dependency if specific versions are needed:

Multiple dependencies can be requested by repeating with --with option.

Note that if uv run is used in a project, these dependencies will be included in addition to the project's dependencies. To opt-out of this behavior, use the --no-project flag.

Python recently added a standard format for inline script metadata. It allows for selecting Python versions and defining dependencies. Use uv init --script to initialize scripts with the inline metadata:

The inline metadata format allows the dependencies for a script to be declared in the script itself.

uv supports adding and updating inline scri

*[Content truncated]*

**Examples:**

Example 1 (unknown):
```unknown
print("Hello world")
```

Example 2 (unknown):
```unknown
$ uv run example.py
Hello world
```

Example 3 (unknown):
```unknown
import os

print(os.path.expanduser("~"))
```

Example 4 (unknown):
```unknown
$ uv run example.py
/Users/astral
```

---

## Compatibility with pip and pip-tools

**URL:** https://docs.astral.sh/uv/pip/compatibility/

**Contents:**
- Compatibility with pip and pip-tools
- Configuration files and environment variables
- Pre-release compatibility
- Packages that exist on multiple indexes
- PEP 517 build isolation
- Transitive URL dependencies
- Virtual environments by default
- Resolution strategy
- pip check
- --user and the user install scheme

uv is designed as a drop-in replacement for common pip and pip-tools workflows.

Informally, the intent is such that existing pip and pip-tools users can switch to uv without making meaningful changes to their packaging workflows; and, in most cases, swapping out pip install for uv pip install should "just work".

However, uv is not intended to be an exact clone of pip, and the further you stray from common pip workflows, the more likely you are to encounter differences in behavior. In some cases, those differences may be known and intentional; in others, they may be the result of implementation details; and in others, they may be bugs.

This document outlines the known differences between uv and pip, along with rationale, workarounds, and a statement of intent for compatibility in the future.

uv does not read configuration files or environment variables that are specific to pip, like pip.conf or PIP_INDEX_URL.

Reading configuration files and environment variables intended for other tools has a number of drawbacks:

Instead, uv supports its own environment variables, like UV_INDEX_URL. uv also supports persistent configuration in a uv.toml file or a [tool.uv.pip] section of pyproject.toml. For more information, see Configuration files.

By default, uv will accept pre-release versions during dependency resolution in two cases:

If dependency resolution fails due to a transitive pre-release, uv will prompt the user to re-run with --prerelease allow, to allow pre-releases for all dependencies.

Alternatively, you can add the transitive dependency to your requirements.in file with pre-release specifier (e.g., flask>=2.0.0rc1) to opt in to pre-release support for that specific dependency.

In sum, uv needs to know upfront whether the resolver should accept pre-releases for a given package. pip, meanwhile, may respect pre-release identifiers in transitive dependencies depending on the order in which the resolver encounters the relevant specifiers (#1641).

Pre-releases are notoriously difficult to model, and are a frequent source of bugs in packaging tools. Even pip, which is viewed as a reference implementation, has a number of open questions around pre-release handling (#12469, #12470, #40505, etc.). uv's pre-release handling is intentionally limited and intentionally requires user opt-in for pre-releases, to ensure correctness.

In the future, uv may support pre-release identifiers in transitive dependencies. However, it's likely contingent on evolution in 

*[Content truncated]*

**Examples:**

Example 1 (unknown):
```unknown
uv pip install wheel && uv pip install --no-build-isolation biopython==1.77
```

Example 2 (unknown):
```unknown
starlette
fastapi
```

Example 3 (unknown):
```unknown
# This file was autogenerated by uv via the following command:
#    uv pip compile requirements.in
annotated-types==0.6.0
    # via pydantic
anyio==4.3.0
    # via starlette
fastapi==0.1.17
idna==3.6
    # via anyio
pydantic==2.6.3
    # via fastapi
pydantic-core==2.16.3
    # via pydantic
sniffio==1.3.1
    # via anyio
starlette==0.37.2
    # via fastapi
typing-extensions==4.10.0
    # via
    #   pydantic
    #   pydantic-core
```

Example 4 (unknown):
```unknown
# This file was autogenerated by uv via the following command:
#    uv pip compile requirements.in
annotated-types==0.6.0
    # via pydantic
anyio==4.3.0
    # via starlette
fastapi==0.110.0
idna==3.6
    # via anyio
pydantic==2.6.3
    # via fastapi
pydantic-core==2.16.3
    # via pydantic
sniffio==1.3.1
    # via anyio
starlette==0.36.3
    # via fastapi
typing-extensions==4.10.0
    # via
    #   fastapi
    #   pydantic
    #   pydantic-core
```

---

## Troubleshooting

**URL:** https://docs.astral.sh/uv/reference/troubleshooting/

**Contents:**
- Troubleshooting

The troubleshooting section provides information about investigating failures in uv:

---

## Third-party services

**URL:** https://docs.astral.sh/uv/concepts/authentication/third-party/

**Contents:**
- Third-party services
- Authentication with alternative package indexes
- Hugging Face support

See the alternative indexes integration guide for details on authentication with popular alternative Python package indexes.

uv supports automatic authentication for the Hugging Face Hub. Specifically, if the HF_TOKEN environment variable is set, uv will propagate it to requests to huggingface.co.

This is particularly useful for accessing private scripts in Hugging Face Datasets. For example, you can run the following command to execute the script main.py script from a private dataset:

You can disable automatic Hugging Face authentication by setting the UV_NO_HF_TOKEN=1 environment variable.

**Examples:**

Example 1 (unknown):
```unknown
$ HF_TOKEN=hf_... uv run https://huggingface.co/datasets/<user>/<name>/resolve/<branch>/main.py
```

---

## uv

**URL:** https://docs.astral.sh/uv/

**Contents:**
- uv
- Highlights
- Installation
- Projects
- Scripts
- Tools
- Python versions
- The pip interface
- Learn more

An extremely fast Python package and project manager, written in Rust.

Installing Trio's dependencies with a warm cache.

uv is backed by Astral, the creators of Ruff.

Install uv with our official standalone installer:

Then, check out the first steps or read on for a brief overview.

uv may also be installed with pip, Homebrew, and more. See all of the methods on the installation page.

uv manages project dependencies and environments, with support for lockfiles, workspaces, and more, similar to rye or poetry:

See the project guide to get started.

uv also supports building and publishing projects, even if they're not managed with uv. See the packaging guide to learn more.

uv manages dependencies and environments for single-file scripts.

Create a new script and add inline metadata declaring its dependencies:

Then, run the script in an isolated virtual environment:

See the scripts guide to get started.

uv executes and installs command-line tools provided by Python packages, similar to pipx.

Run a tool in an ephemeral environment using uvx (an alias for uv tool run):

Install a tool with uv tool install:

See the tools guide to get started.

uv installs Python and allows quickly switching between versions.

Install multiple Python versions:

Download Python versions as needed:

Use a specific Python version in the current directory:

See the installing Python guide to get started.

uv provides a drop-in replacement for common pip, pip-tools, and virtualenv commands.

uv extends their interfaces with advanced features, such as dependency version overrides, platform-independent resolutions, reproducible resolutions, alternative resolution strategies, and more.

Migrate to uv without changing your existing workflows — and experience a 10-100x speedup — with the uv pip interface.

Compile requirements into a platform-independent requirements file:

Create a virtual environment:

Install the locked requirements:

See the pip interface documentation to get started.

See the first steps or jump straight to the guides to start using uv.

**Examples:**

Example 1 (unknown):
```unknown
$ curl -LsSf https://astral.sh/uv/install.sh | sh
```

Example 2 (unknown):
```unknown
PS> powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

Example 3 (unknown):
```unknown
$ uv init example
Initialized project `example` at `/home/user/example`

$ cd example

$ uv add ruff
Creating virtual environment at: .venv
Resolved 2 packages in 170ms
   Built example @ file:///home/user/example
Prepared 2 packages in 627ms
Installed 2 packages in 1ms
 + example==0.1.0 (from file:///home/user/example)
 + ruff==0.5.4

$ uv run ruff check
All checks passed!

$ uv lock
Resolved 2 packages in 0.33ms

$ uv sync
Resolved 2 packages in 0.70ms
Audited 1 package in 0.02ms
```

Example 4 (unknown):
```unknown
$ echo 'import requests; print(requests.get("https://astral.sh"))' > example.py

$ uv add --script example.py requests
Updated `example.py`
```

---

## First steps with uv

**URL:** https://docs.astral.sh/uv/getting-started/first-steps/

**Contents:**
- First steps with uv
- Next steps

After installing uv, you can check that uv is available by running the uv command:

You should see a help menu listing the available commands.

Now that you've confirmed uv is installed, check out an overview of features, learn how to get help if you run into any problems, or jump to the guides to start using uv.

**Examples:**

Example 1 (unknown):
```unknown
$ uv
An extremely fast Python package manager.

Usage: uv [OPTIONS] <COMMAND>

...
```

---

## Using uv with PyTorch

**URL:** https://docs.astral.sh/uv/guides/integration/pytorch/

**Contents:**
- Using uv with PyTorch
- Installing PyTorch
- Using a PyTorch index
- Configuring accelerators with environment markers
- Configuring accelerators with optional dependencies
- The uv pip interface
- Automatic backend selection

The PyTorch ecosystem is a popular choice for deep learning research and development. You can use uv to manage PyTorch projects and PyTorch dependencies across different Python versions and environments, even controlling for the choice of accelerator (e.g., CPU-only vs. CUDA).

Some of the features outlined in this guide require uv version 0.5.3 or later. We recommend upgrading prior to configuring PyTorch.

From a packaging perspective, PyTorch has a few uncommon characteristics:

As such, the necessary packaging configuration will vary depending on both the platforms you need to support and the accelerators you want to enable.

To start, consider the following (default) configuration, which would be generated by running uv init --python 3.12 followed by uv add torch torchvision.

In this case, PyTorch would be installed from PyPI, which hosts CPU-only wheels for Windows and macOS, and GPU-accelerated wheels on Linux (targeting CUDA 12.6):

Supported Python versions

At time of writing, PyTorch does not yet publish wheels for Python 3.14; as such projects with requires-python = ">=3.14" may fail to resolve. See the compatibility matrix.

This is a valid configuration for projects that want to use CPU builds on Windows and macOS, and CUDA-enabled builds on Linux. However, if you need to support different platforms or accelerators, you'll need to configure the project accordingly.

In some cases, you may want to use a specific PyTorch variant across all platforms. For example, you may want to use the CPU-only builds on Linux too.

In such cases, the first step is to add the relevant PyTorch index to your pyproject.toml:

We recommend the use of explicit = true to ensure that the index is only used for torch, torchvision, and other PyTorch-related packages, as opposed to generic dependencies like jinja2, which should continue to be sourced from the default index (PyPI).

Next, update the pyproject.toml to point torch and torchvision to the desired index:

PyTorch doesn't publish CUDA builds for macOS. As such, we gate on sys_platform to instruct uv to use the PyTorch index on Linux and Windows, but fall back to PyPI on macOS:

PyTorch doesn't publish CUDA builds for macOS. As such, we gate on sys_platform to instruct uv to limit the PyTorch index to Linux and Windows, falling back to PyPI on macOS:

PyTorch doesn't publish CUDA builds for macOS. As such, we gate on sys_platform to instruct uv to limit the PyTorch index to Linux and Windows, falling back to P

*[Content truncated]*

**Examples:**

Example 1 (unknown):
```unknown
[project]
name = "project"
version = "0.1.0"
requires-python = ">=3.12"
dependencies = [
  "torch>=2.7.0",
  "torchvision>=0.22.0",
]
```

Example 2 (unknown):
```unknown
[[tool.uv.index]]
name = "pytorch-cpu"
url = "https://download.pytorch.org/whl/cpu"
explicit = true
```

Example 3 (unknown):
```unknown
[[tool.uv.index]]
name = "pytorch-cu118"
url = "https://download.pytorch.org/whl/cu118"
explicit = true
```

Example 4 (unknown):
```unknown
[[tool.uv.index]]
name = "pytorch-cu126"
url = "https://download.pytorch.org/whl/cu126"
explicit = true
```

---

## Python versions

**URL:** https://docs.astral.sh/uv/concepts/python-versions/

**Contents:**
- Python versions
- Managed and system Python installations
- Requesting a version
  - Python version files
- Installing a Python version
  - Installing Python executables
- Upgrading Python versions
  - Minor version directories
- Project Python versions
- Viewing available Python versions

A Python version is composed of a Python interpreter (i.e. the python executable), the standard library, and other supporting files.

Since it is common for a system to have an existing Python installation, uv supports discovering Python versions. However, uv also supports installing Python versions itself. To distinguish between these two types of Python installations, uv refers to Python versions it installs as managed Python installations and all other Python installations as system Python installations.

uv does not distinguish between Python versions installed by the operating system vs those installed and managed by other tools. For example, if a Python installation is managed with pyenv, it would still be considered a system Python version in uv.

A specific Python version can be requested with the --python flag in most uv commands. For example, when creating a virtual environment:

uv will ensure that Python 3.11.6 is available — downloading and installing it if necessary — then create the virtual environment with it.

The following Python version request formats are supported:

Additionally, a specific system Python interpreter can be requested with:

By default, uv will automatically download Python versions if they cannot be found on the system. This behavior can be disabled with the python-downloads option.

The .python-version file can be used to create a default Python version request. uv searches for a .python-version file in the working directory and each of its parents. If none is found, uv will check the user-level configuration directory. Any of the request formats described above can be used, though use of a version number is recommended for interoperability with other tools.

A .python-version file can be created in the current directory with the uv python pin command.

A global .python-version file can be created in the user configuration directory with the uv python pin --global command.

Discovery of .python-version files can be disabled with --no-config.

uv will not search for .python-version files beyond project or workspace boundaries (except the user configuration directory).

uv bundles a list of downloadable CPython and PyPy distributions for macOS, Linux, and Windows.

By default, Python versions are automatically downloaded as needed without using uv python install.

To install a Python version at a specific version:

To install the latest patch version:

To install a version that satisfies constraints:

To install multiple

*[Content truncated]*

**Examples:**

Example 1 (unknown):
```unknown
$ uv venv --python 3.11.6
```

Example 2 (unknown):
```unknown
$ uv python install 3.12.3
```

Example 3 (unknown):
```unknown
$ uv python install 3.12
```

Example 4 (unknown):
```unknown
$ uv python install '>=3.8,<3.10'
```

---

## Git credentials

**URL:** https://docs.astral.sh/uv/concepts/authentication/git/

**Contents:**
- Git credentials
- SSH authentication
  - HTTP authentication
- Persistence of credentials
- Git credential helpers

uv allows packages to be installed from private Git repositories using SSH or HTTP authentication.

To authenticate using an SSH key, use the ssh:// protocol:

SSH authentication requires using the username git.

See the GitHub SSH documentation for more details on how to configure SSH.

To authenticate over HTTP Basic authentication using a password or token:

When using a GitHub personal access token, the username is arbitrary. GitHub doesn't allow you to use your account name and password in URLs like this, although other hosts may.

If there are no credentials present in the URL and authentication is needed, the Git credential helper will be queried.

When using uv add, uv will not persist Git credentials to the pyproject.toml or uv.lock. These files are often included in source control and distributions, so it is generally unsafe to include credentials in them.

If you have a Git credential helper configured, your credentials may be automatically persisted, resulting in successful subsequent fetches of the dependency. However, if you do not have a Git credential helper or the project is used on a machine without credentials seeded, uv will fail to fetch the dependency.

You may force uv to persist Git credentials by passing the --raw option to uv add. However, we strongly recommend setting up a credential helper instead.

Git credential helpers are used to store and retrieve Git credentials. See the Git documentation to learn more.

If you're using GitHub, the simplest way to set up a credential helper is to install the gh CLI and use:

See the gh auth login documentation for more details.

When using gh auth login interactively, the credential helper will be configured automatically. But when using gh auth login --with-token, as in the uv GitHub Actions guide, the gh auth setup-git command will need to be run afterwards to configure the credential helper.

**Examples:**

Example 1 (unknown):
```unknown
$ gh auth login
```

---

## Package indexes

**URL:** https://docs.astral.sh/uv/concepts/indexes/

**Contents:**
- Package indexes
- Defining an index
- Pinning a package to an index
- Searching across multiple indexes
- Authentication
  - Providing credentials directly
  - Using credential providers
  - Ignoring error codes when searching across indexes
  - Disabling authentication
  - Customizing cache control headers

By default, uv uses the Python Package Index (PyPI) for dependency resolution and package installation. However, uv can be configured to use other package indexes, including private indexes, via the [[tool.uv.index]] configuration option (and --index, the analogous command-line option).

To include an additional index when resolving dependencies, add a [[tool.uv.index]] entry to your pyproject.toml:

Indexes are prioritized in the order in which they’re defined, such that the first index listed in the configuration file is the first index consulted when resolving dependencies, with indexes provided via the command line taking precedence over those in the configuration file.

By default, uv includes the Python Package Index (PyPI) as the "default" index, i.e., the index used when a package is not found on any other index. To exclude PyPI from the list of indexes, set default = true on another index entry (or use the --default-index command-line option):

The default index is always treated as lowest priority, regardless of its position in the list of indexes.

Index names may only contain alphanumeric characters, dashes, underscores, and periods, and must be valid ASCII.

When providing an index on the command line (with --index or --default-index) or through an environment variable (UV_INDEX or UV_DEFAULT_INDEX), names are optional but can be included using the <name>=<url> syntax, as in:

A package can be pinned to a specific index by specifying the index in its tool.uv.sources entry. For example, to ensure that torch is always installed from the pytorch index, add the following to your pyproject.toml:

Similarly, to pull from a different index based on the platform, you can provide a list of sources disambiguated by environment markers:

An index can be marked as explicit = true to prevent packages from being installed from that index unless explicitly pinned to it. For example, to ensure that torch is installed from the pytorch index, but all other packages are installed from PyPI, add the following to your pyproject.toml:

Named indexes referenced via tool.uv.sources must be defined within the project's pyproject.toml file; indexes provided via the command-line, environment variables, or user-level configuration will not be recognized.

If an index is marked as both default = true and explicit = true, it will be treated as an explicit index (i.e., only usable via tool.uv.sources) while also removing PyPI as the default index.

By default, uv will stop 

*[Content truncated]*

**Examples:**

Example 1 (unknown):
```unknown
[[tool.uv.index]]
# Optional name for the index.
name = "pytorch"
# Required URL for the index.
url = "https://download.pytorch.org/whl/cpu"
```

Example 2 (unknown):
```unknown
[[tool.uv.index]]
name = "pytorch"
url = "https://download.pytorch.org/whl/cpu"
default = true
```

Example 3 (unknown):
```unknown
# On the command line.
$ uv lock --index pytorch=https://download.pytorch.org/whl/cpu
# Via an environment variable.
$ UV_INDEX=pytorch=https://download.pytorch.org/whl/cpu uv lock
```

Example 4 (unknown):
```unknown
[tool.uv.sources]
torch = { index = "pytorch" }

[[tool.uv.index]]
name = "pytorch"
url = "https://download.pytorch.org/whl/cpu"
```

---

## Building distributions

**URL:** https://docs.astral.sh/uv/concepts/projects/build/

**Contents:**
- Building distributions
- Using uv build
- Build constraints

To distribute your project to others (e.g., to upload it to an index like PyPI), you'll need to build it into a distributable format.

Python projects are typically distributed as both source distributions (sdists) and binary distributions (wheels). The former is typically a .tar.gz or .zip file containing the project's source code along with some additional metadata, while the latter is a .whl file containing pre-built artifacts that can be installed directly.

When using uv build, uv acts as a build frontend and only determines the Python version to use and invokes the build backend. The details of the builds, such as the included files and the distribution filenames, are determined by the build backend, as defined in [build-system]. Information about build configuration can be found in the respective tool's documentation.

uv build can be used to build both source distributions and binary distributions for your project. By default, uv build will build the project in the current directory, and place the built artifacts in a dist/ subdirectory:

You can build the project in a different directory by providing a path to uv build, e.g., uv build path/to/project.

uv build will first build a source distribution, and then build a binary distribution (wheel) from that source distribution.

You can limit uv build to building a source distribution with uv build --sdist, a binary distribution with uv build --wheel, or build both distributions from source with uv build --sdist --wheel.

uv build accepts --build-constraint, which can be used to constrain the versions of any build requirements during the build process. When coupled with --require-hashes, uv will enforce that the requirement used to build the project match specific, known hashes, for reproducibility.

For example, given the following constraints.txt:

Running the following would build the project with the specified version of setuptools, and verify that the downloaded setuptools distribution matches the specified hash:

**Examples:**

Example 1 (unknown):
```unknown
$ uv build
$ ls dist/
example-0.1.0-py3-none-any.whl
example-0.1.0.tar.gz
```

Example 2 (unknown):
```unknown
setuptools==68.2.2 --hash=sha256:b454a35605876da60632df1a60f736524eb73cc47bbc9f3f1ef1b644de74fd2a
```

Example 3 (unknown):
```unknown
$ uv build --build-constraint constraints.txt --require-hashes
```

---

## Declaring dependencies

**URL:** https://docs.astral.sh/uv/pip/dependencies/

**Contents:**
- Declaring dependencies
- Using pyproject.toml
- Using requirements.in

It is best practice to declare dependencies in a static file instead of modifying environments with ad-hoc installations. Once dependencies are defined, they can be locked to create a consistent, reproducible environment.

The pyproject.toml file is the Python standard for defining configuration for a project.

To define project dependencies in a pyproject.toml file:

To define optional dependencies in a pyproject.toml file:

Each of the keys defines an "extra", which can be installed using the --extra and --all-extras flags or package[<extra>] syntax. See the documentation on installing packages for more details.

See the official pyproject.toml guide for more details on getting started with a pyproject.toml.

It is also common to use a lightweight requirements.txt format to declare the dependencies for the project. Each requirement is defined on its own line. Commonly, this file is called requirements.in to distinguish it from requirements.txt which is used for the locked dependencies.

To define dependencies in a requirements.in file:

Optional dependencies groups are not supported in this format.

**Examples:**

Example 1 (unknown):
```unknown
[project]
dependencies = [
  "httpx",
  "ruff>=0.3.0"
]
```

Example 2 (unknown):
```unknown
[project.optional-dependencies]
cli = [
  "rich",
  "click",
]
```

Example 3 (unknown):
```unknown
httpx
ruff>=0.3.0
```

---

## Using uv in GitHub Actions

**URL:** https://docs.astral.sh/uv/guides/integration/github/

**Contents:**
- Using uv in GitHub Actions
- Installation
- Setting up Python
- Multiple Python versions
- Syncing and running
- Caching
- Using uv pip
- Private repos
- Publishing to PyPI

For use with GitHub Actions, we recommend the official astral-sh/setup-uv action, which installs uv, adds it to PATH, (optionally) persists the cache, and more, with support for all uv-supported platforms.

To install the latest version of uv:

It is considered best practice to pin to a specific uv version, e.g., with:

Python can be installed with the python install command:

This will respect the Python version pinned in the project.

Alternatively, the official GitHub setup-python action can be used. This can be faster, because GitHub caches the Python versions alongside the runner.

Set the python-version-file option to use the pinned version for the project:

Or, specify the pyproject.toml file to ignore the pin and use the latest version compatible with the project's requires-python constraint:

When using a matrix to test multiple Python versions, set the Python version using astral-sh/setup-uv, which will override the Python version specification in the pyproject.toml or .python-version files:

If not using the setup-uv action, you can set the UV_PYTHON environment variable:

Once uv and Python are installed, the project can be installed with uv sync and commands can be run in the environment with uv run:

The UV_PROJECT_ENVIRONMENT setting can be used to install to the system Python environment instead of creating a virtual environment.

It may improve CI times to store uv's cache across workflow runs.

The astral-sh/setup-uv has built-in support for persisting the cache:

Alternatively, you can manage the cache manually with the actions/cache action:

The uv cache prune --ci command is used to reduce the size of the cache and is optimized for CI. Its effect on performance is dependent on the packages being installed.

If using uv pip, use requirements.txt instead of uv.lock in the cache key.

When using non-ephemeral, self-hosted runners the default cache directory can grow unbounded. In this case, it may not be optimal to share the cache between jobs. Instead, move the cache inside the GitHub Workspace and remove it once the job finishes using a Post Job Hook.

Using a post job hook requires setting the ACTIONS_RUNNER_HOOK_JOB_STARTED environment variable on the self-hosted runner to the path of a cleanup script such as the one shown below.

If using the uv pip interface instead of the uv project interface, uv requires a virtual environment by default. To allow installing packages into the system environment, use the --system flag on all uv invo

*[Content truncated]*

**Examples:**

Example 1 (unknown):
```unknown
name: Example

jobs:
  uv-example:
    name: python
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v5

      - name: Install uv
        uses: astral-sh/setup-uv@v6
```

Example 2 (unknown):
```unknown
name: Example

jobs:
  uv-example:
    name: python
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v5

      - name: Install uv
        uses: astral-sh/setup-uv@v6
        with:
          # Install a specific version of uv.
          version: "0.9.5"
```

Example 3 (unknown):
```unknown
name: Example

jobs:
  uv-example:
    name: python
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v5

      - name: Install uv
        uses: astral-sh/setup-uv@v6

      - name: Set up Python
        run: uv python install
```

Example 4 (unknown):
```unknown
name: Example

jobs:
  uv-example:
    name: python
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v5

      - name: "Set up Python"
        uses: actions/setup-python@v5
        with:
          python-version-file: ".python-version"

      - name: Install uv
        uses: astral-sh/setup-uv@v6
```

---

## Building and publishing a package

**URL:** https://docs.astral.sh/uv/guides/package/

**Contents:**
- Building and publishing a package
- Preparing your project for packaging
- Building your package
- Updating your version
- Publishing your package
- Installing your package
- Next steps

uv supports building Python packages into source and binary distributions via uv build and uploading them to a registry with uv publish.

Before attempting to publish your project, you'll want to make sure it's ready to be packaged for distribution.

If your project does not include a [build-system] definition in the pyproject.toml, uv will not build it by default. This means that your project may not be ready for distribution. Read more about the effect of declaring a build system in the project concept documentation.

If you have internal packages that you do not want to be published, you can mark them as private:

This setting makes PyPI reject your uploaded package from publishing. It does not affect security or privacy settings on alternative registries.

We also recommend only generating per-project PyPI API tokens: Without a PyPI token matching the project, it can't be accidentally published.

Build your package with uv build:

By default, uv build will build the project in the current directory, and place the built artifacts in a dist/ subdirectory.

Alternatively, uv build <SRC> will build the package in the specified directory, while uv build --package <PACKAGE> will build the specified package within the current workspace.

By default, uv build respects tool.uv.sources when resolving build dependencies from the build-system.requires section of the pyproject.toml. When publishing a package, we recommend running uv build --no-sources to ensure that the package builds correctly when tool.uv.sources is disabled, as is the case when using other build tools, like pypa/build.

The uv version command provides conveniences for updating the version of your package before you publish it. See the project docs for reading your package's version.

To update to an exact version, provide it as a positional argument:

To preview the change without updating the pyproject.toml, use the --dry-run flag:

To increase the version of your package semantics, use the --bump option:

The --bump option supports the following common version components: major, minor, patch, stable, alpha, beta, rc, post, and dev. When provided more than once, the components will be applied in order, from largest (major) to smallest (dev).

To move from a stable to pre-release version, bump one of the major, minor, or patch components in addition to the pre-release component:

When moving from a pre-release to a new pre-release version, just bump the relevant pre-release component:

When movi

*[Content truncated]*

**Examples:**

Example 1 (unknown):
```unknown
[project]
classifiers = ["Private :: Do Not Upload"]
```

Example 2 (javascript):
```javascript
$ uv version 1.0.0
hello-world 0.7.0 => 1.0.0
```

Example 3 (javascript):
```javascript
$ uv version 2.0.0 --dry-run
hello-world 1.0.0 => 2.0.0
$ uv version
hello-world 1.0.0
```

Example 4 (javascript):
```javascript
$ uv version --bump minor
hello-world 1.2.3 => 1.3.0
```

---

## Settings

**URL:** https://docs.astral.sh/uv/reference/settings/

**Contents:**
- Settings
- Project metadata
  - build-constraint-dependencies
  - conflicts
  - constraint-dependencies
  - default-groups
  - dependency-groups
  - dev-dependencies
  - environments
  - index

Constraints to apply when solving build dependencies.

Build constraints are used to restrict the versions of build dependencies that are selected when building a package during resolution or installation.

Including a package as a constraint will not trigger installation of the package during a build; instead, the package must be requested elsewhere in the project's build dependency graph.

In uv lock, uv sync, and uv run, uv will only read build-constraint-dependencies from the pyproject.toml at the workspace root, and will ignore any declarations in other workspace members or uv.toml files.

Declare collections of extras or dependency groups that are conflicting (i.e., mutually exclusive).

It's useful to declare conflicts when two or more extras have mutually incompatible dependencies. For example, extra foo might depend on numpy==2.0.0 while extra bar depends on numpy==2.1.0. While these dependencies conflict, it may be the case that users are not expected to activate both foo and bar at the same time, making it possible to generate a universal resolution for the project despite the incompatibility.

By making such conflicts explicit, uv can generate a universal resolution for a project, taking into account that certain combinations of extras and groups are mutually exclusive. In exchange, installation will fail if a user attempts to activate both conflicting extras.

Type: list[list[dict]]

Constraints to apply when resolving the project's dependencies.

Constraints are used to restrict the versions of dependencies that are selected during resolution.

Including a package as a constraint will not trigger installation of the package on its own; instead, the package must be requested elsewhere in the project's first-party or transitive dependencies.

In uv lock, uv sync, and uv run, uv will only read constraint-dependencies from the pyproject.toml at the workspace root, and will ignore any declarations in other workspace members or uv.toml files.

The list of dependency-groups to install by default.

Can also be the literal "all" to default enable all groups.

Default value: ["dev"]

Type: str | list[str]

Additional settings for dependency-groups.

Currently this can only be used to add requires-python constraints to dependency groups (typically to inform uv that your dev tooling has a higher python requirement than your actual project).

This cannot be used to define dependency groups, use the top-level [dependency-groups] table for that.

The projec

*[Content truncated]*

**Examples:**

Example 1 (unknown):
```unknown
[tool.uv]
# Ensure that the setuptools v60.0.0 is used whenever a package has a build dependency
# on setuptools.
build-constraint-dependencies = ["setuptools==60.0.0"]
```

Example 2 (unknown):
```unknown
[tool.uv]
# Require that `package[extra1]` and `package[extra2]` are resolved
# in different forks so that they cannot conflict with one another.
conflicts = [
    [
        { extra = "extra1" },
        { extra = "extra2" },
    ]
]

# Require that the dependency groups `group1` and `group2`
# are resolved in different forks so that they cannot conflict
# with one another.
conflicts = [
    [
        { group = "group1" },
        { group = "group2" },
    ]
]
```

Example 3 (unknown):
```unknown
[tool.uv]
# Ensure that the grpcio version is always less than 1.65, if it's requested by a
# direct or transitive dependency.
constraint-dependencies = ["grpcio<1.65"]
```

Example 4 (unknown):
```unknown
[tool.uv]
default-groups = ["docs"]
```

---

## Resolver internals

**URL:** https://docs.astral.sh/uv/reference/internals/resolver/

**Contents:**
- Resolver internals
- Resolver
- Forking
- Wheel tags
- Marker and wheel tag filtering
- Metadata consistency
- Requires-python
- URL dependencies
- Prioritization

This document focuses on the internal workings of uv's resolver. For using uv, see the resolution concept documentation.

As defined in a textbook, resolution, or finding a set of version to install from a given set of requirements, is equivalent to the SAT problem and thereby NP-complete: in the worst case you have to try all possible combinations of all versions of all packages and there are no general, fast algorithms. In practice, this is misleading for a number of reasons:

uv uses pubgrub-rs, the Rust implementation of PubGrub, an incremental version solver. PubGrub in uv works in the following steps:

Eventually, the resolver either picks compatible versions for all packages (a successful resolution) or there is an incompatibility including the virtual "root" package which defines the versions requested by the user. An incompatibility with the root package indicates that whatever versions of the root dependencies and their transitive dependencies are picked, there will always be a conflict. From the incompatibilities tracked in PubGrub, an error message is constructed to enumerate the involved packages.

For more details on the PubGrub algorithm, see Internals of the PubGrub algorithm.

In addition to PubGrub's base algorithm, we also use a heuristic that backtracks and switches the order of two packages if they have been conflicting too much.

Python resolvers historically didn't support backtracking, and even with backtracking, resolution was usually limited to single environment, which one specific architecture, operating system, Python version, and Python implementation. Some packages use contradictory requirements for different environments, for example:

Since Python only allows one version of each package, a naive resolver would error here. Inspired by Poetry, uv uses a forking resolver: whenever there are multiple requirements for a package with different markers, the resolution is split.

In the above example, the partial solution would be split into two resolutions, one for python_version >= "3.11" and one for python_version < "3.11".

If markers overlap or are missing a part of the marker space, the resolver splits additional times — there can be many forks per package. For example, given:

A fork would be created for sys_platform == 'darwin', for sys_platform == 'win32', and for sys_platform != 'darwin' and sys_platform != 'win32'.

Forks can be nested, e.g., each fork is dependent on any previous forks that occurred. Forks with identica

*[Content truncated]*

**Examples:**

Example 1 (unknown):
```unknown
numpy>=2,<3 ; python_version >= "3.11"
numpy>=1.16,<2 ; python_version < "3.11"
```

Example 2 (unknown):
```unknown
flask > 1 ; sys_platform == 'darwin'
flask > 2 ; sys_platform == 'win32'
flask
```

Example 3 (unknown):
```unknown
numpy==2.0.0; python_version >= "3.9" and python_version < "3.10"
numpy==2.1.0; python_version >= "3.10"
```

---

## Versioning

**URL:** https://docs.astral.sh/uv/reference/policies/versioning/

**Contents:**
- Versioning
- Cache versioning
- Lockfile versioning
- Minimum supported Rust version

uv uses a custom versioning scheme in which the minor version number is bumped for breaking changes, and the patch version number is bumped for bug fixes, enhancements, and other non-breaking changes.

uv is widely used in production. However, we value the ability to iterate on new features quickly and gather changes that could be breaking into clearly marked releases.

Once uv v1.0.0 is released, the versioning scheme will adhere to Semantic Versioning. There is not a particular goal that must be achieved for uv to reach this milestone.

uv's changelog can be viewed on GitHub.

Cache versions are considered internal to uv, and so may be changed in a minor or patch release. See Cache versioning for more.

The uv.lock schema version is considered part of the public API, and so will only be incremented in a minor release as a breaking change. See Lockfile versioning for more.

The minimum supported Rust version required to compile uv is listed in the rust-version key of the [workspace.package] section in Cargo.toml. It may change in any release (minor or patch). It will never be newer than N-2 Rust versions, where N is the latest stable version. For example, if the latest stable Rust version is 1.85, uv's minimum supported Rust version will be at most 1.83.

This is only relevant to users who build uv from source. Installing uv from the Python package index usually installs a pre-built binary and does not require Rust compilation.

---

## Configuration files

**URL:** https://docs.astral.sh/uv/concepts/configuration-files/

**Contents:**
- Configuration files
- Settings
- .env
- Configuring the pip interface

uv supports persistent configuration files at both the project- and user-level.

Specifically, uv will search for a pyproject.toml or uv.toml file in the current directory, or in the nearest parent directory.

For tool commands, which operate at the user level, local configuration files will be ignored. Instead, uv will exclusively read from user-level configuration (e.g., ~/.config/uv/uv.toml) and system-level configuration (e.g., /etc/uv/uv.toml).

In workspaces, uv will begin its search at the workspace root, ignoring any configuration defined in workspace members. Since the workspace is locked as a single unit, configuration is shared across all members.

If a pyproject.toml file is found, uv will read configuration from the [tool.uv] table. For example, to set a persistent index URL, add the following to a pyproject.toml:

(If there is no such table, the pyproject.toml file will be ignored, and uv will continue searching in the directory hierarchy.)

uv will also search for uv.toml files, which follow an identical structure, but omit the [tool.uv] prefix. For example:

uv.toml files take precedence over pyproject.toml files, so if both uv.toml and pyproject.toml files are present in a directory, configuration will be read from uv.toml, and [tool.uv] section in the accompanying pyproject.toml will be ignored.

uv will also discover user-level configuration at ~/.config/uv/uv.toml (or $XDG_CONFIG_HOME/uv/uv.toml) on macOS and Linux, or %APPDATA%\uv\uv.toml on Windows; and system-level configuration at /etc/uv/uv.toml (or $XDG_CONFIG_DIRS/uv/uv.toml) on macOS and Linux, or %SYSTEMDRIVE%\ProgramData\uv\uv.toml on Windows.

User-and system-level configuration must use the uv.toml format, rather than the pyproject.toml format, as a pyproject.toml is intended to define a Python project.

If project-, user-, and system-level configuration files are found, the settings will be merged, with project-level configuration taking precedence over the user-level configuration, and user-level configuration taking precedence over the system-level configuration. (If multiple system-level configuration files are found, e.g., at both /etc/uv/uv.toml and $XDG_CONFIG_DIRS/uv/uv.toml, only the first-discovered file will be used, with XDG taking priority.)

For example, if a string, number, or boolean is present in both the project- and user-level configuration tables, the project-level value will be used, and the user-level value will be ignored. If an array is present in bot

*[Content truncated]*

**Examples:**

Example 1 (unknown):
```unknown
[[tool.uv.index]]
url = "https://test.pypi.org/simple"
default = true
```

Example 2 (unknown):
```unknown
[[index]]
url = "https://test.pypi.org/simple"
default = true
```

Example 3 (unknown):
```unknown
$ echo "MY_VAR='Hello, world!'" > .env
$ uv run --env-file .env -- python -c 'import os; print(os.getenv("MY_VAR"))'
Hello, world!
```

Example 4 (unknown):
```unknown
[tool.uv.pip]
index-url = "https://test.pypi.org/simple"
```

---

## Using uv in Docker

**URL:** https://docs.astral.sh/uv/guides/integration/docker/

**Contents:**
- Using uv in Docker
- Getting started
  - Available images
  - Installing uv
  - Installing a project
  - Using the environment
  - Using installed tools
  - Installing Python in ARM musl images
- Developing in a container
  - Mounting the project with docker run

Check out the uv-docker-example project for an example of best practices when using uv to build an application in Docker.

uv provides both distroless Docker images, which are useful for copying uv binaries into your own image builds, and images derived from popular base images, which are useful for using uv in a container. The distroless images do not contain anything but the uv binaries. In contrast, the derived images include an operating system with uv pre-installed.

As an example, to run uv in a container using a Debian-based image:

The following distroless images are available:

And the following derived images are available:

As with the distroless image, each derived image is published with uv version tags as ghcr.io/astral-sh/uv:{major}.{minor}.{patch}-{base} and ghcr.io/astral-sh/uv:{major}.{minor}-{base}, e.g., ghcr.io/astral-sh/uv:0.9.5-alpine.

In addition, starting with 0.8 each derived image also sets UV_TOOL_BIN_DIR to /usr/local/bin to allow uv tool install to work as expected with the default user.

For more details, see the GitHub Container page.

Use one of the above images with uv pre-installed or install uv by copying the binary from the official distroless Docker image:

Or, with the installer:

Note this requires curl to be available.

In either case, it is best practice to pin to a specific uv version, e.g., with:

While the Dockerfile example above pins to a specific tag, it's also possible to pin a specific SHA256. Pinning a specific SHA256 is considered best practice in environments that require reproducible builds as tags can be moved across different commit SHAs.

Or, with the installer:

If you're using uv to manage your project, you can copy it into the image and install it:

It is best practice to add .venv to a .dockerignore file in your repository to prevent it from being included in image builds. The project virtual environment is dependent on your local platform and should be created from scratch in the image.

Then, to start your application by default:

It is best practice to use intermediate layers separating installation of dependencies and the project itself to improve Docker image build times.

See a complete example in the uv-docker-example project.

Once the project is installed, you can either activate the project virtual environment by placing its binary directory at the front of the path:

Or, you can use uv run for any commands that require the environment:

Alternatively, the UV_PROJECT_ENVIRONMENT settin

*[Content truncated]*

**Examples:**

Example 1 (unknown):
```unknown
$ docker run --rm -it ghcr.io/astral-sh/uv:debian uv --help
```

Example 2 (unknown):
```unknown
FROM python:3.12-slim-trixie
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/
```

Example 3 (unknown):
```unknown
FROM python:3.12-slim-trixie

# The installer requires curl (and certificates) to download the release archive
RUN apt-get update && apt-get install -y --no-install-recommends curl ca-certificates

# Download the latest installer
ADD https://astral.sh/uv/install.sh /uv-installer.sh

# Run the installer then remove it
RUN sh /uv-installer.sh && rm /uv-installer.sh

# Ensure the installed binary is on the `PATH`
ENV PATH="/root/.local/bin/:$PATH"
```

Example 4 (unknown):
```unknown
COPY --from=ghcr.io/astral-sh/uv:0.9.5 /uv /uvx /bin/
```

---

## Resolution

**URL:** https://docs.astral.sh/uv/concepts/resolution/

**Contents:**
- Resolution
- Dependencies
- Basic examples
- Platform markers
- Platform-specific resolution
- Universal resolution
- Limited resolution environments
- Required environments
- Dependency preferences
- Resolution strategy

Resolution is the process of taking a list of requirements and converting them to a list of package versions that fulfill the requirements. Resolution requires recursively searching for compatible versions of packages, ensuring that the requested requirements are fulfilled and that the requirements of the requested packages are compatible.

Most projects and packages have dependencies. Dependencies are other packages that are necessary in order for the current package to work. A package defines its dependencies as requirements, roughly a combination of a package name and acceptable versions. The dependencies defined by the current project are called direct dependencies. The dependencies added by each dependency of the current project are called indirect or transitive dependencies.

See the dependency specifiers page in the Python Packaging documentation for details about dependencies.

To help demonstrate the resolution process, consider the following dependencies:

In this example, the resolver must find a set of package versions which satisfies the project requirements. Since there is only one version of both foo and bar, those will be used. The resolution must also include the transitive dependencies, so a version of lib must be chosen. foo 1.0.0 allows all available versions of lib, but bar 1.0.0 requires lib>=2.0.0 so lib 2.0.0 must be used.

In some resolutions, there may be more than one valid solution. Consider the following dependencies:

In this example, some version of both foo and bar must be selected; however, determining which version requires considering the dependencies of each version of foo and bar. foo 2.0.0 and bar 2.0.0 cannot be installed together as they conflict on their required version of lib, so the resolver must select either foo 1.0.0 (along with bar 2.0.0) or bar 1.0.0 (along with foo 1.0.0). Both are valid solutions, and different resolution algorithms may yield either result.

Markers allow attaching an expression to requirements that indicate when the dependency should be used. For example bar ; python_version < "3.9" indicates that bar should only be installed on Python 3.8 and earlier.

Markers are used to adjust a package's dependencies based on the current environment or platform. For example, markers can be used to modify dependencies by operating system, CPU architecture, Python version, Python implementation, and more.

See the environment markers section in the Python Packaging documentation for more details about m

*[Content truncated]*

**Examples:**

Example 1 (unknown):
```unknown
[tool.uv]
environments = [
    "sys_platform == 'darwin'",
    "sys_platform == 'linux'",
]
```

Example 2 (unknown):
```unknown
[tool.uv]
environments = [
    "implementation_name == 'cpython'"
]
```

Example 3 (unknown):
```unknown
[tool.uv]
required-environments = [
    "sys_platform == 'darwin' and platform_machine == 'x86_64'"
]
```

Example 4 (unknown):
```unknown
flask>=2.0.0
```

---

## Installing Python

**URL:** https://docs.astral.sh/uv/guides/install-python/

**Contents:**
- Installing Python
- Getting started
- Installing a specific version
- Reinstalling Python
- Viewing Python installations
- Automatic Python downloads
- Using existing Python versions
- Upgrading Python versions
- Next steps

If Python is already installed on your system, uv will detect and use it without configuration. However, uv can also install and manage Python versions. uv automatically installs missing Python versions as needed — you don't need to install Python to get started.

To install the latest Python version:

Python does not publish official distributable binaries. As such, uv uses distributions from the Astral python-build-standalone project. See the Python distributions documentation for more details.

Once Python is installed, it will be used by uv commands automatically. uv also adds the installed version to your PATH:

uv only installs a versioned executable by default. To install python and python3 executables, include the experimental --default option:

See the documentation on installing Python executables for more details.

To install a specific Python version:

To install multiple Python versions:

To install an alternative Python implementation, e.g., PyPy:

See the python install documentation for more details.

To reinstall uv-managed Python versions, use --reinstall, e.g.:

This will reinstall all previously installed Python versions. Improvements are constantly being added to the Python distributions, so reinstalling may resolve bugs even if the Python version does not change.

To view available and installed Python versions:

See the python list documentation for more details.

Python does not need to be explicitly installed to use uv. By default, uv will automatically download Python versions when they are required. For example, the following would download Python 3.12 if it was not installed:

Even if a specific Python version is not requested, uv will download the latest version on demand. For example, if there are no Python versions on your system, the following will install Python before creating a new virtual environment:

Automatic Python downloads can be easily disabled if you want more control over when Python is downloaded.

uv will use existing Python installations if present on your system. There is no configuration necessary for this behavior: uv will use the system Python if it satisfies the requirements of the command invocation. See the Python discovery documentation for details.

To force uv to use the system Python, provide the --no-managed-python flag. See the Python version preference documentation for more details.

Support for upgrading Python patch versions is in preview. This means the behavior is experimental and subject t

*[Content truncated]*

**Examples:**

Example 1 (unknown):
```unknown
$ uv python install
```

Example 2 (unknown):
```unknown
$ python3.13
```

Example 3 (unknown):
```unknown
$ uv python install --default
```

Example 4 (unknown):
```unknown
$ uv python install 3.12
```

---

## The uv installer

**URL:** https://docs.astral.sh/uv/reference/installer/

**Contents:**
- The uv installer
- Changing the installation path
- Disabling shell modifications
- Unmanaged installations
- Passing options to the installation script

By default, uv is installed to ~/.local/bin. If XDG_BIN_HOME is set, it will be used instead. Similarly, if XDG_DATA_HOME is set, the target directory will be inferred as XDG_DATA_HOME/../bin.

To change the installation path, use UV_INSTALL_DIR:

The installer may also update your shell profiles to ensure the uv binary is on your PATH. To disable this behavior, use UV_NO_MODIFY_PATH. For example:

If installed with UV_NO_MODIFY_PATH, subsequent operations, like uv self update, will not modify your shell profiles.

In ephemeral environments like CI, use UV_UNMANAGED_INSTALL to install uv to a specific path while preventing the installer from modifying shell profiles or environment variables:

The use of UV_UNMANAGED_INSTALL will also disable self-updates (via uv self update).

Using environment variables is recommended because they are consistent across platforms. However, options can be passed directly to the installation script. For example, to see the available options:

**Examples:**

Example 1 (unknown):
```unknown
$ curl -LsSf https://astral.sh/uv/install.sh | env UV_INSTALL_DIR="/custom/path" sh
```

Example 2 (unknown):
```unknown
PS> powershell -ExecutionPolicy ByPass -c {$env:UV_INSTALL_DIR = "C:\Custom\Path";irm https://astral.sh/uv/install.ps1 | iex}
```

Example 3 (unknown):
```unknown
$ curl -LsSf https://astral.sh/uv/install.sh | env UV_NO_MODIFY_PATH=1 sh
```

Example 4 (unknown):
```unknown
$ curl -LsSf https://astral.sh/uv/install.sh | env UV_UNMANAGED_INSTALL="/custom/path" sh
```

---

## The uv build backend

**URL:** https://docs.astral.sh/uv/concepts/build-backend/

**Contents:**
- The uv build backend
- Choosing a build backend
- Using the uv build backend
- Bundled build backend
- Modules
- Namespace packages
- Stub packages
- File inclusion and exclusion
  - Include and exclude syntax

A build backend transforms a source tree (i.e., a directory) into a source distribution or a wheel.

uv supports all build backends (as specified by PEP 517), but also provides a native build backend (uv_build) that integrates tightly with uv to improve performance and user experience.

The uv build backend is a great choice for most Python projects. It has reasonable defaults, with the goal of requiring zero configuration for most users, but provides flexible configuration to accommodate most Python project structures. It integrates tightly with uv, to improve messaging and user experience. It validates project metadata and structures, preventing common mistakes. And, finally, it's very fast.

The uv build backend currently only supports pure Python code. An alternative backend is required to build a library with extension modules.

While the backend supports a number of options for configuring your project structure, when build scripts or a more flexible project layout are required, consider using the hatchling build backend instead.

To use uv as a build backend in an existing project, add uv_build to the [build-system] section in your pyproject.toml:

The uv build backend follows the same versioning policy as uv. Including an upper bound on the uv_build version ensures that your package continues to build correctly as new versions are released.

To create a new project that uses the uv build backend, use uv init:

When the project is built, e.g., with uv build, the uv build backend will be used to create the source distribution and wheel.

The build backend is published as a separate package (uv_build) that is optimized for portability and small binary size. However, the uv executable also includes a copy of the build backend, which will be used during builds performed by uv, e.g., during uv build, if its version is compatible with the uv_build requirement. If it's not compatible, a compatible version of the uv_build package will be used. Other build frontends, such as python -m build, will always use the uv_build package, typically choosing the latest compatible version.

Python packages are expected to contain one or more Python modules, which are directories containing an __init__.py. By default, a single root module is expected at src/<package_name>/__init__.py.

For example, the structure for a project named foo would be:

uv normalizes the package name to determine the default module name: the package name is lowercased and dots and dashes are re

*[Content truncated]*

**Examples:**

Example 1 (unknown):
```unknown
[build-system]
requires = ["uv_build>=0.9.5,<0.10.0"]
build-backend = "uv_build"
```

Example 2 (unknown):
```unknown
pyproject.toml
src
└── foo
    └── __init__.py
```

Example 3 (unknown):
```unknown
pyproject.toml
FOO
└── __init__.py
```

Example 4 (unknown):
```unknown
[tool.uv.build-backend]
module-name = "FOO"
module-root = ""
```

---

## Using alternative package indexes

**URL:** https://docs.astral.sh/uv/guides/integration/alternative-indexes/

**Contents:**
- Using alternative package indexes
- Azure Artifacts
  - Authenticate with an Azure access token
  - Authenticate with keyring and artifacts-keyring
  - Publishing packages to Azure Artifacts
- Google Artifact Registry
  - Authenticate with a Google access token
  - Authenticate with keyring and keyrings.google-artifactregistry-auth
  - Publishing packages to Google Artifact Registry
- AWS CodeArtifact

While uv uses the official Python Package Index (PyPI) by default, it also supports alternative package indexes. Most alternative indexes require various forms of authentication, which require some initial setup.

If using the pip interface, please read the documentation on using multiple indexes in uv — the default behavior is different from pip to prevent dependency confusion attacks, but this means that uv may not find the versions of a package as you'd expect.

uv can install packages from Azure Artifacts, either by using a Personal Access Token (PAT), or using the keyring package.

To use Azure Artifacts, add the index to your project:

If there is a personal access token (PAT) available (e.g., $(System.AccessToken) in an Azure pipeline), credentials can be provided via "Basic" HTTP authentication scheme. Include the PAT in the password field of the URL. A username must be included as well, but can be any string.

For example, with the token stored in the $AZURE_ARTIFACTS_TOKEN environment variable, set credentials for the index with:

PRIVATE_REGISTRY should match the name of the index defined in your pyproject.toml.

You can also authenticate to Artifacts using keyring package with the artifacts-keyring plugin. Because these two packages are required to authenticate to Azure Artifacts, they must be pre-installed from a source other than Artifacts.

The artifacts-keyring plugin wraps the Azure Artifacts Credential Provider tool. The credential provider supports a few different authentication modes including interactive login — see the tool's documentation for information on configuration.

uv only supports using the keyring package in subprocess mode. The keyring executable must be in the PATH, i.e., installed globally or in the active environment. The keyring CLI requires a username in the URL, and it must be VssSessionToken.

The tool.uv.keyring-provider setting can be used to enable keyring in your uv.toml or pyproject.toml.

Similarly, the username for the index can be added directly to the index URL.

If you also want to publish your own packages to Azure Artifacts, you can use uv publish as described in the Building and publishing guide.

First, add a publish-url to the index you want to publish packages to. For example:

Then, configure credentials (if not using keyring):

And publish the package:

To use uv publish without adding the publish-url to the project, you can set UV_PUBLISH_URL:

Note this method is not preferable because uv cannot 

*[Content truncated]*

**Examples:**

Example 1 (unknown):
```unknown
[[tool.uv.index]]
name = "private-registry"
url = "https://pkgs.dev.azure.com/<ORGANIZATION>/<PROJECT>/_packaging/<FEED>/pypi/simple/"
```

Example 2 (unknown):
```unknown
export UV_INDEX_PRIVATE_REGISTRY_USERNAME=dummy
export UV_INDEX_PRIVATE_REGISTRY_PASSWORD="$AZURE_ARTIFACTS_TOKEN"
```

Example 3 (unknown):
```unknown
# Pre-install keyring and the Artifacts plugin from the public PyPI
uv tool install keyring --with artifacts-keyring

# Enable keyring authentication
export UV_KEYRING_PROVIDER=subprocess

# Set the username for the index
export UV_INDEX_PRIVATE_REGISTRY_USERNAME=VssSessionToken
```

Example 4 (unknown):
```unknown
[[tool.uv.index]]
name = "private-registry"
url = "https://pkgs.dev.azure.com/<ORGANIZATION>/<PROJECT>/_packaging/<FEED>/pypi/simple/"
publish-url = "https://pkgs.dev.azure.com/<ORGANIZATION>/<PROJECT>/_packaging/<FEED>/pypi/upload/"
```

---
