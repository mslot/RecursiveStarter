This is a small startup project of mine because I want to learn Python.

# When to use
Have you ever cloned a repository from Github, and you just wanted to open it in Visual Studio, but you don't know where to look? It might even be that you want know where the sln file is located, but you dont want to make the massive `cd` down to the directory, and then do a `start NameOfMySolution.sln` (yes you can do that btw - Windows will pick the correct version of Visual Studio). By using this script you just do a `py RecursiveStarter.py` in the root, and it will find the first sln file and call start. I have yet to discover how to make aliases etc in Powershell, so I can just type `r`, but that I am currently investigating how to do.

# Install
If you dont have python installed: open powershell, type python, push enter and you will be guided to the Microsoft Store, where you can download the latest version (pretty neat).

Clone this repo to a location of your own choosing

> git clone https://github.com/mslot/RecursiveStarter.git

Open your powershell profile, and add these lines

```powershell
function recursive-starter {py "[X:\path\to\location\of\cloned\repo]\src\RecursiveStarter.py"}
set-item -Path alias:r -value recursive-starter
```

## Try it out
Restart your powershell, and then try to go into a root directory you know is holding a sln file in some subfolder, type `r` and it should open up your solution in the correct version of Visual Studio.

# Next up
I am currently working on the settings branch: features/settings_control. Feel free to chip in.
