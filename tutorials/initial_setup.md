---
redirect_from: "/readme.md"
---

# Initial Rig Set-Up

I built a semi-powerful machine in preparation for the program with the following specs:

* Ryzen 5 1600: 6 - Physical Cores
* 16GB 3200Mhz RAM, CAS Latency: 14
* 512GB Samsung 960 EVO M.2 SSD Drive
* GTX 1080 Nvidia Graphics Card

In retrospect, I wish I had sprung for at least 32 gigs of RAM.  The timings and frequency of RAM on Ryzen motherboards were very finicky in the first few months after Ryzen's debut, often operating a sub-optimal speeds (or not at all). However, recent BIOS updates have largely fixed these issues.  Even still, the best chance that all of your ram sticks will play well together is to buy them at the same time (from the same manufacturing batch).

The M.2 drive is nice for its speed, but it's not necessary (does not impact the speed of building models as much as your GPU/CPU and RAM).

As for which GPU you should purchase, I recommend following [Tom Dettmers](http://timdettmers.com/2017/04/09/which-gpu-for-deep-learning/).

Basically, you'll benefit from having more RAM on the GPU and more processing power.  A GTX 1070, 1070TI, 1080 or 1080TI will serve you well.  

## Hey, I'm Using AWS

That's great because this guide was tested on an AWS instance!  A couple of notes about AWS:

* You'll find most of the GPU instances in the "Oregon" region.  Unfortunately, they're not immediately available and you will have to send a request for access.
* P2 instances feature a K80 GPU (~5.5 - 8 TFlops of Floating Point 32-bit (FP-32) performance, 2x12 GB RAM). The K80 is essentially two K20s on a single GPU with a wide range of clock speeds, hence the performance range [source](https://aws.amazon.com/ec2/instance-types/p2/)
* P3 instances feature a V100 GPU (~15 TFlops @ FP-32, 120 TFlops @ FP-16, 16 Gigs of Memory).  

Although CUDA supports the use of FP-16 operations, [PyTorch](https://github.com/pytorch/pytorch/issues/1539) (and many of the other major deep learning frameworks) do not yet.  All computations are performed at FP-32 so that will be the key metric to watch when selecting a GPU.

* Pricing can be found [here](https://aws.amazon.com/ec2/pricing/on-demand/)


## Installing Ubuntu

* I installed Ubuntu 16.04.3 LTS Desktop (which uses kernel 4.10 by default, earlier versions had issues playing nicely with Ryzen) from: <https://www.ubuntu.com/download/desktop>
* Via a USB Drive using this tool:
[Tutorials for Windows, Mac, or Ubuntu](https://tutorials.ubuntu.com/tutorial/tutorial-create-a-usb-stick-on-windows)

The LTS stands for Long Term Support, meaning that Canonical will continue to release updates for five years (Oct 2020).  It seems like many data scientists and tools are being developed on this particular breed of linux, but I've also had success with [Mint](https://linuxmint.com/).  However, this guide will assume that you're either on OS X or Ubuntu.  If you have no need for a GUI Desktop, feel free to install Ubuntu Server.

## Installing GPU Drivers and CUDA (Optional)

### Install the Graphics Driver:

If you will be using an NVIDIA graphics card to accelerate PyTorch and XGBoost, this section applies to you.

To begin, we need to install the NVIDIA Graphics Driver.  Thankfully, a [team](https://launchpad.net/~graphics-drivers/+archive/ubuntu/ppa) handles the latest graphics updates for you on Ubuntu.  You have two options:

* Add the repository and let update/upgrade grab driver packages: `sudo add-apt-repository ppa:graphics-drivers/ppa`
* Grab their standalone [packages](https://packages.ubuntu.com/xenial/misc/) (version 384.90 was the latest at writing): `sudo apt-get install nvidia-384`

### Install the CUDA Toolkit

I'll be using CUDA 8.0 as PyTorch does not currently support 9.0.  Fortunately, NVIDIA maintains an [archive of previous CUDA builds](https://developer.nvidia.com/cuda-80-ga2-download-archive).  Simply select: `Linux` > `x86_64` > `Ubuntu` > `16.04` > `runfile`

As of Oct 2017, you will be given instructions to download two files (~1.5 GB).  Simply follow the instructions in the terminal: `sudo sh FILENAME`

Next, we will cover the software necessary for the MSAN program/base data science.

## Data Science Software

In total we will be setting up and utilizing the following packages, software, or libraries (based on MSAN requirements):

* [Python 2.7 and 3.6](): Our Bread and Butter for Deep Learning
* [R](): In our courses, utilized for statistics, regression and time series analysis
* [PySpark, Spark, Hadoop](): Distributed computing stuff
* Anaconda2 - Covered under the Python Installation Guide
* Git
* [PyTorch](): Deep Learning in Python
* [XGBoost](xgboost.md): Gradient Boosted Trees, with or without GPU acceleration
* Jeremy Howard's [FastAI Libraries](https://github.com/fastai/fastai)

I primarily work in Jupyter Notebooks with Anaconda Environments.  For Machine Learning or Deep Learning, I utilize the env created by [Jeremy Howard](http://course.fast.ai/) for his classes.  On top of the fast.ai environment, we will install GPU-accelerated XGBoost and cuda80, cudnn for PyTorch.

## Good Computing Practices

After you install Ubuntu, make sure that you stay current with updates.  With the command `sudo apt-get update`, you can update installed software without upgrading to newer versions (which may cause issues with dependencies).  If you do desire the newest software, `sudo apt-get upgrade` will perform this task while `sudo apt-get dist-upgrade` will attempt to deal with dependencies intelligently [source](https://askubuntu.com/questions/222348/what-does-sudo-apt-get-update-do). 

Additionally, keep hardware drivers up-to-date, particularly your mainboard's BIOS and your router's firmware.  These can be found on the manufacturer's webpage (do not trust other sources unless you are using something like DD-WRT on your router).  Updates to my mainboard often lead to increased speed and stability while router updates are often crucial for security purposes.  

## Useful Stuff

* [How I use my home computer from my laptop with SSH and tmux]()
* [SSH FTP for convenient file transfers]()
* [Handy Terminal Commands]()
* [Psst, they're spying on you, VPN stuff]()
* [Useful Network Security Considerations]()
