# Initial Rig Set-Up

I built a semi-powerful machine in preparation for the program with the following specs:

* Ryzen 5 1600: 6 - Physical Cores
* 16GB 3200Mhz RAM, CAS Latency: 14
* 512GB Samsung 960 EVO M.2 SSD Drive
* GTX 1080 Nvidia Graphics Card

In retrospect, I wish I had sprung for at least 32 gigs of RAM.  The timings and frequency of RAM on Ryzen motherboards were very finicky in the first few months after Ryzen's debut, often operating a sub-optimal speeds (or not at all). However, recent BIOS updates have largely fixed these issues.  Even still, the best chance that all of your ram sticks will play well together is to buy them at the same time (from the same manufacturing batch).

The M.2 drive is nice for its speed, but it's not necessary (does not impact the speed of building models as much as your GPU/CPU and RAM).

As for which GPU you should purchase, I recommend following [Tom Dettmers](http://timdettmers.com/2017/04/09/which-gpu-for-deep-learning/).

Basically, you'll benefit from having more RAM on the GPU and more processing power.  A GTX 1070, 1070TI, 1080 or 1080TI will server you well.  

## Installing Ubuntu

* I installed Ubuntu 16.04.3 LTS Desktop (which uses kernel 4.10 by default, earlier versions had issues playing nicely with Ryzen) from:

[Ubuntu](https://www.ubuntu.com/download/desktop)

The LTS stands for Long Term Support, meaning that Canonical will continue to release updates for five years (Oct 2020).  It seems like many data scientists and tools are being developed on this particular breed of linux, but I've also had success with [Mint](https://linuxmint.com/).  However, this guide will assume that you're either on OS X or Ubuntu.  If you have no need for GUI Desktop, feel free to install Ubuntu Server (alternatively, you can push `CTRL + ALT + F1` to deactivate the GUI on Ubuntu Desktop).

* Via a USB Drive using this tool:
[Tutorials for Windows, Mac, or Ubuntu](https://tutorials.ubuntu.com/tutorial/tutorial-create-a-usb-stick-on-windows)

## Good Computing Practices

After you install Ubuntu, make sure that you stay up-to-date with updates.  With command `sudo apt-get update`, you can update installed software without upgrading to newer versions (which may cause issues with dependencies).  If you do desire the newest software, `sudo apt-get upgrade` will perform this task while `sudo apt-get dist-upgrade` will attempt to deal with dependencies intelligently [source](https://askubuntu.com/questions/222348/what-does-sudo-apt-get-update-do). 

Additionally, keep hardware drivers up-to-date, particularly your mainboard's BIOS and your router's firmware.  These can be found on the manufacturer's webpage (do not trust other sources unless you are using something like DD-WRT on your router).  Updates to my mainboard often lead to increased speed and stability while router updates are often crucial for security purposes.  

## Data Science Software

In total I will be setting up and utilizing the following packages, software, or libraries:

* [Python 2.7 and 3.6](https://github.com/ernestk-git/data-scientist-ish/blob/master/tutorials/python.md)
* [R](https://github.com/ernestk-git/data-scientist-ish/blob/master/tutorials/)
* [PySpark, Spark, Hadoop](https://github.com/ernestk-git/data-scientist-ish/blob/master/tutorials/)
* Anaconda2 - Covered under the Python Installation Guide
* Git
* [PyTorch](https://github.com/ernestk-git/data-scientist-ish/blob/master/tutorials/)
* [XGBoost](https://github.com/ernestk-git/data-scientist-ish/blob/master/tutorials/xgboost.md)
* Jeremy Howard's [FastAI Libraries](https://github.com/fastai/fastai)

## Useful Stuff

* [How I use my home computer from my laptop with SSH and tmux](https://github.com/ernestk-git/data-scientist-ish/blob/master/tutorials/)
* [SSH FTP for convenient file transfers](https://github.com/ernestk-git/data-scientist-ish/blob/master/tutorials/)
* [Handy Terminal Commands](https://github.com/ernestk-git/data-scientist-ish/blob/master/tutorials/)
* [Psst, they're spying on you, VPN stuff](https://github.com/ernestk-git/data-scientist-ish/blob/master/tutorials/)
* [Useful Network Security Considerations](https://github.com/ernestk-git/data-scientist-ish/blob/master/tutorials/)
