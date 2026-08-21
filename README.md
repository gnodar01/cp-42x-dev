# CellProfiler 4.2.x Dev

This is the dev envrionment for CellProfiler 4.2.x-related work.

Mostly it just serves to reproduce a `pixi` setup.

## Setup

Clone the directory and setup submodules:

```bash
git clone --recursive https://github.com/gnodar01/cp-42x-dev.git
```

[Install pixi](https://pixi.sh/latest/#__tabbed_1_1)

```bash
curl -fsSL https://pixi.sh/install.sh | bash
```

Enter the repository

```bash
cd cp-42x-dev
```

**NOTE:** If building on Linux, the wx dependency is pinned to a particular Linux version (Ubuntu 24.04 as of August 2026); ensure you change the `pixi.toml` file to point to the wheel for your version of Linux. Linux wheels can be found at https://extras.wxpython.org/wxPython4/extras/linux/gtk3/

Install the project dependencies:

```bash
pixi install -e dev
```

Run cellprofiler:

```bash
pixi run -e dev cp
```

or activate the python envrionment

```bash
pixi shell -e dev
```

**NOTE:** make sure to run `pixi` commands from the top level of `cp-42x-dev`.\
If, for instance, you run it from within the `release/` submodule, which has its\
own `pixi` setup, you will activate the wrong environment. Once the environment\
is active, you can `cd` into `release` or wherever else.

