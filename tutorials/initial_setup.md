# Initial Rig Set-Up

I built a semi-powerful machine in preparation for the program with the following specs:

* Ryzen 5 1600: 6 - Physical Cores
* 16GB 3200Mhz RAM, CAS Latency: 14
* 512GB Samsung 960 EVO M.2 SSD Drive
* GTX 1080 Nvidia Graphics Card

In retrospect, I wish I had sprung for at least 32 gigs of RAM.  The timings and frequency of RAM on Ryzen motherboards was very finicky in the first few months after Ryzen's debut, often operating a sub-optimal speeds (or not at all). However, recent BIOS updates have largely fixed these issues.  Even still, the best chance of all of your ram sticks playing well together is to buy them at the same time (from the same manufacturing batch).

The M.2 drive is nice for its speed, but it's not necessary (does not impact the speed of building models as much as your GPU/CPU and RAM).

As for which GPU you should purchase, I recommend following

## Installing Ubuntu

* I installed Ubuntu 16.04.3 (which uses kernel 4.10 by default, earlier versions had issues playing nicely with Ryzen) from:

[Ubuntu](https://www.ubuntu.com/download/desktop)

* Via a USB Drive using this tool:
[Tutorials for Windows, Mac, or Ubuntu](https://tutorials.ubuntu.com/tutorial/tutorial-create-a-usb-stick-on-windows)

## Data Science Software

We use Anaconda2 in the program based on Python 2.7.  You should know that Python 2 is set to become depracated in 2019.  To switch between Python2 and 3, we use Conda environments.

* Grab the Anaconda package from: https://www.anaconda.com/download/
* I
