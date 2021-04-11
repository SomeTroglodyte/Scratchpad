## Comments on Unciv "getting started"
Specific to a fresh installation on Mint 20.1 (ubuntu 20.04 focal)

### Android Studio
I do the install from the [maarten-fonville PPA](http://ppa.launchpad.net/maarten-fonville/android-studio).

Pay attention to versions (the PPA offers betas) - if in doubt google first. The [shell snippets below](#shell-code) show how I chose 4.2 over 4.1 - this got me a beta which then self-updated to a RC1, and which suggested a SDK unsuitable for Unciv, but in the end was just fine.

Setting up Android Studio will download at least one SDK - make sure you get the one Unciv specifies (at time of writing API level 29 matching Android 10 "Q"), Unciv will not build against a different API level SDK.

Do an update check from within Android Studio immediately, also for SDK tools, SDK and plugins. Updating Android Studio itself requires root, so run it under sudo as [shown below](#shell-code), but do not allow it to dowload any optionals components in that context - cancel everything until you get to the small intro menu, then bottom-right `Configure->Check for Updates`. When that is done, restart under your normal user and in the same place, no project loaded yet, go to `Configure->Settings->Appearance & Behaviour->System Settings->Android SDK` and check the Status column on the `SDK Platforms` *and* `SDK Tools` tabs and update as applicable, then in the same window go to `Plugins` from the left menu, and check the Kotlin plugin for an update. I'd also suggest going to `Settings->Appearance & Behaviour->System Settings->Memory Settings` and increasing the IDE max heap size if you got RAM to spare.

### Java JDK
The Ubuntu 20.04 default JRE is an OpenJDK 11 variant with a bug rendering it unable to run Unciv (see also [#3770](https://github.com/yairm210/Unciv/issues/3770)). Just installing Android Studio will change the system to use a ubuntu-supplied OpenJDK 14 (full JDK) as default java, and this one boasts the same bug. But it also brought along a separate OpenJDK 11 version not known to `apt` or `update-alternatives` which works - in my case located at `/opt/android-studio/jre`.

After cloning your fork into Android Studio, I'd suggest you immediately check its JDK settings and change it to use said bundled JDK - with a different one you might get [gradle errors](https://duckduckgo.com/?q="org.codehaus.groovy.control.MultipleCompilationErrorsException") or the ubuntu bug. `File->Project Structure->SDK Location`, field `JDK location`. Just ensure the first option from the dropdown named `Embedded...` is selected - in my case it was not for whatever reason.

If you did need to change the project JDK, thanks to gradle havong already run unasked, you might get a stale cache - if you see an unsuccessful gradle build at first, look for the well-hidden `File/Invalidate Caches` command.

### git and SSH
If you can't clone your fork of the repo due to login/authentication errors, consider setting up your github account for SSH access as [described here](https://docs.github.com/en/github/authenticating-to-github/connecting-to-github-with-ssh) and summarized in the [shell code section below](#shell-code). For example, if your account has been set up to use SSH and you move to a different machine, you could get problems - in my case there were no keys whatsoever, and therefore none that matched those github knew about.

If you generate a key, you'll want to decide whether it can be reused (just use or generate a default one) or it's meant to be specific for github development, and whether to use an empty passphrase or maximize security - beware that you'll need to actually type it at least once; as pasting a keepass-generated password won't work in all places, the `ssh-add` command blocks the clipboard by design. You will also need that passphrase at least once while cloning your repo in Android Studio. You will also have to decide on a filename and the "comment" field - I'd suggest using the actual github account name for the former and the actual email the account is registered to for the latter. I suspect, however, that neither match is strictly necessary.

### Shell code
*do not execute everything blindly*
```bash
# New software source - can be removed from update manager
sudo apt-add-repository ppa:maarten-fonville/android-studio
# Refresh software lsit
sudo apt update
# Check out which packages are available - look only at the "Note, selecting" lines (or just below those whether one is already installed)
sudo apt install android-studio-* -s
# Now choose from the offered versions and install one of them
sudo apt install git android-studio-4.2 -y
# Run with root rights to self-update - cancel all import settings/download SDK/etc and quit immediately after
sudo /opt/android-studio/bin/studio.sh

# Check which SSH keys exist (uppercase L!):
ssh-add -L
# If there's a listing and any of these seem suitable, copy the whole line into the clipboard and use it to register the key at github - see below.
# Generate a new key, decide on and replace <filename> (suggested: your github name), <comment> (suggested: your github email) and <passphrase> (your choice) as needed:
cd ~/.ssh
ssh-keygen -t ed25519 -C "<comment>" -f <filename> -N "<passphrase>"
# Just make sure the ssh agent is running - output irrelevant unless some scary errors
eval "$(ssh-agent -s)"
# Add the key, type your passphrase, do not copy&paste it
ssh-add ./<filename>
# List keys
ssh-add -L
# copy the whole line corresponding to your new key, and in your browser go to yout github profile settings, "SSH and GPG keys" section, add new and paste that line. Done!
```

### Markdown
It might be useful to have markdown support as some documents a contributor might want to edit are Markdown, e.g. source attribution for imported open media resources.

There's an IntelliJ [plugin for Markdown fom JetBrains](https://plugins.jetbrains.com/plugin/7793-markdown) that can be installed directly from the Settings Plugins page.

A nice Markdown cheat sheet is [here](https://www.markdownguide.org/cheat-sheet) - though only 90% applies to files that will be rendered by github. Particularly, footnotes work differently.

### Initial Run Config
The existing [Getting-Started](https://github.com/yairm210/Unciv/wiki/Getting-Started) says to "set <repo_folder>\android\assets\ as the Working directory", but I prefer a slight modification.

Ouside the folder the IDE sees as the mirror of your fork, say that is ~/Development/foo/bar/Unciv, create a parallel on for use as Working directory, which might be ~/Development/foo/bar/Unciv.workdir, and set that in your desktop run config. Then link some subfolders from the mentioned assets folder and copy the textures:
```bash
# cd to your new empty working folder (or use the open in terminal feature of your file manager)
ln -s ../Unciv/android/assets/ExtraImages
ln -s ../Unciv/android/assets/jsons
ln -s ../Unciv/android/assets/skin
ln -s ../Unciv/android/assets/sounds
cp ../Unciv/android/assets/*.atlas .
cp ../Unciv/android/assets/*.png .
```
This means data added due to playtesting will not affect commits and you can test with mods without them appearing in Android Studio, no need to fiddle with exlusions and making sure the exclusion list does not end up in a commit - except if you use the "generate translation files" button. Caveat: If your proposed change actually needs to change the atlas/texture files that should be part of a release, you'll have to copy them back manually.
