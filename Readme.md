This is a small startup project of mine because I want to learn Python.

# When to use
Have you ever cloned a repository from Github, and you just wanted to open it in Visual Studio, but you don't know where to look? It might even be that you want know where the sln file is located, but you dont want to make the massive `cd` down to the directory, and then do a `start NameOfMySolution.sln` (yes you can do that btw - Windows will pick the correct version of Visual Studio). By using this script you just do `r` in the root of your project, and it will find the first sln file and call `start` on it.

# Install
If you dont have python installed: open powershell, type python, push enter and you will be guided to the Microsoft Store, where you can download the latest version (pretty neat).

Clone this repo to a location of your own choosing

> git clone https://github.com/mslot/starter.git

Open your powershell profile, and add these lines

```powershell
function starter {py "[X:\path\to\location\of\cloned\repo]\src\Starter.py"}
set-item -Path alias:s -value starter
```

## Try it out
Restart your powershell, and then try to go into a root directory you know is holding a sln file in some subfolder, type `s` and it should open up your solution in the correct version of Visual Studio.

# Next up
I am currently working on the settings branch: features/settings_control. Feel free to chip in. I want to add some sort of control if there is more than one sln file found (maybe it is even going to remember what you choose, so you can just do a `r [ret] [ret]`). Lots of features needs to be added to this.
