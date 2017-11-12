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

4. `cd ~/xgboost` or whever it is located

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

* `python setup.py install`

# Installing XGBoost on MacOS X - no GPU Acceleration :(

...under construction...

# My First Gradient Boosted Tree!

...under construction...