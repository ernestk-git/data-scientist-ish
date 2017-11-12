# Installing XGBoost on Ubuntu

This guide will follow two paths:

* You created a conda environment (env) with Jeremy Howard's fast.ai library and want to add XGBoost to it (or any other environment)
* You want to install XGBoost in the default environment

## Adding XGBoost to a Conda Environment

While there is a pip package to install XGBoost, it has not been updated since 2016.  As such, we will be grabbing the repository off of github and compiling it ourselves.

1. First, we need to get cmake: `sudo apt install cmake`
2. We also need distutils: `sudo apt-get install python-distutils-extra`
3. Next, grab the repository (be aware of where you are cloning this, I used my ~ or home directory): `git clone --recursive https://github.com/dmlc/xgboost`

Following the XGBoost [instructions](http://xgboost.readthedocs.io/en/latest/build.html), change directory to .../xgboost:

4. `cd ~/xgboost` or wherever it is located

### With GPU Acceleration

* `mkdir build`
* `cd build`
* `cmake .. -DUSE_CUDA=ON`
* `make -j`

### Without GPU Acceleration

* `make -j4`

### For a Specific Conda Env

This is the tricky part, to install XGBoost to our conda env, we will have to use `sudo` at some point.  By default, `sudo` will install anything to the default environment.  We have to trick it to work for us:

5. cd python-package
6. Activate the shell: `sudo -s`
7. Activate your conda env: `source activate fastai`
8. Install XGBoost: `python setup.py install`

You should be up and running!

Now you may be asking: why did you go to the trouble of installing XGBoost to your environment?  In my current [program](https://www.usfca.edu/arts-sciences/graduate-programs/analytics), we use Python 2/Anaconda2 for most of our classes.  Since I created a conda env for Python 3 and Jeremy Howard's Deep Learning course, I felt it wise to package all of the CUDA-accelerated libraries into one environment, not knowing how Python 2 might behave.  If you are not a student in this program, you might be interested in the following installation steps:

## Installing XGBoost in your default environment

You will essentially follow the same steps as listed before.  However, after step 5, instead of evoking `sudo -s`, simply run:

6a. `python setup.py install`

# Installing XGBoost on MacOS X - no GPU Acceleration :(

The installation on Mac is not terribly different, but we'll go step-by-step:

1. Follow the instructions and install Homebrew, if you haven't already: [Homebrew](https://brew.sh/)
2. Install gcc: `brew install gcc`
    * What's going on here is rather complicated, but basically, Apple uses its own C compiler called Clang.  By default, Apple also maps `gcc` to clang.  So to use the gcc compiler, we'll need to brew install it.  The current version of gcc is 7, a factoid we'll use next.
3. Go to `~/xgboost` or wherever you cloned it: `cd ~/xgboost`
4. We'll need to edit the config.mk file in the xgboost directory, use your favorite text editor or: `nano config.mk`
5. Find the line `# choice of compiler, by default use system preference.` just below the intro crawl:
    * uncomment (delete #) lines:
        * export CC = gcc
        * export CXX = g++
    * edit these lines to:
        * export CC = gcc-7
        * export CXX = g++-7
    * You can check your current version of gcc by running `brew install gcc` again...it should report back that it is already installed and the current version number (i.e. 'gcc 7.2.0 is already installed')
6. `cp make/config.mk ./config.mk`
7. `make -j4`
8. `cd python-package`
8a. If you wish to install xgboost to a particular env (python 3 or fastai, for instance), activate it now: `source activate fastai`
9. python setup.py install
       
Alternatively, you can brew install gcc5, but I like to have the latest version of things.

# My First Gradient Boosted Tree!

...under construction...