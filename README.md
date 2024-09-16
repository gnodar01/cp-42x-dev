# CellProfiler 4.2.x Dev

This is the dev envrionment for CellProfiler 4.2.x-related work.

Mostly it just serves to reproduce a `pixi` setup.

## Setup

Clone the directory and setup submodules:

```bash
git clone git@github.com:gnodar01/cp-42x-dev.git
git submodule init
git submodule update
```

[Install pixi](https://pixi.sh/latest/#__tabbed_1_1)

```bash
curl -fsSL https://pixi.sh/install.sh | bash
```

Install the project dependencies:

**NOTE:** unlike the CellProfiler 5 branch, this does not come with `mysql` or `java`. Those must be installed beforehand.

```bash
pixi install --all
```

Run cellprofiler:

```bash
pixi run -e dev cp
```

